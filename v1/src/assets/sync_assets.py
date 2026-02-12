#!/usr/bin/env python3
import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MAP = ROOT / 'v1' / 'src' / 'assets' / 'asset-source-map.json'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Sync website assets from brand-kit sources based on asset-source-map.json.',
    )
    parser.add_argument(
        '--map',
        default=str(DEFAULT_MAP),
        help='Path to asset-source-map.json (default: v1/src/assets/asset-source-map.json)',
    )
    parser.add_argument(
        '--only',
        default=None,
        help='Filter mappings by substring match on source or dest path',
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List planned sync actions without copying files',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would change without copying files',
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Report which dest files differ from source or are missing',
    )
    parser.add_argument(
        '--missing',
        action='store_true',
        help='Only list missing or differing dest files (implies --verify)',
    )
    return parser.parse_args()


def load_map(path: Path) -> dict:
    if not path.exists():
        print(f"Missing map file: {path}")
        sys.exit(1)
    return json.loads(path.read_text())


def files_identical(src: Path, dest: Path) -> bool:
    if not src.exists() or not dest.exists():
        return False
    if src.stat().st_size != dest.stat().st_size:
        return False
    return src.read_bytes() == dest.read_bytes()


def main() -> int:
    args = parse_args()
    map_path = Path(args.map)
    data = load_map(map_path)

    base_dir = Path(data.get('base_dir', '.'))
    mappings = data.get('mappings', [])
    if not mappings:
        print('No mappings found.')
        return 1

    planned = []
    for entry in mappings:
        src = ROOT / base_dir / entry['source']
        dest = ROOT / base_dir / entry['dest']
        planned.append((src, dest))

    if args.only:
        needle = args.only
        planned = [
            (src, dest) for (src, dest) in planned
            if needle in str(src) or needle in str(dest)
        ]

    if args.list:
        for src, dest in planned:
            print(f"{src} -> {dest}")
        return 0

    if args.missing:
        args.verify = True

    if args.verify:
        rows = []
        for src, dest in planned:
            status = 'OK' if files_identical(src, dest) else 'MISSING/DIFF'
            rows.append((status, src, dest))
        if args.missing:
            rows = [r for r in rows if r[0] != 'OK']
        for status, src, dest in rows:
            print(f"[{status}] {src} -> {dest}")
        return 0

    for src, dest in planned:
        if not src.exists():
            print(f"Missing source: {src}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if args.dry_run:
            action = 'update' if dest.exists() else 'create'
            print(f"[DRY-RUN] {action}: {dest} <- {src}")
        else:
            shutil.copy2(src, dest)
            print(f"synced: {dest}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
