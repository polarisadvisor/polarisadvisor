---
name: sync-website-assets
description: "Sync website assets in v1/src/assets from brand-kit sources using sync_assets.py. Use when updating site images, favicons, OG images, or when asked to sync website assets."
---

# Sync Website Assets

## Preconditions
- Confirm `v1/src/assets/asset-source-map.json` is up to date.
- Ensure brand-kit source assets exist at the mapped paths.
- Do not modify SVG sources in this workflow.

## Run The Sync
- Inspect planned changes:
  - `python3 v1/src/assets/sync_assets.py --verify`
- Sync assets:
  - `python3 v1/src/assets/sync_assets.py`
- Review diffs:
  - `git status`

## Bookkeeping
- If mappings change, update `v1/src/assets/asset-source-map.json`.
