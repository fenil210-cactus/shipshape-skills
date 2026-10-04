# Shipshape Skills

Practical, self-contained skills for coding assistants that support `SKILL.md` packages. The instructions are assistant-neutral. Each skill lives in its own directory, so this repository can grow without coupling unrelated workflows.

## Skills

| Skill | Use it for | Files |
| --- | --- | --- |
| [writing-good-tests](skills/writing-good-tests/SKILL.md) | Writing a small set of behavior-focused tests with meaningful regression protection | `SKILL.md`, `references/examples.md` |
| [test-audit](skills/test-audit/SKILL.md) | Reviewing existing tests and removing weak or duplicate coverage without losing contracts | `SKILL.md`, `CAMPAIGN.md` |

The two skills complement each other: `writing-good-tests` guides test creation; `test-audit` provides a more detailed audit and cleanup workflow.

`test-audit` is adapted from [OpenClaw's test-audit skill](https://github.com/openclaw/openclaw/tree/main/.agents/skills/test-audit). Its original MIT copyright and permission notice is preserved in [`skills/test-audit/LICENSE`](skills/test-audit/LICENSE).

## Install the skills

You can ask a coding assistant to install them, or use the commands below. The prompts name the [complete skill folders](https://github.com/fenil210-cactus/shipshape-skills/tree/main/skills), including their supporting files.

| Assistant | Personal/global location | Repository location |
| --- | --- | --- |
| [Codex](https://developers.openai.com/blog/eval-skills) | `~/.codex/skills/` | `.codex/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` |

For another assistant that supports `SKILL.md`, use its documented skills location. To run the manual commands, clone this repository and enter it first:

```sh
git clone https://github.com/fenil210-cactus/shipshape-skills.git
cd shipshape-skills
```

### Install globally

Paste this prompt into your coding assistant:

```text
Install writing-good-tests and test-audit from https://github.com/fenil210-cactus/shipshape-skills/tree/main/skills into my personal/global skills directory for this coding assistant. Copy each complete skill folder, including its supporting files. Do not change the current repository. Tell me the installed paths when done.
```

Or run from the clone:

```sh
skills_destination="$HOME/.codex/skills" # use "$HOME/.claude/skills" for Claude Code
mkdir -p "$skills_destination"
cp -Rn skills/writing-good-tests skills/test-audit "$skills_destination/"
```

### Install in a repository

Paste this prompt while working in the repository where you want the skills:

```text
Install writing-good-tests and test-audit from https://github.com/fenil210-cactus/shipshape-skills/tree/main/skills into this repository's project-scoped skills directory for the coding assistant I am using. Copy each complete skill folder, including its supporting files. Do not install them globally or overwrite existing skills. Tell me the installed paths when done.
```

Or run from the clone, naming the target repository:

```sh
project_dir="/absolute/path/to/your/repository"
skills_destination="$project_dir/.codex/skills" # use "$project_dir/.claude/skills" for Claude Code
mkdir -p "$skills_destination"
cp -Rn skills/writing-good-tests skills/test-audit "$skills_destination/"
```

To install one skill, name only its link in the prompt or copy only its folder in the command. Start a new assistant session after installation so it discovers the skills.

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
