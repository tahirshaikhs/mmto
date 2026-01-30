# app/instagram.py
import os
import requests

SESSIONID = os.environ.get("hmac.AR2vh1btke1C1NE7KGgQrez3SndLEVSwODh497yg8UNjPi-f")

if not SESSIONID:
    raise RuntimeError("INSTAGRAM_SESSIONID is missing")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "X-IG-App-ID": "936619743392459",
    "Cookie": f"sessionid={SESSIONID}",
}

def fetch_posts(keyword):
    url = "https://www.instagram.com/api/v1/web/search/topsearch/"
    params = {"query": keyword}

    r = requests.get(url, headers=HEADERS, params=params)
    if r.status_code != 200:
        raise RuntimeError("Instagram blocked request")

    return r.json()
