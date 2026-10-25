# Deploy on Cloudflare

The site is static files built into `dist/`. Cloudflare Workers can serve static assets from that folder for free. Dashboard labels change over time, so match the meaning rather than the exact wording.

## 1. Project configuration

`wrangler.jsonc` in the repository root tells Cloudflare what to serve:

```jsonc
{
  "name": "your-site-name",
  "main": "./worker/index.ts",
  "compatibility_date": "2026-09-01",
  "assets": {
    "directory": "./dist",
    "binding": "ASSETS",
    "run_worker_first": ["/og.mp4"],
    "not_found_handling": "404-page"
  }
}
```

- `directory` must match the build output folder.
- `not_found_handling: "404-page"` serves your `404.html` page for unknown URLs.
- Use `run_worker_first` only for files that need a small Worker, such as a video that must answer byte-range requests (see [pitfalls.md](pitfalls.md)). Leave it out if you have no such file.
- Copy the `observability` block from the dashboard into this file, so a deploy from the repository does not change dashboard settings. Logs and traces are separate settings; do not turn one on because you meant the other.

## 2. Connect the repository

1. Create a Cloudflare account and sign in.
2. Go to **Workers & Pages**, then **Create**, then **Import a repository**.
3. Connect GitHub. Authorise the Cloudflare GitHub app for the one repository you need, not for all repositories.
4. Set the build settings:
   - **Root directory:** `/` (unless the site lives in a subfolder).
   - **Build command:** `bun install && bun run build`
   - **Deploy command:** `bunx wrangler deploy`
   - If the dashboard asks for a version or deploy command field and it is optional, leave it empty.
5. Deploy. Every push to the production branch (usually `main`) now deploys automatically.

If the first build fails, read the build log. The usual causes are a missing `dist/` folder (the build command did not run or failed) or a wrong `directory` in `wrangler.jsonc`.

## 3. Custom domain

1. The owner buys the domain themselves; give them the steps and wait for them to confirm the domain name. Never enter payment details or ask for account credentials.
2. In the Worker's settings, open **Domains & Routes**, then **Add**, then **Custom domain**. Enter the bare domain, for example `example.com`. Cloudflare creates the DNS record.
3. Open the new address in a private browser window and confirm the site loads over HTTPS.

## 4. Security and redirects

In the zone (the domain) settings:

- **SSL/TLS → Edge Certificates → Always Use HTTPS:** on. Plain `http://` then redirects to `https://`.
- **HSTS** (same page): enable with a maximum age of 6 months, with "include subdomains" and "preload" off to start. HSTS is hard to undo for browsers that have seen it, so only turn it on once the HTTPS redirect works.
- **www:** choose one canonical address and redirect the other. Create a **Redirect Rule** (Rules → Redirect Rules) with:
  - When: hostname equals `www.example.com`
  - Then: dynamic redirect, expression `concat("https://example.com", http.request.uri.path)`, status 301, preserve query string.
- **Security → Bots (or Settings):** if "Block AI bots" is on, the AI crawlers that you want to read the site may be refused. Turn it off, or allow the crawlers you want. Confirm the managed robots.txt setting is off, so the site's own `robots.txt` is the one served.
- **Caching → Configuration → Crawler Hints:** on. This tells search engines when a page changes.

## 5. Web analytics

If the site's footer or privacy text says nothing leaves the page, turn off Cloudflare Web Analytics' automatic setup. If the owner wants analytics, keep it and say so in the footer. Make the footer and the reality match.

## 6. Headers

Put security headers in `public/_headers`, served on every response:

- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`
- `X-Frame-Options: DENY`
- A Content-Security-Policy. Start with `Content-Security-Policy-Report-Only`, read the browser's reports for a few days, then switch the header name to enforce it.

Cache hashed build files for a year: `/_astro/*` with `Cache-Control: public, max-age=31536000, immutable`. Hashed names change when content changes, so this is safe.

## 7. Check the deployment

Run these from a terminal and compare with the expected result:

```bash
curl -sI http://example.com/ | head -1                       # 301 to https
curl -sI https://www.example.com/ | head -1                  # 301 to the bare domain
curl -sI https://example.com/ | grep -i strict-transport     # HSTS present
curl -s https://example.com/robots.txt | head -5             # the site's own file
curl -s -o /dev/null -w "%{http_code}\n" https://example.com/no-such-page   # 404
```
