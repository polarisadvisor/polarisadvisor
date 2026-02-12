#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / 'assets' / 'brand-kit' / 'exports-map.json'


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


def main() -> int:
    if not MAP_PATH.exists():
        print(f"Missing map file: {MAP_PATH}")
        return 1

    data = json.loads(MAP_PATH.read_text())
    base_dir = ROOT / data.get('base_dir', 'assets/brand-kit')
    rsvg = ensure_rsvg_convert(find_rsvg_convert(data.get('rsvg_convert', 'rsvg-convert')))

    exports = data.get('exports', [])
    if not exports:
        print('No exports configured.')
        return 1

    for item in exports:
        src = base_dir / item['source']
        if not src.exists():
            print(f"Missing source SVG: {src}")
            continue

        for out in item.get('outputs', []):
            out_path = base_dir / out['path']
            out_path.parent.mkdir(parents=True, exist_ok=True)
            width = out.get('width')
            height = out.get('height')
            cmd = build_cmd(rsvg, src, out_path, width, height)
            print(' '.join(cmd))
            subprocess.run(cmd, check=True)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
