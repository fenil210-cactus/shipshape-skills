Start with this prompt:

You're building my personal portfolio site, starting from an empty repository. It should look like a design studio made it: original, restrained and well made. It should not look like a template or typical AI output.

Before you start, read the build-portfolio-site skill: https://github.com/fenil210-cactus/shipshape-skills/tree/main/skills/build-portfolio-site
Read SKILL.md now. Read each file in references/ when you reach its phase:
- brief-and-prompts.md: facts and inputs
- design-and-copy.md: design direction, copy, local checks
- pitfalls.md: whenever something breaks
- deploy-cloudflare.md, repo-and-profiles.md, seo-geo.md: later, not in this session

## Who I am
Don't wait for me to describe myself. Gather the facts from these sources:
- Attached files: {résumé / CV / research CV / profile screenshots}
- Links: {GitHub}, {LinkedIn}, {X}, {Google Scholar}, {other}
- My browser is signed in to all of these, so open them and look around: pinned repos, READMEs, posts, papers.

Write everything you find to content/facts.md: role, employer, what I work on, projects, papers, dates and links. Each fact gets its source next to it. This file is the only source for copy. Don't invent metrics, dates, papers or claims. When a fact is missing, put a visible placeholder like [NEED: ...] and add it to a list of questions for me.

When describing work done at my employer, say "worked on". Use "built" only for my own projects.

## How to work
Work in this order. Stop at each checkpoint and show me what you have before going on.

1. Inspiration. Find 8–10 strong reference sites: engineer and researcher portfolios, design studios, engineering blogs. For each one, note one thing to take and one thing to avoid. Don't copy any layout.

2. Mood board. Turn the references into one page (references/moodboard.md or a simple local HTML page). Include screenshots or links, type pairings, a colour palette with one accent, illustration style and motion examples.

3. Visual direction. Write one short paragraph that names the feel, the typefaces, the accent colour and the single idea that makes this site different from other portfolios. If you have two directions in mind, show me both.
CHECKPOINT: show me the mood board and the direction. Wait for my pick.

4. Copy. Draft every piece of text: hero line, bio, section headings, project entries, contact.
CHECKPOINT: show me the draft. Wait for my approval or edits.

5. Build one section at a time. Don't generate the whole site in one go. Start with the hero. Build it, check it in the browser and show me screenshots.
CHECKPOINT after the hero. Once I approve it, build the remaining sections one by one in the same way. Show me each one, but you don't need to wait for approval unless something is a real judgment call.

6. Check everything in the browser before calling it done. Test at 375 px and 1440 px, in light and dark themes. Look for console errors and horizontal scrolling, make sure every link works, keyboard focus is visible, and body text contrast is at least 4.5:1. Run Lighthouse on the production build. Show me screenshots and tell me what you didn't check.

## Design rules
- No decorative gradients, glowing blobs or stock photos.
- Exactly one accent colour, used only for buttons, links and illustration accents.
- Left-aligned body text.
- One spacing scale: 8 / 16 / 24 / 48 / 96 px. Nothing outside it without a reason.
- One display typeface and one text typeface, with a size-adjusted fallback so the layout doesn't shift when fonts load.
- No emoji icons. Use simple line drawings, or one consistent illustration style like {illustration reference}.
- Dark mode by default, with a visible toggle. The link-preview image matches the default theme.
- Balance: not so busy that the eye gets pulled five ways, not so bare that it feels empty. One clear entry point at the top and one clear next step at the bottom.
- Ambition is welcome: custom assets, shaders, canvas renderers, any framework. But every effect has to earn its place. Turn it off when reduced motion is on, make it pausable if it loops, and keep the page fast. Nothing fixed on top of content.

## Copy rules
- Plain words. This is an introduction to who I am and what I work on, not a sales page.
- The bio answers "who is this person and what do they do" in two or three sentences, including one fact that can be checked.
- Headings just name the section: Projects, Research, Writing, Contact.
- No "passionate about", "journey", "crafting", "cutting-edge", "seamless", "not just X, it's Y", or any line that could appear on anyone's site.
- No "Hire me" button. A plain Contact section is enough.

## Tech
- Use Bun as the package manager and runtime. Pick the framework yourself; a static site is usually enough.
- One reviewable commit per change, grouped by area. No AI attribution lines in commits.

## Not in this session
Deploying, the custom domain, SEO/GEO and profile updates come after I'm happy with the site. We'll do them later using the deploy-cloudflare.md, repo-and-profiles.md and seo-geo.md references.

Start with step 1.
