# SVG → Image Regeneration Workflow

This is the canonical process for regenerating PNGs (and other raster outputs) from SVGs in the brand-kit.

## 1) Shared SVG Sources
- Shared base SVGs live in `assets/brand-kit/logos/`.
- If an SVG is used in more than one place, keep it in `logos/` and reference it from local folder READMEs.
- Folder-local SVGs are allowed only if they are **unique to that folder’s PNG outputs** (e.g., LinkedIn-specific cover layouts).
- Do not duplicate shared SVGs across folders.

## 2) Human Export Contract
- `assets/brand-kit/EXPORTS.md` is the authoritative human-readable export contract.
- It must match the actual assets and folder contents.
- Update it any time outputs change.

## 3) Automation Map
- `assets/brand-kit/exports-map.json` is the authoritative source→output map for scripts.
- Every automated PNG export must be listed here.
- Keep it consistent with `EXPORTS.md`.

## 4) Regenerate PNGs
- Script: `assets/brand-kit/scripts/export_pngs.py`
- Uses `rsvg-convert` (librsvg). If it isn’t on PATH, install librsvg or set `rsvg_convert` in the JSON.
- Run:
  - `python3 assets/brand-kit/scripts/export_pngs.py`

## 5) Verify & Reconcile
- Confirm files exist and are correctly sized.
- Update `EXPORTS.md` if any output set changes.
- Always review the `EXPORTS.md` diff after regeneration.
- Ensure `EXPORTS.md` reflects shared-source usage (e.g., `logos/` as the origin for shared SVGs).

## 6) Folder READMEs
- Each folder README should describe outputs **in that folder**.
- If a PNG is derived from a shared SVG in `logos/`, the README must point to the shared source.
