"""
Gemini Image Connector — wrapper untuk image generation pakai
Google Gemini "Nano Banana 2" (gemini-3-pro-image-preview) dan kerabatnya.

Catatan billing:
- Per 2026-05-22, model image generation Gemini (Nano Banana 1 & 2)
  WAJIB paid tier. Free tier limit = 0 untuk model image.
- Aktifkan billing di https://aistudio.google.com/app/billing
  atau via Google Cloud project.

Model yang didukung:
- gemini-3-pro-image-preview      (Nano Banana 2, kualitas tertinggi)
- gemini-2.5-flash-image          (Nano Banana 1, lebih murah)
- gemini-3.1-flash-image-preview  (Nano Banana 2 mini, cepat)

Output: bytes PNG/JPEG yang siap di-save.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from utils import get_logger

log = get_logger(__name__)


# Default model (Nano Banana 2). Bisa override via env GEMINI_IMAGE_MODEL.
DEFAULT_IMAGE_MODEL = os.getenv("GEMINI_IMAGE_MODEL", "gemini-3-pro-image-preview")

# Fallback chain bila primary tidak available — gemini-2.5-flash-image lebih murah
FALLBACK_MODELS = [
    "gemini-3-pro-image-preview",
    "gemini-3.1-flash-image-preview",
    "gemini-2.5-flash-image",
]


class GeminiImageError(Exception):
    pass


class QuotaError(GeminiImageError):
    """Diraise saat hit 429 — caller bisa decide skip atau retry nanti."""


@dataclass
class ImageResult:
    bytes_data: bytes
    mime_type: str
    model_used: str

    def save(self, path: Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(self.bytes_data)
        return path


class GeminiImageConnector:
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ) -> None:
        from dotenv import load_dotenv
        load_dotenv()
        key = api_key or os.getenv("GEMINI_API_KEY")
        if not key:
            raise GeminiImageError("GEMINI_API_KEY belum diset di .env")

        try:
            from google import genai  # type: ignore
        except ImportError as e:
            raise GeminiImageError(
                "google-genai SDK belum terinstall. "
                "Install: pip install google-genai"
            ) from e

        self._genai = genai
        self.client = genai.Client(api_key=key)
        self.model = model or DEFAULT_IMAGE_MODEL
        log.info("GeminiImageConnector ready (model=%s)", self.model)

    def generate(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        try_fallback: bool = True,
    ) -> ImageResult:
        """
        Generate satu image dari prompt.

        aspect_ratio: '1:1' (default), '16:9', '9:16', '4:3', '3:4'
                      (didukung Gemini image models)
        try_fallback: kalau primary model 404/429, coba model lain di chain.
        """
        models_to_try = [self.model]
        if try_fallback:
            models_to_try += [m for m in FALLBACK_MODELS if m != self.model]

        last_err: Optional[Exception] = None
        for m in models_to_try:
            try:
                log.debug("Try image gen with %s (aspect=%s)", m, aspect_ratio)
                result = self._call(m, prompt, aspect_ratio)
                return result
            except QuotaError as e:
                log.warning("Quota habis untuk %s: %s", m, e)
                last_err = e
            except Exception as e:
                msg = str(e)[:200]
                if "404" in msg or "NOT_FOUND" in msg:
                    log.debug("%s not available, try next", m)
                    last_err = e
                    continue
                raise

        raise QuotaError(
            f"Semua model image gagal (quota/billing): {last_err}. "
            "Aktifkan billing di https://aistudio.google.com/app/billing"
        )

    def _call(self, model: str, prompt: str, aspect_ratio: str) -> ImageResult:
        # Tambah hint aspect ratio ke prompt agar konsisten (model Gemini
        # belum semua support aspect ratio param di config)
        full_prompt = f"{prompt}\n\nGenerate as a {aspect_ratio} aspect ratio image."

        try:
            resp = self.client.models.generate_content(
                model=model,
                contents=full_prompt,
            )
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                raise QuotaError(str(e)[:300]) from e
            raise

        if not resp.candidates or not resp.candidates[0].content.parts:
            raise GeminiImageError("Empty response dari Gemini")

        for part in resp.candidates[0].content.parts:
            if part.inline_data and part.inline_data.data:
                return ImageResult(
                    bytes_data=part.inline_data.data,
                    mime_type=part.inline_data.mime_type or "image/png",
                    model_used=model,
                )

        # Tidak ada inline image — kemungkinan model balas text-only
        text_parts = [p.text for p in resp.candidates[0].content.parts if p.text]
        raise GeminiImageError(
            f"Tidak ada image di response {model}. "
            f"Model mungkin tidak support image output. "
            f"Text response: {''.join(text_parts)[:200]}"
        )
