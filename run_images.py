"""
CLI untuk image batch generation pakai Gemini "Nano Banana 2".

Sub-commands:
  chapter-covers   Generate cover image untuk SEMUA chapter (10 image).
  social-visuals   Generate 2 variant visual untuk 1 chapter.
  custom           Generate dari prompt list di file JSON.

Output: folder images/YYYY-MM-DD/ otomatis dibuat per tanggal saat run.

Catatan billing:
- Image generation Gemini (Nano Banana 1 & 2) saat ini hanya tersedia
  di PAID TIER. Aktifkan di https://aistudio.google.com/app/billing
- Pakai --dry-run untuk preview prompt list tanpa panggil API.

Contoh:
  python run_images.py chapter-covers --series series/qa_thomas_journey --dry-run
  python run_images.py chapter-covers --series series/qa_thomas_journey
  python run_images.py social-visuals --series series/qa_thomas_journey --chapter 00-intro --variants 3
  python run_images.py custom --prompts my-prompts.json
"""

import argparse
import json
import sys
from pathlib import Path

# UTF-8 console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from agents.image_batch_agent import (
    ImageBatchAgent,
    ImageJob,
    chapter_cover_jobs,
    social_visual_jobs,
)
from utils import get_logger

log = get_logger("images-cli")


def _print_results(results) -> int:
    ok = sum(1 for r in results if r.success)
    fail = len(results) - ok
    print()
    for r in results:
        flag = "✅" if r.success else "❌"
        line = f"{flag} {r.name:40s}"
        if r.file and r.success:
            line += f"  {r.file}"
        if r.error:
            line += f"  ERR: {r.error[:120]}"
        print(line)
    print(f"\nTotal: {len(results)} | OK: {ok} | FAIL: {fail}")
    return 0 if fail == 0 else 1


def cmd_chapter_covers(args):
    jobs = chapter_cover_jobs(Path(args.series))
    agent = ImageBatchAgent(
        base_dir=Path(args.output),
        dry_run=args.dry_run,
        throttle_seconds=args.throttle,
    )
    print(f"Akan generate {len(jobs)} cover (chapter), ratio 4:3.")
    if args.dry_run:
        print("[DRY-RUN] tidak panggil API.")
    return _print_results(agent.run(jobs))


def cmd_social_visuals(args):
    jobs = social_visual_jobs(args.chapter, Path(args.series), n_variants=args.variants)
    agent = ImageBatchAgent(
        base_dir=Path(args.output),
        dry_run=args.dry_run,
        throttle_seconds=args.throttle,
    )
    print(f"Akan generate {len(jobs)} visual untuk chapter '{args.chapter}', ratio 1:1.")
    if args.dry_run:
        print("[DRY-RUN] tidak panggil API.")
    return _print_results(agent.run(jobs))


def cmd_custom(args):
    data = json.loads(Path(args.prompts).read_text(encoding="utf-8"))
    jobs = [ImageJob(**item) for item in data]
    agent = ImageBatchAgent(
        base_dir=Path(args.output),
        dry_run=args.dry_run,
        throttle_seconds=args.throttle,
    )
    print(f"Akan generate {len(jobs)} image dari {args.prompts}.")
    if args.dry_run:
        print("[DRY-RUN] tidak panggil API.")
    return _print_results(agent.run(jobs))


def _add_common(s):
    s.add_argument("--output", default="images", help="Root dir output (default: images/)")
    s.add_argument("--dry-run", action="store_true",
                   help="Skip API, hanya tulis manifest")
    s.add_argument("--throttle", type=float, default=2.0,
                   help="Sleep detik antar request (default 2.0)")


def build_parser():
    p = argparse.ArgumentParser(description="Image batch generation via Gemini Nano Banana")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("chapter-covers")
    s.add_argument("--series", required=True)
    _add_common(s)
    s.set_defaults(func=cmd_chapter_covers)

    s = sub.add_parser("social-visuals")
    s.add_argument("--series", required=True)
    s.add_argument("--chapter", required=True)
    s.add_argument("--variants", type=int, default=2)
    _add_common(s)
    s.set_defaults(func=cmd_social_visuals)

    s = sub.add_parser("custom")
    s.add_argument("--prompts", required=True,
                   help="File JSON berisi list of {name,prompt,aspect_ratio,notes}")
    _add_common(s)
    s.set_defaults(func=cmd_custom)

    return p


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
