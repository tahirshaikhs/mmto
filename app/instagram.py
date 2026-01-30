import os
import requests

SESSIONID = os.getenv("INSTAGRAM_SESSIONID")

if not SESSIONID:
    raise RuntimeError("INSTAGRAM_SESSIONID is missing")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "X-IG-App-ID": "936619743392459",
    "Accept": "application/json",
    "Cookie": f"sessionid={SESSIONID}",
}

def fetch_posts(keyword):
    url = "https://www.instagram.com/api/v1/web/search/topsearch/"
    params = {"query": keyword}

    r = requests.get(url, headers=HEADERS, params=params, timeout=15)

    # 🔴 Instagram blocked or returned HTML
    if "text/html" in r.headers.get("Content-Type", ""):
        raise RuntimeError(
            "Instagram returned HTML instead of JSON "
            "(blocked / challenge / expired session)"
        )

    if r.status_code != 200:
        raise RuntimeError(f"Instagram HTTP {r.status_code}")

    try:
        return r.json()
    except Exception:
        raise RuntimeError(
            "Instagram response is not JSON.\n"
            f"First 200 chars:\n{r.text[:200]}"
        )
