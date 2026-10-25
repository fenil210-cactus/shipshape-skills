# Brief and inputs

Read this at the start of every portfolio build. It covers which facts to collect, the run order and
its three checkpoints, the rules for this build, and the feedback from earlier builds.

## 1. Collect the facts first

Put every fact in one file in the repository, `content/facts.md`, so every later step reads from the
same source and nothing is guessed. Next to each fact, note where it came from (CV page, LinkedIn,
GitHub repo, Scholar, or "owner said").

Gather the facts yourself before asking. Read every source the owner gave you: attached résumé, CV,
research CV, screenshots, and every profile link. The owner's browser is usually signed in, so open
the links and read them directly: pinned repositories and READMEs, recent posts, the LinkedIn
experience section, the Scholar publication list. Ask only for what the sources do not answer.

### Input checklist

- **Name** as it should appear, and the name people search for.
- **Role and employer**, in the owner's own words. Confirm the exact job title.
- **What the owner works on**: two or three areas, described as the owner describes them.
- **Two or three projects**: what it is, what the owner worked on, the outcome, and the stack. Ask
  for a verifiable outcome (users, requests per day, a paper, a published product). Do not write an
  outcome the owner has not confirmed.
- **Profiles**: GitHub, LinkedIn, X or other social, Google Scholar if there are papers, and any
  others. Check that each URL opens.
- **Résumé or CV PDF**, if one exists. Use it as the source for dates, roles and education. Ask
  before publishing education details the owner has not chosen to show.
- **Research**, if relevant: each paper with its authors, venue, year and DOI. Take the details from
  the owner's CV or the publisher's page, not from memory.
- **Articles or writing**: the links and the owner's own text. Publish the owner's text as written.
  Do not add headings, paragraphs or claims.
- **Optional sections**: travel, photography, talks, hobbies. If the sources do not make it clear,
  leave them out and ask at checkpoint 2.
- **Domain preference** and whether the repository should be public. Ask at checkpoint 2.

When a fact is missing, write a visible placeholder (`[NEED: exact job title]`) in `facts.md` and on
the page, and add it to one list of questions. Do not stop for a missing fact; keep building and ask
at the next checkpoint.

## 2. Run order and checkpoints

There are three checkpoints. Between them, work without asking for clarification: interpret the
brief, make reasonable choices, and note them for the owner.

### Phase A: facts and direction

1. **Facts.** Write `content/facts.md` and the list of open questions.
2. **Inspiration.** Before designing anything, find eight to ten reference sites in this space:
   engineer and researcher portfolios, design studios, engineering blogs. For each, note one thing to
   take and one thing to avoid. Do not copy layouts.
3. **Mood board.** Collect the references into one local HTML page (`moodboard/index.html`):
   screenshots or links, type pairings, a palette with one accent, the illustration style, and any
   motion examples.
4. **Directions.** Propose two or three visual directions. For each, write one short paragraph naming
   the feel, the two typefaces, the accent colour, and the one idea that makes it different from other
   portfolios. Recommend one.

**Checkpoint 1: show the mood board and the directions. Wait for the owner to pick one** (or combine
them). This is the only design approval. Do not ask for approval again until the site is built.

### Phase B: build the whole site

5. **Set up** the project with Bun (`bun init` or the framework's Bun template). Use the framework the
   owner named; if none, choose a simple static setup and say why. Put every value that depends on
   the domain (site URL, canonical base) in one config constant, so the domain can be set later in
   one place.
6. **Write the copy** from `facts.md`, following design-and-copy.md. Do not stop for approval; the
   owner reviews it on the local site.
7. **Build section by section** in one go: the hero first, then each section in order, then the 404
   page, the theme toggle and the link-preview image. Finish and check each section in the browser
   before starting the next. Do not generate the whole site in one pass.
8. **Verify** with "Build and check locally" in design-and-copy.md, on the production build and not
   only the dev server. Fix what you find before handing over.

**Checkpoint 2: hand over the local site.** Give the owner:
- the local URL and the command to run it (`bun run dev`, and the production preview command);
- screenshots at 375 px and 1440 px, in both themes;
- a short note on the direction you built and any choices you made on their behalf;
- the list of `[NEED: ...]` placeholders and open questions;
- what was not checked.

Then ask:
- What should change? (Apply all feedback before moving on, and record it in `content/feedback.md`.)
- Which domain do you want? Suggest two or three available options, but the owner chooses.
- Should the repository be public?
- Start the SEO and GEO phase now?

### Phase C: search and AI visibility, on-site

9. Once the owner says to go ahead, read seo-geo.md and do everything that can be done in code before
   the site is live. Use the chosen domain in the config constant.

Install only these, at project scope (never global):
- seo-audit, ai-seo and copywriting from https://github.com/coreyhaines31/marketingskills
- the claude-seo plugin from https://github.com/AgriciDaniel/claude-seo

Do not install anything else without asking. Skip Next.js-specific skills unless the repository uses
Next.js.

Work in this order. Run the audit on the local production preview (or a Cloudflare preview URL):

1. **Audit** with seo-audit and `/seo audit {preview url}`. Record the baseline (seo-geo.md section 1)
   and list findings as Critical, High, Medium, Low.
2. **Technical**: unique titles and descriptions per page, canonical URLs on the chosen domain,
   sitemap.xml, robots.txt, Open Graph and Twitter cards with an image, favicon, image alt text,
   heading order, Core Web Vitals.
3. **Structured data**: Person, WebSite, ProfilePage, and project or paper schema (seo-geo.md section
   4). Every name and headline in the markup must appear on the visible page.
4. **GEO**: a quotable bio near the top, llms.txt, llms-full.txt, Markdown copies of key pages,
   robots.txt rules for reputable AI crawlers, and `/seo agentic` for agent readiness.
5. **Copy**: tighten the hero, about text and project write-ups with the copywriting skill. Ask the
   owner before rewriting any personal copy or making any claim about them.
6. **Other checks**: accessibility, the 404 page, internal links, content that renders without
   JavaScript.

Commit by area. For each change, note why it matters and how to verify it in `seo-report.md`.

**Checkpoint 3: show `seo-report.md`** (the findings, what changed, what is left). Then go straight
into hosting.

### Phase D: hosting and domain

10. Read deploy-cloudflare.md. Prepare everything in the repository first: `wrangler.jsonc`,
    `public/_headers`, and the 404 handling. Run `bunx wrangler dev` on the production build.
11. **Give the owner the steps they must do themselves**, as one numbered list:
    - create or sign in to a Cloudflare account;
    - buy the chosen domain through Cloudflare Registrar (Domain Registration → Register Domains),
      or point the nameservers of an existing domain at Cloudflare;
    - in Workers & Pages, import the GitHub repository, authorising the Cloudflare app for this one
      repository only, with the build settings from deploy-cloudflare.md section 2.
12. **Ask the owner to reply with**:
    - the domain they bought, and confirmation that it shows as active in Cloudflare;
    - the Worker name and the `*.workers.dev` URL from the first deploy;
    - any build error, pasted in full, if the first deploy failed.
    Never ask for passwords, API tokens or payment details. Wait for the reply.
13. With those details, walk the owner through adding the custom domain, then the security and
    redirect settings, analytics and headers (deploy-cloudflare.md sections 3 to 6). Make the matching
    code changes and push them. Run the deployment checks in section 7, and report each result.

### Phase E: after it is live

14. Do seo-geo.md sections 2 and 7: Google Search Console and Bing Webmaster Tools (give the owner the
    steps, since they own the accounts), then Lighthouse, the agent check and the Rich Results Test on
    the live site. Update `seo-report.md` with the before and after numbers.
15. Read repo-and-profiles.md and update the repository and the owner's profiles.

## 3. Rules for this build

These apply on top of design-and-copy.md. They are what keeps the result from looking generic.

Design:
- Look designed, not generated. No decorative gradients, glowing blobs or stock imagery.
- One accent colour, used only for buttons, links and illustration accents.
- Left-align body text. One spacing scale: 8, 16, 24, 48, 96 px.
- No emoji icons. Use simple line drawings or one consistent illustration style; if the owner names
  an illustration source, use it.
- Not so busy that it pulls the eye in five directions, and not so bare it looks sad.
- Dark mode by default, with a visible toggle. The link preview card matches the default theme.
- If the owner asks for ambitious visuals (custom renderers, shaders, motion), each effect must earn
  its place: it respects reduced motion, can be paused if it loops, does not cover content, and does
  not noticeably hurt performance.

Copy:
- Say what the work is, plainly. No selling, no cute lines, no "not X, it's Y" constructions.
- The bio answers "who is this person and what do they do" in two or three sentences.

## 4. Feedback that shaped the best results

Record every piece of owner feedback in `content/feedback.md` as you get it, apply it everywhere it is
relevant, and check new copy against it. Feedback from earlier builds:

- Write from the reader's side: "Would a stranger know what this means?" Rewrite any line that needs
  insider knowledge.
- Replace jargon phrases with plain nouns. Replace the word "discipline" with the specific skill.
- Remove sections that explain the layout. "Let the layout do the explaining."
- Persistent overlays that block links or text are a defect, not a feature. Put ambient features in
  the page flow.
- Use the owner's own categories for lists (for example the order of places visited, or the list of
  states to mark on a map). Ask for the list rather than guessing it.
