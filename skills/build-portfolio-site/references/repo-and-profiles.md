# Repository and profiles

## Public or private

- A portfolio is public by nature. Make the repository public unless it holds something you would not publish: private notes, keys, unpublished drafts.
- Never commit secrets (API keys, tokens, `.env` files). Keep them in the hosting platform's settings.
- Use `.gitignore` for build output (`dist/`, `node_modules/`) and local settings files.

## Two GitHub accounts on one machine

If a work account and a personal account both use this computer, pick the account per repository rather than changing the global setting.

1. Create an SSH key for the personal account and add it to that GitHub account.
2. Add a host alias in `~/.ssh/config`, for example `Host github-personal` with the personal key, and point its `HostName` at `github.com`.
3. Set the repository's remote to the alias: `git@github-personal:USERNAME/REPO.git`. Only this repository uses the alias.
4. In that repository only, set the commit identity to the account's GitHub noreply address:
   `git config user.name "Your Name"` and `git config user.email "ID+USERNAME@users.noreply.github.com"`.
5. The GitHub CLI (`gh`) signs in to one account at a time. Use it for the account it is signed in to, and check with `gh auth status` before creating a repository.

Check the result with `git remote -v` and `git log -1 --format='%an <%ae>'`.

## Profiles that point back to the site

Consistency helps search engines and AI tools decide that the profiles belong to one person. Use the same name, the same role line, and the bare domain in each:

- **GitHub:** profile "Website" field.
- **LinkedIn:** the website field under contact info, and a headline that matches the site's role line.
- **Google Scholar:** the homepage field, if the owner has papers.
- **X or other social:** website field in the profile.
- **Any other profile** the owner uses: add the site link if the platform allows it.

Confirm each link opens the site. Confirm the headline matches the site's role line exactly, or decide with the owner which one should change.

## Choosing the domain

- Use the owner's name if it is available. The `.com` version is the default expectation for a personal site.
- Check that the name is not used by another well-known person or product before buying.
- The owner decides. Give two or three options with reasons, and let them choose.
