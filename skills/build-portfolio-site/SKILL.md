---
name: build-portfolio-site
description: Plan, design, write, deploy and optimise a personal portfolio website, from the first brief to a live custom domain that search engines and AI answer engines can read. Use when someone wants to build or rebuild a personal portfolio, resume site, research page or articles section; host it on Cloudflare Workers; buy and connect a domain; or improve how the site appears in Google, Bing, and AI answers (SEO, GEO, llms.txt, structured data, agent readiness). Work through the phases in order, and read each reference file when its phase starts.
---

# Build a portfolio site

Build one personal site end to end: brief, design, copy, a local build that is checked in a real browser, deployment to Cloudflare, a custom domain, profiles, and search and AI visibility. Each phase has a reference file. Read it when you reach that phase.

## Phases

1. **Brief and inputs**: [references/brief-and-prompts.md](references/brief-and-prompts.md). Collect the facts before any design or copy.
2. **Design direction**: [references/design-and-copy.md](references/design-and-copy.md). Collect references, choose one accent, set the rules.
3. **Copy**: same file. Draft, show it to the owner, and only then write it into the site.
4. **Build and check locally**: same file, the verification section.
5. **Deploy and domain**: [references/deploy-cloudflare.md](references/deploy-cloudflare.md).
6. **Repository and profiles**: [references/repo-and-profiles.md](references/repo-and-profiles.md).
7. **Search and AI visibility**: [references/seo-geo.md](references/seo-geo.md). Run after the site is live.
8. **When something breaks**: [references/pitfalls.md](references/pitfalls.md).

## Rules for the whole job

- **Facts come from the owner.** Ask for the role, employer, work, projects, links and outcomes before writing copy. Do not invent metrics, papers, links, dates or claims. If a fact is missing, leave a visible placeholder and ask.
- **Show copy before it ships.** Draft the bio, description and headings, get approval, then commit. Owners reject wording that sounds odd or generic, so expect a round of edits.
- **Describe work the owner worked on, not work they own.** Employers own their systems. "I work on the platform" or "I worked on the ranking system" is accurate. "I built" is only accurate for the owner's own projects.
- **Respect removals.** When the owner removes a detail (a location, a grade, a metric), remove it everywhere it appears: the page, the meta description, structured data, the llms.txt summary and the Markdown copies.
- **Owner decisions stay with the owner.** Domain name, repository visibility, what to publish, what to claim, which accounts to link. Recommend, then wait.
- **One change, one reviewable commit**, grouped by area (design, copy, schema, deploy). Do not add AI attribution lines (`Co-Authored-By`, model names) to commits or pull requests unless the owner asks.
- **Verify in a browser before saying it is done.** Check phone and desktop widths, light and dark themes, console errors and horizontal scrolling. Show screenshots, and report what was not checked.
- **Keep it simple.** Use the framework's built-in features before adding a library. A static site is usually enough for a portfolio.
