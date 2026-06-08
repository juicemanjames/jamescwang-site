#!/usr/bin/env python3
"""
Crawl jamescwang.com (Webflow static site), download all HTML + assets,
rewrite Webflow CDN URLs to local /assets paths, and write a self-contained
static site into ../public ready for Vercel.

Usage: python3 crawl.py
"""

import os
import re
import sys
import time
import hashlib
import urllib.request
import urllib.parse
from html import unescape

BASE = "https://www.jamescwang.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
ASSETS = os.path.join(PUBLIC, "assets")
IMG_DIR = os.path.join(ASSETS, "images")
CSS_DIR = os.path.join(ASSETS, "css")
JS_DIR = os.path.join(ASSETS, "js")
FILE_DIR = os.path.join(ASSETS, "files")

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# Pages to fetch (sitemap + nav-discovered tutorials). Webflow utility stubs
# (/untitled, /icons) intentionally excluded.
PAGES = [
    "/",
    "/about",
    "/all-posts",
    "/career-advice",
    "/tableauplayground",
    "/video-list/videos-life",
    "/video-list/videos",
    "/codetutorial",
    "/tutorialfolder/spatial-join",
    "/tutorialfolder/radar-chart",
    "/categories/art",
    "/categories/tech",
    "/categories/travel",
    "/categories/music",
    "/posts/jobsearch",
    "/posts/facebook",
    "/posts/startup",
    "/posts/dukebasketball",
    "/posts/vote",
    "/posts/no-no-spammers",
    "/posts/license",
    "/posts/who-will-keep-paying",
    "/posts/pornhub",
    "/career-advice/life-after-layoff",
    "/career-advice/ds-newgrad",
    "/career-advice/hamlet",
]

# Map remote asset URL -> local path (under /assets). Filled during crawl.
asset_map = {}
_seen_names = set()


def fetch(url, binary=False):
    # Guard against malformed URLs that slipped through HTML parsing
    # (e.g. trailing quotes/spaces from inline style attributes).
    url = url.strip().strip('"').strip("'").strip()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "replace")
        except Exception as e:
            if attempt == 2:
                print(f"  !! FAILED {url}: {e}", file=sys.stderr)
                return None
            time.sleep(1.5)


def asset_subdir(url):
    low = url.lower().split("?")[0]
    if low.endswith(".css"):
        return CSS_DIR, "/assets/css"
    if low.endswith(".js"):
        return JS_DIR, "/assets/js"
    if low.endswith(".pdf"):
        return FILE_DIR, "/assets/files"
    return IMG_DIR, "/assets/images"


def safe_name(url):
    """Build a readable, unique local filename from a CDN url."""
    path = urllib.parse.urlparse(url).path
    base = os.path.basename(path) or "index"
    base = urllib.parse.unquote(base)
    base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    if "." not in base:
        base += ".bin"
    if base in _seen_names:
        h = hashlib.md5(url.encode()).hexdigest()[:8]
        stem, ext = os.path.splitext(base)
        base = f"{stem}_{h}{ext}"
    _seen_names.add(base)
    return base


def localize_asset(url):
    """Download an asset (once) and return its local site path."""
    url = url.strip().strip('"').strip("'").strip()
    if not url or url.startswith("data:"):
        return None
    if url in asset_map:
        return asset_map[url]
    # Only localize Webflow CDN + same-origin assets.
    if not re.search(
        r"(website-files\.com|website\.files|cloudfront\.net|jamescwang\.com)", url
    ):
        return None
    # Same-origin (jamescwang.com) URLs are localized ONLY if they point to a
    # real asset file. Extension-less same-origin URLs are page links and must
    # be left for normalize_internal_links to handle.
    if "jamescwang.com" in url and not re.search(
        r"\.(png|jpe?g|gif|svg|webp|ico|css|js|pdf|woff2?|ttf|eot|mp4|webm)(\?|$)",
        url.lower(),
    ):
        return None
    disk_dir, web_dir = asset_subdir(url)
    name = safe_name(url)
    disk_path = os.path.join(disk_dir, name)
    local = f"{web_dir}/{name}"
    if os.path.exists(disk_path) and os.path.getsize(disk_path) > 0:
        asset_map[url] = local
        return local
    data = fetch(url, binary=True)
    if data is None:
        return None
    with open(disk_path, "wb") as f:
        f.write(data)
    asset_map[url] = local
    print(f"  asset {url.split('/')[-1][:50]:50s} -> {local}")
    return local


def rewrite_srcset(value):
    out = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        bits = part.split()
        u = bits[0]
        local = localize_asset(unescape(u))
        if local:
            bits[0] = local
        out.append(" ".join(bits))
    return ", ".join(out)


def process_html(html):
    # src="..."
    def _src(m):
        u = unescape(m.group(2))
        local = localize_asset(u)
        return f'{m.group(1)}="{local}"' if local else m.group(0)

    html = re.sub(r'(src|href)="([^"]+)"', _src, html)

    # srcset="..."
    def _srcset(m):
        return f'srcset="{rewrite_srcset(unescape(m.group(1)))}"'

    html = re.sub(r'srcset="([^"]+)"', _srcset, html)

    # inline style background-image:url("...") or url(...)
    def _bg(m):
        u = unescape(m.group(1).strip("'\""))
        local = localize_asset(u)
        return f'url("{local}")' if local else m.group(0)

    html = re.sub(r"url\(([^)]+)\)", _bg, html)

    return html


def normalize_internal_links(html):
    """Make internal links work as clean URLs on Vercel (leading slash kept)."""
    # Strip protocol+domain on internal absolute links -> root-relative.
    html = html.replace("https://www.jamescwang.com", "")
    html = html.replace("http://www.jamescwang.com", "")
    html = html.replace("https://jamescwang.com", "")
    html = html.replace("http://jamescwang.com", "")
    return html


def out_path_for(page):
    if page == "/":
        return os.path.join(PUBLIC, "index.html")
    rel = page.strip("/")
    return os.path.join(PUBLIC, rel, "index.html")


def main():
    for d in (IMG_DIR, CSS_DIR, JS_DIR, FILE_DIR):
        os.makedirs(d, exist_ok=True)

    ok, fail = 0, 0
    for page in PAGES:
        url = BASE + page
        print(f"PAGE {page}")
        html = fetch(url)
        if html is None:
            fail += 1
            continue
        html = process_html(html)
        html = normalize_internal_links(html)
        dest = out_path_for(page)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
        ok += 1
        time.sleep(0.3)

    print(f"\nDONE. pages ok={ok} fail={fail}, assets={len(asset_map)}")


if __name__ == "__main__":
    main()
