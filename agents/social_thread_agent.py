"""
Social Thread Agent — ubah satu chapter (markdown panjang) jadi
serangkaian post social media per platform.

Strategi hemat quota: 1 API call per chapter menghasilkan output JSON
untuk SEMUA platform sekaligus (bukan 1 call per platform).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

from connectors.gemini_connector import GeminiConnector
from utils import get_logger, split_for_platform
from utils.text_splitter import _pack, _split_paragraphs
from agents.geo_optimizer import geo_prompt_fragment, upgrade_caption, check_caption

log = get_logger(__name__)


PLATFORM_BRIEF = {
    "twitter": "Twitter/X thread. Tiap tweet max ~260 char (sistem akan tambah numbering otomatis, JANGAN ditambah sendiri). Hook kuat di tweet 1. Tweet terakhir = CTA + link ke book.",
    "instagram": "Instagram caption tunggal. Awali hook 1-2 baris, lanjut bullet/short paragraf. Akhiri CTA + 5-8 hashtag relevan.",
    "facebook": "Facebook post storytelling 2-3 paragraf. Tone hangat, contoh konkret, tutup dengan CTA. 2-3 hashtag.",
    "linkedin": "LinkedIn post profesional. Hook 1 kalimat, body insight-driven dengan 1-2 contoh nyata, framework/list singkat, tutup refleksi & ajakan diskusi. 3-5 hashtag.",
}


SYSTEM_PROMPT = """Anda adalah social media copywriter berbahasa Indonesia
untuk audiens profesional QA / tester / engineering. Tulisan harus:
- Hook menarik (bukan 'Hai semua!')
- Konkret, ada contoh atau angka
- Hindari motivational-fluff
- Tone Bahasa Indonesia profesional-santai
- Output WAJIB JSON valid persis sesuai skema yang diminta.
"""


SCHEMA_TEMPLATE = """{
  "twitter": ["tweet 1 (max 260 char, NO numbering)", "tweet 2", "..."],
  "linkedin": "string panjang utuh, ~1500-2500 char, multi paragraf",
  "instagram": "string panjang utuh, ~1000-1800 char dengan hashtag di akhir",
  "facebook": "string storytelling utuh, ~1000-1500 char dengan hashtag di akhir"
}"""


class SocialThreadAgent:
    def __init__(
        self,
        gemini: Optional[GeminiConnector] = None,
        geo_enabled: bool = True,
    ) -> None:
        self.gemini = gemini or GeminiConnector(temperature=0.8)
        self.geo_enabled = geo_enabled
        log.info("SocialThreadAgent ready (geo=%s)", geo_enabled)

    def generate(
        self,
        chapter_markdown: Path,
        chapter_title: str,
        chapter_number: int,
        platforms: list[str],
        output_dir: Path,
        book_cta: str = "Full book PDF tersedia di akhir series — DM untuk dapatkan early access.",
    ) -> dict[str, list[str]]:
        content = chapter_markdown.read_text(encoding="utf-8")

        # 1 API call untuk semua platform sekaligus
        log.info("Generating posts (all platforms) for chapter %s", chapter_title)
        prompt = self._build_prompt(platforms, chapter_title, chapter_number, content, book_cta)
        if self.geo_enabled:
            prompt = prompt + "\n\n" + geo_prompt_fragment(platforms)
        raw_json = self.gemini.generate_json(prompt, schema_hint=SCHEMA_TEMPLATE)

        # Post-process per platform
        result: dict[str, list[str]] = {}
        for plat in platforms:
            plat = plat.lower()
            if plat not in PLATFORM_BRIEF:
                log.warning("Skip platform tidak dikenal: %s", plat)
                continue
            raw_value = raw_json.get(plat)
            if raw_value is None:
                log.warning("Platform %s tidak ada di response Gemini", plat)
                continue
            posts = self._postprocess(raw_value, plat)

            # GEO post-pass: untuk non-twitter, jaminan hashtag set sesuai.
            # Untuk twitter, upgrade hanya tweet penutup.
            if self.geo_enabled and posts:
                if plat == "twitter":
                    posts[-1] = upgrade_caption(posts[-1], plat)
                    # Re-check kalau >280 char setelah penambahan, pecah
                    if len(posts[-1]) > 280:
                        # Split jadi 2 tweet
                        sr = split_for_platform(posts[-1], "twitter", add_numbering=False)
                        posts = posts[:-1] + sr.parts
                        # Renumber semua
                        n = len(posts)
                        # Strip old numbering
                        posts = [re.sub(r"^\d+\s*/\s*\d+\s+", "", t).strip() for t in posts]
                        posts = [f"{i+1}/{n} {t}" for i, t in enumerate(posts)]
                else:
                    posts[0] = upgrade_caption(posts[0], plat)
                # Log audit
                first_text = posts[-1] if plat == "twitter" else posts[0]
                check = check_caption(first_text, plat)
                log.info("GEO check %s: score=%d/100 (pass=%s)",
                         plat, check.score, check.passes)

            result[plat] = posts

        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / "posts.json"
        out_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        log.info("Posts saved -> %s", out_file)
        return result

    @staticmethod
    def _build_prompt(
        platforms: list[str],
        chapter_title: str,
        chapter_number: int,
        chapter_content: str,
        cta: str,
    ) -> str:
        platform_briefs = "\n".join(
            f"- {p}: {PLATFORM_BRIEF[p]}" for p in platforms if p in PLATFORM_BRIEF
        )
        return f"""Tulis konten social media untuk semua platform ini:

{platform_briefs}

Konten ini bagian dari series "Journey QA Thomas — Chapter {chapter_number}: {chapter_title}".

CTA wajib disebut di post terakhir/tunggal tiap platform:
{cta}

Materi sumber (chapter Markdown):
---
{chapter_content[:6000]}
---

Aturan output:
- Twitter: array of strings. Tiap string adalah 1 tweet, max ~260 char.
  JANGAN tambah numbering "1/n" di awal — sistem yang melakukan.
- LinkedIn, Instagram, Facebook: satu string utuh (boleh multi paragraf).
"""

    @staticmethod
    def _postprocess(raw_value, platform: str) -> list[str]:
        # Twitter: expect list of strings
        if platform == "twitter":
            tweets = raw_value if isinstance(raw_value, list) else [str(raw_value)]
            # Defensive: hapus numbering yang mungkin tetap ditambahkan Gemini
            num_prefix = re.compile(r"^(?:\[)?\d+\s*/\s*\d+(?:\])?[\s.:\-]+")
            cleaned: list[str] = []
            for t in tweets:
                s = str(t).strip()
                # Iteratif strip prefix
                prev = None
                while prev != s:
                    prev = s
                    s = num_prefix.sub("", s, count=1).strip()
                if not s:
                    continue
                # Safety: pecah lagi kalau ada yang masih > 270 char
                if len(s) <= 270:
                    cleaned.append(s)
                else:
                    paragraphs = _split_paragraphs(s)
                    cleaned.extend(_pack(paragraphs, 270))
            n = len(cleaned)
            if n > 1:
                cleaned = [f"{i+1}/{n} {t}" for i, t in enumerate(cleaned)]
            return cleaned

        # Non-twitter: satu string utuh, mungkin perlu split kalau over limit
        text = raw_value if isinstance(raw_value, str) else json.dumps(raw_value, ensure_ascii=False)
        sr = split_for_platform(text.strip(), platform, add_numbering=True)
        return sr.parts
