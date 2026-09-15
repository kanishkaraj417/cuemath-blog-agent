---
type: design-reference
version: 1
last-updated: 2026-03-30
---

# Cuemath Design Guidelines — Forge Reference

This document is Forge's single source of truth for visual design when building or reviewing Cuemath website pages and microtools. Every page Forge builds must pass against this doc. Every review must flag deviations.

---

## Layout Rule — Always Observed

**Every page must have left and right breathing room.** All content lives inside a centred container:
- `max-width: 1140px`
- `margin: 0 auto`
- `padding: 0 24px`

This applies to every section on every page — hero text columns, stat grids, review cards, FAQ blocks, form sections, everything. Content must never run edge-to-edge on desktop. This is how every page (referral, refund policy, city pages, homepage) has always been built. Never skip the container wrapper.

---

## How Forge Uses This Document

| Task | What to check |
|---|---|
| Building a new page/microtool | Copy the font block, use only approved colors, follow the type scale |
| Reviewing a page/microtool | Check fonts, colors, spacing, button styles against this doc — flag deviations as P1 or P2 |
| Handoff to dev | Paste the font block verbatim, reference color tokens by hex, call out any deviations explicitly |

---

## 1. Fonts

### Rule
- **Website pages and microtools:** Use **Athletics** for everything — headings, body, labels, buttons
- **Untitled Sans:** App/product contexts only. Do NOT use on website pages or microtools
- **Ghost blog:** Exception — use Avenir Next / Nunito Sans / Helvetica Neue (Ghost handles this automatically)

### Font Declaration Block (copy verbatim into every page)

```css
@font-face {
  font-family: athleticsblack;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Black.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: athleticsbold;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Bold.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: athleticslight;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Light.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: Athletics-Medium;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Medium.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: Athletics-Regular;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Regular.otf") format("opentype");
  font-display: swap;
}
```

> **Untitled Sans — available but NOT for website/microtool use:**
```css
@font-face {
  font-family: untitledsansblack;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/UntitledSansTest-Black.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: untitledsansbold;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/UntitledSansTest-Bold.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: Untitled Sans Medium;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/UntitledSansTest-Medium.otf") format("opentype");
  font-display: swap;
}
@font-face {
  font-family: Untitled Sans Regular;
  src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/UntitledSansTest-Regular.otf") format("opentype");
  font-display: swap;
}
```

### Font Weight → Family Name Mapping

| Weight | Family Name to Use | Usage |
|---|---|---|
| Black (900) | `athleticsblack` | Hero H1, stat numbers, logo wordmark |
| Bold (700) | `athleticsbold` | Section headings, subheadings, button text |
| Medium (500) | `Athletics-Medium` | Card labels, medium emphasis, nav links |
| Regular (400) | `Athletics-Regular` | Body text, paragraphs |
| Light | `athleticslight` | Large decorative text only |

### ⚠️ Known Bug in Source Code
The original font code has a typo in the last declaration: `font-family:untitledsansblack';` — note the stray single quote. This is already fixed in the block above. Flag this if it appears in any dev code.

---

## 2. Typography Scale

### Headings — aH Series (Athletics)

| Token | Size | Weight/Family | Line Height | Usage |
|---|---|---|---|---|
| aH1 | 64px | athleticsblack | 72px | Largest hero (desktop only) |
| aH2 | 48px | athleticsblack / athleticsbold | 56px | Main hero headline (desktop only) |
| aH3 | 32px | athleticsbold | 40px | Section headings |
| aH4 | 24px | athleticsbold | 32px | Sub-sections, feature titles |

### Body — aB Series (Athletics)

| Token | Size | Weight/Family | Line Height | Usage |
|---|---|---|---|---|
| aB1 | 20px | Athletics-Regular | 28px | Large body, card text |
| aB2 | 16px | Athletics-Regular | 22px | Standard body copy |
| aB3 | 14px | Athletics-Regular | 20px | Nav links, small labels |

### All Caps Labels — AC Series

| Token | Size | Weight | Letter Spacing | Usage |
|---|---|---|---|---|
| AC1 | 20px | athleticsbold | 1px | Section tags, pill labels |
| AC2 | 16px | athleticsbold | 1px | Smaller labels |
| AC3 | 14px | athleticsbold | 1px | Nav/badge labels |
| AC4 | 12px | athleticsbold | 1px | Fine print labels |

### CSS Snippet — Type Scale

```css
/* Headings */
.h1 { font-family: athleticsblack; font-size: 64px; line-height: 72px; }
.h2 { font-family: athleticsblack; font-size: 48px; line-height: 56px; }
.h3 { font-family: athleticsbold; font-size: 32px; line-height: 40px; }
.h4 { font-family: athleticsbold; font-size: 24px; line-height: 32px; }

/* Body */
.body-lg { font-family: Athletics-Regular; font-size: 20px; line-height: 28px; }
.body-md { font-family: Athletics-Regular; font-size: 16px; line-height: 22px; }
.body-sm { font-family: Athletics-Regular; font-size: 14px; line-height: 20px; }

/* Labels */
.label { font-family: athleticsbold; font-size: 14px; letter-spacing: 1px; text-transform: uppercase; }
```

---

## 3. Color Palette

### Primary Colors — Use These First

| Name | Hex | Usage |
|---|---|---|
| **Dark Purple-Navy** | `#221B35` | Primary text, button text, borders. **This is the brand "black" — never use #000000** |
| **Golden Yellow (CTA)** | `#FFD24D` | Primary CTA / button fill. Softened from `#FFB700` on 2026-07-16 — applies to all blogs. |
| **Accent Gold** | `#FFB700` | Accents only: ToC left rails, link underlines, avatar rings (NOT button fills) |
| **White** | `#FFFFFF` | Page backgrounds, card backgrounds, nav |
| **Near-black** | `#0D0D0D` | Body text on dark backgrounds |

### Pastel Accent Backgrounds

| Name | Hex | Pair with vibrant |
|---|---|---|
| Light Gold | `#FFF1CC` | Yellow CTA, warm highlights |
| Light Peach | `#FFDDCC` | Orange accent sections |
| Light Green | `#D0FBE5` | Success/trust badges |
| Light Pink | `#FFE0FD` | Accent cards |
| Light Blue | `#D6F5FF` | Accent cards |

### Vibrant Accent Text (use on dark backgrounds)

| Name | Hex | Usage |
|---|---|---|
| Cyan | `#33CCFF` | Accent text on dark |
| Green | `#00E573` | Success accent |
| Pink | `#FF80F4` | Vibrant accent |

### Neutral Grays

| Name | Hex | Usage |
|---|---|---|
| Section BG | `#F5F5F5` | Alternate section backgrounds |
| Dividers | `#EBEBEB` | Horizontal rules, separators |
| Footer upper | `#313131` | Upper footer |
| Footer lower | `#191919` | Bottom bar |

### CSS Variables Block

```css
:root {
  --color-primary-text: #221B35;      /* Brand "black" — use everywhere #000 would go */
  --color-cta-yellow: #FFD24D;        /* Primary CTA button fill */
  --color-white: #FFFFFF;
  --color-body-text: #0D0D0D;

  --color-pastel-gold: #FFF1CC;
  --color-pastel-peach: #FFDDCC;
  --color-pastel-green: #D0FBE5;
  --color-pastel-pink: #FFE0FD;
  --color-pastel-blue: #D6F5FF;

  --color-vibrant-cyan: #33CCFF;
  --color-vibrant-green: #00E573;
  --color-vibrant-pink: #FF80F4;

  --color-section-bg: #F5F5F5;
  --color-divider: #EBEBEB;
  --color-footer-upper: #313131;
  --color-footer-lower: #191919;
}
```

---

## 4. Buttons

### Primary CTA Button

```css
.btn-primary {
  background-color: #FFD24D;
  color: #221B35;             /* Always dark purple-navy on yellow — never white */
  font-family: athleticsbold;
  font-size: 16px;
  height: 48px;
  padding: 0 24px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
}
```

**CTA text rule:** "Book a Free Class" or "Try a Free 1-on-1 Cuemath Class" — never "Sign Up", "Learn More", or "Get Started" as standalone text without context.

### Secondary / Ghost Button

```css
.btn-secondary {
  background: transparent;
  color: #221B35;
  font-family: athleticsbold;
  font-size: 16px;
  height: 48px;
  padding: 0 24px;
  border-radius: 12px;
  border: 1px solid #221B35;
  cursor: pointer;
}
```

---

## 5. Layout & Spacing

```css
:root {
  --max-width: 1480px;
  --border-radius: 12px;
  --button-height: 48px;

  --space-4: 4px;
  --space-8: 8px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;
  --space-48: 48px;
}

.container {
  max-width: 1480px;
  margin: 0 auto;
  padding: 0 20px;
}
```

---

## 6. Ready-to-Use Page Snippet

Copy this as the boilerplate for any new page or microtool:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title | Cuemath</title>
  <style>
    /* ── Fonts ── */
    @font-face {
      font-family: athleticsblack;
      src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Black.otf") format("opentype");
      font-display: swap;
    }
    @font-face {
      font-family: athleticsbold;
      src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Bold.otf") format("opentype");
      font-display: swap;
    }
    @font-face {
      font-family: Athletics-Medium;
      src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Medium.otf") format("opentype");
      font-display: swap;
    }
    @font-face {
      font-family: Athletics-Regular;
      src: url("https://wmznlejcfq.s3.ap-southeast-1.amazonaws.com/static/Performance+Marketing/Cuemath_2020/Aryan/2021+Fonts/Athletics-Regular.otf") format("opentype");
      font-display: swap;
    }

    /* ── Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: Athletics-Regular, Arial, sans-serif; color: #221B35; background: #fff; }

    /* ── Tokens ── */
    :root {
      --color-primary-text: #221B35;
      --color-cta-yellow: #FFD24D;
      --color-white: #FFFFFF;
      --color-body: #0D0D0D;
      --color-pastel-gold: #FFF1CC;
      --color-pastel-green: #D0FBE5;
      --color-pastel-blue: #D6F5FF;
      --color-section-bg: #F5F5F5;
      --color-divider: #EBEBEB;
      --border-radius: 12px;
      --button-height: 48px;
      --max-width: 1480px;
    }

    /* ── Layout ── */
    .container { max-width: var(--max-width); margin: 0 auto; padding: 0 20px; }

    /* ── Typography ── */
    h1 { font-family: athleticsblack; font-size: 48px; line-height: 56px; color: var(--color-primary-text); }
    h2 { font-family: athleticsbold; font-size: 32px; line-height: 40px; color: var(--color-primary-text); }
    h3 { font-family: athleticsbold; font-size: 24px; line-height: 32px; color: var(--color-primary-text); }
    p  { font-family: Athletics-Regular; font-size: 16px; line-height: 22px; color: var(--color-body); }

    /* ── Primary CTA ── */
    .btn-primary {
      display: inline-flex;
      align-items: center;
      background: var(--color-cta-yellow);
      color: var(--color-primary-text);
      font-family: athleticsbold;
      font-size: 16px;
      height: var(--button-height);
      padding: 0 24px;
      border-radius: var(--border-radius);
      border: none;
      cursor: pointer;
      text-decoration: none;
    }

    /* ── Responsive ── */
    @media (max-width: 768px) {
      h1 { font-size: 32px; line-height: 40px; }
      h2 { font-size: 24px; line-height: 32px; }
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Hero Headline Here</h1>
    <p>Supporting copy here.</p>
    <a href="https://www.cuemath.com/" class="btn-primary">Book a Free Class</a>
  </div>

</body>
</html>
```

---

## 7. Forge Design Review Checklist

Run this on every build and review before sign-off:

### Fonts
- [ ] Only Athletics font families used (not Arial, not Google Fonts, not Untitled Sans)
- [ ] Font declarations copied from Section 1 of this doc verbatim
- [ ] No stray quote in `font-family` name (known bug — check carefully)
- [ ] `font-display: swap` present on all declarations

### Colors
- [ ] Primary text uses `#221B35` — not `#000000`
- [ ] CTA button background is `#FFD24D` with `#221B35` text
- [ ] No off-brand colors (no generic blues, reds, or greens not in the palette)
- [ ] White backgrounds use `#FFFFFF`, not off-white variants

### Typography
- [ ] H1 uses `athleticsblack`
- [ ] H2/H3 use `athleticsbold`
- [ ] Body uses `Athletics-Regular`
- [ ] Labels/pills use `athleticsbold` with `text-transform: uppercase` and `letter-spacing: 1px`

### Buttons
- [ ] Primary CTA is yellow (`#FFD24D`) with dark text (`#221B35`)
- [ ] Button height is 48px, border-radius is 12px
- [ ] CTA copy is specific — not generic "Learn More"

### Layout
- [ ] Max-width container: 1480px
- [ ] Mobile responsive (tested at 375px minimum)
- [ ] Spacing follows 4px base unit (8, 12, 16, 20, 24, 32, 48)

---

## 8. Common Deviations to Flag in Reviews

| Deviation | Priority | Fix |
|---|---|---|
| Using Arial or system fonts instead of Athletics | P1 | Replace with correct Athletics declaration |
| `#000000` used for text | P2 | Replace with `#221B35` |
| CTA button is not golden yellow | P1 | Change to `#FFD24D` |
| White text on yellow button | P1 | Change to `#221B35` |
| Untitled Sans used on website page | P2 | Replace with Athletics equivalent weight |
| Missing `font-display: swap` | P2 | Add to all `@font-face` declarations |
| Border-radius not 12px on cards/buttons | P3 | Align to `--border-radius: 12px` |
| Stray `'` in font-family name | P1 | Fix the declaration — browser won't load the font |

---

_Design guidelines extracted from: Figma design system + DevTools audit of cuemath.com/en-us/ (March 2026). Font URLs verified against S3 source provided by dev team (March 2026)._
_To update this doc: `/forge` → [4] Update the foundation document._
