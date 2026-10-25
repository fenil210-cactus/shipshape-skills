# build-portfolio-site

Paste the prompt below into your coding assistant in an empty repository. Fill in the braces and
delete any line you don't need.

```text
Build my personal portfolio site in this repository using the build-portfolio-site skill.
If the skill isn't installed, read it from
https://github.com/fenil210-cactus/shipshape-skills/tree/main/skills/build-portfolio-site
and follow it. Read SKILL.md first, and each reference file when its phase starts.

About me: {Name}, {Role} at {Employer}.
Attached: {résumé / CV / research CV / profile screenshots}
Links: {GitHub}, {LinkedIn}, {X}, {Google Scholar}, {other}
My browser is signed in to these. Open them and read everything useful: pinned repos, READMEs,
posts, experience, papers. Write what you find to content/facts.md with a source for each fact.
Don't invent anything; mark missing facts as [NEED: ...] and ask me at the next stop.

Preferences:
- Framework: {framework, or "your choice"}. Use Bun.
- Illustration style: {name or link}
- Sites I like: {links}. Sites I don't want to look like: {links}
- Leave out: {anything I don't want published, such as location, grades, a past role}

Work on your own and stop only at these three points:

1. Theme choice. After the facts, the inspiration research, the mood board and two or three visual
   directions, show me the mood board and the directions with your recommendation. Wait for my pick.

2. Local site ready. Write the copy and build the whole site with Bun, section by section, checking
   each in the browser. Verify the production build at phone and desktop widths in both themes. Then
   give me the local URL, the run commands, screenshots, the open [NEED: ...] questions and what you
   didn't check. Ask me for feedback, which domain I want (suggest a few), whether the repo should be
   public, and whether to start the SEO/GEO phase.

3. SEO/GEO done. After applying my feedback, do the on-site SEO and GEO work on the local build using
   my chosen domain, and show me seo-report.md. Then prepare the Cloudflare config and give me
   numbered steps to: create or sign in to my Cloudflare account, buy the domain through Cloudflare
   Registrar, and import this repo in Workers & Pages. Tell me exactly which details to send back.
   When I reply, connect the domain, set up redirects, security and headers, run the deployment
   checks, and finish the live-site SEO steps.

I'll do every account and payment step myself. Never ask me for passwords, tokens or payment details.

Start now with the facts file.
```

## Coming back in a new session

```text
Continue my portfolio build with the build-portfolio-site skill. Read content/facts.md,
content/feedback.md and seo-report.md (if it exists), and check the git log to see where we stopped.
Tell me which phase we're in, then carry on from there.
```
