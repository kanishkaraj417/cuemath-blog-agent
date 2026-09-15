
# Brain — Claude Code Instructions

This directory is a personal knowledge and productivity workspace.

## Projects in this directory
- `diary/` — personal diary (handled by /toystoy)
- `samwise/` — people and relationships tracker (handled by /samwise)
- `cuemath/` — Cuemath blog system (see below)
- `memory/` — persistent memory across conversations

---

## Cuemath Blog System

When the user mentions blogs, Cuemath, writing, or drafts — operate as the Cuemath Blog Agent.

### Knowledge files (always read ALL of these before any blog task)
Read every file under `/Users/nikita.joshi/Documents/brain/cuemath/` — including all subdirectories:
- `cuemath/Blog writing and overall guidelines.md` ← read first. The single source for structure, voice, style, CTA strategy, and the pre-publish checklist. (Replaces the former `style-guide.md` and `seo-gold-standards.md`, both archived 2026-08-13 to `_archives/`.)
- `cuemath/product-knowledge/` — all files

Do not skip any file. This ensures positioning, stats, competitor data, and style inputs are all current before writing.

(Read only when actually needed, not up front: `cuemath/html-templates.md` and `cuemath/design-guidelines.md` are read at the HTML-build step; `cuemath/blogs/published/tracker.md` is read at the interlinking step.)

### Two workflows available:

---

### WORKFLOW 1 — Feed data (`feed` keyword)
**Trigger:** User says "feed", "add this", "save this", "update product", pastes a URL/text with intent to store it, or shares writing style inputs, references, or blog examples.

1. Read the content (fetch URL if needed, or read pasted text)
2. Identify what type it is:
   - **Product feature / brand stat / campaign** → append to `cuemath/product-knowledge.md`
   - **HTML element / template** → append to `cuemath/html-templates.md`
   - **Writing style input, reference blog, style change, writing example, competitor blog, new content pattern** → append to `cuemath/Blog writing and overall guidelines.md` as a new dated section: `## Update — [YYYY-MM-DD] — [Short Label]`
   - **General resource** → append to the most relevant knowledge file
3. Confirm: "Added to [filename]: [one-line summary]"
4. If it conflicts with existing info, flag it: "⚠️ Conflict: previously had [X], now seeing [Y]. Which is current?"

Do not rewrite existing files. Append new dated sections only.

---

### WORKFLOW 2 — Generate blog (`blog` keyword)
**Trigger:** User says "blog", "write a blog", "draft", or describes a blog topic.

See `.claude/commands/blog.md` for the full 5-stage flow. Summary:

- **Stage 1:** Read files → ask topic, keyword, type (3 questions only)
- **Stage 2:** Keywords (Ahrefs if needed) → live SERP + AI Overview research (ask user to VPN first) → optional Reddit sweep (ask permission first) → anything else to share
- **Stage 3:** Write full draft with [HTML CARD] and [IMAGE] placeholders → save to Obsidian → open in Obsidian
- **Stage 4:** After user reviews → auto-resolve images + CTAs → ask for Trustpilot quotes, achievement cards, Cuemath links → build enriched draft + Ghost JSON (Reddit research from Stage 2 informs the writing but is never quoted/attributed in the post)
- **Stage 5:** Ask author slug + tags → output FAQ schema → upload to Ghost

**Files to read at drafting time (Stage 3):**
- `cuemath/Blog writing and overall guidelines.md`
- **Every file in `cuemath/product-knowledge/`** (read all of them; this covers any added or renamed files)

**Files to read later, only when needed:**
- `cuemath/html-templates.md` + `cuemath/design-guidelines.md` — at the HTML-build step (Stage 4)
- `cuemath/blogs/published/tracker.md` — at the interlinking step (Stage 4)

---

### FULL BLOG OUTPUT FORMAT

Produce every section in this exact order. Do not skip any.

#### SEO TITLE
- Target keyword included
- Year if it's a list or guide ("2026")
- Value hook: number, [bracket claim], or emotional trigger
- Max 60 characters

#### META DESCRIPTION
- 150–160 characters
- First-person voice
- Target keyword included
- Ends with a value promise

#### BLOG EXCERPT
- 2–3 sentences
- What the reader gets from this blog
- No Cuemath mention

#### TABLE OF CONTENTS
Use the exact, mandatory ToC card from `html-templates.md` → **"Table of Contents (2026-06-04)"**: white card, `2px solid #EBEBEB` border with a `4px solid #FFB700` left accent, `border-radius:12px`. Top-level items are bold with a 2px gold link underline; nested sub-items indented 18px with a thin 1px `#EBEBEB` underline. `href` slugs must match the post's heading anchor IDs exactly. Do not use any other ToC style.

#### FULL BLOG CONTENT

Structure is judgment-based — decide per audience and topic, following the principles in `Blog writing and overall guidelines.md`. There is no required template. The patterns below are **common starting points you can adapt or ignore**, not mandatory flows. Draft the content first, then choose the structure that serves the reader best.

**Type A (Comparison) — common pattern:** Intro → at-a-glance/quick answer → how we reviewed → reviewed items (H3 each) → CTA → comparison table → FAQ

**Type B (Practice problems) — common pattern:** Brief intro → topic sections with emoji H2s → each: explainer + mistake callout + problems (Easy/Medium/Hard) + solutions → CTA → mixed practice → FAQ

**Type C (Guide) — common pattern:** Key Takeaways box → ToC → each H2 opens with a quick answer → tables → Cuemath in a resources section → CTA → FAQ

**Type D (Cuemath-specific):** Ask for clarification on structure before drafting.

FAQ count: `Blog writing and overall guidelines.md`'s checklist sets 6–8 as the real floor (more is fine if genuinely specific) — treat that as a minimum, not just a judgment call. CTA count defaults to 2 per `html-templates.md` (mid-blog + before FAQ); placement within the blog is still a judgment call.

#### HTML ELEMENTS
`html-templates.md` is a **design system reference** — colors, fonts, and code patterns to draw from, not a checklist of things to include.

**HTML vs. plain text rule — follow this strictly:**
- Regular prose paragraphs, H2s, H3s, bullet lists, blockquotes → **plain text** in the Ghost post. Ghost renders these natively. No kg-card wrapper needed or wanted.
- Custom styled elements only → **kg-card HTML**: CTA boxes, callout boxes, testimonials, styled comparison tables, author cards, worksheet download blocks, suggested reading boxes.
- Rule of thumb: if it would look fine in a standard blog without special styling, write it as plain text. Only reach for HTML when the design element genuinely adds value a plain heading or paragraph cannot.

Use your editorial judgment:
- Place HTML elements where they add value to the reader, not on a schedule
- A CTA might appear once or twice — wherever it fits the flow
- Testimonials, suggested reading, worksheet blocks — include them if relevant
- You can combine, adapt, or adjust heading/subheading copy inside any element
- Keep consistent: the color palette, font choices, and code structure from the templates

Produce all HTML elements filled in, in context (woven into the draft at the point where they appear), not as a separate section at the end.

#### IMAGE SUGGESTIONS
For every image location:
```
Image [N]: After "[Heading]"
Unsplash query: "[search terms]"
Alt text: "[descriptive alt text]"
```
Flag branded images as: **[IMAGE REQUEST: what is needed]**

#### FAQ SECTION
```html
<h2>Frequently Asked Questions</h2>

<h3>[Exact-match keyword question]</h3>
<p>[Answer — 3–6 sentences. First sentence repeats keyword phrase.]</p>
```

#### SOURCES
Before the author card, add a plain sources list — minimum 4 links. Target: .edu pages, official curriculum docs, Trustpilot, government data, or research studies cited in the blog.

```html
<h2>Sources</h2>
<ul>
  <li><a href="[URL]" rel="nofollow noopener" target="_blank">[Source name — brief description]</a></li>
</ul>
```

Required for E-E-A-T compliance and LLM citeability. Even 4 authoritative links make the blog quotable by AI systems and signal trustworthiness to Google.

#### FAQ JSON-LD SCHEMA
Do NOT embed the FAQ schema in the post HTML. After uploading, output the script block separately with this instruction to the user:

> **Add to Ghost:** Post Settings → Code Injection → Post Header → paste this block:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text — plain text, no HTML tags inside]"
      }
    }
  ]
}
</script>
```

Ghost's code injection (Post Header) renders the script in the page `<head>` where Google crawlers expect structured data. Embedding it in the post body is incorrect placement.

#### PRE-PUBLISH CHECKLIST
End every draft with this filled in:

**Content & Voice**
- [ ] Intro has no fixed formula — open with the most useful thing first, per the Rule of 2 Sentences in the guidelines file (do NOT use the old stat → problem → resolve → credibility hook, which is banned)
- [ ] "Reviewed by Cuemath's expert tutors" in intro or byline
- [ ] Original analysis or first-hand perspective — not a summary of other sites
- [ ] No paragraph over 5 sentences
- [ ] No vague qualifiers ("generally," "typically," "tends to") — replaced with specific data

**Keywords & Structure**
- [ ] Target keyword in: title, meta, first paragraph, 2+ H2s, FAQ questions, image alt text
- [ ] Each major H2 serves a distinct sub-query angle (comparison, evidence, risk/skepticism, use-case, evaluation criteria) — not a restatement of the head keyword
- [ ] Section format matches query type: cost → table/FAQ; how-to → numbered steps; comparison → table; trust → evidence + UGC quote

**AI Retrieval — Passage Level**
- [ ] Every paragraph leads with the verifiable fact/claim — no build-up leads
- [ ] Subject program named explicitly in: intro paragraph, every differentiating claim, every FAQ answer (never "the platform," "it," or "the program")
- [ ] Every challengeable claim has a number, named source, or named mechanism — no bare "research shows"
- [ ] Every program claim is scoped: grade range + need type stated
- [ ] Competitor blogs include one explicit "recommended alternative" passage naming Cuemath with a specific reason (near the end, not hedged)

**Trust & UGC**
- [ ] Every trust/"is it worth it" section has at least one real attributed Trustpilot quote (name + date, never invented). Reddit research informs the writing but is never quoted or credited to Reddit in the post.
- [ ] At least one embedded tutor quote in body content (specific grade + topic, not generic praise)

**FAQ**
- [ ] FAQs answer what a reader still wonders after the blog (6–8 minimum per the guidelines file's checklist; more is fine if genuinely specific)
- [ ] Every FAQ answer: first sentence = direct answer; Cuemath named explicitly; 1–2 sentences max
- [ ] FAQ questions phrased conversationally (as a parent would type into ChatGPT or Perplexity)
- [ ] FAQ JSON-LD in Ghost code injection (Post Header), not post body

**Technical & Publishing**
- [ ] Images: descriptive filenames + accurate contextual alt text (not keyword-stuffed)
- [ ] CTA(s) placed where they convert best for this blog (default is 2, per html-templates.md; placement within the blog is a judgment call)
- [ ] Each CTA heading and copy written fresh for this blog and placement — no recycled "Where Hard Work Turns Into Real Results" or other generic lines
- [ ] HTML elements used where they add value (not forced in)
- [ ] Image suggestions for every image slot
- [ ] Sources section included (4+ links: .edu, official curriculum, Trustpilot, government data, or cited research)
- [ ] "Last reviewed: [Month Year]" in intro or author section

#### SAVE THE DRAFT
Save the completed draft to: `cuemath/blogs/drafts/[YYYY-MM-DD]-[slug].md`

#### RESOLVE UNSPLASH IMAGES
For each image in the blog, run this bash command to get a real photo ID:
```bash
curl -sL "https://unsplash.com/s/photos/[query-words-with-dashes]" | grep -o 'photo-[a-zA-Z0-9_-]\{15,\}' | head -1
```
Use the returned ID to build the final image URL: `https://images.unsplash.com/photo-[ID]?w=1200&q=80`
Replace all image placeholders in the HTML with these real URLs before uploading.

#### GHOST HTML CARD RULE (critical — apply to every blog)
Ghost does NOT render raw `<div>` blocks from the API. Every custom HTML element (CTA boxes, callout boxes, testimonials, tables, author card, images, suggested reading) MUST be wrapped in Ghost's HTML card tags:

```html
<!--kg-card-begin: html-->
<div style="...">your HTML here</div>
<!--kg-card-end: html-->
```

Without these wrappers, Ghost strips all styling and renders the content as plain text. Regular prose (`<p>`, `<h2>`, `<h3>`, `<ul>`, `<blockquote>`) does NOT need wrapping — only the custom styled elements do.

In Python, use this helper for every HTML element:
```python
def html_card(html: str) -> str:
    return f"\n<!--kg-card-begin: html-->\n{html}\n<!--kg-card-end: html-->\n"
```

#### UPLOAD TO GHOST
After saving the draft, create a Ghost payload file and upload:

1. Build the full HTML string for the post with **all custom HTML elements wrapped using `html_card()`** as described above.

2. Save `cuemath/blogs/drafts/[YYYY-MM-DD]-[slug]_ghost.json` with this structure:
```json
{
  "title": "...",
  "slug": "...",
  "meta_title": "...",
  "meta_description": "...",
  "excerpt": "...",
  "html": "...mixed plain text + kg-card wrappers only on custom HTML elements...",
  "feature_image": "...first image URL...",
  "author": "...exact Ghost username/slug from question 6...",
  "tags": ["...tags from question 7..."]
}
```

**Author rule:** Use the exact Ghost username/slug provided by the user in Q6. Never derive it from a display name — Ghost silently falls back to the default admin user if a slug doesn't match.

**Tags rule:** Use exactly the tags the user specified in Q7. Never add tags on your own judgment.

3. Run: `python3 /Users/nikita.joshi/Documents/brain/cuemath/ghost_uploader.py /Users/nikita.joshi/Documents/brain/cuemath/blogs/drafts/[YYYY-MM-DD]-[slug]_ghost.json`

4. Report the Ghost preview URL returned by the script.
