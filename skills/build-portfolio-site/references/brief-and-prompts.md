# Brief and inputs

Gather these before any design work. Put them in one file in the repository (for example `content/facts.md`), so every later step reads from the same source and nothing is guessed.

## Input checklist

- **Name** as it should appear, and the name people search for.
- **Role and employer**, in the owner's own words. Confirm the exact job title.
- **What the owner works on**: two or three areas, described as the owner describes them.
- **Two or three projects**: what it is, what the owner worked on, the outcome, and the stack. Ask for a verifiable outcome (users, requests per day, a paper, a published product). Do not write an outcome the owner has not confirmed.
- **Profiles**: GitHub, LinkedIn, X or other social, Google Scholar if there are papers, and any others. Ask for each URL and check it opens.
- **Résumé or CV PDF**, if one exists. Use it as the source for dates, roles and education. Ask before publishing education details the owner has not chosen to show.
- **Research**, if relevant: each paper with its authors, venue, year and DOI. Take the details from the owner's CV or the publisher's page, not from memory.
- **Articles or writing**: the links and the owner's own text. Publish the owner's text as written. Do not add headings, paragraphs or claims.
- **Optional sections**: travel, photography, talks, hobbies. Ask whether they should be on the site at all.
- **Domain preference**, if any, and whether the repository should be public.

## Kickoff prompt (adapt the placeholders)

Paste this to start. Replace the braces with the owner's facts. Keep the design and restraint rules: they stop the generic result.

```text
I need a personal portfolio site for {Name}, {Role} at {Employer}. They work on {areas}.
Links: {GitHub}, {LinkedIn}, {X}, {Scholar}. My CV is attached.

Build it in this repository with {framework and package manager}. Do not ask me for clarification
unless a fact is missing; then leave a visible placeholder and list what you need.

Design:
- Look designed, not generated. No decorative gradients.
- One accent colour, used only for buttons, links and illustration accents.
- Left-align body text. One spacing scale: 8, 16, 24, 48, 96 px.
- No emoji icons.
- Not so busy that it pulls the eye in five directions, and not so bare it looks sad.
- Find and write down at least five reference sites in this space before you design anything.
- Dark mode by default, with a toggle. The link preview card matches the default theme.

Copy:
- Say what the work is, plainly. No selling, no cute lines, no "not X, it's Y" constructions.
- Write the bio so it answers "who is this person and what do they do" in two or three sentences.
- Draft all copy first and show it to me before you write it into the site.

Work in phases. Show me the design direction and the draft copy before building the full site.
```

## SEO and GEO kickoff prompt (run after the site is live)

```text
You are working in {repository}, the live site {url}.

Goal: the site ranks for {Name} and for the roles I want to be found for, is cited correctly by AI
answer engines when someone asks who {Name} is, and is technically sound (fast, crawlable,
accessible, with correct structured data).

Install only these, at project scope (never global):
- seo-audit, ai-seo and copywriting from https://github.com/coreyhaines31/marketingskills
- The claude-seo plugin from https://github.com/AgriciDaniel/claude-seo (project scope)
Do not install anything else without asking me. Skip Next.js-specific skills unless this repo uses Next.js.

Work plan, one pass per step, and show me findings before you edit code:
1. Audit with seo-audit and /seo audit {url}. List findings as Critical, High, Medium, Low.
2. Technical: unique titles and descriptions per page, canonical URLs, sitemap.xml, robots.txt,
   Open Graph and Twitter cards with an image, favicon, Core Web Vitals, image alt text, heading order.
3. Structured data: Person, WebSite, ProfilePage and project or paper schema. Every name and headline in
   the markup must appear on the visible page.
4. GEO: a quotable bio near the top, llms.txt, Markdown copies of key pages, robots.txt rules for
   reputable AI crawlers, /seo agentic for agent readiness.
5. Copy: tighten the hero, the about text and the project write-ups with the copywriting skill. Ask me
   before rewriting any personal copy or making any claim about me.
6. Other checks: accessibility, the 404 page, HTTPS and www redirects, internal links, content that
   renders without JavaScript.

Output: seo-report.md at the repository root (findings, changes, what is left), commits grouped by area,
and for each change why it matters and how to verify it.
```

## Feedback that shaped the best results

Owners give the most useful feedback on copy and layout. Collect it in the repository, and reuse it on the next site:

- Write from the reader's side: "Would a stranger know what this means?" Rewrite any line that needs insider knowledge.
- Replace jargon phrases with plain nouns. Replace the word "discipline" with the specific skill.
- Remove sections that explain the layout. "Let the layout do the explaining."
- Persistent overlays that block links or text are a defect, not a feature. Put ambient features in the page flow.
- Use the owner's own categories for lists (for example the order of places visited, or the list of states to mark on a map). Ask for the list rather than guessing it.
