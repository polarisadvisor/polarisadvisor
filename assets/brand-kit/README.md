# Polaris Advisor Brand Kit

Complete brand assets organized by use case.

## Folder Structure

```
brand-kit/
├── logos/              Baseline SVG source files (light & dark)
├── favicon/            Browser favicons and app icons
├── social-media/       Social platform assets (profile, cover, OG images)
├── email-signature/    Email signature logos
├── web/                Website assets (SVG & PNG)
└── print/              High-resolution print assets
```

## Quick Start

### For Web Use
→ Use `/web/polaris-logo-horizontal.svg` directly in your website
→ SVG is preferred (scalable, small, retina-ready)

### For Social Media
→ Export `/social-media/profile/polaris-logo.svg` to 500×500px PNG
→ Export `/social-media/cover/polaris-logo-horizontal.svg` to platform specs

### For Favicons
→ Export `/favicon/polaris-icon.svg` to required PNG sizes (see folder README)

### For Email
→ Export `/email-signature/polaris-logo-horizontal.svg` to ~200px height PNG

### For Print
→ Use SVGs from `/print/` or export to 300 DPI PNG/PDF

## Baseline Logo Files

Located in `/logos/`:

### Primary Logos
- `polaris-logo-horizontal.svg` - **Primary** horizontal lockup (light bg)
- `polaris-logo-horizontal-dark.svg` - Horizontal lockup (dark bg)
- `polaris-logo-vertical.svg` - Medium vertical lockup
- `polaris-logo.svg` - Compact vertical lockup

### Supporting
- `polaris-icon.svg` - Icon only (light bg)
- `polaris-icon-dark.svg` - Icon only (dark bg)

## Brand Colors

| Color | Hex | RGB | Use |
|-------|-----|-----|-----|
| Primary | `#1a3a52` | 26, 58, 82 | Main brand color, text |
| Primary Light | `#2d5270` | 45, 82, 112 | Hover states |
| Accent | `#4a7c9e` | 74, 124, 158 | Star center, accents |
| Secondary Text | `#5a6c7d` | 90, 108, 125 | "ADVISOR" text |
| White | `#ffffff` | 255, 255, 255 | Dark mode, backgrounds |

## Typography

- **Font Family**: -apple-system, 'Helvetica Neue', Arial, sans-serif
- **"Polaris"**: 600 weight (Semibold), tight letter-spacing
- **"ADVISOR"**: 400 weight (Regular), uppercase, increased letter-spacing

## Exporting PNGs from SVG

### Using ImageMagick (Command Line)
```bash
# Install: brew install imagemagick (macOS) or apt-get install imagemagick (Linux)
convert input.svg -resize 500x500 output.png
convert input.svg -resize x200 output.png  # Height only, auto width
```

### Using Figma/Sketch/Illustrator
1. Import SVG
2. Export as PNG at desired resolution
3. For retina: Export at 2x-3x size

### Using Online Tools
- svg2png.com
- cloudconvert.com
- Any SVG to PNG converter

## Usage Guidelines

### Do's ✅
- Use SVGs directly when possible
- Maintain aspect ratio when resizing
- Leave clear space around logo (equal to icon height)
- Use dark variants on dark backgrounds

### Don'ts ❌
- Don't distort or skew the logo
- Don't change colors unless using approved dark variant
- Don't place on busy backgrounds without sufficient contrast
- Don't use logos smaller than minimum sizes (see print README)

## File Naming Convention

- `polaris-logo-[variant]-[background].svg` - Source files
- `[use-case]-[dimensions].[ext]` - Exported files
- Example: `profile-500x500.png`, `email-logo-200h.png`

## Questions?

Each folder contains a detailed README with:
- Recommended export sizes
- Platform-specific requirements
- Usage examples
- Technical specifications
