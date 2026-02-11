# AI Agent Maintenance Guide - Polaris Advisor Website

This document provides context and guidelines for AI agents and developers maintaining the Polaris Advisor website. Following these guidelines ensures consistency with the established positioning, tone, technical architecture, and cross-device compatibility.

---

## Table of Contents

1. [Site Purpose & Positioning](#site-purpose--positioning)
2. [Tone & Voice Guidelines](#tone--voice-guidelines)
3. [Technical Architecture](#technical-architecture)
4. [Development Workflow](#development-workflow)
5. [Deployment Process](#deployment-process)
6. [Testing Requirements](#testing-requirements)
7. [Mobile & Cross-Device Support](#mobile--cross-device-support)
8. [Common Pitfalls](#common-pitfalls)
9. [File Structure](#file-structure)
10. [Code Conventions](#code-conventions)

---

## Site Purpose & Positioning

### Core Purpose
The Polaris Advisor Program website filters for serious buyers who are dissatisfied with off-the-shelf engineering metrics and establishes credibility through open work and clear thinking.

### What We Sell
- **Advisory services** - Custom measurement system design
- **NOT software** - Tools enable the work but aren't the product
- **Insight and expertise** - Not dashboards or metrics tools

### Target Audience
- **Primary**: Leaders accountable for engineering/business outcomes (CTO, VP Engineering, COO)
- **Mindset**: Already tried dashboards/metrics and found them lacking
- **Need**: Measurement that adapts to their system, not vice versa

### Anti-Audience (Deliberately Repel)
- "Install a tool and get visibility" seekers
- Generic benchmark/scorecard seekers
- People wanting simplistic productivity metrics
- Those wanting instant answers without engagement

### Key Differentiators
1. **Sample-path analysis** - Calculus not statistics, 50 years of mathematics
2. **Deterministic, inspectable metrics** - No other approach can claim this
3. **Open source foundation** - Theory and tooling published openly
4. **Advisory-first** - Tools enable, humans deliver value

---

## Tone & Voice Guidelines

### Core Principles

**✅ DO:**
- **Minimal, direct, credible** - Say what you mean without hype
- **Technical but readable** - Don't oversimplify, don't obscure
- **Concrete nouns and verbs** - model, measure, simulate, interpret
- **Short paragraphs** - Aim for 40-60 words max per paragraph
- **Confident assertions** - Back claims with specifics
- **Filter actively** - Make it easy for wrong-fit prospects to self-select out

**❌ DON'T:**
- Use buzzwords: "revolutionary," "paradigm shift," "game-changer"
- Claim "AI-driven insights" as primary value prop
- Promise "fully automated" anything
- Use vague productivity claims
- Oversimplify complex topics
- Use emojis (unless user explicitly requests)

### Voice Consistency

**First Person Singular** - Use "I" throughout:
- ✅ "I help software companies design..."
- ✅ "I bring expertise in measurement design"
- ❌ "We help..." (inconsistent unless referring to Polaris Program as entity)

### Writing Quality Checks

Before publishing copy, verify:
- [ ] No buzzwords or hype language
- [ ] Concrete nouns/verbs (not abstract)
- [ ] Paragraphs under 60 words
- [ ] Filters for serious buyers
- [ ] Credible without overpromising
- [ ] Differentiation from SaaS vendors clear

### Emphasis and Italics

Use `<em>` sparingly for emphasis:
- ✅ "measure what *you* need to improve"
- ✅ "*The Presence Calculus*" (proper nouns, first mention)
- ❌ Random word emphasis for drama

---

## Technical Architecture

### Stack

- **Static Site Generator**: Eleventy (11ty) 2.0+
- **Templating**: Nunjucks (.njk)
- **Content**: Markdown (.md) with HTML when needed
- **Styling**: Pure CSS3 (no preprocessors)
- **JavaScript**: Vanilla ES6+ (minimal, no frameworks)
- **Hosting**: GitHub Pages via GitHub Actions
- **Version Control**: Git

### Build Process

```bash
# Development
npm start           # Runs eleventy --serve (hot reload on localhost:8080)

# Production
npm run build       # Builds to _site/ directory
```

### Path Prefix Support

Site supports both root domain and subdirectory hosting via `pathPrefix` in `.eleventy.js`:

```javascript
const pathPrefix = process.env.ELEVENTY_PATH_PREFIX || "/";
```

**Always use the `url` filter** in templates:
```njk
<a href="{{ '/contact/' | url }}">Contact</a>
<img src="{{ '/assets/images/photo.jpg' | url }}" alt="...">
```

### Key Dependencies

**Production:**
- `@11ty/eleventy` (^2.0.1)

**None others** - Keep it simple.

---

## Development Workflow

### Making Changes

1. **Content Changes** (copy, images):
   - Edit files in `src/`
   - Test locally: `npm start`
   - Check at http://localhost:8080

2. **Styling Changes**:
   - Edit `src/css/style.css`
   - Hot reload shows changes immediately
   - Test at multiple breakpoints (320px, 768px, 1024px, 1440px)

3. **Layout/Template Changes**:
   - Edit files in `src/_includes/`
   - Test all pages that use the template
   - Verify navigation and footer on all pages

4. **Data Changes**:
   - Edit `src/_data/site.json`
   - Used for URLs, email, GitHub links, etc.

### Testing Locally

**Before every commit:**

```bash
# 1. Start dev server
npm start

# 2. Test key flows
# - Homepage loads
# - Navigation works (mobile + desktop)
# - Hamburger menu works on mobile
# - All links work
# - Images load
# - Forms work

# 3. Test production build
npm run build
# Verify _site/ folder contains expected files

# 4. Check for errors
# - No JavaScript console errors
# - No CSS layout breaks
# - No 404s for assets
```

### Git Workflow

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Update homepage hero copy for clarity"

# Push to trigger deployment
git push origin main
```

**GitHub Actions automatically:**
1. Builds the site (`npm run build`)
2. Deploys to `gh-pages` branch
3. GitHub Pages serves from `gh-pages`

---

## Deployment Process

### Automatic Deployment

**Trigger**: Every push to `main` branch

**Process**:
1. GitHub Actions workflow runs (`.github/workflows/deploy.yml`)
2. Checks out code
3. Installs Node.js and dependencies
4. Runs `npm run build` in `v1/` directory
5. Deploys `v1/_site/` contents to `gh-pages` branch
6. GitHub Pages serves updated site (~1-2 minutes)

### Manual Deployment

From GitHub repository → Actions tab → "Deploy to GitHub Pages" → "Run workflow"

### Deployment Checklist

Before pushing to production:

- [ ] Tested locally (`npm start`)
- [ ] Tested production build (`npm run build`)
- [ ] No console errors in browser
- [ ] Mobile navigation works (hamburger menu)
- [ ] All links functional
- [ ] Images load correctly
- [ ] Copy proofread for typos
- [ ] Tone consistent with guidelines
- [ ] No broken internal links

### GitHub Pages Settings

**Repository Settings → Pages:**
- Source: **Deploy from a branch**
- Branch: **gh-pages**
- Folder: **/ (root)**

### Custom Domain (if used)

If deploying to custom domain:
1. `src/CNAME` file must contain domain
2. DNS records configured at domain registrar
3. HTTPS enforcement enabled in GitHub settings

---

## Testing Requirements

### Browser Testing Matrix

**Desktop:**
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)

**Mobile:**
- ✅ iOS Safari (iPhone 15 Pro and similar)
- ✅ Android Chrome (recent versions)
- ✅ Android Samsung Internet

### Screen Size Testing

**Required test viewports:**

| Device Type | Width | Breakpoint |
|------------|-------|------------|
| Mobile Small | 320px | Default mobile styles |
| Mobile Medium | 375px | Default mobile styles |
| Mobile Large | 414px | Default mobile styles |
| Small Mobile Specific | <480px | Enhanced mobile styles |
| Tablet Portrait | 768px | Tablet-specific layout |
| Tablet Landscape | 1024px | Transition to desktop |
| Desktop | 1440px+ | Full desktop layout |

**Test in Chrome DevTools:**
1. Open DevTools (F12)
2. Toggle Device Toolbar (Cmd+Shift+M / Ctrl+Shift+M)
3. Test each viewport width listed above
4. Verify no horizontal scroll at any width

### Critical Tests

**Navigation:**
- [ ] Desktop: All 5 links visible, clickable
- [ ] Tablet (769-1024px): Quick links + hamburger menu visible
- [ ] Mobile (<768px): Quick links (Program | Open Source | Contact) + hamburger visible
- [ ] Hamburger menu opens/closes smoothly on mobile
- [ ] Hamburger works on iOS Safari (iPhone)
- [ ] Hamburger works on Android Chrome
- [ ] Menu closes when clicking overlay
- [ ] Menu closes when clicking nav link
- [ ] Menu closes on Escape key

**Layout:**
- [ ] Hero section: Photo + text side-by-side on desktop
- [ ] Hero section: Photo above text on mobile
- [ ] Value props: 3 columns on desktop (>1024px)
- [ ] Value props: 2 columns + centered 3rd on tablet (769-1024px)
- [ ] Value props: 1 column on mobile (<768px)
- [ ] Intro/Credibility/Qualifier sections: Always left-aligned
- [ ] No sections centered on desktop (except value prop 3rd item on tablet)

**Typography:**
- [ ] All text readable (min 14px on mobile, 16px on desktop)
- [ ] No awkward line breaks or orphaned words
- [ ] Technical terms wrap properly (e.g., "sample-path analysis")
- [ ] Emphasis (`<em>`) renders correctly

**Interactive Elements:**
- [ ] All buttons meet 44×44px minimum touch target
- [ ] Form inputs easy to tap on mobile
- [ ] No iOS auto-zoom on input focus (inputs are 16px font size)
- [ ] Links have adequate spacing (no accidental taps)

### Performance Testing

**Required:**
- [ ] Page load <2 seconds on 3G
- [ ] No layout shift as page loads
- [ ] Images optimized (<200KB each)
- [ ] CSS and JS minified for production (optional for v1)

**Test with:**
- Chrome DevTools → Network → Throttle to "Fast 3G"
- Lighthouse audit (aim for >90 performance score)

---

## Mobile & Cross-Device Support

### Mobile-First Approach

**Default styles = mobile styles**, then enhance for larger screens:

```css
/* Mobile default (320px+) */
.element { ... }

/* Tablet (769px+) */
@media (min-width: 769px) { ... }

/* Desktop (1025px+) */
@media (min-width: 1025px) { ... }
```

### Touch Target Requirements

**All interactive elements:**
- **Minimum**: 44×44px (iOS guideline)
- **Recommended**: 48×48px (Material Design)

**Current implementations:**
- Buttons: 44px min-height
- Nav links: 44px min-height with padding
- Form inputs: 44px min-height
- Hamburger button: 44×44px

### iOS Safari Specific

**Required CSS properties for touch:**

```css
.interactive-element {
  -webkit-tap-highlight-color: rgba(0,0,0,0); /* Remove blue flash */
  -webkit-touch-callout: none;                /* Disable callout */
  -webkit-user-select: none;                  /* Disable text selection */
  touch-action: manipulation;                 /* Fast tap, no zoom */
  cursor: pointer;                            /* Show it's clickable */
}
```

**Applied to:**
- `.nav-toggle` (hamburger button)
- `.nav-overlay`
- All buttons
- All links with padding

### JavaScript for Mobile

**Event handling:**
- Use standard `click` events (work on modern iOS/Android)
- Add `e.preventDefault()` and `e.stopPropagation()` to prevent issues
- Avoid complex touch event handling unless necessary

**Body scroll locking:**
```javascript
// When menu opens
body.style.overflow = 'hidden';

// When menu closes
body.style.overflow = '';
```

### Responsive Images

**Current approach:**
- Single image source for all devices
- Appropriate resolution (400×400px minimum for photos)
- Optimized file size (<200KB)

**Future enhancement (optional):**
```html
<img srcset="photo-small.jpg 400w,
             photo-large.jpg 800w"
     sizes="(max-width: 768px) 200px, 280px"
     src="photo-large.jpg" alt="...">
```

### Font Sizes

**Minimum readable sizes:**
- Body text: 16px (desktop), 15px (mobile)
- Never below 14px
- Form inputs: 16px (prevents iOS auto-zoom)

**Current scale:**
```css
/* Desktop */
h1: 3rem (48px)
h2: 2rem (32px)
h3: 1.5rem (24px)
body: 1rem (16px)

/* Mobile <480px */
html: 15px base
h1: 1.85rem (~28px)
h2: 1.75rem (~26px)
```

# Assets and Images
Read assets/brand-kit/README.md for guidelines on brand assets and how to create them including tools you should use. 
---

## Common Pitfalls

### Deployment Issues

**❌ Problem**: Jekyll builds instead of Eleventy
**✅ Solution**: Ensure `src/.nojekyll` file exists and is copied to output

**❌ Problem**: Assets (CSS/JS/images) don't load on GitHub Pages
**✅ Solution**: Always use `{{ '/path/to/asset' | url }}` filter in templates

**❌ Problem**: Site works locally but breaks on GitHub Pages
**✅ Solution**: Test production build with `npm run build` before pushing

**❌ Problem**: Workflow fails with "Missing package-lock.json"
**✅ Solution**: Run `npm install` to generate, commit it

### Content Issues

**❌ Problem**: Text is centered on desktop when it should be left-aligned
**✅ Solution**: Check for `text-align: center` in CSS, use `!important` to override if needed

**❌ Problem**: Value props layout is awkward (2+1 with left-aligned 3rd item)
**✅ Solution**: Verify tablet breakpoint (769-1024px) centers 3rd item with `grid-column: 1 / -1; margin: 0 auto;`

**❌ Problem**: Long technical terms cause horizontal scroll
**✅ Solution**: Add `word-wrap: break-word; overflow-wrap: break-word;` to text containers

**❌ Problem**: Voice inconsistency ("I" vs "We")
**✅ Solution**: Use "I" throughout unless referring to Polaris Program as entity

### Mobile Issues

**❌ Problem**: Hamburger menu doesn't work on iPhone
**✅ Solution**: Verify:
- JavaScript file loading (`src/js/main.js`)
- Elements exist (`.nav-toggle`, `.site-nav-full`, `.nav-overlay`)
- CSS properties set (`-webkit-tap-highlight-color`, `touch-action`)
- Event listeners attached to `click` events
- No JavaScript errors in console

**❌ Problem**: Form inputs cause page zoom on iOS
**✅ Solution**: Ensure all inputs have `font-size: 16px` or larger

**❌ Problem**: Touch targets too small
**✅ Solution**: Add `min-width: 44px; min-height: 44px;` and adequate padding

**❌ Problem**: Navigation takes too much vertical space on mobile
**✅ Solution**: Use quick links (3 items) + hamburger for full menu

### CSS Issues

**❌ Problem**: Styles not applying as expected
**✅ Solution**: Check specificity, consider `!important` if overriding inherited styles

**❌ Problem**: Layout breaks at certain viewport widths
**✅ Solution**: Test at all required breakpoints, adjust media queries

**❌ Problem**: Grid creates unexpected layouts
**✅ Solution**: Use explicit column counts (`grid-template-columns: repeat(3, 1fr)`) instead of `auto-fit`

---

## File Structure

```
v1/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions deployment
├── src/                        # SOURCE FILES (edit these)
│   ├── _data/
│   │   └── site.json          # Global data (URLs, email, etc.)
│   ├── _includes/
│   │   ├── base.njk           # Base HTML layout
│   │   ├── header.njk         # Site header + navigation
│   │   └── footer.njk         # Site footer
│   ├── assets/
│   │   └── images/
│   │       └── krishna-kumar.jpg
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   └── main.js            # Navigation JavaScript
│   ├── .nojekyll              # Disable Jekyll on GitHub Pages
│   ├── index.md               # Homepage
│   ├── contact.md             # Contact page
│   ├── program.md             # Program page (TODO)
│   ├── approach.md            # Approach page (TODO)
│   └── open-source.md         # Open Source page (TODO)
├── _site/                      # GENERATED (don't edit)
├── .eleventy.js               # Eleventy configuration
├── .gitignore                 # Git ignore rules
├── package.json               # Dependencies and scripts
├── package-lock.json          # Locked dependency versions
├── README.md                  # Project documentation
├── AGENTS.md                  # This file
├── CONTEXT.md                 # Original positioning document
├── DEPLOYMENT.md              # Deployment guide
├── TACTICAL_PLAN.md           # Implementation plan
└── MOBILE-FIXES.md            # Mobile fix documentation
```

### What to Edit

**Content/Copy**: Edit `src/*.md` files
**Navigation/Header**: Edit `src/_includes/header.njk`
**Footer**: Edit `src/_includes/footer.njk`
**Styles**: Edit `src/css/style.css`
**JavaScript**: Edit `src/js/main.js`
**Global Data**: Edit `src/_data/site.json`

### What NOT to Edit

**Never edit `_site/`** - It's auto-generated by Eleventy
**Never edit `node_modules/`** - Managed by npm

---

## Code Conventions

### HTML/Nunjucks

**Use semantic HTML5:**
```html
<header>, <nav>, <main>, <section>, <article>, <footer>
```

**Always include:**
- `alt` attributes on images
- `aria-label` on buttons without text
- `aria-expanded` on toggle buttons

**Use the `url` filter for all paths:**
```njk
<a href="{{ '/contact/' | url }}">Contact</a>
<img src="{{ '/assets/images/photo.jpg' | url }}" alt="Description">
<link rel="stylesheet" href="{{ '/css/style.css' | url }}">
<script src="{{ '/js/main.js' | url }}"></script>
```

### CSS

**Organization:**
```css
/* ==================== Section Name ==================== */
.class-name {
  /* Layout properties first */
  display: flex;
  position: relative;

  /* Box model */
  width: 100%;
  padding: 1rem;
  margin: 0 auto;

  /* Typography */
  font-size: 1rem;
  line-height: 1.6;

  /* Visual */
  color: var(--color-text);
  background: var(--color-background);

  /* Misc */
  cursor: pointer;
  transition: all 0.3s ease;
}
```

**Use CSS custom properties:**
```css
:root {
  --color-primary: #1a3a52;
  --spacing-md: 2rem;
  --max-width: 1200px;
}

.element {
  color: var(--color-primary);
  padding: var(--spacing-md);
}
```

**Mobile-first media queries:**
```css
/* Base styles for mobile */
.element { ... }

/* Tablet and up */
@media (min-width: 769px) { ... }

/* Desktop and up */
@media (min-width: 1025px) { ... }
```

**Use `!important` sparingly:**
Only when absolutely necessary to override inherited styles (e.g., text-align on specific sections).

### JavaScript

**Use modern ES6+:**
```javascript
// const/let, not var
const element = document.querySelector('.class');
let isActive = false;

// Arrow functions
elements.forEach(el => {
  el.addEventListener('click', handleClick);
});

// Template literals
console.log(`Element found: ${element}`);
```

**Always check elements exist:**
```javascript
const navToggle = document.querySelector('.nav-toggle');

if (!navToggle) {
  console.error('Nav toggle not found!');
  return;
}

// Safe to use navToggle here
```

**Use event delegation when appropriate:**
```javascript
// Instead of adding listener to each link
navFull.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', closeMenu);
});
```

**Prevent default and stop propagation:**
```javascript
button.addEventListener('click', function(e) {
  e.preventDefault();     // Prevent default button behavior
  e.stopPropagation();    // Prevent event bubbling
  // Your code here
});
```

### Markdown

**Front matter required:**
```markdown
---
layout: base.njk
title: Page Title
description: Meta description for SEO
---

Content here
```

**Mix HTML when needed:**
```markdown
---
layout: base.njk
title: Home
---

<section class="hero">
  <div class="container">
    # Markdown heading works here too

    But use HTML for complex layouts
  </div>
</section>
```

---

## Maintenance Scenarios

### Adding a New Page

1. **Create markdown file** in `src/`:
   ```bash
   touch src/newpage.md
   ```

2. **Add front matter and content:**
   ```markdown
   ---
   layout: base.njk
   title: New Page
   description: Description for SEO
   ---

   <section>
     <div class="container">
       <h1>New Page</h1>
       <p>Content here</p>
     </div>
   </section>
   ```

3. **Add to navigation** in `src/_includes/header.njk`:
   ```html
   <a href="{{ '/newpage/' | url }}">New Page</a>
   ```

4. **Test locally** and commit

### Updating Copy

1. **Edit markdown file** (e.g., `src/index.md`)
2. **Check tone/voice guidelines**:
   - No buzzwords?
   - Concrete language?
   - Filters for fit?
3. **Test locally**: `npm start`
4. **Proofread** for typos and grammar
5. **Commit and push**

### Changing Styles

1. **Edit `src/css/style.css`**
2. **Test at all breakpoints**:
   - 320px, 768px, 1024px, 1440px
3. **Check mobile touch targets** (44px minimum)
4. **Verify no horizontal scroll**
5. **Test on actual mobile device** if possible
6. **Commit and push**

### Fixing Mobile Issues

1. **Identify the issue**:
   - Layout problem? Check CSS media queries
   - Interaction problem? Check JavaScript
   - Touch target too small? Add padding and min dimensions

2. **Test locally on mobile**:
   - Use Chrome DevTools device emulation
   - Test on actual device via local network

3. **Common fixes**:
   - Add `-webkit-tap-highlight-color: rgba(0,0,0,0)`
   - Ensure `touch-action: manipulation`
   - Check z-index layering
   - Verify JavaScript event listeners attached

4. **Deploy and verify on live site**

---

## Emergency Procedures

### Site is Down

1. **Check GitHub Pages status**: https://www.githubstatus.com/
2. **Check Actions tab** for failed workflows
3. **Check DNS** (if using custom domain)
4. **Verify gh-pages branch** exists and has content

### Broken Deployment

1. **Check Actions tab** for error messages
2. **Common issues**:
   - Missing `package-lock.json`: Run `npm install`, commit
   - Build errors: Run `npm run build` locally, fix errors
   - Wrong branch: Check workflow points to correct branch

3. **Rollback if needed**:
   ```bash
   git revert HEAD
   git push origin main
   ```

### JavaScript Not Working

1. **Check browser console** for errors
2. **Verify JavaScript file loaded**:
   - DevTools → Network tab → Look for `main.js`
   - Check `<script src="{{ '/js/main.js' | url }}">` in `base.njk`

3. **Check selectors**:
   ```javascript
   console.log(document.querySelector('.nav-toggle')); // Should not be null
   ```

4. **Verify elements exist** in HTML

---

## Checklist for AI Agents

When making changes to this site, verify:

**Tone & Content:**
- [ ] No buzzwords or hype
- [ ] Concrete, specific language
- [ ] Filters for anti-audience
- [ ] Voice consistent (use "I" not "We")
- [ ] Paragraphs under 60 words
- [ ] Technical but readable

**Code Quality:**
- [ ] Uses `{{ path | url }}` filter for all links/assets
- [ ] Semantic HTML5
- [ ] Accessible (ARIA labels, alt text)
- [ ] Mobile-first CSS
- [ ] Modern ES6+ JavaScript

**Testing:**
- [ ] Tested locally (`npm start`)
- [ ] Tested production build (`npm run build`)
- [ ] Tested on mobile viewports (320px, 768px, 1024px)
- [ ] Navigation works (especially hamburger menu)
- [ ] No horizontal scroll
- [ ] Touch targets ≥44px
- [ ] No console errors

**Deployment:**
- [ ] Changes committed with clear message
- [ ] Pushed to `main` branch
- [ ] GitHub Actions workflow succeeds
- [ ] Site updated on GitHub Pages
- [ ] Verified live site works

**Documentation:**
- [ ] Updated AGENTS.md if process changed
- [ ] Updated README.md if setup changed
- [ ] Noted any new patterns or conventions

---

## Contact & Resources

**Original Context Document**: `CONTEXT.md`
**Tactical Implementation Plan**: `TACTICAL_PLAN.md`
**Deployment Guide**: `DEPLOYMENT.md`
**Mobile Fixes**: `MOBILE-FIXES.md`

**Key Technologies:**
- [Eleventy Documentation](https://www.11ty.dev/docs/)
- [Nunjucks Templating](https://mozilla.github.io/nunjucks/)
- [GitHub Pages](https://docs.github.com/en/pages)
- [GitHub Actions](https://docs.github.com/en/actions)

**Questions or Issues?**
Refer to these documents first, then review commit history for context on past decisions.

---

**Last Updated**: 2026-02-07
**Site Version**: v1
**Eleventy Version**: 2.0.1
**Node Version**: 20.x
