"""
Image Batch Agent
=================
Generate banyak image dalam satu run lalu organisir ke folder per-tanggal.

Use case utama:
1. Generate cover image untuk tiap chapter book.
2. Generate ilustrasi pendamping social post.
3. Generate visual brand asset (logo variant, header banner, dst).

Layout output:
    images/
    └── YYYY-MM-DD/
        ├── manifest.json              # daftar prompt + hasil
        ├── 01-cover-chapter-0.png
        ├── 02-cover-chapter-1.png
        └── ...

Mode:
- live: panggil Gemini API beneran (butuh paid tier)
- dry-run: skip API, tulis manifest saja untuk preview prompt list.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, asdict, field
from datetime import date
from pathlib import Path
from typing import Optional

from connectors.gemini_image_connector import (
    GeminiImageConnector,
    QuotaError,
    GeminiImageError,
)
from utils import get_logger

log = get_logger(__name__)


@dataclass
class ImageJob:
    name: str              # nama file tanpa ekstensi, mis. "cover-chapter-0"
    prompt: str
    aspect_ratio: str = "1:1"
    notes: str = ""        # konteks bebas — disimpan di manifest


@dataclass
class JobResult:
    name: str
    success: bool
    file: Optional[str] = None
    model_used: Optional[str] = None
    error: Optional[str] = None
    elapsed_ms: int = 0


class ImageBatchAgent:
    def __init__(
        self,
        base_dir: Path = Path("images"),
        dry_run: bool = False,
        connector: Optional[GeminiImageConnector] = None,
        throttle_seconds: float = 2.0,
    ) -> None:
        self.base_dir = Path(base_dir)
        self.dry_run = dry_run
        self.throttle = throttle_seconds
        self._connector = connector
        log.info("ImageBatchAgent ready (dry_run=%s, dir=%s)", dry_run, base_dir)

    def _conn(self) -> GeminiImageConnector:
        if self._connector is None:
            self._connector = GeminiImageConnector()
        return self._connector

    def today_dir(self) -> Path:
        d = self.base_dir / date.today().isoformat()
        d.mkdir(parents=True, exist_ok=True)
        return d

    def run(self, jobs: list[ImageJob]) -> list[JobResult]:
        out_dir = self.today_dir()
        log.info("Batch: %d jobs -> %s", len(jobs), out_dir)

        results: list[JobResult] = []
        for i, job in enumerate(jobs):
            safe_name = re.sub(r"[^A-Za-z0-9_-]+", "-", job.name).strip("-")
            target = out_dir / f"{i+1:02d}-{safe_name}.png"
            t0 = time.time()

            if self.dry_run:
                log.info("[DRY] %s -> %s", job.name, target.name)
                results.append(JobResult(
                    name=job.name,
                    success=True,
                    file=str(target),
                    model_used="dry-run",
                    elapsed_ms=0,
                ))
                continue

            try:
                img = self._conn().generate(job.prompt, aspect_ratio=job.aspect_ratio)
                img.save(target)
                elapsed = int((time.time() - t0) * 1000)
                log.info("OK  %s -> %s (%d ms, model=%s)",
                         job.name, target.name, elapsed, img.model_used)
                results.append(JobResult(
                    name=job.name,
                    success=True,
                    file=str(target),
                    model_used=img.model_used,
                    elapsed_ms=elapsed,
                ))
            except QuotaError as e:
                log.error("QUOTA %s: %s", job.name, e)
                results.append(JobResult(
                    name=job.name, success=False,
                    error=f"QUOTA: {str(e)[:200]}",
                    elapsed_ms=int((time.time() - t0) * 1000),
                ))
                # Stop early — semua job berikutnya akan gagal juga
                log.warning("Quota habis, skip sisa %d jobs", len(jobs) - i - 1)
                break
            except Exception as e:
                log.exception("FAIL %s", job.name)
                results.append(JobResult(
                    name=job.name, success=False,
                    error=str(e)[:200],
                    elapsed_ms=int((time.time() - t0) * 1000),
                ))

            if self.throttle and i < len(jobs) - 1:
                time.sleep(self.throttle)

        self._write_manifest(out_dir, jobs, results)
        return results

    @staticmethod
    def _write_manifest(out_dir: Path, jobs: list[ImageJob], results: list[JobResult]) -> None:
        manifest_path = out_dir / "manifest.json"
        manifest = {
            "date": date.today().isoformat(),
            "total": len(jobs),
            "successful": sum(1 for r in results if r.success),
            "failed": sum(1 for r in results if not r.success),
            "jobs": [
                {
                    "input": asdict(jobs[i]) if i < len(jobs) else None,
                    "output": asdict(r),
                }
                for i, r in enumerate(results)
            ],
        }
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        log.info("Manifest written -> %s", manifest_path)


# ============================================================
# Prompt presets — brand-aligned (pink/cyan/yellow)
# ============================================================
BRAND_STYLE_SUFFIX = (
    "Flat-design illustration, bold geometric shapes, vibrant colors "
    "hot pink (#E91E63), cyan (#26C6DA), and yellow (#FFD600) as primary palette, "
    "with accent green (#66BB6A) and purple (#7E57C2). Clean white background. "
    "Editorial poster style, no text in image, no watermark. "
    "Inspired by modern tech publication covers."
)


def chapter_cover_jobs(series_dir: Path) -> list[ImageJob]:
    """Generate ImageJob list untuk cover tiap chapter."""
    outline_path = series_dir / "outline.json"
    if not outline_path.exists():
        raise FileNotFoundError(f"outline.json tidak ditemukan: {outline_path}")
    data = json.loads(outline_path.read_text(encoding="utf-8"))

    stage_colors = {
        "00": "introduction theme with gateway and checkmark icons",
        "01": "magnifying glass over a document, PRD review theme, hot pink dominant",
        "02": "blueprint layout with test cases in 4 categories, cyan dominant",
        "03": "racing track with smoke→functional→exploratory→regression stages, yellow dominant",
        "04": "bug ticket with severity tags P0-P3, red and orange accents",
        "05": "stack of reports and documents, green dominant",
        "06": "people meeting around a table, demo screen, purple dominant",
        "07": "browser automation with Playwright logo (subtle), cyan dominant",
        "08": "interconnected tools (Notion, Slack, Drive) as nodes, mixed palette",
        "09": "summit / mountain peak with checkered flag, achievement theme",
    }

    jobs: list[ImageJob] = []
    for ch in data["chapters"]:
        ch_id = ch["id"]
        ch_num = ch_id.split("-", 1)[0]
        theme_hint = stage_colors.get(ch_num, "QA quality assurance theme")
        prompt = (
            f"Cover illustration for a book chapter titled '{ch['title']}'. "
            f"Visual concept: {theme_hint}. "
            f"{BRAND_STYLE_SUFFIX}"
        )
        jobs.append(ImageJob(
            name=f"cover-{ch_id}",
            prompt=prompt,
            aspect_ratio="4:3",
            notes=f"Chapter {ch_num}: {ch['title']}",
        ))
    return jobs


def social_visual_jobs(chapter_id: str, series_dir: Path, n_variants: int = 2) -> list[ImageJob]:
    """Generate social media visual variants untuk satu chapter."""
    outline_path = series_dir / "outline.json"
    data = json.loads(outline_path.read_text(encoding="utf-8"))
    ch = next((c for c in data["chapters"] if c["id"] == chapter_id), None)
    if not ch:
        raise ValueError(f"Chapter id {chapter_id} tidak ada di outline")

    key_points = ch.get("key_points", [])
    jobs: list[ImageJob] = []
    for i in range(n_variants):
        kp = key_points[i % len(key_points)] if key_points else ch["title"]
        prompt = (
            f"Instagram square post visual for QA topic. "
            f"Headline concept: '{kp}'. {BRAND_STYLE_SUFFIX} "
            f"Strong central focal element, leave space at the bottom for text overlay."
        )
        jobs.append(ImageJob(
            name=f"social-{chapter_id}-v{i+1}",
            prompt=prompt,
            aspect_ratio="1:1",
            notes=f"Variant {i+1} for {ch['title']}",
        ))
    return jobs
