"""
Gemini Pro Connector
====================
Wrapper untuk Google Generative AI (Gemini Pro).
Mendukung:
- Plain text generation
- Structured JSON generation (via response_mime_type)
- Multimodal (text + image)
- Retry otomatis untuk transient errors
"""

from __future__ import annotations

import json
import re
import time
from typing import Any, Callable, Optional, TypeVar

from config import gemini as gemini_cfg
from utils import get_logger

log = get_logger(__name__)

T = TypeVar("T")


def _retry_on_quota(fn: Callable[[], T], max_attempts: int = 5) -> T:
    """Retry helper khusus untuk 429 (ResourceExhausted) dari Gemini.
    Backoff: ambil 'retry in Xs' dari pesan kalau ada, kalau tidak — exponential.
    """
    attempt = 0
    while True:
        try:
            return fn()
        except Exception as exc:
            attempt += 1
            msg = str(exc)
            is_quota = "RESOURCE_EXHAUSTED" in msg or "429" in msg or "quota" in msg.lower()
            if not is_quota or attempt >= max_attempts:
                raise
            # Coba ekstrak waktu retry dari pesan
            m = re.search(r"retry in ([\d.]+)", msg)
            wait = float(m.group(1)) + 1 if m else min(60.0, 2 ** attempt)
            log.warning("Quota hit (attempt %d/%d). Sleeping %.1fs...",
                        attempt, max_attempts, wait)
            time.sleep(wait)


class GeminiConnectorError(Exception):
    """Raised when Gemini API call fails after retries."""


class GeminiConnector:
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        temperature: float = 0.8,
    ) -> None:
        key = api_key or gemini_cfg.api_key
        if not key:
            raise GeminiConnectorError(
                "GEMINI_API_KEY belum diset. Isi di .env atau lewatkan via argumen."
            )
        try:
            import google.generativeai as genai  # type: ignore
        except ImportError as e:
            raise GeminiConnectorError(
                "Package google-generativeai belum terinstall. "
                "Jalankan: pip install -r requirements.txt"
            ) from e
        self._genai = genai
        genai.configure(api_key=key)
        self.model_name = model or gemini_cfg.model
        self.temperature = temperature
        self._model = genai.GenerativeModel(self.model_name)
        log.info("Gemini connector initialized (model=%s)", self.model_name)

    def generate_text(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        """Generate plain text dari prompt."""
        config = {
            "temperature": temperature if temperature is not None else self.temperature,
        }
        model = (
            self._genai.GenerativeModel(self.model_name, system_instruction=system_instruction)
            if system_instruction
            else self._model
        )
        log.debug("Calling Gemini generate_text (len=%d)", len(prompt))

        def _call() -> str:
            response = model.generate_content(prompt, generation_config=config)
            return (response.text or "").strip()

        return _retry_on_quota(_call)

    def generate_json(
        self,
        prompt: str,
        schema_hint: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> dict[str, Any]:
        """Generate structured JSON output."""
        full_prompt = prompt
        if schema_hint:
            full_prompt = f"{prompt}\n\nIkuti skema JSON berikut secara persis:\n{schema_hint}"

        config = {
            "temperature": temperature if temperature is not None else self.temperature,
            "response_mime_type": "application/json",
        }
        log.debug("Calling Gemini generate_json")

        def _call() -> str:
            response = self._model.generate_content(full_prompt, generation_config=config)
            return (response.text or "").strip()

        raw = _retry_on_quota(_call)
        return self._parse_json_lenient(raw)

    @staticmethod
    def _parse_json_lenient(raw: str) -> dict[str, Any]:
        """Parse JSON dengan toleransi:
        - Strip code fence (```json ... ```)
        - Extract object pertama kalau ada 'extra data' setelahnya
        """
        text = raw.strip()
        # Buang code fence
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\s*", "", text)
            text = re.sub(r"\s*```\s*$", "", text)

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Fallback: pakai raw_decode untuk ambil object pertama
        try:
            decoder = json.JSONDecoder()
            obj, _end = decoder.raw_decode(text)
            log.warning("JSON had extra data; took first object only")
            return obj
        except json.JSONDecodeError as exc:
            log.warning("Failed to parse JSON, raw=%s", text[:300])
            raise GeminiConnectorError(f"Gemini returned invalid JSON: {exc}") from exc

    def generate_with_image(
        self,
        prompt: str,
        image_path: str,
        temperature: Optional[float] = None,
    ) -> str:
        """Multimodal generation: text + image."""
        import PIL.Image  # lazy import — only needed for multimodal

        config = {
            "temperature": temperature if temperature is not None else self.temperature,
        }
        image = PIL.Image.open(image_path)
        response = self._model.generate_content([prompt, image], generation_config=config)
        return (response.text or "").strip()
