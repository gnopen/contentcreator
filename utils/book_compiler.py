"""
Book Compiler — gabung chapter markdown jadi book lengkap (Markdown + PDF).

PDF compile pakai 2 jalur (fallback urut):
  1. `markdown-pdf` (pure Python via markdown + weasyprint)
  2. `pandoc` (kalau terinstall di sistem)
  3. Kalau dua-duanya gagal → tetap simpan full markdown; user bisa convert manual.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from utils.logger import get_logger

log = get_logger(__name__)


def compile_markdown(
    chapter_files: list[Path],
    output_md: Path,
    title: str,
    author: str = "QA Thomas",
    subtitle: str = "",
) -> Path:
    """Gabungkan semua chapter markdown jadi satu file dengan front-matter & TOC."""
    output_md.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    # Front matter sederhana
    lines.append(f"# {title}\n")
    if subtitle:
        lines.append(f"_{subtitle}_\n")
    lines.append(f"\n**Penulis**: {author}\n")
    lines.append("\n---\n\n")

    # Table of Contents
    lines.append("## Daftar Isi\n\n")
    for i, ch in enumerate(chapter_files):
        title_line = _extract_title(ch) or ch.stem
        lines.append(f"{i+1}. {title_line}\n")
    lines.append("\n---\n\n")

    # Append chapter contents
    for ch in chapter_files:
        content = ch.read_text(encoding="utf-8").strip()
        lines.append(content)
        lines.append("\n\n---\n\n")

    output_md.write_text("".join(lines), encoding="utf-8")
    log.info("Markdown book ditulis ke %s (%d chapter)", output_md, len(chapter_files))
    return output_md


def compile_pdf(input_md: Path, output_pdf: Path) -> Path | None:
    """
    Convert markdown -> PDF.
    Return path PDF kalau sukses, None kalau gagal (tetap punya markdown).
    """
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    html_body = None
    try:
        import markdown as md_lib  # type: ignore
        html_body = md_lib.markdown(
            input_md.read_text(encoding="utf-8"),
            extensions=["extra", "toc", "tables", "fenced_code"],
        )
    except Exception as e:
        log.debug("markdown lib unavailable: %s", e)

    # Brand stylesheet v2 — Editorial Edition
    # Cream paper + ink text + mustard accent + serif display
    css = """
@page { margin: 2.2cm 2cm; background: #F5F1E8; }
body {
    font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
    color: #1A1A1A;
    background: #F5F1E8;
    max-width: 700px;
    margin: 2cm auto;
    line-height: 1.65;
    font-size: 11pt;
}
h1 {
    font-family: 'Playfair Display', 'Lora', Georgia, serif;
    font-weight: 800;
    color: #1A1A1A;
    margin-top: 2.5em;
    margin-bottom: 0.6em;
    letter-spacing: 0;
    font-size: 30pt;
    line-height: 1.15;
    page-break-before: auto;
}
h1::before {
    content: "";
    display: block;
    width: 60px;
    height: 8px;
    background: #E8B547;
    margin-bottom: 18px;
}
h2 {
    font-family: 'Playfair Display', 'Lora', Georgia, serif;
    font-weight: 700;
    color: #1A1A1A;
    margin-top: 2em;
    margin-bottom: 0.4em;
    font-size: 20pt;
    line-height: 1.3;
}
h3 {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-weight: 700;
    color: #4A4A4A;
    margin-top: 1.6em;
    margin-bottom: 0.4em;
    font-size: 14pt;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
p { margin: 0.8em 0; }
strong { color: #1A1A1A; font-weight: 700; }
em { color: #4A4A4A; font-style: italic; }
code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    background: #E8E4DA;
    color: #1A1A1A;
    padding: 2px 6px;
    border-radius: 2px;
    font-size: 0.9em;
}
pre {
    background: #FAF7F0;
    border-left: 4px solid #E8B547;
    padding: 16px 18px;
    border-radius: 2px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 9.5pt;
    line-height: 1.5;
    color: #1A1A1A;
}
pre code { background: transparent; color: #1A1A1A; padding: 0; }
blockquote {
    border-left: 4px solid #1A1A1A;
    background: transparent;
    padding: 0 0 0 20px;
    margin: 1.6em 0;
    color: #1A1A1A;
    font-family: 'Playfair Display', Georgia, serif;
    font-style: italic;
    font-size: 13pt;
    line-height: 1.5;
}
blockquote p { margin: 0.3em 0; }
table {
    border-collapse: collapse;
    margin: 1.4em 0;
    width: 100%;
    font-size: 10pt;
}
th {
    background: #E8B547;
    color: #1A1A1A;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    padding: 10px 14px;
    text-align: left;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    font-size: 9pt;
    border-bottom: 2px solid #1A1A1A;
}
td {
    border-bottom: 1px solid #E8E4DA;
    padding: 9px 14px;
    vertical-align: top;
}
tr:nth-child(even) td { background: #FAF7F0; }
ul, ol {
    padding-left: 22px;
    margin: 0.8em 0;
}
li { margin-bottom: 6px; }
hr {
    border: none;
    border-top: 1px solid #1A1A1A;
    margin: 3em auto;
    width: 80px;
}
a {
    color: #1A1A1A;
    text-decoration: none;
    border-bottom: 1px solid #E8B547;
}
"""
    if html_body:
        html_doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{html_body}</body></html>'

        # Strategi 1: weasyprint (best output, butuh GTK di Windows)
        try:
            from weasyprint import HTML  # type: ignore
            HTML(string=html_doc).write_pdf(str(output_pdf))
            log.info("PDF compiled via weasyprint -> %s", output_pdf)
            return output_pdf
        except Exception as e:
            log.debug("weasyprint path failed: %s", e)

        # Strategi 2: xhtml2pdf (pure Python, no external deps)
        try:
            from xhtml2pdf import pisa  # type: ignore
            with open(output_pdf, "wb") as fh:
                status = pisa.CreatePDF(html_doc, dest=fh, encoding="utf-8")
            if status.err == 0:
                log.info("PDF compiled via xhtml2pdf -> %s", output_pdf)
                return output_pdf
        except Exception as e:
            log.debug("xhtml2pdf path failed: %s", e)

    # Strategi 3: pandoc CLI
    if shutil.which("pandoc"):
        try:
            subprocess.run(
                ["pandoc", str(input_md), "-o", str(output_pdf), "--toc"],
                check=True,
                capture_output=True,
            )
            log.info("PDF compiled via pandoc -> %s", output_pdf)
            return output_pdf
        except Exception as e:
            log.debug("pandoc path failed: %s", e)

    log.warning(
        "PDF compile gagal. Markdown tetap di %s — install: pip install xhtml2pdf markdown",
        input_md,
    )
    return None


def _extract_title(md_file: Path) -> str | None:
    for line in md_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return None
