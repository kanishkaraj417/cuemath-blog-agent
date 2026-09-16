# Cuemath Blog Agent (`/blog`) — Setup

This folder gives you the `/blog` slash command in Claude Code: a 5-stage flow that researches a keyword, drafts a full blog post to Cuemath's style guide, builds the Ghost-ready HTML, and publishes it.

You'll need your own access to: **Ghost** (admin), **Ahrefs**, and **Claude Code**. Nothing in this folder includes anyone else's API keys — each person fills in their own below.

> **2026-09-16: Rebrandly is no longer used.** Links to the Cuemath website get UTM parameters appended directly to the full URL instead of a `cuemath.link` short link — see `cuemath/rebrandly-link-guide.md` for the current convention. No `REBRANDLY_API_KEY`/`REBRANDLY_DOMAIN_ID` needed.

> **Fastest path: let Claude do steps 1-3 for you.** Unzip the folder, open it in your terminal, run `claude`, and say something like: *"Read ONBOARDING.md and set this up for me — create cuemath/.env, and here are my keys: Ghost Admin API key is ..., Ahrefs token is ..."* Claude will create the `.env` file, fill it in, and add the MCP server connections in step 3 for you. You can still do it manually with the commands below if you'd rather.

## 1. Unzip and open as a Claude Code project

```bash
unzip cuemath-blog-agent.zip -d cuemath-blog-agent
cd cuemath-blog-agent
claude
```

`/blog` should now show up as a slash command (it reads `.claude/commands/blog.md`).

## 2. Add your own credentials

```bash
cp .env.example cuemath/.env
```

Fill in `cuemath/.env`:
- `GHOST_ADMIN_API_KEY` — Ghost Admin -> Settings -> Integrations -> (your custom integration) -> Admin API Key
- `AHREFS_TOKEN` — your Ahrefs account's API token (used below for the MCP connection, not read directly by any script)

**Never share your filled-in `.env` file or commit it anywhere.** It's per-person.

The three Ghost scripts (`ghost_uploader.py`, `ghost_update.py`, `ghost_image_uploader.py`) auto-install `PyJWT` and `requests` on first run — no manual pip install needed.

## 3. Connect the MCP servers `/blog` uses

- **Ahrefs** (Stage 2A keyword research) — connect it with your own Ahrefs API token. Exact command depends on Ahrefs' current MCP setup docs (Settings -> Integrations, or ahrefs.com/mcp) — as of this writing it's an HTTP MCP server at `https://api.ahrefs.com/mcp/mcp` with your token in the `Authorization` header:
  ```bash
  claude mcp add --transport http ahrefs https://api.ahrefs.com/mcp/mcp --header "Authorization: <your Ahrefs token>"
  ```
- **Reddit** (optional — Stage 2C's Reddit sweep, only runs if you say yes when asked). Requires [`uv`](https://docs.astral.sh/uv/) installed:
  ```bash
  claude mcp add reddit -- uvx mcp-server-reddit
  ```
- **Browser for live SERP research** (Stage 2B) — if your Claude Code client doesn't already have a built-in browser, add Playwright's MCP server:
  ```bash
  claude mcp add playwright -- npx @playwright/mcp@latest
  ```

Run `claude mcp list` to confirm they're connected.

## 4. Optional: Obsidian

Stage 3 offers to open the draft in Obsidian. This only works if you have an Obsidian vault open on this same folder — if you don't use Obsidian, ignore that step; the draft is a plain `.md` file you can open anywhere.

## 5. Run it

Type `/blog` in Claude Code and follow the 5 stages. It will stop and wait for your approval before touching HTML (Stage 4) and before publishing (Stage 5) — nothing goes to Ghost without you confirming.

## What's in this folder

| Path | Purpose |
|---|---|
| `.claude/commands/blog.md` | The `/blog` command itself — the full 5-stage flow |
| `cuemath/CLAUDE.md` | Auto-loaded context that routes blog-related requests to this system |
| `cuemath/Blog writing and overall guidelines.md` | Structure, voice, CTA rules, pre-publish checklist |
| `cuemath/product-knowledge/` | Product facts, USPs, pricing, competitor research, trust/results |
| `cuemath/html-templates.md` | CTA/author/table/callout HTML card templates |
| `cuemath/design-guidelines.md` | Color palette + font stack referenced when building HTML |
| `cuemath/rebrandly-link-guide.md` | How to create `cuemath.link` short links for CTAs |
| `cuemath/blogs/published/tracker.md` | Live list of published posts, used for interlinking suggestions |
| `cuemath/blogs/drafts/` | Where new drafts and their Ghost JSON payloads get saved |
| `cuemath/ghost_uploader.py` / `ghost_update.py` / `ghost_image_uploader.py` | Publish/update posts and images on Ghost |
| `.env.example` | Template for your personal API keys — copy to `cuemath/.env` |

## Keeping this in sync

This is a point-in-time export. When the guidelines file or `/blog` itself gets updated, ask whoever maintains it for a refreshed zip, or better, ask about moving this into a shared git repo so updates sync automatically.
