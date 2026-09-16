---
name: Cuemath link UTM tagging process
description: How to tag Cuemath-bound blog links with UTM parameters directly on the full URL (no shortener) — which links need it, the UTM convention, and the app.cuemath.com fixed exception
---

## Tagging Cuemath links for blog CTAs and internal links

**2026-09-16: Rebrandly access was removed. Do not create short links, do not reference `cuemath.link`, and do not use any URL shortener.** Every link that used to go through Rebrandly now gets its UTM parameters appended directly onto the full destination URL, and that tagged full URL is the `href` used in the HTML.

### Which links need UTMs
Any link pointing to the Cuemath website itself — `cuemath.com` (signup, tutors, math-test, pricing, curriculum, about, etc.) — or `app.cuemath.com`, plus external third-party app store links (e.g. Apple App Store for a Cuemath app). The test is "does this link go to the Cuemath website (or an app store for a Cuemath app)," not a fixed list of pages.

### Never add UTMs to
Any URL under `cuemath.com/blog/` — these are internal blog-to-blog links and go in the HTML as raw `cuemath.com` URLs directly. No UTM needed.

### Standard UTM convention
```
https://destination-url.com/?utm_source=blog-lead&utm_medium=FULL_BLOG_URL&utm_campaign=CAMPAIGN_NAME
```
- `utm_source`: `blog-lead` (always)
- `utm_medium`: the full blog URL this link lives on, e.g. `www.cuemath.com/blog/cuemath-vs-khan-academy/`
- `utm_campaign`: a blog-specific campaign name (ask the user if unsure)

### app.cuemath.com links — fixed campaign convention
**Rule:** Any link or CTA pointing to `app.cuemath.com`, from any blog, uses `utm_campaign=blog-app-cta`. This value never changes per blog — it's the single bucket for tracking total app signups sourced from blog CTAs, without needing to know or list every blog URL.

- `utm_source=blog-lead`, `utm_medium=<blog URL>` still follow the standard convention above
- Use `utm_content` (e.g. `mid`, `end`) to tell apart multiple app CTAs placed on the same blog
- Example: `https://app.cuemath.com/?utm_source=blog-lead&utm_medium=www.cuemath.com/blog/fun-preschool-math-activities-for-kids/&utm_campaign=blog-app-cta&utm_content=mid`

**Converting an existing evaluation-signup link to an app link:** the old Rebrandly back-half convention (e.g. `calcpuns-signup` → `calcpuns-app`) no longer applies since there's no short link — just point the tagged full URL at `app.cuemath.com` instead of the signup page.

### Back-half naming convention
No longer applicable — there is no short link to name a back-half for. Skip this step entirely.

