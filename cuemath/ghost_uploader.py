#!/usr/bin/env python3
"""
Reusable Ghost uploader for Cuemath blog drafts.
Usage: python3 ghost_uploader.py path/to/[slug]_ghost.json
"""

import sys
import json
import time
import os
import pathlib

# ── Config ────────────────────────────────────────────────────────────────────
def _load_dotenv():
    env_path = pathlib.Path(__file__).resolve().parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

_load_dotenv()

GHOST_URL       = os.environ.get("GHOST_URL", "https://www.cuemath.com/blog")
ADMIN_API_KEY   = os.environ.get("GHOST_ADMIN_API_KEY")
if not ADMIN_API_KEY:
    sys.exit("Missing GHOST_ADMIN_API_KEY. Copy .env.example to cuemath/.env and fill in "
              "your Ghost Admin API key (Ghost Admin -> Settings -> Integrations -> your custom integration).")

# ── Dependencies ──────────────────────────────────────────────────────────────
try:
    import jwt
    import requests
except ImportError:
    print("Installing dependencies...")
    os.system("pip3 install PyJWT requests --quiet")
    import jwt
    import requests

# ── HTML Card Helper ─────────────────────────────────────────────────────────
def html_card(html: str) -> str:
    """
    Wrap raw HTML in Ghost's kg-card comment tags.
    REQUIRED for every custom HTML element: CTA boxes, callout boxes,
    testimonials, styled tables, author card, images, suggested reading.
    Without this, Ghost strips all inline styles and renders plain text.

    Usage:
        content += html_card('<div style="...">...</div>')
    """
    return f"\n<!--kg-card-begin: html-->\n{html}\n<!--kg-card-end: html-->\n"


# ── Auth ──────────────────────────────────────────────────────────────────────
def ghost_token() -> str:
    key_id, secret = ADMIN_API_KEY.split(":")
    iat = int(time.time())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    token = jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})
    return token if isinstance(token, str) else token.decode("utf-8")

# ── Upload ────────────────────────────────────────────────────────────────────
def upload(payload_path: str):
    with open(payload_path) as f:
        data = json.load(f)

    required = ["title", "html"]
    for field in required:
        if field not in data:
            print(f"❌ Missing required field: {field}")
            sys.exit(1)

    token   = ghost_token()
    headers = {
        "Authorization": f"Ghost {token}",
        "Content-Type": "application/json",
    }

    # Resolve author: convert "First Last" → "first-last" slug for Ghost API
    author_name = data.get("author", "").strip()
    author_slug = author_name.lower().replace(" ", "-") if author_name else ""

    post_body = {
        "title":            data["title"],
        "slug":             data.get("slug", ""),
        "html":             data["html"],
        "status":           "draft",
        "custom_excerpt":   data.get("excerpt", ""),
        "meta_title":       data.get("meta_title", data["title"]),
        "meta_description": data.get("meta_description", ""),
        "feature_image":    data.get("feature_image", ""),
        "tags":             [{"name": t} for t in data.get("tags", [])],
    }
    if author_slug:
        post_body["authors"] = [{"slug": author_slug}]

    post = {"posts": [post_body]}

    url = f"{GHOST_URL}/ghost/api/admin/posts/?source=html"
    print(f"Uploading to Ghost: {data['title']}")

    r = requests.post(url, json=post, headers=headers, timeout=30)

    if r.status_code in (200, 201):
        result      = r.json()["posts"][0]
        post_id     = result.get("id", "")
        preview_url = result.get("url", "")
        print(f"\n✅ Draft uploaded successfully!")
        print(f"   Title   : {data['title']}")
        print(f"   Post ID : {post_id}")
        print(f"   Preview : {preview_url}")
        print(f"   Ghost   : {GHOST_URL}/ghost/#/editor/post/{post_id}")
    else:
        print(f"\n❌ Upload failed (HTTP {r.status_code}):")
        try:
            err = r.json()
            print(json.dumps(err, indent=2)[:600])
        except Exception:
            print(r.text[:600])
        sys.exit(1)

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ghost_uploader.py path/to/payload.json")
        sys.exit(1)
    upload(sys.argv[1])
