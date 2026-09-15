#!/usr/bin/env python3
"""Update an existing Ghost post (by id) from a *_ghost.json payload, source=html.
Usage: python3 ghost_update.py <payload.json> <post_id>"""
import sys, time, json, os, pathlib

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

GHOST_URL     = os.environ.get("GHOST_URL", "https://www.cuemath.com/blog")
ADMIN_API_KEY = os.environ.get("GHOST_ADMIN_API_KEY")
if not ADMIN_API_KEY:
    sys.exit("Missing GHOST_ADMIN_API_KEY. Copy .env.example to cuemath/.env and fill in "
              "your Ghost Admin API key (Ghost Admin -> Settings -> Integrations -> your custom integration).")
try:
    import jwt, requests
except ImportError:
    os.system("pip3 install PyJWT requests --quiet"); import jwt, requests

def token():
    kid, sec = ADMIN_API_KEY.split(":")
    iat = int(time.time())
    return jwt.encode({"iat": iat, "exp": iat+300, "aud": "/admin/"}, bytes.fromhex(sec),
                      algorithm="HS256", headers={"kid": kid})

def main(payload_path, post_id):
    data = json.load(open(payload_path))
    hdr = {"Authorization": f"Ghost {token()}", "Content-Type": "application/json"}
    # 1) fetch current updated_at (optimistic locking)
    g = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{post_id}/", headers=hdr, timeout=30)
    g.raise_for_status()
    cur = g.json()["posts"][0]
    body = {
        "updated_at":       cur["updated_at"],
        "title":            data["title"],
        "html":             data["html"],
        "custom_excerpt":   data.get("excerpt", ""),
        "meta_title":       data.get("meta_title", data["title"]),
        "meta_description": data.get("meta_description", ""),
        "feature_image":    data.get("feature_image", ""),
    }
    author = data.get("author", "").strip()
    if author:
        body["authors"] = [{"slug": author.lower().replace(" ", "-")}]
    r = requests.put(f"{GHOST_URL}/ghost/api/admin/posts/{post_id}/?source=html",
                     json={"posts": [body]}, headers=hdr, timeout=30)
    if r.status_code == 200:
        res = r.json()["posts"][0]
        print("✅ Updated:", res.get("title"))
        print("   Status :", res.get("status"))
        print("   Preview:", res.get("url"))
        print("   Editor :", f"{GHOST_URL}/ghost/#/editor/post/{post_id}")
    else:
        print(f"❌ HTTP {r.status_code}"); print(r.text[:600]); sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
