# Shipshape Skills

Practical, self-contained skills for coding assistants that support `SKILL.md` packages. The instructions are assistant-neutral. Each skill lives in its own directory, so this repository can grow without coupling unrelated workflows.

## Skills

| Skill | Use it for | Files |
| --- | --- | --- |
| [writing-good-tests](skills/writing-good-tests/SKILL.md) | Writing a small set of behavior-focused tests with meaningful regression protection | `SKILL.md`, `references/examples.md` |
| [test-audit](skills/test-audit/SKILL.md) | Reviewing existing tests and removing weak or duplicate coverage without losing contracts | `SKILL.md`, `CAMPAIGN.md` |

The two skills complement each other: `writing-good-tests` guides test creation; `test-audit` provides a more detailed audit and cleanup workflow.

`test-audit` is adapted from [OpenClaw's test-audit skill](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit). Its original MIT copyright and permission notice is preserved in [`skills/test-audit/LICENSE`](skills/test-audit/LICENSE).

## Install in a coding assistant

Clone the repository and copy the skill directories into your assistant's personal skills folder:

| Assistant | Personal skills folder |
| --- | --- |
| [Codex](https://developers.openai.com/blog/eval-skills) | `~/.codex/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` |

```sh
git clone https://github.com/fenil210-cactus/shipshape-skills.git
skills_destination="$HOME/.codex/skills" # use "$HOME/.claude/skills" for Claude Code
mkdir -p "$skills_destination"
cp -R shipshape-skills/skills/* "$skills_destination/"
```

For another coding assistant, use its documented skill directory if it supports `SKILL.md` packages. Start a new session after installing so the assistant discovers them. To update an installed skill, replace its directory with the latest version from this repository. Review a skill's instructions before using it in a project.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md` with YAML frontmatter containing a unique `name` and a clear `description` of when to use it. Match the directory and frontmatter names.
2. Put optional guides and examples inside the same directory. Link to them with relative paths from `SKILL.md`.
3. Keep the skill usable across repositories and coding assistants: remove hardcoded local paths, unavailable sibling skill calls, assistant-specific commands, and secrets.
4. Add one row to the table above. Verify every relative link and try the skill on a representative task before publishing.

Run `python3 scripts/check_skills.py` before pushing. CI runs the same check for every push and pull request.

```text
skills/
  <skill-name>/
    SKILL.md
    references/       # optional supporting material
```

Skill instructions should be concise at the entry point and keep deeper examples in supporting files. A new skill needs a distinct job; extend an existing skill when its workflow already fits.

## License

This repository is available under the [MIT License](LICENSE). The adapted `test-audit` skill also retains its [OpenClaw MIT notice](skills/test-audit/LICENSE).
