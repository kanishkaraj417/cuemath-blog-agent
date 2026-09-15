---
name: Rebrandly link creation process
description: How to create Cuemath short links on cuemath.link via Rebrandly API using curl, including domain ID, UTM structure, and back-half naming
---

## Creating Rebrandly short links for Cuemath blogs

**API key:** put yours in `cuemath/.env` as `REBRANDLY_API_KEY` (Rebrandly dashboard -> Account Settings -> API Keys). Never hardcode it in a script or paste it into a shared doc.

**Custom domain:** `cuemath.link`
**Domain ID:** `9d834e1bec424526bf751151a21a767c` (Rebrandly dashboard -> Domains -> cuemath.link, if this ever changes, look it up there)

The domain ID MUST be passed explicitly — omitting it defaults to `rebrand.ly` (wrong domain).

### curl command template

```bash
curl -s -X POST https://api.rebrandly.com/v1/links \
  -H "Content-Type: application/json" \
  -H "apikey: $REBRANDLY_API_KEY" \
  -d '{
    "destination": "https://destination-url.com?utm_source=blog-lead&utm_medium=PAGE_URL&utm_campaign=CAMPAIGN_NAME",
    "slashtag": "BACKHALF",
    "domain": { "id": "9d834e1bec424526bf751151a21a767c" }
  }'
```

### UTM parameter convention (from cuemath-vs-khan-academy blog)
- `utm_source`: `blog-lead`
- `utm_campaign`: `insights-cuemathvsothers` (or blog-specific campaign name)
- `utm_medium`: full blog URL e.g. `www.cuemath.com/blog/cuemath-vs-khan-academy/`

### Which URLs need Rebrandly short links

**Always Rebrandly:**
- `/parent/signup/` — CTA links and anywhere free trial is encouraged
- `/our-tutors/` — when Cuemath tutors are mentioned/linked
- `/math-test/` — MathFit Evaluation links
- `app.cuemath.com` — when a blog CTA promotes the Cuemath app instead of a trial signup (e.g. for age groups Cuemath doesn't tutor live, like preschoolers)
- External third-party app stores (e.g. Apple App Store for MathGym app)

### app.cuemath.com links — fixed campaign convention

**Rule:** Any link or CTA pointing to `app.cuemath.com`, from any blog, uses `utm_campaign=blog-app-cta`. This value never changes per blog — it's the single bucket for tracking total app signups sourced from blog CTAs, without needing to know or list every blog URL.

- `utm_source=blog-lead`, `utm_medium=<blog URL>` still follow the standard convention above
- Use `utm_content` (e.g. `mid`, `end`) to tell apart multiple app CTAs placed on the same blog
- Example: `https://app.cuemath.com/?utm_source=blog-lead&utm_medium=www.cuemath.com/blog/fun-preschool-math-activities-for-kids/&utm_campaign=blog-app-cta&utm_content=mid`

**Converting an existing evaluation-signup link to an app link:** new slug = old slug + `-app` suffix (e.g. `calcpuns-signup` -> `calcpuns-app`).

**Never Rebrandly:**
- Any URL under `cuemath.com/blog/` — these are internal blog-to-blog links and go in the HTML as raw `cuemath.com` URLs directly. No UTM needed.

### Back-half naming convention
- Always ask the blog owner to confirm back-half slugs (e.g. `cvskblog1`, `cvskblog2`) and what each link points to before creating. Never guess or invent them.

### To delete a wrong link
```bash
curl -s -X DELETE https://api.rebrandly.com/v1/links/LINK_ID \
  -H "apikey: $REBRANDLY_API_KEY"
```

**Why the domain ID matters:** omitting it creates links on `rebrand.ly` instead of `cuemath.link`. Always include `"domain": {"id": "9d834e1bec424526bf751151a21a767c"}` in every create call.
