"""
Series Orchestrator — pipeline khusus untuk content series berbasis book.

Flow:
1. Load outline.json
2. (Optional) Generate chapter markdown via BookAgent
3. (Optional) Generate social media posts per chapter via SocialThreadAgent
4. (Optional) Compile semua chapter -> book Markdown + PDF
5. (Optional) Publish posts ke social media via SocialMediaAgent
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from agents.book_agent import BookAgent, BookOutline
from agents.social_thread_agent import SocialThreadAgent
from agents.social_media_agent import SocialMediaAgent
from agents.content_creator_agent import PlatformContent, ContentPackage
from connectors.base import PostResult
from utils import compile_markdown, compile_pdf, get_logger

log = get_logger(__name__)


class SeriesOrchestrator:
    def __init__(
        self,
        series_dir: Path,
        dry_run: bool = True,
    ) -> None:
        self.series_dir = Path(series_dir)
        self.outline_path = self.series_dir / "outline.json"
        self.chapters_dir = self.series_dir / "chapters"
        self.social_dir = self.series_dir / "social"
        self.book_dir = self.series_dir / "book"
        self.dry_run = dry_run
        # Agents di-init lazy supaya outline + offline ops bisa jalan tanpa GEMINI_API_KEY
        self._book_agent: Optional[BookAgent] = None
        self._social_agent: Optional[SocialThreadAgent] = None
        self._publisher: Optional[SocialMediaAgent] = None

    @property
    def outline(self) -> BookOutline:
        return BookOutline.load(self.outline_path)

    def _book(self) -> BookAgent:
        if self._book_agent is None:
            self._book_agent = BookAgent()
        return self._book_agent

    def _social(self) -> SocialThreadAgent:
        if self._social_agent is None:
            self._social_agent = SocialThreadAgent()
        return self._social_agent

    def _pub(self) -> SocialMediaAgent:
        if self._publisher is None:
            self._publisher = SocialMediaAgent(dry_run=self.dry_run)
        return self._publisher

    # ---------- step 1: chapters ----------
    def generate_chapters(self, only_id: Optional[str] = None) -> list[Path]:
        outline = self.outline
        if only_id:
            outline.chapters = [c for c in outline.chapters if c.id == only_id]
            if not outline.chapters:
                raise ValueError(f"Chapter id '{only_id}' tidak ada di outline")
        return self._book().generate_all(outline, self.chapters_dir, skip_existing=True)

    # ---------- step 2: social posts ----------
    def generate_social(self, platforms: list[str], only_id: Optional[str] = None) -> dict:
        outline = self.outline
        chapters = outline.chapters
        if only_id:
            chapters = [c for c in chapters if c.id == only_id]
        all_posts: dict[str, dict[str, list[str]]] = {}
        for idx, ch in enumerate(chapters):
            chap_md = self.chapters_dir / f"{ch.id}.md"
            if not chap_md.exists():
                log.warning("Lewati %s: chapter markdown belum ada di %s", ch.id, chap_md)
                continue
            posts = self._social().generate(
                chapter_markdown=chap_md,
                chapter_title=ch.title,
                chapter_number=idx,
                platforms=platforms,
                output_dir=self.social_dir / ch.id,
            )
            all_posts[ch.id] = posts
        return all_posts

    # ---------- step 3: book compile ----------
    def compile_book(self) -> tuple[Path, Path | None]:
        outline = self.outline
        chapter_files = []
        for ch in outline.chapters:
            p = self.chapters_dir / f"{ch.id}.md"
            if p.exists():
                chapter_files.append(p)
            else:
                log.warning("Chapter belum ada, skip: %s", p)

        if not chapter_files:
            raise RuntimeError("Tidak ada chapter markdown untuk dikompilasi.")

        md_path = self.book_dir / f"{self.series_dir.name}.md"
        pdf_path = self.book_dir / f"{self.series_dir.name}.pdf"
        compile_markdown(
            chapter_files=chapter_files,
            output_md=md_path,
            title=outline.title,
            subtitle=outline.subtitle,
            author=outline.author,
        )
        pdf_result = compile_pdf(md_path, pdf_path)
        return md_path, pdf_result

    # ---------- step 4: publish ----------
    def publish_chapter(
        self,
        chapter_id: str,
        platforms: list[str],
    ) -> list[PostResult]:
        """Publish posts dari file social/{chapter_id}/posts.json ke platform."""
        import json

        posts_file = self.social_dir / chapter_id / "posts.json"
        if not posts_file.exists():
            raise FileNotFoundError(f"Posts belum di-generate: {posts_file}")
        data = json.loads(posts_file.read_text(encoding="utf-8"))

        results: list[PostResult] = []
        for plat in platforms:
            posts = data.get(plat, [])
            if not posts:
                log.warning("Tidak ada post untuk %s di chapter %s", plat, chapter_id)
                continue

            # Bungkus jadi ContentPackage minimal untuk reuse SocialMediaAgent
            for i, text in enumerate(posts):
                pkg = ContentPackage(
                    topic=f"{chapter_id} [{plat} {i+1}/{len(posts)}]",
                    twitter=PlatformContent(text=text if plat == "twitter" else ""),
                    instagram=PlatformContent(text=text if plat == "instagram" else ""),
                    facebook=PlatformContent(text=text if plat == "facebook" else ""),
                    linkedin=PlatformContent(text=text if plat == "linkedin" else ""),
                )
                results.extend(self._pub().publish(pkg, [plat]))
        return results
