# Favicon Assets

## Source Files
Shared sources in `/logos/`:
- `logos/polaris-icon.svg` - Icon only (light)
- `logos/polaris-icon-dark.svg` - Icon only (dark)
- `logos/polaris-icon-favicon.svg` - Favicon-sized icon (light)
- `logos/polaris-icon-tiny.svg` - Tiny favicon icon (light)

## Required Export Sizes (PNG)

Export from the shared sources as follows:
- `favicon-16x16.png` (16×16px) ← `logos/polaris-icon-tiny.svg`
- `favicon-32x32.png` (32×32px) ← `logos/polaris-icon-favicon.svg`
- `favicon-48x48.png` (48×48px) ← `logos/polaris-icon-favicon.svg`
- `apple-touch-icon.png` (180×180px) ← `logos/polaris-icon.svg`
- `android-chrome-192x192.png` (192×192px) ← `logos/polaris-icon.svg`
- `android-chrome-512x512.png` (512×512px) ← `logos/polaris-icon.svg`

## Usage
- **Web favicon**: Use 16×16, 32×32, 48×48
- **Apple touch icon**: Use 180×180
- **Android icons**: Use 192×192 and 512×512
- **PWA manifest**: Reference android-chrome sizes

