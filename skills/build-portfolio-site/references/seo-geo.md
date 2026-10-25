# Search and AI visibility

Run this after the site is live. Measure first, then change, then measure again. No one can promise a ranking; the aim is for the site to be complete, crawlable and accurate, so search engines and AI tools can find it and describe it correctly.

## 1. Baseline

Record these before changing anything, for every page:

- the HTTP status, and whether the canonical address is the page's own URL;
- the title (under about 60 characters) and meta description (under about 160 characters);
- one `h1` and a sensible heading order;
- `lang` on the `html` element, and a viewport meta tag;
- Lighthouse scores, mobile and desktop;
- what a search for the owner's name returns, in a private window.

Save the baseline in `seo-report.md`. The report is what the owner reads to see the change.

## 2. Tell search engines the site exists

- **Google Search Console:** add a Domain property for the bare domain. Verify through the DNS (Cloudflare can add the record). Submit `https://example.com/sitemap.xml`. Use **URL Inspection** on the home page and **Request indexing**.
- **Bing Webmaster Tools:** import the site from Search Console. Bing's index feeds some AI assistants, so this matters too.

Indexing takes days to weeks. "URL is not on Google" right after submitting is expected.

## 3. Sitemap and robots.txt

- `/sitemap.xml` lists every public page with its last-modified date taken from real content dates. Do not list the Markdown copies (see below).
- `/robots.txt` allows the crawlers the owner wants: search crawlers, answer-engine crawlers, and training crawlers if the owner allows training. Name each group, and add a `Sitemap:` line.
- Lighthouse's robots.txt check fails on directives it does not know, such as `Content-Signal` lines. If you want to state content signals, write them as comments instead.

## 4. Structured data (JSON-LD)

Use the schema that matches what is visible on each page:

- **Home:** `ProfilePage` whose main entity is a `Person` (name, job title, employer, `sameAs` links to the owner's real profiles, `knowsAbout`), plus `WebSite`.
- **Research pages:** `CollectionPage` with `ScholarlyArticle` per paper (name, authors, venue, year, DOI as an identifier).
- **Articles:** `Blog` for the index and `BlogPosting` per article (headline, dates, image, author, the blog it belongs to, and the original post as `discussionUrl` if there is one).
- **Breadcrumbs:** only where the page shows a visible trail.

Rules:

- Every name, headline and date in the markup must appear on the visible page. Write a quick check that compares them.
- `sameAs` lists only profiles that belong to the owner.
- Validate with Google's Rich Results Test and the schema.org validator. Read the warnings, not just the errors.

## 5. Generative engines (GEO)

AI answer engines pick passages they can quote. Make these easy:

- **A quotable bio near the top** that answers "Who is this?" in two or three sentences: the role, the employer, the work, and one verifiable fact.
- **`/llms.txt`** at the root: a short summary in Markdown, with the bio, the role, the site's sections as links, the profiles and the main projects or articles.
- **`/llms-full.txt`**: the home page as Markdown.
- **Markdown copies** of the main pages (`/index.md`, `/research.md`, `/articles/<slug>.md`), served as `text/markdown` with `X-Robots-Tag: noindex`. Search engines then list the HTML page, and agents can still read the Markdown.
- **Links between related pages.** Each project links to its article, each article links to its research or project.
- **Agent readiness:** run `/seo agentic` (claude-seo) or `agentic_check` from the plugin. It tests robots rules per AI user agent, llms.txt, Markdown delivery and the 404 page.

## 6. Accessibility and speed

- Lighthouse targets: accessibility and best practices 100; SEO 100; performance as high as the page allows on a slow mobile connection.
- Do not preload a large web font by default. Measure first: on one site a preload raised mobile largest-contentful-paint from about 1.8 s to 2.7 s. Preload only if the measurement says it helps.
- Stop layout shift when a web font loads: use a fallback `@font-face` from a system font, with `size-adjust` set so its text matches the web font's width.
- Give every image width and height, and useful alt text. Mark decorative images and numbers `aria-hidden`.
- Give each drawing or chart a one-line label.

## 7. Measure again

- Run Lighthouse on the live site, mobile and desktop, two runs each, and keep the median or worst result.
- Run the agent check on the home page, a research page and one article.
- Run the Rich Results Test on the home page and one article.
- Search for the owner's name in a private window once the site is indexed. Note what appears.

## The claude-seo plugin

Install these at project scope, inside the repository, not globally. The owner asked for this approach; keep it.

```text
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo   (choose project scope)
/seo setup
```

Useful commands for a portfolio: `/seo audit`, `/seo page`, `/seo geo`, `/seo schema`, `/seo agentic`, `/seo technical`, `/seo images`, `/seo sitemap`.

Skip the local, maps, ecommerce, programmatic and backlink modules. They do not apply to a personal site.

## Report format

`seo-report.md` at the repository root:

1. A status line and the date.
2. A before and after table of the key numbers.
3. Findings by severity: Critical, High, Medium, Low. Each finding: what is wrong, the evidence, the fix, and how to check it.
4. The changes, grouped by area, with the commit for each.
5. What is still open, and who owns each item (the owner, in a dashboard, or the assistant, in code).
6. What to expect, stated honestly: indexing takes time, and the name search improves only when the site is indexed and the profiles agree.
