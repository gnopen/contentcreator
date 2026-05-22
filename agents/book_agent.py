"""
Book Agent — generate content per chapter dari outline + source materials.

Workflow:
1. Load outline (list of chapter dicts: id, title, theme, source_files, key_points).
2. Untuk tiap chapter: gabungkan source materials, kirim ke Gemini dengan
   instruksi panjang & gaya book (tutorial+story).
3. Simpan hasil sebagai markdown ke direktori chapters/.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from connectors.gemini_connector import GeminiConnector
from utils import get_logger

log = get_logger(__name__)


SYSTEM_PROMPT = """Anda adalah technical writer berbahasa Indonesia yang
menulis buku praktis tentang Quality Assurance. Gaya:
- Tutorial step-by-step, tidak menggurui
- Sertakan contoh nyata (kode, template, dialog)
- Pakai 'Anda' bukan 'kamu' (formal-friendly)
- Diakhiri dengan rangkuman & checklist actionable
- Format Markdown rapi (heading hierarki, tabel, code block)
- Panjang per chapter: 1500-2500 kata.
"""


@dataclass
class Chapter:
    id: str            # mis. "00-intro"
    title: str
    theme: str
    key_points: list[str] = field(default_factory=list)
    source_files: list[str] = field(default_factory=list)  # path absolut atau relatif

    @classmethod
    def from_dict(cls, d: dict) -> "Chapter":
        return cls(
            id=d["id"],
            title=d["title"],
            theme=d["theme"],
            key_points=d.get("key_points", []),
            source_files=d.get("source_files", []),
        )


@dataclass
class BookOutline:
    title: str
    subtitle: str
    author: str
    chapters: list[Chapter]

    @classmethod
    def load(cls, path: Path) -> "BookOutline":
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            title=data["title"],
            subtitle=data.get("subtitle", ""),
            author=data.get("author", "QA Thomas"),
            chapters=[Chapter.from_dict(c) for c in data["chapters"]],
        )


class BookAgent:
    def __init__(self, gemini: Optional[GeminiConnector] = None) -> None:
        self.gemini = gemini or GeminiConnector(temperature=0.7)
        log.info("BookAgent ready")

    def generate_chapter(
        self,
        chapter: Chapter,
        outline_context: str,
        output_dir: Path,
    ) -> Path:
        """Generate satu chapter berdasarkan source files & key points. Return path file."""
        sources_text = self._load_sources(chapter.source_files)
        prompt = self._build_prompt(chapter, outline_context, sources_text)

        log.info("Generating chapter %s — %s", chapter.id, chapter.title)
        text = self.gemini.generate_text(prompt, system_instruction=SYSTEM_PROMPT)

        output_dir.mkdir(parents=True, exist_ok=True)
        out_path = output_dir / f"{chapter.id}.md"
        out_path.write_text(text.strip() + "\n", encoding="utf-8")
        log.info("Chapter saved -> %s (%d chars)", out_path, len(text))
        return out_path

    def generate_all(
        self,
        outline: BookOutline,
        output_dir: Path,
        skip_existing: bool = True,
    ) -> list[Path]:
        outline_ctx = self._format_outline_context(outline)
        paths: list[Path] = []
        for ch in outline.chapters:
            target = output_dir / f"{ch.id}.md"
            if skip_existing and target.exists():
                log.info("Skip (sudah ada): %s", target)
                paths.append(target)
                continue
            paths.append(self.generate_chapter(ch, outline_ctx, output_dir))
        return paths

    @staticmethod
    def _load_sources(source_files: list[str]) -> str:
        chunks: list[str] = []
        for src in source_files:
            p = Path(src)
            if not p.exists():
                log.warning("Source file tidak ada: %s", p)
                continue
            chunks.append(f"\n=== {p.name} ===\n{p.read_text(encoding='utf-8')}")
        return "\n".join(chunks) if chunks else "(tidak ada source file terlampir)"

    @staticmethod
    def _format_outline_context(outline: BookOutline) -> str:
        lines = [f"Buku: {outline.title}", f"Sub: {outline.subtitle}", "", "Daftar chapter:"]
        for ch in outline.chapters:
            lines.append(f"- {ch.id}: {ch.title} — {ch.theme}")
        return "\n".join(lines)

    @staticmethod
    def _build_prompt(chapter: Chapter, outline_ctx: str, sources_text: str) -> str:
        key_points = "\n".join(f"- {kp}" for kp in chapter.key_points)
        return f"""Konteks buku keseluruhan:
{outline_ctx}

================
Chapter yang akan ditulis SEKARANG:
ID    : {chapter.id}
Judul : {chapter.title}
Tema  : {chapter.theme}

Poin utama yang HARUS dibahas:
{key_points}

================
Source material (gunakan ini sebagai bahan utama; parafrase dalam Bahasa
Indonesia, jangan menyalin mentah; sertakan contoh konkret):
{sources_text}

================
Tulis chapter ini dalam format Markdown.
Struktur yang diharapkan:
- `# Chapter X: <judul>`
- Pembuka (1-2 paragraf naratif yang menarik)
- Beberapa section `## ...` sesuai key points
- Contoh konkret (code block / tabel / dialog) di setiap section
- `## Rangkuman` di akhir
- `## Checklist Actionable` di akhir (5-10 item bullet)
"""
