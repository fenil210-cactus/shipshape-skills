# Pitfalls

Read this when something breaks. Each item is a problem that came up on a real portfolio build, with what fixed it.

## Layout

- **A sticky element inside a grid item stops at the grid container, not the grid cell.** A table of contents that should follow the reader can stop early or overlap the footer. Fix it by putting the sticky element inside a wrapper that stretches the full height of the grid cell (`align-self: stretch`), and making the inner element sticky.
- **Long URLs overflow on phones.** Give text containers `overflow-wrap: anywhere` (or `break-word`).
- **A class name clashes with a library.** A `.year` class collided with a chart's axis styles. Prefix section classes with the page name (`.paper-year`).
- **Badges or counts make a line taller.** Position them absolutely or with `position: relative; top: ...` instead of changing the line box.

## Fonts and loading

- **A web font swap shifts the text.** The system fallback is narrower or wider, the paragraphs rewrap, and the page jumps (layout shift 0.1 or more on an article). Fix with a `@font-face` for a local system font, using `size-adjust` (and optionally `ascent-override`) so the widths match. Measure the widths on real body text before you pick a value.
- **Preloading a large font made mobile loading slower.** The font competed with the page on a slow connection. Measure with and without the preload, several runs each, and ship the faster one.
- **Scripts inlined by the bundler break the Content Security Policy.** Set the bundler to keep scripts as files (for Astro, `vite.build.assetsInlineLimit: 0`), so the policy needs only one hash for the one inline script that must stay inline.
- **A CSP hash is wrong after a script edit.** Any change to an inline script changes its hash. Read the new hash from the browser's CSP report or compute it with `sha256` over the exact script text, and update `_headers`.

## Testing

- **Playwright needs Chrome.** If the bundled Chromium is missing, launch with `channel: "chrome"` and the installed browser.
- **An iframe test harness fails under `X-Frame-Options: DENY`.** That header is intentional. Test the page directly in the browser instead of inside an iframe.
- **Screenshots at one width miss bugs.** Check 375 px and 1440 px, light and dark, every time.
- **Console errors appear only on the built site.** Test `bun run build` output, not only the dev server, before you call it done.

## Video and previews

- **iPhone and some link previews need byte-range requests for video.** A static file host always sends the whole file, so the video does not play in the preview. Add a small Worker that answers `Range` requests from the asset binding, and route only that file through it (`run_worker_first`). Keep a static image as the fallback preview.
- **The Open Graph image must match the theme.** If the site defaults to dark, make the preview card dark too.

## Deployment

- **The first build fails with a missing output folder.** The build command did not run or failed. Read the build log, then check that `dist/` appears locally after `bun run build`.
- **The deploy succeeds but the domain shows an old page.** Check the custom domain points at the Worker, then do a hard refresh. Check the cache headers for HTML files are not set to a long cache.
- **Redirect loops after turning on Always Use HTTPS.** Check there is no other redirect rule forcing `http://`, and that the Worker or host is not redirecting too.

## Copy and content

- **Generic AI phrasing gets rejected.** Lines like "passionate about", "journey", "not just X, it's Y" and "cutting-edge" make owners reject the whole section. Rewrite them in plain nouns and verbs.
- **Unverified claims get removed.** Do not state numbers, outcomes, awards or affiliations the owner has not confirmed. Use placeholders until they are.
- **Removed details come back.** A location or grade removed from the bio often remains in the meta description, structured data or llms.txt. Search the whole repository for the removed term before pushing.
- **Editing someone's articles.** Do not add headings or paragraphs to their articles. Publish the text as written.
