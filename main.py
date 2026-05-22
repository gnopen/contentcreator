"""
CLI entrypoint untuk Content Creator Agent System.

Contoh:
    python main.py --topic "Tips produktivitas remote working" \
        --platforms twitter,linkedin --dry-run

    python main.py --topic "Promo flash sale akhir bulan" \
        --platforms twitter,facebook,linkedin \
        --tone "santai tapi persuasif" \
        --audience "anak muda 18-30"
"""

import argparse
import json
import sys
from datetime import datetime

from agents import Orchestrator
from utils import get_logger

log = get_logger("main")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Content Creator Agent System")
    p.add_argument("--topic", required=True, help="Topik / brief konten")
    p.add_argument(
        "--platforms",
        default="twitter,linkedin",
        help="Comma-separated: twitter,instagram,facebook,linkedin",
    )
    p.add_argument("--tone", default="engaging dan profesional")
    p.add_argument("--audience", default="umum")
    p.add_argument("--language", default="Indonesia")
    p.add_argument("--context", default=None, help="Konteks tambahan (opsional)")
    p.add_argument(
        "--image",
        action="append",
        default=[],
        help="Format: platform=path_or_url (boleh diulang)",
    )
    p.add_argument(
        "--schedule",
        default=None,
        help="Jadwal posting ISO format, mis. 2026-05-22T09:00:00",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Jangan benar-benar posting; cukup tampilkan preview",
    )
    p.add_argument(
        "--output-json",
        default=None,
        help="Simpan ContentPackage + hasil ke file JSON",
    )
    return p.parse_args()


def parse_image_args(items: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            log.warning("Skipping invalid --image %r (perlu format platform=path)", item)
            continue
        k, v = item.split("=", 1)
        out[k.strip().lower()] = v.strip()
    return out


def main() -> int:
    args = parse_args()
    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    images = parse_image_args(args.image)
    post_at = datetime.fromisoformat(args.schedule) if args.schedule else None

    orch = Orchestrator(dry_run=args.dry_run)
    package, results = orch.run(
        topic=args.topic,
        platforms=platforms,
        tone=args.tone,
        target_audience=args.audience,
        language=args.language,
        extra_context=args.context,
        image_paths=images,
        post_at=post_at,
    )

    print("\n========== GENERATED CONTENT ==========")
    print(json.dumps(package.to_dict(), indent=2, ensure_ascii=False))

    print("\n========== POSTING RESULTS ==========")
    any_failure = False
    for r in results:
        status = "OK " if r.success else "FAIL"
        line = f"[{status}] {r.platform:10s} id={r.post_id or '-'}"
        if r.url:
            line += f"  {r.url}"
        if r.error:
            line += f"  error={r.error}"
            any_failure = True
        print(line)

    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "package": package.to_dict(),
                    "results": [r.__dict__ for r in results],
                },
                fh,
                indent=2,
                ensure_ascii=False,
            )
        log.info("Output disimpan ke %s", args.output_json)

    return 1 if any_failure else 0


if __name__ == "__main__":
    sys.exit(main())
