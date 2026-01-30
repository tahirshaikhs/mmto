import psycopg2
from psycopg2.extras import RealDictCursor
from .config import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL, sslmode="require")

def already_posted(url):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT 1 FROM posted WHERE url=%s", (url,))
        return cur.fetchone() is not None

def mark_posted(url):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO posted(url) VALUES(%s) ON CONFLICT DO NOTHING", (url,))
        conn.commit()
