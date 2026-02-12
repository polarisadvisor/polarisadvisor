---
requires:
  - assets/skills/sync-website-assets.md
# models:
#   - openai:gpt-4o-mini
#   - anthropic:claude-3-haiku
---

# Sync Website Assets (Agent Task)

## Goal
- Sync deployed website assets from the canonical brand-kit sources.

## Preconditions
- The asset source map is correct: `v1/src/assets/asset-source-map.json`.
- This task does not modify SVG sources; it only syncs files.

## Steps
1) Inspect planned changes:
   - `python3 v1/src/assets/sync_assets.py --verify`
2) Sync assets:
   - `python3 v1/src/assets/sync_assets.py`
3) Review diffs:
   - `git status`

## Outputs
- Updated files under `v1/src/assets/`.

## Bookkeeping
- If mappings are updated, update `v1/src/assets/asset-source-map.json`.
