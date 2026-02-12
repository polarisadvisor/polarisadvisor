# Polaris Advisor — Logo Design Brief

## Brand Context

Polaris Advisor is an advisory program for custom measurement system design. It is not a SaaS company, not a metrics dashboard, not an "AI-powered insights" vendor. It is a consultancy built on 50 years of mathematics (sample-path analysis, presence calculus) that helps CTOs and VPs of Engineering design measurement systems fitted to how their organizations actually work.

The brand tone is academic, not startup. "Sounds like a professor, not a pitch deck." The site filters more than it converts — it deliberately repels casual browsers and attracts serious, technically sophisticated buyers. Language is minimal, direct, and credible. No buzzwords. No hype. Concrete nouns and verbs.

Related properties include The Polaris Flow Dispatch (newsletter/publication) and the open-source Presence Calculus project (github.com/presence-calculus).

### Brand Palette (from existing site CSS)

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#1a3a52` | Deep blue — trust, technical depth |
| Primary Light | `#2d5270` | Hover states, secondary elements |
| Accent | `#4a7c9e` | Links, highlights, secondary marks |
| Text | `#2c3e50` | Body copy |
| Text Light | `#5a6c7d` | Secondary/caption text |
| Background | `#ffffff` | Page background |
| Background Light | `#f8f9fa` | Section backgrounds |
| Border | `#e1e4e8` | Subtle dividers |

### Typography

Font: Liberation Sans (use files in `../fonts/`). The wordmark should use a light weight (300) with wide letter-spacing to match the site's minimal aesthetic.

---

## Logo Requirements

### Core Concepts (in priority order)

1. **Precision** — The defining quality. This is a service built on mathematical rigor and exact measurement. Think engineering instruments, calipers, precise geometry. The Acura automotive logo is a key reference: two lines converging to an exact point, forming a shape that reads as both "A" and a precision caliper. The logo should feel engineered, not illustrated.

2. **North Star (Polaris)** — The name itself. Polaris is the navigation star — fixed, reliable, the thing you orient by. A four-pointed star is the most common representation. This can be the primary symbol or a secondary accent within a larger form. It should feel astronomical/navigational, not decorative.

3. **Flow** — Central to the methodology. "Flow" appears in the tagline ("how your work actually flows"), the related publication (Polaris Flow Dispatch), and the underlying math (presence calculus studies flow of work through systems). Represent as clean arcs, S-curves, or streaming lines — not waves, not swooshes, not ribbons. Think fluid dynamics diagrams, not water features.

### Design Constraints

- **Minimal and elegant.** Every element must earn its place. If removing something doesn't hurt, remove it.
- **Works at 24px.** Must be recognizable as a browser favicon and mobile app icon.
- **Works on dark and light backgrounds.** Single-color versions required.
- **Social media ready.** Must work as a circle-cropped avatar (Twitter/LinkedIn/GitHub).
- **Memorable at a glance.** A CTO scrolling LinkedIn should be able to identify this in their peripheral vision.
- **No gradients in final mark.** Gradients are acceptable in presentation mockups but the mark itself must work as flat single-color.
- **SVG native.** All work in SVG. No raster dependencies.
- **Not generic.** Should not look like: a generic compass rose, a generic starburst, a consulting firm's abstract swoosh, or a tech startup's rounded-everything logo.

### Anti-patterns

- No rounded/bubbly shapes (this isn't friendly SaaS)
- No thick strokes (precision means thin, exact lines)
- No gradients as structural elements
- No decorative flourishes
- No circles-and-dots abstract patterns
- No lowercase wordmarks (the brand registers as authoritative)

---

## Exploration So Far — Round 1 Concepts

Four SVG concepts were created in the initial exploration. Files are in the repo root alongside this brief.

### Concept A — Precision Caliper Star (`logo-concept-a.svg`)

Two curved arms converge upward to frame a four-pointed north star at the apex. Small tick marks along the arms reference measurement graduations. Flow represented as nested arcs between the lower arms.

**What works:** The caliper/measurement-tool metaphor is strong and unique. Directly communicates "precision" without being literal.
**What doesn't:** The curved arms feel slightly organic — precision should feel straighter, more engineered. The tick marks may not survive at small sizes. The flow lines at the bottom feel disconnected from the main form.

### Concept B — Geometric North Star + Flow (`logo-concept-b.svg`)

A traditional 8-pointed star with elongated north ray. Diamond-shaped rays along cardinal and diagonal axes. Three parallel flow arcs sweep across the lower half of the star.

**What works:** Immediately reads as "north star." The elongated north ray creates visual hierarchy. The flow lines create a nice tension with the static star.
**What doesn't:** Feels more like a traditional compass rose or nautical mark than a precision/engineering mark. The diagonal rays add visual noise at small sizes. The flow lines feel overlaid rather than integrated.

### Concept C — P-Star Monogram (`logo-concept-c.svg`)

The letter "P" constructed from a vertical stroke and an open bowl, with a four-pointed star embedded inside the bowl's negative space. Flow lines extend from the letterform's base.

**What works:** The monogram approach gives a strong, ownable form factor. The star-in-bowl idea is clever. Works naturally as a social media avatar.
**What doesn't:** The P letterform construction needs refinement — the bowl feels loose and the vertical stroke is too heavy relative to the star detail. The flow lines at the base feel tacked on. The star needs to be more integrated, less "floating inside."

### Concept D — Acura-Inspired Precision Mark (`logo-concept-d.svg`)

Two straight lines converging to a sharp point at top, with a horizontal crossbar (directly referencing the Acura "A" / caliper shape). A small north star sits at the apex. A single S-curve threads through the structure.

**What works:** Most minimal of the four. The Acura reference is clear. The single flow line is more elegant than multiple. Strong geometric simplicity.
**What doesn't:** May read too literally as the letter "A." The crossbar creates a static, closed feel that works against "flow." The star at the apex is too small to register at favicon size.

### Comparison Page

`logo-concepts.html` shows all four concepts on light/dark backgrounds with size tests at 64px, 40px, and 24px.

---

## Direction for Round 2

Based on the Round 1 exploration, the strongest elements to carry forward are:

1. **From D:** The converging-lines / caliper form. This is the most distinctive shape and most directly communicates precision. But open the form — don't close it with a crossbar.

2. **From B:** The elongated north ray concept. The north star should be structurally prominent, not a small accent.

3. **From D:** The single flow line (not three). One clean arc is more elegant and precise than parallel multiples.

4. **From C:** The monogram potential. A version that works as both standalone icon and initial would be valuable for social/favicon use.

### Possible synthesis directions

- **Converging lines whose apex IS the north star** — rather than the star sitting atop the form, the form itself resolves into a star point. The precision and the navigation become one gesture.
- **Open caliper with flow threading through** — instead of a crossbar, a single flowing arc passes between the arms, creating tension and movement while the arms provide precision framing.
- **Asymmetric star** — a four-pointed star where the north ray is dramatically longer, so the whole form reads as both "star" and "pointer/indicator" (like a measurement needle).

---

## Technical Specifications

### Deliverable Sizes

| Context | Size | Notes |
|---------|------|-------|
| Favicon | 16×16, 32×32 | Must be recognizable — likely icon-only, no wordmark |
| Social avatar | 400×400 | Circle-cropped — ensure mark works in circular frame |
| Site header | ~40px height | Icon + wordmark horizontal lockup |
| Open Graph / social cards | 1200×630 | Centered mark with wordmark |
| Print | Vector | For business cards, one-pagers |

### File Formats Needed (final)

- SVG (source / web)
- PNG at 1× and 2× for each size above
- Favicon `.ico` multi-resolution
- Single-color white version (for dark backgrounds)
- Single-color dark version (for light backgrounds)

### Lockup Variations Needed (final)

1. **Icon only** — the mark without any text
2. **Horizontal lockup** — icon + "POLARIS" wordmark side by side
3. **Stacked lockup** — icon above "POLARIS" wordmark
4. **Full name lockup** — icon + "POLARIS ADVISOR" (for formal contexts)

---

## Reference Points

- **Acura logo** — Two converging lines forming both "A" and a caliper. Precision engineering communicated through geometry alone. Key reference for the caliper/convergence concept.
- **North Star / Polaris** — Astronomical fixed point. Traditional four-pointed or eight-pointed star representations. The logo should evoke navigation and fixed reference, not decoration.
- **Fluid dynamics diagrams** — Clean streamlines showing flow through and around objects. This is the visual language for "flow" — not ocean waves, not decorative swooshes.
- **Engineering drawings** — Thin precise lines, minimal ornamentation, everything purposeful. The overall aesthetic register.

---

## Working with This Brief

When iterating on logo concepts:

1. Create SVGs at 400×400 viewBox for working size
2. Test every concept at 24px (favicon) and inside a circle crop (social avatar)
3. Ensure the mark works as single-color (no gradients, no two-tone required)
4. Use the brand palette: primary `#1a3a52` for main strokes, accent `#4a7c9e` for secondary elements only
5. Keep the wordmark as `font-weight: 300`, `letter-spacing: 6px`, uppercase "POLARIS"
6. Name files `logo-concept-[letter].svg` and update `logo-concepts.html` to include new variants
7. Prioritize precision over friendliness, engineering over artistry, restraint over expression
