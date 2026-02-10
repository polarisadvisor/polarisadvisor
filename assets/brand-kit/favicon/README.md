# Favicon Assets

## Source Files
- `polaris-icon.svg` - Icon only (light backgrounds)
- `polaris-icon-dark.svg` - Icon only (dark backgrounds)

## Required Export Sizes (PNG)

Export `polaris-icon.svg` to:
- `favicon-16x16.png` (16×16px)
- `favicon-32x32.png` (32×32px)
- `favicon-48x48.png` (48×48px)
- `apple-touch-icon.png` (180×180px)
- `android-chrome-192x192.png` (192×192px)
- `android-chrome-512x512.png` (512×512px)

## Usage
- **Web favicon**: Use 16×16, 32×32, 48×48
- **Apple touch icon**: Use 180×180
- **Android icons**: Use 192×192 and 512×512
- **PWA manifest**: Reference android-chrome sizes

## Export Command Example
```bash
# Using ImageMagick or similar:
convert polaris-icon.svg -resize 16x16 favicon-16x16.png
convert polaris-icon.svg -resize 32x32 favicon-32x32.png
convert polaris-icon.svg -resize 180x180 apple-touch-icon.png
```
