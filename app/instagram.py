import os
import requests

SESSIONID = os.getenv("INSTAGRAM_SESSIONID")

if not SESSIONID:
    raise RuntimeError("INSTAGRAM_SESSIONID is missing")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "X-IG-App-ID": "936619743392459",
    "Cookie": f"sessionid={SESSIONID}",
}

def fetch_posts(keyword):
    url = "https://www.instagram.com/api/v1/web/search/topsearch/"
    params = {"query": keyword}

    r = requests.get(url, headers=HEADERS, params=params, timeout=15)

    if r.status_code != 200:
        raise RuntimeError(
            f"Instagram blocked request ({r.status_code})"
        )

    return r.json()
