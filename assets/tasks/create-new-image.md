---
requires:
  - assets/brand-kit/README.md
  - assets/brand-kit/logos/README.md
  - assets/brand-kit/logos/LOGO-DESIGN-BRIEF.md
  - .codex/skills/generate-image-files/SKILL.md
  - .codex/skills/sync-website-assets/SKILL.md
---

# Add A New Brand SVG Asset

## Goal
- Add a new SVG to the brand kit with correct structure, naming, and usage notes, then generate PNG exports and sync website assets when the design is final.

## Preconditions
- New SVG design intent is approved or ready for iteration.
- SVG has no live `<text>` elements and uses the brand palette and type rules.
- Target folder and naming convention are known.

## Steps
1) Identify the correct base source folder and confirm whether the SVG belongs in `assets/brand-kit/logos/` or a use-case folder (`web/`, `social-media/`, `email-signature/`, `print/`, `favicon/`).
2) Identify the target folder for images generated from this svg from the user.
3) Add or update the SVG with paths only (no live text). Use Liberation Sans metrics for text-to-path conversions if needed.
4) Update the relevant README with usage notes and export guidance if the asset is new or changes expectations.
5) Iterate on the SVG design as needed until final.
6) Update `assets/brand-kit/exports-map.json` to map the newly added file to it target png file.  
7) Run the image generation workflow to export PNGs from the SVG sources.
8) Ask the user if the svg or images will be exported as assets to the website. If so, update `v1/src/assets/asst-source-map.json` to map the source file to the target asset file. 
9) Run the website asset sync workflow to push updated assets into `v1/src/assets/`.
10) Spot-check key outputs (exported PNG filenames, expected sizes, and website asset paths).

## Outputs
- New or updated SVG in the correct brand-kit folder.
- Updated README documentation for the asset.
- Regenerated PNG exports where required.
- Synced website assets under `v1/src/assets/`.

## Bookkeeping
- Verify `git status` shows the expected asset and README changes only.
