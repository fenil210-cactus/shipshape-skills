---
name: build-portfolio-site
description: Plan, design, write, deploy and optimise a personal portfolio website, from the first brief to a live custom domain that search engines and AI answer engines can read. Use when someone wants to build or rebuild a personal portfolio, resume site, research page or articles section; host it on Cloudflare Workers; buy and connect a domain; or improve how the site appears in Google, Bing, and AI answers (SEO, GEO, llms.txt, structured data, agent readiness). Work through the phases in order, and read each reference file when its phase starts.
---

# Build a portfolio site

Build one personal site end to end: facts, design direction, a complete local build checked in a real
browser, search and AI visibility, deployment to Cloudflare, a custom domain, and profiles. Each phase
has a reference file. Read it when you reach that phase. The run order and checkpoints are in
[references/brief-and-prompts.md](references/brief-and-prompts.md), section 2.

## Phases

1. **Facts**: [references/brief-and-prompts.md](references/brief-and-prompts.md). Read every source
   the owner gave you and write `content/facts.md` before any design or copy.
2. **Design direction**: [references/design-and-copy.md](references/design-and-copy.md). Inspiration,
   mood board, two or three directions.
   **Checkpoint 1: the owner picks a direction.**
3. **Copy and full build**: same file. Write the copy and build the whole site with Bun, section by
   section, without stopping. Verify it in a browser.
   **Checkpoint 2: hand over the local URL and screenshots. Ask for feedback, the domain name, and
   whether to start the SEO/GEO phase.**
4. **Search and AI visibility (on-site)**: [references/seo-geo.md](references/seo-geo.md). Everything
   that can be done in code before the site is live, using the domain the owner chose.
   **Checkpoint 3: show `seo-report.md`, then start hosting.**
5. **Deploy and domain**: [references/deploy-cloudflare.md](references/deploy-cloudflare.md). Give the
   owner the account and domain purchase steps, wait for their details, then connect and harden.
6. **Search and AI visibility (live)**: seo-geo.md, sections 2 and 7. Search Console, Bing, and
   measuring again on the live site.
7. **Repository and profiles**: [references/repo-and-profiles.md](references/repo-and-profiles.md).
8. **When something breaks**: [references/pitfalls.md](references/pitfalls.md), in any phase.

## Rules for the whole job

- **Facts come from the sources and the owner.** Read the CV, profiles and links first. Do not invent
  metrics, papers, links, dates or claims. If a fact is missing, leave a visible `[NEED: ...]`
  placeholder and ask at the next checkpoint.
- **Copy is reviewed on the local site.** The owner sees all copy at checkpoint 2, before anything is
  deployed. Owners reject wording that sounds odd or generic, so expect a round of edits.
- **Describe work the owner worked on, not work they own.** Employers own their systems. "I work on
  the platform" or "I worked on the ranking system" is accurate. "I built" is only accurate for the
  owner's own projects.
- **Respect removals.** When the owner removes a detail (a location, a grade, a metric), remove it
  everywhere it appears: the page, the meta description, structured data, the llms.txt summary and
  the Markdown copies.
- **Owner decisions stay with the owner.** Domain name, buying anything, repository visibility, what
  to publish, what to claim, which accounts to link. Recommend, then wait. Never make purchases or
  enter payment details yourself.
- **One change, one reviewable commit**, grouped by area (design, copy, schema, deploy). Do not add AI
  attribution lines (`Co-Authored-By`, model names) to commits or pull requests unless the owner asks.
- **Verify in a browser before saying it is done.** Check phone and desktop widths, light and dark
  themes, console errors and horizontal scrolling. Show screenshots, and report what was not checked.
- **Keep it simple.** Use the framework's built-in features before adding a library. A static site is
  usually enough for a portfolio.
