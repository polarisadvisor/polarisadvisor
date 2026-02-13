---
name: create-new-image
description: Add or update Polaris Advisor brand SVG assets in the brand kit. Use when creating or iterating on new SVG logo/icon variants, ensuring SVGs are path-only (no live text), updating brand-kit docs, and running the generate-image-files and sync-website-assets workflows to refresh PNG exports and website assets.
---

# Create Brand SVG

## Overview
Create or update a brand SVG asset with correct structure and naming, then regenerate PNG exports and sync website assets once the design is final.

## Required Context
Read these files at the start of the task:
- `assets/brand-kit/README.md`
- `assets/brand-kit/logos/README.md`
- `assets/brand-kit/logos/LOGO-DESIGN-BRIEF.md`
- `assets/tasks/create-new-image.md`

## SVG Rules
- Use paths only; no live `<text>` elements.
- Use Liberation Sans metrics for any text-to-path conversions.
- Match brand palette and typography rules from the brand kit.
- Follow the brand-kit naming conventions and place the SVG in the correct folder.

## Workflow
1) Identify the correct target folder (shared `assets/brand-kit/logos/` vs use-case folders like `web/`, `social-media/`, `email-signature/`, `print/`, `favicon/`).
2) Add or iterate on the SVG until the design is approved.
3) Update relevant README usage notes if the asset is new or changes expectations.
4) After design finalization, run the `generate-image-files` skill to regenerate PNG exports.
5) Run the `sync-website-assets` skill to update `v1/src/assets/`.
6) Spot-check output filenames and sizes before handing off.

## Notes
- Use the task file as the minimal checklist and the skills for deterministic exports/syncing.
- Do not edit `_site/` or `node_modules/`.
