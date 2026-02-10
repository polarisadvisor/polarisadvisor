# Web Assets

## Source Files
- `polaris-logo-horizontal.svg` - Primary (light backgrounds)
- `polaris-logo-horizontal-dark.svg` - Dark mode version

## Recommended Uses

### SVG (Preferred)
Use the SVG files directly in web contexts:
- Infinitely scalable
- Small file size
- CSS-controllable
- Retina-ready

```html
<img src="polaris-logo-horizontal.svg" alt="Polaris Advisor" height="72" />
```

### PNG Exports (if needed)
For contexts where SVG isn't supported:

- `logo-web-1x.png` - Height: 72px (1x resolution)
- `logo-web-2x.png` - Height: 144px (2x retina)
- `logo-web-3x.png` - Height: 216px (3x retina)

## Dark Mode
Use `polaris-logo-horizontal-dark.svg` for:
- Dark mode websites
- Dark-themed headers
- Presentations on dark backgrounds
- Video overlays

## CSS Styling
```css
.logo {
  height: 72px;
  width: auto;
}

/* Responsive */
@media (max-width: 768px) {
  .logo { height: 56px; }
}
```
