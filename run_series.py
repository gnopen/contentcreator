"""
CLI untuk content-series mode.

Subcommands:
  generate-chapter --chapter 00-intro              # generate satu chapter
  generate-chapters                                # generate semua chapter (skip yang sudah ada)
  generate-social --chapter 00-intro --platforms twitter,linkedin
  generate-social-all --platforms twitter,linkedin
  compile-book                                     # gabung markdown -> PDF
  publish --chapter 00-intro --platforms twitter   # post ke socmed (default dry-run)
  status                                           # rekap state series

Contoh:
  python run_series.py status --series series/qa_thomas_journey
  python run_series.py generate-chapter --series series/qa_thomas_journey --chapter 00-intro
  python run_series.py compile-book --series series/qa_thomas_journey
  python run_series.py publish --series series/qa_thomas_journey --chapter 00-intro \\
      --platforms twitter,linkedin --dry-run
"""

import argparse
import json
import sys
from pathlib import Path

# Force UTF-8 untuk console Windows (default cp1252 tidak support emoji)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from agents import SeriesOrchestrator
from utils import get_logger

log = get_logger("series-cli")


def cmd_status(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series))
    outline = orch.outline
    print(f"\n📚 {outline.title}")
    if outline.subtitle:
        print(f"   {outline.subtitle}")
    print(f"   Author: {outline.author}\n")

    rows = []
    for ch in outline.chapters:
        chap_md = orch.chapters_dir / f"{ch.id}.md"
        posts_json = orch.social_dir / ch.id / "posts.json"
        chap_status = "✅" if chap_md.exists() else "⬜"
        posts_status = "✅" if posts_json.exists() else "⬜"
        rows.append((ch.id, ch.title, chap_status, posts_status))

    print(f"{'ID':<28} {'CHAPTER':<55} {'MD':<4} {'POSTS':<5}")
    print("-" * 95)
    for r in rows:
        print(f"{r[0]:<28} {r[1][:54]:<55} {r[2]:<4} {r[3]:<5}")

    book_md = orch.book_dir / f"{Path(args.series).name}.md"
    book_pdf = orch.book_dir / f"{Path(args.series).name}.pdf"
    print(f"\nBook MD:  {'✅ ' + str(book_md) if book_md.exists() else '⬜ belum dibuat'}")
    print(f"Book PDF: {'✅ ' + str(book_pdf) if book_pdf.exists() else '⬜ belum dibuat'}\n")
    return 0


def cmd_generate_chapter(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series))
    paths = orch.generate_chapters(only_id=args.chapter)
    for p in paths:
        print(f"✅ {p}")
    return 0


def cmd_generate_chapters(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series))
    paths = orch.generate_chapters()
    print(f"\n{len(paths)} chapter siap.")
    return 0


def cmd_generate_social(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series))
    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    posts = orch.generate_social(platforms=platforms, only_id=args.chapter)
    print(json.dumps({k: {p: len(v) for p, v in d.items()} for k, d in posts.items()}, indent=2))
    return 0


def cmd_compile_book(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series))
    md_path, pdf_path = orch.compile_book()
    print(f"✅ Markdown: {md_path}")
    if pdf_path:
        print(f"✅ PDF:      {pdf_path}")
    else:
        print("⚠️  PDF gagal di-compile (install weasyprint atau pandoc untuk dapat PDF)")
    return 0


def cmd_geo_audit(args: argparse.Namespace) -> int:
    """Audit existing posts.json terhadap aturan GEO."""
    from agents.geo_optimizer import check_caption
    from pathlib import Path as _P
    series = _P(args.series)
    chapters = [args.chapter] if args.chapter else [
        p.parent.name for p in sorted((series / "social").glob("*/posts.json"))
    ]
    any_fail = False
    for ch in chapters:
        pf = series / "social" / ch / "posts.json"
        if not pf.exists():
            print(f"⬜ {ch}: posts.json belum ada")
            continue
        data = json.loads(pf.read_text(encoding="utf-8"))
        print(f"\n📖 {ch}")
        for plat, posts in data.items():
            if not posts:
                continue
            text = posts[-1] if plat == "twitter" else posts[0]
            r = check_caption(text, plat)
            flag = "✅" if r.passes else "⚠️"
            print(f"  {flag} {plat:10s} score={r.score}/100")
            if not r.passes:
                any_fail = True
                for f in r.findings[:3]:
                    print(f"      - {f}")
                print(f"      Suggested: {' '.join(r.suggested_hashtags[:5])}")
    return 0 if not any_fail else 0  # audit informational, jangan fail CLI


def cmd_geo_upgrade(args: argparse.Namespace) -> int:
    """Upgrade hashtag block sesuai GEO bank."""
    from agents.geo_optimizer import upgrade_posts_file
    from pathlib import Path as _P
    series = _P(args.series)
    chapters = [args.chapter] if args.chapter else [
        p.parent.name for p in sorted((series / "social").glob("*/posts.json"))
    ]
    for ch in chapters:
        pf = series / "social" / ch / "posts.json"
        if not pf.exists():
            continue
        s = upgrade_posts_file(pf)
        print(f"✅ {ch}: upgraded {list(s.keys())}")
    return 0


def cmd_publish(args: argparse.Namespace) -> int:
    orch = SeriesOrchestrator(Path(args.series), dry_run=args.dry_run)
    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    results = orch.publish_chapter(args.chapter, platforms)
    any_fail = False
    for r in results:
        flag = "OK " if r.success else "FAIL"
        line = f"[{flag}] {r.platform:10s} id={r.post_id or '-'}"
        if r.error:
            line += f" error={r.error}"
            any_fail = True
        if r.url:
            line += f" {r.url}"
        print(line)
    return 1 if any_fail else 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Content-series CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_series(sp):
        sp.add_argument("--series", required=True, help="Path direktori series, mis. series/qa_thomas_journey")

    s = sub.add_parser("status")
    add_series(s); s.set_defaults(func=cmd_status)

    s = sub.add_parser("generate-chapter")
    add_series(s); s.add_argument("--chapter", required=True); s.set_defaults(func=cmd_generate_chapter)

    s = sub.add_parser("generate-chapters")
    add_series(s); s.set_defaults(func=cmd_generate_chapters)

    s = sub.add_parser("generate-social")
    add_series(s); s.add_argument("--chapter", required=True)
    s.add_argument("--platforms", default="twitter,linkedin")
    s.set_defaults(func=cmd_generate_social)

    s = sub.add_parser("generate-social-all")
    add_series(s); s.add_argument("--platforms", default="twitter,linkedin")
    s.add_argument("--chapter", default=None)  # optional filter
    s.set_defaults(func=cmd_generate_social)

    s = sub.add_parser("compile-book")
    add_series(s); s.set_defaults(func=cmd_compile_book)

    s = sub.add_parser("publish")
    add_series(s); s.add_argument("--chapter", required=True)
    s.add_argument("--platforms", required=True)
    s.add_argument("--dry-run", action="store_true", default=True)
    s.add_argument("--live", dest="dry_run", action="store_false",
                   help="Hapus dry-run, posting beneran")
    s.set_defaults(func=cmd_publish)

    s = sub.add_parser("geo-audit",
                       help="Audit posts.json terhadap aturan GEO (caption+hashtag)")
    add_series(s); s.add_argument("--chapter", default=None,
                                  help="Chapter id, kosong = semua chapter")
    s.set_defaults(func=cmd_geo_audit)

    s = sub.add_parser("geo-upgrade",
                       help="Apply GEO hashtag bank ke posts.json yang sudah ada")
    add_series(s); s.add_argument("--chapter", default=None)
    s.set_defaults(func=cmd_geo_upgrade)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
