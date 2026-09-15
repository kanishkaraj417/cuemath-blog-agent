#!/usr/bin/env python3
"""
Upload local images to Ghost's image storage and print the resulting URLs.
Usage: python3 ghost_image_uploader.py img1.png img2.png ...
"""
import sys, time, os, json, pathlib

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
    os.system("pip3 install PyJWT requests --quiet")
    import jwt, requests

def ghost_token() -> str:
    key_id, secret = ADMIN_API_KEY.split(":")
    iat = int(time.time())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    token = jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})
    return token if isinstance(token, str) else token.decode("utf-8")

def upload_image(path: str) -> str:
    token = ghost_token()
    headers = {"Authorization": f"Ghost {token}"}
    url = f"{GHOST_URL}/ghost/api/admin/images/upload/"
    fname = os.path.basename(path)
    with open(path, "rb") as f:
        files = {"file": (fname, f, "image/png")}
        data = {"purpose": "image", "ref": fname}
        r = requests.post(url, files=files, data=data, headers=headers, timeout=60)
    if r.status_code in (200, 201):
        return r.json()["images"][0]["url"]
    raise RuntimeError(f"Failed {fname}: HTTP {r.status_code} {r.text[:300]}")

if __name__ == "__main__":
    results = {}
    for p in sys.argv[1:]:
        try:
            u = upload_image(p)
            results[os.path.basename(p)] = u
            print(f"OK  {os.path.basename(p)}  ->  {u}")
        except Exception as e:
            print(f"ERR {p}: {e}")
    print("\nJSON_MAP=" + json.dumps(results))
