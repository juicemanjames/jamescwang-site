# jamescwang.com

Static personal site, migrated off Webflow and self-hosted. Every page, image,
CSS, JS, and the resume PDF is vendored into this repo — no runtime dependency on
the Webflow CDN.

## What this is

- Plain static HTML/CSS/JS (originally authored in Webflow, May 2020).
- 23 pages, ~165 local assets.
- Deployed on Vercel as a zero-build static site.
- Analytics via Vercel Analytics (the old dead Universal Analytics tag was removed).

## Layout

```
/                       index.html (home)
/about, /all-posts, /career-advice, /tableauplayground
/posts/*                9 data-science project posts
/career-advice/*        3 career posts
/video-list/*           2 video pages
/categories/*           4 Webflow category pages
/assets/images          all images + favicon/webclip
/assets/css             site stylesheet
/assets/js              jquery + webflow.js (mobile nav only)
/assets/files           resume PDF
/scripts/crawl.py       the one-off migration crawler (not deployed)
vercel.json             cleanUrls + asset caching
```

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000  (use trailing slashes locally, e.g. /about/)
```

`cleanUrls` in `vercel.json` makes extension-less paths (`/about`) work on Vercel
without the trailing slash.

## Deploy to Vercel

First time:

```bash
npm i -g vercel        # if not installed
vercel login
vercel                 # link + preview deploy
vercel --prod          # production deploy
```

Subsequent deploys: push to the connected Git repo (Vercel auto-deploys), or run
`vercel --prod`.

### Framework preset

This is a **static site, no build step**. In the Vercel project settings:

- Framework Preset: **Other**
- Build Command: *(leave empty)*
- Output Directory: *(leave empty / `.`)*

### Enable Analytics

Vercel project → **Analytics** tab → Enable. The tracking snippet is already
embedded in every page (`/_vercel/insights/script.js`), which Vercel serves
automatically once Analytics is on.

## DNS cutover (jamescwang.com)

1. In Vercel: Project → **Settings → Domains** → add `jamescwang.com` and
   `www.jamescwang.com`.
2. Vercel will show the required records. Typical setup:
   - Apex `jamescwang.com` → **A** record `76.76.21.21` (or the ALIAS/ANAME
     Vercel shows).
   - `www` → **CNAME** `cname.vercel-dns.com`.
3. At your DNS registrar, replace the current Webflow records with the Vercel
   records above.
4. Pick the primary domain in Vercel (recommend `www` → apex redirect or vice
   versa) so you don't split traffic.
5. Wait for propagation (minutes to a few hours). Vercel auto-provisions HTTPS.
6. Verify: `curl -sIL https://jamescwang.com | head` should show `200` from
   Vercel, not Webflow.

> Keep the Webflow site published until DNS has fully propagated and the Vercel
> site is confirmed live, then cancel Webflow.

## Known cosmetic follow-ups (optional)

- `favicon.ico` / `webclip.png` are Webflow's generic defaults (the originals
  were never customized). Swap in a custom icon if desired.
- Markup is Webflow-generated (verbose). Fine for a low-traffic static site; a
  future clean rebuild (e.g. Astro, posts as Markdown) is the "do it right" path
  if you start posting again.
- Dead `/codetutorial` and `/tutorialfolder/*` tutorial pages (already 404 on the
  live Webflow site) were removed from the nav. The "Build a Radar Chart" button
  now points to `/tableauplayground`.

## Re-running the migration crawler

Only needed if you want to re-pull from the live Webflow site:

```bash
python3 scripts/crawl.py
```

It is idempotent for assets (skips already-downloaded files).
