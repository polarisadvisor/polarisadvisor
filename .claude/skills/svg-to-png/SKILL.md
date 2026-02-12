---
name: svg-to-png
description: "Convert SVG files to PNG at specified sizes and resolutions using rsvg-convert. Use when generating PNGs from SVG sources for favicons, social media assets, web logos, print exports, or any other rasterization task in this project."
---

# SVG to PNG Conversion

This project uses `rsvg-convert` (from `librsvg2-bin`) as the standard tool for converting SVG to PNG. Do not use ImageMagick, Inkscape, or other tools unless explicitly asked.

## Setup

Before running any conversion, ensure `rsvg-convert` is available:

```bash
if ! command -v rsvg-convert &> /dev/null; then
    sudo apt-get update -qq && sudo apt-get install -y -qq librsvg2-bin
fi
```

Always run this check at the start of a conversion task. Do not skip it.

## Usage

### Fixed width (height auto-calculated from aspect ratio)
```bash
rsvg-convert -w 500 -o output.png input.svg
```

### Fixed height (width auto-calculated from aspect ratio)
```bash
rsvg-convert -h 200 -o output.png input.svg
```

### Exact dimensions (may distort if aspect ratio differs)
```bash
rsvg-convert -w 500 -h 500 -o output.png input.svg
```

### High-DPI / retina (2x)
```bash
rsvg-convert -w 1000 -h 1000 -o output@2x.png input.svg
```

## Project Conventions

### Brand kit location
All baseline SVG sources live in `assets/brand-kit/logos/`. Use-case-specific SVGs and exported PNGs are organized by folder:

```
assets/brand-kit/
  logos/           SVG source files
  favicon/         Browser favicons and app icons
  social-media/    Profile, cover, OG images
  email-signature/ Email logos
  web/             Website assets
  print/           High-resolution print assets
```

### Naming conventions
- Source files: `polaris-{type}-{variant}.svg` (e.g., `polaris-logo-horizontal.svg`)
- Exported PNGs: `{use-case}-{dimensions}.png` (e.g., `profile-500x500.png`, `logo-web-2x.png`)
- Keep filenames consistent with each folder's README instructions.

### SVG authoring rules
- **Never generate SVGs with live `<text>` elements.** Convert all text to `<path>` elements before export to avoid font rendering differences across environments.
- Always verify the source SVG renders correctly before batch-exporting PNGs.

### Export inventory
See `assets/brand-kit/EXPORTS.md` for the full inventory of PNGs and their source SVGs. Update it when adding new exports.

## Common Tasks

### Regenerate all favicons
```bash
cd assets/brand-kit/favicon
for size in 16 32 48; do
    rsvg-convert -w $size -h $size -o favicon-${size}x${size}.png polaris-icon.svg
done
rsvg-convert -w 180 -h 180 -o apple-touch-icon.png polaris-icon.svg
rsvg-convert -w 192 -h 192 -o android-chrome-192x192.png polaris-icon.svg
rsvg-convert -w 512 -h 512 -o android-chrome-512x512.png polaris-icon.svg
```

### Regenerate web logos (1x, 2x, 3x)
```bash
cd assets/brand-kit/web
for variant in "" "-dark"; do
    src="polaris-logo-horizontal${variant}.svg"
    tag="${variant:+-dark}"  # empty or "-dark"
    rsvg-convert -h 72  -o "logo-web${tag:--}1x.png" "$src"
    rsvg-convert -h 144 -o "logo-web${tag:--}2x.png" "$src"
    rsvg-convert -h 216 -o "logo-web${tag:--}3x.png" "$src"
done
```

### Single conversion
```bash
rsvg-convert -w 1200 -h 630 -o og-image.png source.svg
```

## Troubleshooting

### "command not found: rsvg-convert"
Run the setup step above. The library (`librsvg2-2`) is often pre-installed but the CLI binary (`librsvg2-bin`) may not be.

### Blank or broken output
The source SVG likely uses `<text>` elements with fonts not available in this environment. Convert text to paths in the SVG source first.

### Wrong dimensions
`rsvg-convert` preserves aspect ratio when only `-w` or `-h` is given. Use both flags together only when you need exact pixel dimensions and accept potential distortion.
