# Email Signature Assets

## Source Files
- `polaris-logo-horizontal.svg` - Light backgrounds
- `polaris-logo-horizontal-dark.svg` - Dark backgrounds (dark mode email)

## Recommended Export Sizes

Export `polaris-logo-horizontal.svg` to PNG:
- `email-logo-150h.png` - Height: 150px, width: auto (compact)
- `email-logo-200h.png` - Height: 200px, width: auto (standard)
- `email-logo-250h.png` - Height: 250px, width: auto (large)

## Usage Tips
- **Most email clients**: Use 150-200px height
- **File size**: Keep under 50KB for email compatibility
- **Retina**: Export at 2x size, then specify smaller dimensions in HTML

## Email Signature HTML Example
```html
<img src="polaris-logo.png"
     alt="Polaris Advisor"
     width="400"
     height="150"
     style="display:block; max-width:400px; height:auto;" />
```
