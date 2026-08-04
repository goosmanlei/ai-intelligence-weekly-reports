#!/usr/bin/env python3
import argparse
import re
from datetime import datetime
from pathlib import Path


DATE_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2})(?=\.pdf$)")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True)
    parser.add_argument("--keep", type=int, default=10)
    parser.add_argument(
        "--pattern",
        action="append",
        help="Glob pattern for matching PDF files. Can be passed multiple times.",
    )
    return parser.parse_args()


def sort_key(path: Path):
    match = DATE_PATTERN.search(path.name)
    if match:
        report_date = datetime.strptime(match.group(1), "%Y-%m-%d")
    else:
        report_date = datetime.min
    return report_date, path.stat().st_mtime, path.name


def main():
    args = parse_args()
    target_dir = Path(args.dir)
    patterns = args.pattern or [
        "global-china-ai-weekly-*.pdf",
        "ai-frontiers-weekly-*.pdf",
        "anthropic-claude-code-x-weekly-*.pdf",
    ]
    files = sorted(
        {
            path
            for pattern in patterns
            for path in target_dir.glob(pattern)
        },
        key=sort_key,
    )
    stale_files = files[:-args.keep] if args.keep > 0 else files
    for path in stale_files:
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
