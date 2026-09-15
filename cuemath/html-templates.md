
# Cuemath HTML Templates for Ghost

All templates use the official Cuemath design palette (design-guidelines.md).
Font stack for Ghost: `'Avenir Next', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif`
Copy the block, fill in [placeholders], paste into Ghost HTML card.

**Color palette reference:**
- Primary text: `#221B35`
- Body text: `#0D0D0D`
- CTA button bg: `#FFD24D` | CTA button text: `#221B35`
- Accent gold (rails, underlines, avatar rings — NOT button fills): `#FFB700`
- Pastel gold: `#FFF1CC` | Pastel peach: `#FFDDCC` | Pastel green: `#D0FBE5` | Pastel blue: `#D6F5FF`
- Section bg: `#F5F5F5` | Dividers/borders: `#EBEBEB`

Colors and the Ghost font stack above are the only things this file pulls from `design-guidelines.md` — nothing else in that file (Athletics fonts, the typography scale, the CSS button classes, the 1480px layout tokens, the page boilerplate) applies to a Ghost blog post. Everything about how a blog card is actually built lives here.

**Border-radius standard (2026-08-13): every card container and button is `12px`, no exceptions.** This was inconsistent across templates (8/10/14/16px in different places) until normalized. Circles (avatar, check/✕ marks) and pills (difficulty badges, the "Most platforms don't do this" highlight tag) are exempt — they're a different shape on purpose, not a card, and shouldn't be flattened to 12px.

---

## Author Card

*(2026-08-13: rebuilt. The old version used a `<style>` block with CSS classes, a `:hover` state, a `@media` query, an external Font Awesome stylesheet `<link>`, and a `font-family: 'Athletics'` that's never loaded in Ghost. All of that either gets stripped by Ghost or never worked, silently. This version is fully inline, no external dependency, and uses the same Avenir Next stack as every other card in this file.)*

```html
<!-- Cuemath Author Bio Card — Nikita Joshi -->
<div style="font-family: 'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; max-width: 680px; margin: 40px auto 0;">
  <div style="background: #ffffff; border: 1px solid #EBEBEB; border-radius: 12px; padding: 24px; box-sizing: border-box; box-shadow: 0 2px 10px rgba(34,27,53,0.07);">

    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px; flex-wrap: wrap;">
      <img
        src="https://www.cuemath.com/blog/content/images/2025/11/IMG_20230223_002701_895.jpg"
        alt="Nikita Joshi"
        width="56"
        height="56"
        style="width: 56px; height: 56px; min-width: 56px; border-radius: 50%; object-fit: cover; object-position: center top; box-shadow: 0 0 0 2.5px #FFB700; flex-shrink: 0; display: block;"
      >

      <div>
        <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 5px;">
          <span style="font-size: 17px; font-weight: 700; color: #221B35; line-height: 1.3;">Nikita Joshi</span>
          <a href="https://www.linkedin.com/in/nikitajoshii" target="_blank" rel="noopener noreferrer" title="LinkedIn" style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; background: #F5F5F5; border-radius: 12px; text-decoration: none; color: #221B35; font-size: 11px; font-weight: 700; font-family: Arial, sans-serif;">in</a>
          <a href="https://medium.com/@nikitajoshii" target="_blank" rel="noopener noreferrer" title="Medium" style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; background: #F5F5F5; border-radius: 12px; text-decoration: none; color: #221B35; font-size: 13px; font-weight: 700; font-family: Georgia, serif;">M</a>
          <a href="mailto:nikita.joshi@cuemath.com" title="Email" style="display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; background: #F5F5F5; border-radius: 12px; text-decoration: none; color: #221B35; font-size: 13px;">&#9993;</a>
        </div>
        <span style="font-size: 12px; color: #6B6480; font-weight: 500; letter-spacing: 0.4px; text-transform: uppercase;">Writer and Editor</span>
      </div>
    </div>

    <div style="height: 1px; background: #EBEBEB; margin-bottom: 16px;"></div>

    <p style="margin: 0; font-size: 15px; line-height: 1.75; color: #0D0D0D; font-weight: 400;">
      I grew up a science kid. Math was not my best subject. Class moved fast, I was too shy to ask for help, and I somehow ended up more curious about how people learn than about the subjects themselves.
      <br><br>
      That's what pulled me into education — not to teach, but to understand how colleges and tutoring programs actually work and what students genuinely need from them.
      <br><br>
      My love for writing did the rest. I had too many observations and nowhere to put them, so I started writing, and haven't stopped. Over the last five years I've written about edtech, student life, and college programs. For the past year, my focus has been math tutoring specifically.
      <br><br>
      I work at Cuemath now, so factor that in. I research by going where parents actually talk: forums, reviews, and direct conversations with students and families. I'm writing for the kid who's too scared to raise their hand in class. I was that kid.
    </p>

  </div>
</div>
```

**Usage:** End of every blog. This is the canonical author card — do not use any previous version. No `<style>` block, no CSS classes, no `:hover`, no `@media`, no external stylesheet — everything is inline, matching how every other card in this file is built. There's no hover effect and no mobile-specific padding override anymore; the card is sized to work at every width without either.

---

## CTA Box

```html
<div style="padding:28px 24px; border-radius:12px; background-color:#FFF1CC; width:100%; max-width:100%; box-sizing:border-box; text-align:center; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;">
  <h2 style="color:#221B35; font-size:24px; font-weight:700; margin:0 0 12px;">[HEADING — write based on blog topic and placement position, see rules below]</h2>
  <p style="font-size:18px; line-height:1.6; color:#221B35; margin:0 0 22px;">[SUPPORTING LINE — 1–2 sentences, specific to what the reader just read or needs next]</p>
  <a href="https://cuemath.link/mathapps" target="_blank" style="display:inline-block; padding:14px 32px; background-color:#FFD24D; color:#221B35; text-decoration:none; font-weight:700; font-size:18px; border-radius:12px; letter-spacing:0.4px;">Book a Free Class</a>
  <p style="font-size:16px; color:#221B35; margin-top:18px; font-weight:600;">For Students in Grades K to 12 Worldwide</p>
</div>
```

**Usage:** Twice per blog — once mid-blog after first major section, once near the end before FAQ.

**CTA copy rules — write fresh for every blog and every placement:**

The heading and supporting line must reflect the blog topic and where the CTA sits. Never reuse "Where Hard Work Turns Into Real Results" or any other generic phrase across blogs.

| Placement | Heading angle | Supporting line angle |
|---|---|---|
| Mid-blog (after methodology or first review section) | The tension the reader is still feeling — the unsolved problem | What Cuemath specifically offers for that problem |
| End of blog (before FAQ) | The decision moment — reader has the info, now they need to act | Direct value promise tied to what the blog covered |

**Examples by blog type:**

- Kumon cost blog, mid: *"Spending $300/Month on Kumon and Still Not Sure It's Working?"* → "Cuemath's live 1:1 sessions cost less and come with a free MathFit Evaluation to show you exactly where your child stands."
- Kumon cost blog, end: *"Your Child Doesn't Have to Figure It Out Alone"* → "Book a free Cuemath class — same-tutor sessions, grades K–12, no worksheet drills."
- Math anxiety blog, mid: *"Math Anxiety Doesn't Go Away on Its Own"* → "A patient 1:1 tutor who shows up every week makes more difference than any app. Try a free Cuemath class."
- Best math programs blog, end: *"Found the Right Fit? Start With a Free Class"* → "Cuemath works best for grades 3–8 students who need concept-building, not drill repetition. One free session to see if it clicks."
- Practice problems blog, mid: *"Problems Are Easier When Someone Explains the Why"* → "Cuemath tutors don't just mark answers right or wrong — they walk through the reasoning. Try a free live session."

---

## Callout Box — Factual / Info

```html
<div style="background:#FFFFFF; border:2px solid #EBEBEB; border-left:4px solid #FFB700; border-radius:12px; padding:20px 24px; max-width:950px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; color:#221B35; line-height:1.7;">
  💡 <strong>[Label — e.g. What tutors observe]:</strong> [Factual callout text — a tutor insight, stat, or key finding.]
</div>
```

**Usage:** Factual observations, tutor insights, stats worth highlighting. Use for "did you know" or informational callouts.

---

## Callout Box — Caution / Mistake

```html
<div style="background:#FFF1CC; border:2px solid #FFB700; border-radius:12px; padding:20px 24px; max-width:950px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; color:#221B35; line-height:1.7;">
  ⚠️ <strong>Where students make mistakes:</strong> [Observation from tutors about a common error or misconception.]
</div>
```

**Usage:** Practice problem blogs — after the concept explainer in each section. Use for cautionary or error-pattern callouts.

---

## Question with Answer (Easy/Medium — no steps shown)

```html
<div style="background:#FFFFFF; border:1px solid #EBEBEB; border-radius:12px; max-width:950px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; display:flex; overflow:hidden;">
  <!-- Left: Question -->
  <div style="flex:2; padding:22px 24px; border-right:1px solid #EBEBEB;">
    <div style="font-size:20px; color:#221B35;">
      <span style="font-weight:700;">Q[N].</span> [Question text]
    </div>
  </div>
  <!-- Right: Answer -->
  <div style="flex:1; padding:22px 24px; background:#FFF9F0;">
    <div style="font-size:20px; font-weight:700; margin-bottom:8px; color:#221B35;">
      Answer: [Answer]
    </div>
    <div style="display:inline-block; font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:0.8px; background:#D0FBE5; color:#155724; padding:3px 10px; border-radius:20px;">
      Easy
    </div>
  </div>
</div>
```

**Difficulty label variants:**
- Easy: `background:#D0FBE5; color:#155724`
- Medium: `background:#FFF1CC; color:#856404`
- Hard: `background:#FFDDCC; color:#842029`

**Usage:** Easy/Medium problems in practice blogs with no step-by-step needed.

---

## Question with Step-by-Step Solution (Medium/Hard)

```html
<div style="background:#FFFFFF; border:1px solid #EBEBEB; border-radius:12px; max-width:1000px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; overflow:hidden;">
  <!-- Question Row -->
  <div style="display:flex; border-bottom:2px solid #EBEBEB;">
    <!-- Left: Question -->
    <div style="flex:2; padding:22px 24px; border-right:1px solid #EBEBEB;">
      <div style="font-size:20px; color:#221B35;">
        <span style="font-weight:700;">Q[N].</span> [Question text]
      </div>
    </div>
    <!-- Right: Answer + Difficulty -->
    <div style="flex:1; padding:22px 24px; background:#FFF9F0;">
      <div style="font-size:20px; font-weight:700; margin-bottom:8px; color:#221B35;">
        Answer: [Answer]
      </div>
      <div style="display:inline-block; font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:0.8px; background:#FFF1CC; color:#856404; padding:3px 10px; border-radius:20px;">
        Medium
      </div>
    </div>
  </div>
  <!-- Solution Section -->
  <div style="background:#FFFBF0; padding:22px 24px; border-top:1px solid #EBEBEB;">
    <div style="font-size:17px; font-weight:700; color:#221B35; margin-bottom:14px;">
      🔍 Step-by-Step Solution:
    </div>
    <div style="font-size:17px; line-height:1.8; color:#0D0D0D;">
      <div style="margin-bottom:8px;"><strong style="color:#221B35;">Step 1:</strong> [Step description]</div>
      <div style="margin-bottom:8px;"><strong style="color:#221B35;">Step 2:</strong> [Step description]</div>
      <div style="margin-bottom:8px;"><strong style="color:#221B35;">Step 3:</strong> [Step description]</div>
      <div><strong style="color:#221B35;">Step 4:</strong> [Final step / answer restatement]</div>
    </div>
  </div>
</div>
```

**Usage:** Medium and Hard problems in practice blogs. Change difficulty label to Hard variant for hard problems.

---

## Trustpilot Review / Testimonial Box

```html
<div style="background:#FFFFFF; padding:24px 28px; border-radius:12px; border:1px solid #EBEBEB; border-left:4px solid #FFB700; max-width:900px; font-family:'Georgia',serif; line-height:1.8; color:#221B35;">
  <div style="font-size:19px; font-style:italic; margin-bottom:16px; color:#0D0D0D;">
    "[Parent quote]"
  </div>
  <div style="font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; font-size:14px; color:#6b7280;">
    — [Parent name], Parent of Grade [N] student · <a href="https://www.trustpilot.com/review/cuemath.com" style="color:#221B35; text-decoration:underline;">Trustpilot Review</a>
  </div>
</div>
```

**Usage:** Include one parent testimonial per blog. Place after a major section or before a CTA. Quote must be real — pull from Reddit or Trustpilot research files. Never invent.

---

## Suggested Reading Box — Multiple Links

```html
<div style="max-width:800px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; background:#FFF9F0; border:1px solid #EBEBEB; border-radius:12px; padding:16px 20px;">
  <p style="margin-top:0; font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#221B35; margin-bottom:10px;">Suggested Reading</p>
  <ul style="line-height:1.8; font-size:15px; padding-left:18px; margin-bottom:0; color:#221B35;">
    <li><a href="[URL]" target="_blank" rel="nofollow noopener noreferrer" style="color:#221B35; text-decoration:underline;">[Article title]</a></li>
    <li><a href="[URL]" target="_blank" rel="nofollow noopener noreferrer" style="color:#221B35; text-decoration:underline;">[Article title]</a></li>
    <li><a href="[URL]" target="_blank" rel="nofollow noopener noreferrer" style="color:#221B35; text-decoration:underline;">[Article title]</a></li>
  </ul>
</div>
```

**Usage:** End of practice blogs as "Related Reading." Also usable mid-blog for internal links.

---

## Suggested Reading Box — Single Link

```html
<div style="max-width:700px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; background:#FFF9F0; border:1px solid #EBEBEB; border-radius:12px; padding:10px 16px; font-size:15px;">
  <span style="color:#221B35; font-weight:700;">Read more: </span>
  <a href="[URL]" target="_blank" rel="nofollow noopener noreferrer" style="color:#221B35; text-decoration:underline; margin-left:4px;">[Link text]</a>
</div>
```

**Usage:** Inline within a section to reference one internal or external resource.

---

## Worksheet Download Section

```html
<div style="background:#FFF1CC; padding:26px 28px; border-radius:12px; border:1px solid #FFB700; max-width:950px; font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif; color:#221B35;">
  <div style="font-size:20px; font-weight:700; margin-bottom:12px;">📥 Free Worksheet — [Topic Name]</div>
  <div style="font-size:16px; line-height:1.7; margin-bottom:18px; color:#0D0D0D;">
    Your child has now seen the problems and how they're solved. These Cuemath worksheets are the next step — designed by the same tutors who reviewed this blog, with graded difficulty and clear visuals.
  </div>
  <div style="margin-bottom:12px; font-size:16px;">
    ↓ <a href="#" style="text-decoration:none; color:#221B35; font-weight:700;">[Worksheet 1 title] →</a>
  </div>
  <div style="font-size:16px;">
    ↓ <a href="#" style="text-decoration:none; color:#221B35; font-weight:700;">[Worksheet 2 title] →</a>
  </div>
</div>
```

**Usage:** Practice problem blogs — at the end of each topic section, linking to free Cuemath worksheets.

---

## FAQ Schema (JSON-LD)

```html
<!--kg-card-begin: html-->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text — match exactly to the H3 in your FAQ section]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text — plain text only, no HTML tags inside. 3–6 sentences. First sentence repeats the keyword phrase from the question.]"
      }
    },
    {
      "@type": "Question",
      "name": "[Question 2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer 2]"
      }
    }
  ]
}
</script>
<!--kg-card-end: html-->
```

**Usage:** Every blog. Paste as the LAST element in the post, after the author card.
**How to generate:** Copy every Q&A from your FAQ section into `mainEntity`. One object per question.
**Ghost note:** Already wrapped in kg-card tags above — paste as-is.
**Why it matters:** FAQ schema turns your FAQ section into Google Rich Results. Also the primary signal that makes your FAQs citable by ChatGPT, Perplexity, and other LLMs.

---

<!-- APPEND NEW ELEMENTS BELOW WITH DATE AND LABEL -->

## Button Link — Secondary Navigation (2026-05-29)

Use for in-content links to other pages (pricing page, reviews page, grade-level pages). **Not a CTA** — do not use for "Book a Free Class" or primary conversion actions. These sit inline near relevant content.

Two approved variants — pick one per use, do not mix on the same page:

**Variant A — Pastel Gold (preferred)**
```html
<!--kg-card-begin: html-->
<div style="text-align: center; margin: 24px 0;">
  <a href="[URL]" target="_blank" rel="noopener" style="display: inline-block; padding: 13px 28px; background: #FFF1CC; color: #221B35; font-family: 'Avenir Next', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif; font-weight: 700; font-size: 15px; border-radius: 12px; border: 1.5px solid #FFB700; text-decoration: none; letter-spacing: 0.2px;">[Anchor text] →</a>
</div>
<!--kg-card-end: html-->
```

**Variant B — Pastel Peach**
```html
<!--kg-card-begin: html-->
<div style="text-align: center; margin: 24px 0;">
  <a href="[URL]" target="_blank" rel="noopener" style="display: inline-block; padding: 13px 28px; background: #FFDDCC; color: #221B35; font-family: 'Avenir Next', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif; font-weight: 700; font-size: 15px; border-radius: 12px; border: 1.5px solid #FFBB99; text-decoration: none; letter-spacing: 0.2px;">[Anchor text] →</a>
</div>
<!--kg-card-end: html-->
```

**Anchor text examples by use case:**
- Pricing page: "Check Full Pricing Page →"
- Reviews: "See What Parents Say About Cuemath →"
- Grade-level page: "Explore Math Classes by Grade →"
- Competitor comparison: "Compare Cuemath vs [Competitor] →"

**Rule:** Always end anchor text with `→`. Always use `target="_blank" rel="noopener"` for external links.

## Comparison Table — Pricing / Program (2026-05-29)

Use for any multi-program comparison table (cost, features, sessions). Cuemath rows are highlighted with `#FFF1CC` background and a `4px #FFB700` left border. Non-Cuemath rows alternate between white and `#F5F5F5`. Scrolls horizontally on mobile.

```html
<!--kg-card-begin: html-->
<div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 32px 0;">
  <table style="width: 100%; min-width: 620px; border-collapse: collapse; font-family: 'Avenir Next', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif; color: #221B35; font-size: 15px; line-height: 22px;">
    <thead>
      <tr>
        <th style="background: #221B35; color: #ffffff; font-weight: 700; text-align: left; padding: 14px 16px;">[Column 1]</th>
        <th style="background: #221B35; color: #ffffff; font-weight: 700; text-align: left; padding: 14px 16px;">[Column 2]</th>
        <th style="background: #221B35; color: #ffffff; font-weight: 700; text-align: left; padding: 14px 16px;">[Column 3]</th>
        <th style="background: #221B35; color: #ffffff; font-weight: 700; text-align: left; padding: 14px 16px;">[Column 4]</th>
      </tr>
    </thead>
    <tbody>
      <!-- Non-Cuemath row (white) -->
      <tr style="border-bottom: 1px solid #EBEBEB;">
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
      </tr>
      <!-- Cuemath row — repeat for each Cuemath tier -->
      <tr style="background: #FFF1CC; border-bottom: 1px solid #EBEBEB;">
        <td style="padding: 14px 16px; font-weight: 700; border-left: 4px solid #FFB700;">[Cuemath tier]</td>
        <td style="padding: 14px 16px; font-weight: 700;">[Value]</td>
        <td style="padding: 14px 16px; font-weight: 700;">[Value]</td>
        <td style="padding: 14px 16px; font-weight: 700;">[Value]</td>
      </tr>
      <!-- Non-Cuemath row (gray alternate) -->
      <tr style="background: #F5F5F5; border-bottom: 1px solid #EBEBEB;">
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
        <td style="padding: 14px 16px;">[Value]</td>
      </tr>
    </tbody>
  </table>
  <!-- Optional footnote for estimated/sourced data -->
  <p style="font-family: 'Avenir Next', 'Nunito Sans', 'Helvetica Neue', Arial, sans-serif; font-size: 13px; color: #666666; margin-top: 10px; line-height: 20px;">[* Footnote text for estimated or community-sourced figures.]</p>
</div>
<!--kg-card-end: html-->
```

**Usage:** Comparison blogs (cost, programs, platforms). Adapt column count by adding/removing `<th>` and `<td>` pairs consistently.

**Row pattern:**
- Cuemath rows: `background: #FFF1CC` + `border-left: 4px solid #FFB700` on first `<td>` + `font-weight: 700` on all cells
- Odd non-Cuemath rows: `background: #ffffff`
- Even non-Cuemath rows: `background: #F5F5F5`
- All rows except last: `border-bottom: 1px solid #EBEBEB`

**Footnote rule:** Include the `<p>` footnote only when any cell contains estimated or community-sourced data (e.g., Kumon/Mathnasium parent-reported prices). Omit if all data is from official sources.

## Table of Contents (2026-06-04)

**This is the exact, mandatory design and color scheme for every blog Table of Contents.** Do not invent a different ToC style. Replace the old plain `<ul>` ToC. White card, 2px `#EBEBEB` border with a 4px `#FFB700` left accent, 12px radius. Top-level items are bold with a 2px gold underline on the link; nested sub-items are indented 18px and use a thin 1px `#EBEBEB` underline.

```html
<!--kg-card-begin: html-->
<div style="background:#FFFFFF;border:2px solid #EBEBEB;border-left:4px solid #FFB700;border-radius:12px;padding:22px 26px;max-width:950px;font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;color:#221B35;">
  <div style="font-size:18px;font-weight:700;margin-bottom:14px;">Table of Contents</div>
  <ul style="list-style:none;margin:0;padding:0;line-height:1.6;font-size:15px;">
    <!-- Top-level item -->
    <li style="margin:10px 0;font-weight:700;"><a href="#[section-slug]" style="color:#221B35;text-decoration:none;border-bottom:2px solid #FFB700;">[Section Name]</a></li>
    <!-- Nested sub-item (indented, thin border) -->
    <li style="margin:6px 0 6px 18px;"><a href="#[sub-section-slug]" style="color:#221B35;text-decoration:none;border-bottom:1px solid #EBEBEB;">[Sub-section Name]</a></li>
  </ul>
</div>
<!--kg-card-end: html-->
```

**Rules:**
- Top-level entry: `<li style="margin:10px 0;font-weight:700;">` + link `border-bottom:2px solid #FFB700;`
- Nested entry: `<li style="margin:6px 0 6px 18px;">` + link `border-bottom:1px solid #EBEBEB;` (no `font-weight:700`)
- All links: `color:#221B35;text-decoration:none;`
- `href` slugs must exactly match the heading anchor IDs in the post (lowercase, hyphenated).
- Card container is fixed: `#FFFFFF` bg, `2px solid #EBEBEB` border, `4px solid #FFB700` left border, `border-radius:12px`, `padding:22px 26px`, `max-width:950px`.
- Heading label is always literally "Table of Contents" at `font-size:18px;font-weight:700`.

---

## Stat / Student Story Cards (2026-07-16)

**The canonical, Ghost-tested card for showing data, statistics, or student success stories.** Use this whenever you want to surface a set of numbers (scores, percentiles, results) or student achievements with a link out to the full story. Supersedes the older "Student Success Story Cards" pastel/dark-pill style.

**Why this build:** Fully inline styles only (Ghost strips `<style>` blocks and `@font-face`, so no Athletics web font, no CSS classes, no `:hover`, no media queries). Layout uses `flex-wrap` with `flex:1 1 250px` so cards sit **2 across** in the ~720px Ghost content column and collapse to 1 column on mobile — no lonely full-width card. `white-space:nowrap` on the big number keeps "1530/1600" from breaking across lines.

```html
<!--kg-card-begin: html-->
<div style="font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;color:#221B35;margin:28px 0;">
  <div style="display:flex;flex-wrap:wrap;gap:14px;">

    <div style="flex:1 1 250px;border:1px solid #EBEBEB;border-radius:12px;padding:20px 22px;">
      <div style="font-size:30px;font-weight:800;line-height:1.1;letter-spacing:-0.3px;color:#3AAE5F;margin-bottom:10px;white-space:nowrap;">[STAT]</div>
      <div style="font-size:15px;line-height:1.45;color:#221B35;margin-bottom:12px;">[One-line description of who/what]</div>
      <a href="[STORY URL]" style="font-size:14px;color:#221B35;text-decoration:underline;text-underline-offset:3px;">Read the story</a>
    </div>

    <div style="flex:1 1 250px;border:1px solid #EBEBEB;border-radius:12px;padding:20px 22px;">
      <div style="font-size:30px;font-weight:800;line-height:1.1;letter-spacing:-0.3px;color:#E4632A;margin-bottom:10px;white-space:nowrap;">[STAT]</div>
      <div style="font-size:15px;line-height:1.45;color:#221B35;margin-bottom:12px;">[One-line description of who/what]</div>
      <a href="[STORY URL]" style="font-size:14px;color:#221B35;text-decoration:underline;text-underline-offset:3px;">Read the story</a>
    </div>

    <div style="flex:1 1 250px;border:1px solid #EBEBEB;border-radius:12px;padding:20px 22px;">
      <div style="font-size:30px;font-weight:800;line-height:1.1;letter-spacing:-0.3px;color:#2E86DE;margin-bottom:10px;white-space:nowrap;">[STAT]</div>
      <div style="font-size:15px;line-height:1.45;color:#221B35;margin-bottom:12px;">[One-line description of who/what]</div>
      <a href="[STORY URL]" style="font-size:14px;color:#221B35;text-decoration:underline;text-underline-offset:3px;">Read the story</a>
    </div>

    <div style="flex:1 1 250px;border:1px solid #EBEBEB;border-radius:12px;padding:20px 22px;">
      <div style="font-size:30px;font-weight:800;line-height:1.1;letter-spacing:-0.3px;color:#C42FB2;margin-bottom:10px;white-space:nowrap;">[STAT]</div>
      <div style="font-size:15px;line-height:1.45;color:#221B35;margin-bottom:12px;">[One-line description of who/what]</div>
      <a href="[STORY URL]" style="font-size:14px;color:#221B35;text-decoration:underline;text-underline-offset:3px;">Read the story</a>
    </div>

  </div>
  <div style="text-align:right;margin-top:14px;">
    <a href="[READ-ALL URL]" style="font-size:15px;font-weight:700;color:#221B35;text-decoration:underline;text-underline-offset:3px;">Read all</a>
  </div>
</div>
<!--kg-card-end: html-->
```

**Rules:**
- **Colors (in order):** green `#3AAE5F`, orange `#E4632A`, blue `#2E86DE`, magenta `#C42FB2`. These are saturated-for-white variants; rotate through them for each card. Text stays `#221B35`, borders `#EBEBEB`.
- **Never use `#FFD24D` or `#FFB700` on the "Read all" link** — both yellows are reserved (CTA button fill and accent rails/underlines). All links are brand navy `#221B35`, underlined.
- **Number sizing:** keep `font-size:30px` + `white-space:nowrap` so long stats ("1530/1600") stay on one line. If a stat still wraps, shorten the string, don't enlarge the card.
- **Card count:** works with 2, 3, or 4 cards (they wrap 2-per-row). For 3 cards, the third sits alone on row 2 — that's fine, or drop to `flex:1 1 200px` for 3-across.
- **Fonts:** system stack only (`'Avenir Next','Nunito Sans','Helvetica Neue',Arial`). Do NOT add Athletics `@font-face` — Ghost strips it and it renders the numbers in fallback font at the wrong weight anyway.
- **Links:** every "Read the story" points to a real impact-story URL; verify each resolves. "Read all" points to `https://www.cuemath.com/blog/tag/impact-stories/`.
- Drop the "Read all" row entirely if the card is used for pure statistics rather than student stories.

## Update — 2026-07-16 — Icon cards, best-for/not-for table, softened CTA (#FFD24D)

**CTA/button standard changed:** button fill is now `#FFD24D` (softer), text `#221B35`. `#FFB700` is retained as *accent gold* only (ToC left rails, link underlines, avatar rings). Use ONE button colour per section — no mixed primary/outline.

*(2026-08-13: this is now applied directly in the main CTA Box template above and the color palette reference at the top of this file — both used to still show the old `#FFB700` button fill, which caused a real mix-up while drafting a blog. If you ever see `#FFB700` on a button fill anywhere in this file again, it's a bug — fix it in place rather than treating it as a second valid option.)

All blocks below are inline-styled (Ghost posts have no stylesheet) and must be wrapped in `<!--kg-card-begin: html-->` / `<!--kg-card-end: html-->`. Card titles stay real `<h3>` with anchor ids. Mobile-safe via `flex-wrap`.

### Scannable icon-card set (replaces dense sub-sections)
Use ONE toned-down card colour for the whole set (neutral `#F7F6F3` card + single accent icon tile `#FFF1CC`), not rainbow.

```html
<!--kg-card-begin: html-->
<div style="display:flex;flex-direction:column;gap:14px;margin:26px 0;font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;">
  <div style="display:flex;gap:16px;align-items:flex-start;background:#F7F6F3;border:1px solid #EBEBEB;border-radius:12px;padding:20px 22px;box-sizing:border-box;">
    <div style="flex:0 0 auto;width:52px;height:52px;border-radius:12px;background:#FFF1CC;display:flex;align-items:center;justify-content:center;font-size:26px;">🔍</div>
    <div style="flex:1 1 auto;min-width:0;">
      <h3 id="anchor-id" style="font-size:18px;line-height:1.35;font-weight:700;color:#221B35;margin:2px 0 7px;">Card title (answer-style)</h3>
      <p style="font-size:15.5px;line-height:1.6;color:#221B35;margin:0;">Two tight lines. Optional inline link: <a href="URL" style="color:#221B35;text-decoration:none;border-bottom:2px solid #FFB700;font-weight:600;">anchor text</a>.</p>
      <!-- optional button row: -->
      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:15px;">
        <a href="URL" style="display:inline-flex;align-items:center;height:44px;padding:0 20px;border-radius:12px;font-size:14.5px;font-weight:700;text-decoration:none;background:#FFD24D;color:#221B35;border:1px solid #FFD24D;box-sizing:border-box;">Button label</a>
      </div>
    </div>
  </div>
  <!-- repeat the card div for each point -->
</div>
<!--kg-card-end: html-->
```
Optional highlight pill (put above the `<h3>` inside a card): `<span style="display:inline-block;font-size:11px;font-weight:700;letter-spacing:.7px;text-transform:uppercase;color:#8a5a00;background:#FFF1CC;border-radius:999px;padding:3px 9px;margin-bottom:9px;">Most platforms don't do this</span>`

### Best-for ✓ / not-for ✕ comparison table
Multi-row ✓ column vs a single ✕ item — the imbalance is the message. Follow with one crisp concluding line + one CTA.

```html
<!--kg-card-begin: html-->
<div style="display:flex;flex-wrap:wrap;gap:14px;margin:24px 0;font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;">
  <div style="flex:1 1 280px;border:1px solid #EBEBEB;border-radius:12px;overflow:hidden;box-sizing:border-box;">
    <div style="padding:14px 18px;font-size:16px;font-weight:700;color:#221B35;background:#D0FBE5;">✅ Best for</div>
    <div style="display:flex;gap:11px;align-items:flex-start;padding:13px 18px;border-top:1px solid #F0EFEC;font-size:15.5px;line-height:1.5;color:#221B35;">
      <span style="flex:0 0 auto;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;background:#00C46A;color:#fff;margin-top:1px;">✓</span>
      <span>Positive item</span>
    </div>
    <!-- repeat ✓ rows -->
  </div>
  <div style="flex:1 1 280px;border:1px solid #EBEBEB;border-radius:12px;overflow:hidden;box-sizing:border-box;">
    <div style="padding:14px 18px;font-size:16px;font-weight:700;color:#6B6480;background:#F5F5F5;">Not for</div>
    <div style="display:flex;gap:11px;align-items:flex-start;padding:13px 18px;border-top:1px solid #F0EFEC;font-size:15.5px;line-height:1.5;color:#6B6480;">
      <span style="flex:0 0 auto;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;background:#E4E2E6;color:#6B6480;margin-top:1px;">✕</span>
      <span>The one thing it's not for</span>
    </div>
  </div>
</div>
<!--kg-card-end: html-->
```

### Soft CTA card
```html
<!--kg-card-begin: html-->
<div style="margin:26px 0 8px;text-align:center;background:#FFF9E8;border:1px solid #F1E4BD;border-radius:12px;padding:26px 22px;font-family:'Avenir Next','Nunito Sans','Helvetica Neue',Arial,sans-serif;">
  <p style="margin:0 0 16px;font-size:17px;font-weight:700;color:#221B35;">One-line nudge written fresh for this blog.</p>
  <a href="URL" style="display:inline-flex;align-items:center;height:50px;padding:0 26px;border-radius:12px;background:#FFD24D;color:#221B35;font-size:16px;font-weight:700;text-decoration:none;border:1px solid #FFD24D;">Book a free class</a>
</div>
<!--kg-card-end: html-->
```
