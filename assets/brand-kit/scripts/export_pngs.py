#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MAP_PATH = ROOT / 'assets' / 'brand-kit' / 'exports-map.json'


def find_rsvg_convert(config_path: str) -> str:
    preferred = Path(config_path)
    if preferred.exists():
        return str(preferred)
    return 'rsvg-convert'


def ensure_rsvg_convert(cmd: str) -> str:
    if cmd == 'rsvg-convert':
        result = subprocess.run(['which', cmd], capture_output=True, text=True)
        resolved = result.stdout.strip() if result.returncode == 0 else None
    else:
        resolved = cmd
    if resolved and Path(resolved).exists():
        return resolved
    print('rsvg-convert not found. Install librsvg or set "rsvg_convert" in exports-map.json.')
    print('macOS: brew install librsvg')
    print('Linux: apt-get install librsvg2-bin')
    raise FileNotFoundError('rsvg-convert not available')


def build_cmd(rsvg: str, src: Path, out: Path, width: int | None, height: int | None) -> list[str]:
    cmd = [rsvg]
    if width:
        cmd += ['-w', str(width)]
    if height:
        cmd += ['-h', str(height)]
    cmd += ['-o', str(out), str(src)]
    return cmd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Generate PNG exports from SVG sources using exports-map.json.',
    )
    parser.add_argument(
        '--map',
        default=str(DEFAULT_MAP_PATH),
        help='Path to exports-map.json (default: repo assets/brand-kit/exports-map.json)',
    )
    parser.add_argument(
        '--rsvg',
        default=None,
        help='Path to rsvg-convert (overrides map setting)',
    )
    parser.add_argument(
        '--only',
        default=None,
        help='Filter exports by substring match on source or output path',
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List planned export actions without running them',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print commands without executing them',
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Report which outputs are missing without generating them',
    )
    parser.add_argument(
        '--missing',
        action='store_true',
        help='Only list missing outputs (implies --verify)',
    )
    parser.add_argument(
        '--delta-only',
        action='store_true',
        help='Only process outputs whose source SVGs have changed in git',
    )
    return parser.parse_args()


def git_changed_files(repo_root: Path) -> set[str]:
    changed = set()
    # Unstaged changes
    result = subprocess.run(['git', 'diff', '--name-only'], cwd=repo_root, capture_output=True, text=True)
    if result.returncode == 0:
        changed.update(line.strip() for line in result.stdout.splitlines() if line.strip())
    # Staged changes
    result = subprocess.run(['git', 'diff', '--name-only', '--cached'], cwd=repo_root, capture_output=True, text=True)
    if result.returncode == 0:
        changed.update(line.strip() for line in result.stdout.splitlines() if line.strip())
    # Untracked files
    result = subprocess.run(['git', 'status', '--porcelain'], cwd=repo_root, capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            if line.startswith('?? '):
                changed.add(line[3:].strip())
    return changed


def main() -> int:
    args = parse_args()
    map_path = Path(args.map)

    if not map_path.exists():
        print(f"Missing map file: {map_path}")
        return 1

    data = json.loads(map_path.read_text())
    base_dir = ROOT / data.get('base_dir', 'assets/brand-kit')

    rsvg_config = args.rsvg or data.get('rsvg_convert', 'rsvg-convert')
    rsvg = ensure_rsvg_convert(find_rsvg_convert(rsvg_config))

    exports = data.get('exports', [])
    if not exports:
        print('No exports configured.')
        return 1

    planned = []
    for item in exports:
        src = base_dir / item['source']
        for out in item.get('outputs', []):
            out_path = base_dir / out['path']
            width = out.get('width')
            height = out.get('height')
            planned.append((src, out_path, width, height))

    if args.only:
        needle = args.only
        planned = [
            (src, out_path, width, height)
            for (src, out_path, width, height) in planned
            if needle in str(src) or needle in str(out_path)
        ]

    if args.delta_only:
        changed = git_changed_files(ROOT)
        planned = [
            (src, out_path, width, height)
            for (src, out_path, width, height) in planned
            if str(src.relative_to(ROOT)) in changed
        ]
        if not planned:
            print('No changed source SVGs detected.')
            return 0

    if args.list:
        for src, out_path, width, height in planned:
            print(f"{src} -> {out_path} ({width or ''}x{height or ''})")
        return 0

    if args.missing:
        args.verify = True

    if args.verify:
        missing = []
        for src, out_path, width, height in planned:
            if not out_path.exists():
                missing.append((src, out_path, width, height))
        if args.missing:
            for src, out_path, width, height in missing:
                print(f"{src} -> {out_path} ({width or ''}x{height or ''})")
        else:
            for src, out_path, width, height in planned:
                status = 'MISSING' if not out_path.exists() else 'OK'
                print(f"[{status}] {src} -> {out_path} ({width or ''}x{height or ''})")
        return 0

    for src, out_path, width, height in planned:
        if not src.exists():
            print(f"Missing source SVG: {src}")
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = build_cmd(rsvg, src, out_path, width, height)
        print(' '.join(cmd))
        if not args.dry_run:
            subprocess.run(cmd, check=True)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
