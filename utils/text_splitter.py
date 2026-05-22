"""
Text splitter — pecah teks panjang jadi multi-post untuk social media.

Strategi:
- Hormati batas karakter per platform (Twitter 280, IG/FB 2200, LinkedIn 3000).
- Pecah pada batas paragraf > kalimat > kata (tidak pernah di tengah kata).
- Tambahkan numbering [1/n], [2/n] ... pada thread.
- Untuk Twitter thread: sisakan ruang untuk numbering (~10 char).
"""

from __future__ import annotations

import re
from dataclasses import dataclass


PLATFORM_LIMITS = {
    "twitter": 280,
    "instagram": 2200,
    "facebook": 5000,
    "linkedin": 3000,
}


@dataclass
class SplitResult:
    platform: str
    parts: list[str]

    @property
    def is_thread(self) -> bool:
        return len(self.parts) > 1


def _split_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p for p in parts if p]


def _pack(units: list[str], limit: int, joiner: str = "\n\n") -> list[str]:
    """Pack units secara greedy ke chunk dengan batas `limit`."""
    chunks: list[str] = []
    current = ""
    for unit in units:
        candidate = unit if not current else current + joiner + unit
        if len(candidate) <= limit:
            current = candidate
            continue

        if current:
            chunks.append(current)
            current = ""

        if len(unit) <= limit:
            current = unit
        else:
            # Unit sendiri sudah melebihi limit → pecah lebih halus
            for piece in _force_split(unit, limit):
                if not current:
                    current = piece
                elif len(current + joiner + piece) <= limit:
                    current = current + joiner + piece
                else:
                    chunks.append(current)
                    current = piece

    if current:
        chunks.append(current)
    return chunks


def _force_split(text: str, limit: int) -> list[str]:
    """Pecah kalimat per kalimat; kalau kalimat masih > limit, pecah per kata."""
    out: list[str] = []
    for sentence in _split_sentences(text):
        if len(sentence) <= limit:
            out.append(sentence)
            continue
        # pecah per kata
        words = sentence.split()
        buf = ""
        for w in words:
            cand = w if not buf else buf + " " + w
            if len(cand) <= limit:
                buf = cand
            else:
                if buf:
                    out.append(buf)
                buf = w
        if buf:
            out.append(buf)
    return out


def split_for_platform(text: str, platform: str, add_numbering: bool = True) -> SplitResult:
    """
    Split teks panjang untuk satu platform.
    Kalau muat dalam 1 post → return 1 part tanpa numbering.
    """
    platform = platform.lower()
    if platform not in PLATFORM_LIMITS:
        raise ValueError(f"Unknown platform: {platform}")

    limit = PLATFORM_LIMITS[platform]
    text = text.strip()
    if len(text) <= limit:
        return SplitResult(platform=platform, parts=[text])

    # Reserve ~10 chars for numbering on thread platforms
    effective_limit = limit - 10 if add_numbering else limit

    paragraphs = _split_paragraphs(text)
    chunks = _pack(paragraphs, effective_limit)

    if add_numbering and len(chunks) > 1:
        total = len(chunks)
        chunks = [f"[{i+1}/{total}] {c}" for i, c in enumerate(chunks)]

    return SplitResult(platform=platform, parts=chunks)
