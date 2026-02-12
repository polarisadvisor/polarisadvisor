---
name: generate-image-files
description: Regenerate PNG image exports from brand SVG sources using the brand-kit export script. Use when updating brand assets, syncing website assets, or needing deterministic SVG-to-PNG exports for web, social, favicon, email, or print deliverables. Covers prerequisites, running the CLI, and required post-run bookkeeping.
---

# Generate Image Files

## Read First
- Review `assets/brand-kit/README.md` for asset usage and export guidelines.
- Follow the workflow in `assets/skills/generate-image-files.md` for end-to-end steps and context.

## Preconditions
- Ensure `assets/brand-kit/exports-map.json` reflects the desired source-to-target mappings.
- Ensure `rsvg-convert` is available, or set `rsvg_convert` in the JSON.

## Run the Export Script
- Use the CLI help to confirm options:

```bash
python3 assets/brand-kit/scripts/export_pngs.py --help
```

- Run the script with the needed flags per the help output.

## Post-Run Requirements
- Update `assets/brand-kit/EXPORTS.md` for any output changes.
- Ensure folder READMEs still point to correct shared sources.
- Review `git status` and keep only expected diffs.

## Scope
- Do not create or modify SVG sources in this workflow.
