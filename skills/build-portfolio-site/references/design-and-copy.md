# Design and copy

## Design direction

Choose the direction before you write any component. Write it down in one short paragraph and show it to the owner.

1. **Collect references first.** Find five to ten sites in the same space (portfolios, research pages, engineering blogs, design studios). For each, note one thing to take and one thing to avoid. Do not copy layouts.
2. **Pick one accent colour.** Use it only for buttons, links and illustration accents. Everything else is text colour and background.
3. **Set the scale.** Use one spacing scale, for example 8, 16, 24, 48, 96 px. Use it for every margin and padding. Reject values outside it unless there is a reason.
4. **Set the type.** One display face for headings and one text face. Use a size-adjusted fallback font so the page does not shift when the web font loads (see [pitfalls.md](pitfalls.md)).
5. **Left-align body text.** Centred paragraphs are harder to read and look generated.
6. **No emoji icons.** Use simple line drawings, a single illustration, or no icon.
7. **No decorative gradients**, glowing blobs or stock imagery. If the owner wants illustration, commission or draw one consistent style.
8. **Dark by default**, with a visible toggle. The Open Graph image and link preview card match the default theme, so a shared link looks like the site.
9. **Restraint.** One clear entry point at the top, one clear next step at the bottom. Not every section needs a heading, a caption and a description.

### Components that earned their place

- **A strong first screen** that says who the person is and what they do, in plain words.
- **A research or publications index** when the owner has papers. Group by year. Each entry links to the publisher's DOI. Add a Cite control with copyable BibTeX when that helps readers. Show citation counts only with their source and date.
- **An article list with reading time** when the owner writes. Reading time is useful for articles, not for every link. Show it only in article lists and on article pages.
- **Article pages** with a contents list that follows the reader's place, numbered figures and code blocks with a copy button, and a footer that offers the next and previous article.
- **A map or a grid** when the content is naturally spatial or periodic (places visited, papers by theme). Make every region or cell an accessible link or labelled item.

### Things to avoid

- Overlays fixed on top of content, including floating chat or assistant bubbles that cover text on hover or while scrolling.
- Auto-playing motion that cannot be paused, and any animation that the reduced-motion setting does not disable.
- Gimmicks that need explanation. If the user needs an instruction to understand an element, redesign it.
- Mixed treatments for the same kind of thing (some regions with solid outlines and others dotted, for example).

## Copy

Write copy after the facts are approved. Draft every block, show the draft, and wait for approval.

- **Headings name the section.** Use "Research", "Projects", "Writing", "Contact", "Travel". Do not use clever headings.
- **The lede is one or two sentences** that say what the person does and where to find the work.
- **The bio answers "who is this?"** in two or three sentences: role, employer, what they work on, and one verifiable fact. No adjectives doing the job of facts.
- **Project entries** give what it is, what the owner worked on, the outcome if confirmed, and the stack. Keep each entry to a few sentences.
- **No sales CTA** ("Hire me", "Let's talk!") unless the owner asks for one. A plain "Contact" section with the email is enough.
- **No secondary labels that repeat the heading.** If the heading says "Research", the first line does not need to say "Research papers and publications".
- **Avoid these phrases**: "passionate about", "journey", "crafting", "cutting-edge", "seamless", "not just X, it's Y", "in today's fast-paced world", and any line that a reader could find on any other site.
- **Articles stay as written.** Publish the owner's text, figures and code unchanged. Only add the structure the site needs: the title, date, reading time, and figure numbers.

### Read-through test

Read each paragraph as someone who has never heard of the owner. Mark any sentence they would skip, and any term they would need to look up. Cut the first and define or replace the second.

## Build and check locally

1. Install and run the site with the project's commands (for example `bun install`, then `bun run dev`).
2. Build the production output (`bun run build`) and serve it the way the host does. Cloudflare's local preview is `bunx wrangler dev`. Test the built site, not only the dev server, because headers and redirects appear only there.
3. Check each page at 375 px and 1440 px width, in both themes:
   - no horizontal scrolling;
   - no console errors;
   - every link resolves;
   - focus is visible when tabbing;
   - text contrast meets 4.5:1 for body text.
4. Run Lighthouse on the built site, mobile and desktop, two runs each, and keep the worst result. Accessibility and best practices should be 100. Investigate any performance drop before accepting it.
5. Take screenshots of the key pages and show them to the owner.
