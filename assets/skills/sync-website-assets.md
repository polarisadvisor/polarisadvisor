# Skill: Sync Website Assets (CLI Wrapper)

Purpose: Keep website assets in v1/src/assets in sync with brand-ket assets using the tool  `v1/src/assets/sync_assets.py`.

## Preconditions
- `v1/src/assets/asset-source-map.json` is up to date.
- Brand-kit source assets exist at the mapped paths.

## How To Use
Run the CLI help and follow its instructions:

```
python3 v1/src/assets/sync_assets.py --help
```

## Post-Run Requirements (Bookkeeping)
- Review `git status` and keep only expected diffs.
- If mappings change, update `v1/src/assets/asset-source-map.json`.
