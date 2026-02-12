# Skill: Regenerate Image Files (CLI Wrapper)

Purpose: Use `assets/brand-kit/scripts/export_pngs.py` to create pngs from svgs,

## Preconditions
- The source to target mapping in `assets/brand-kit/exports-map.json` is up to date.
- `rsvg-convert` is available (or `rsvg_convert` is configured in the JSON).

## How To Use
Run the CLI help and follow its instructions:

```
python3 assets/brand-kit/scripts/export_pngs.py --help
```

## Post-Run Requirements (Bookkeeping)
- Update `assets/brand-kit/EXPORTS.md` for any output changes.
- Ensure folder READMEs still point to correct shared sources.
- Review `git status` and keep only expected diffs.

## Notes
- This skill does not create or modify SVG sources. 
