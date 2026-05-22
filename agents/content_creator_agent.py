"""
Content Creator Agent
=====================
Agent yang mengubah brief/topik jadi konten siap-posting per platform.

Output: ContentPackage berisi varian konten untuk Twitter, Instagram,
Facebook, dan LinkedIn (caption, hashtags, CTA, image-prompt).
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional

from connectors.gemini_connector import GeminiConnector
from utils import get_logger

log = get_logger(__name__)


SYSTEM_PROMPT = """Anda adalah Content Strategist profesional yang bertugas membuat
konten social media berkualitas tinggi. Selalu:
- Sesuaikan tone & panjang dengan platform (Twitter: singkat 280 char,
  LinkedIn: profesional & insight-driven, Instagram: visual & engaging,
  Facebook: storytelling).
- Sertakan hashtag yang relevan (5-10 untuk IG, 2-3 untuk Twitter/LinkedIn).
- Sertakan call-to-action yang jelas.
- Output WAJIB JSON valid sesuai skema yang diminta.
"""

SCHEMA = """{
  "topic": "string - topik asli",
  "twitter": {
    "text": "string max 280 char termasuk hashtag",
    "hashtags": ["string"]
  },
  "instagram": {
    "caption": "string panjang, paragraf engaging",
    "hashtags": ["string"],
    "image_prompt": "deskripsi visual untuk image generator"
  },
  "facebook": {
    "text": "string storytelling, 2-4 paragraf",
    "hashtags": ["string"]
  },
  "linkedin": {
    "text": "string profesional, insight-driven, 3-5 paragraf",
    "hashtags": ["string"]
  }
}"""


@dataclass
class PlatformContent:
    text: str
    hashtags: list[str] = field(default_factory=list)
    image_prompt: Optional[str] = None


@dataclass
class ContentPackage:
    topic: str
    twitter: PlatformContent
    instagram: PlatformContent
    facebook: PlatformContent
    linkedin: PlatformContent

    def for_platform(self, platform: str) -> PlatformContent:
        platform = platform.lower()
        if not hasattr(self, platform):
            raise ValueError(f"Platform tidak dikenal: {platform}")
        return getattr(self, platform)

    def to_dict(self) -> dict:
        return asdict(self)


class ContentCreatorAgent:
    def __init__(self, gemini: Optional[GeminiConnector] = None) -> None:
        self.gemini = gemini or GeminiConnector()
        log.info("ContentCreatorAgent ready")

    def create(
        self,
        topic: str,
        tone: str = "engaging dan profesional",
        target_audience: str = "umum",
        language: str = "Indonesia",
        extra_context: Optional[str] = None,
    ) -> ContentPackage:
        """Hasilkan paket konten multi-platform dari satu topik."""
        prompt = self._build_prompt(topic, tone, target_audience, language, extra_context)
        log.info("Generating content for topic=%r", topic)
        data = self.gemini.generate_json(prompt, schema_hint=SCHEMA)
        return self._parse(data, topic)

    @staticmethod
    def _build_prompt(
        topic: str,
        tone: str,
        target_audience: str,
        language: str,
        extra_context: Optional[str],
    ) -> str:
        extra = f"\nKonteks tambahan: {extra_context}" if extra_context else ""
        return f"""{SYSTEM_PROMPT}

Tugas: Buat konten social media untuk topik berikut.

Topik         : {topic}
Bahasa        : {language}
Tone          : {tone}
Target audiens: {target_audience}{extra}

Hasilkan varian untuk: twitter, instagram, facebook, linkedin.
"""

    @staticmethod
    def _parse(data: dict, topic: str) -> ContentPackage:
        def pc(d: dict, text_key: str) -> PlatformContent:
            return PlatformContent(
                text=d.get(text_key, ""),
                hashtags=d.get("hashtags", []) or [],
                image_prompt=d.get("image_prompt"),
            )

        return ContentPackage(
            topic=data.get("topic", topic),
            twitter=pc(data.get("twitter", {}), "text"),
            instagram=pc(data.get("instagram", {}), "caption"),
            facebook=pc(data.get("facebook", {}), "text"),
            linkedin=pc(data.get("linkedin", {}), "text"),
        )
