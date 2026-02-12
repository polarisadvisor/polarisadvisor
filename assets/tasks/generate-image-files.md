---
requires:
  - assets/skills/regenerate-image-files.md
---

# SVG → Image Regeneration (Agent Task)

This task is the canonical, **bullet‑proof** process for regenerating PNGs from SVGs in this repo. Follow every step in order.

## 1) Confirm Source Map (No SVG Edits)
- Regeneration must not modify or restructure SVG sources.
- If SVG consolidation or creation is needed, stop and use the separate “create source image” task.

## 2) Update the Automation Map (Authoritative for Scripts)
- `assets/brand-kit/exports-map.json` is the source→output map for automation.
- Add or edit entries for every PNG that should be generated.
- Ensure all new outputs are listed here **before** regeneration.

## 3) Regenerate PNGs (CLI)
- Script: `assets/brand-kit/scripts/export_pngs.py`
- Uses `rsvg-convert` (librsvg). If missing, install it or set `rsvg_convert` in the JSON.
- For usage and options, run:
  - `python3 assets/brand-kit/scripts/export_pngs.py --help`
- Common modes:
  - Full regen: `python3 assets/brand-kit/scripts/export_pngs.py`
  - Only missing: `python3 assets/brand-kit/scripts/export_pngs.py --missing`
  - Only changed SVGs: `python3 assets/brand-kit/scripts/export_pngs.py --delta-only`
  - Dry run: `python3 assets/brand-kit/scripts/export_pngs.py --dry-run`

## 4) Verify Outputs
- Run: `python3 assets/brand-kit/scripts/export_pngs.py --verify`
- If anything is missing, fix the map or sources and regenerate.

## 5) Update the Human Contract (Authoritative for Humans)
- `assets/brand-kit/EXPORTS.md` is the authoritative human‑readable export contract.
- Update it after every regen:
  - File list and counts must match actual files.
  - File sizes must be refreshed if outputs changed.
  - Mark missing outputs only if they truly don’t exist.
  - Keep “Source Notes” accurate (shared `logos/` vs folder‑specific sources).
- Always review the `EXPORTS.md` diff after regeneration.

## 6) Update Folder READMEs
- Each folder README must describe outputs in that folder.
- If a PNG is derived from a shared SVG in `logos/`, the README must point to the shared source.
- If a folder has custom SVGs, list them explicitly as folder‑specific.

## 7) Final Consistency Check
- `git status` should show only expected diffs.
- `EXPORTS.md` and `exports-map.json` must agree.
