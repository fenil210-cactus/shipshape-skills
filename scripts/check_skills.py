"""Validate the minimal, portable layout expected of each skill package."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def check_skill(directory: Path) -> list[str]:
    errors: list[str] = []
    entry = directory / "SKILL.md"
    if not entry.is_file():
        return [f"{directory.name}: missing SKILL.md"]

    text = entry.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        errors.append(f"{entry}: missing YAML frontmatter")
    else:
        frontmatter = parts[1]
        name = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
        description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        if not name or name.group(1).strip().strip('"\'') != directory.name:
            errors.append(f"{entry}: name must match directory {directory.name!r}")
        if not description or not description.group(1).strip().strip('"\''):
            errors.append(f"{entry}: description is required")

    for markdown in directory.rglob("*.md"):
        for target in LINK.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            local_path = target.split("#", 1)[0]
            if local_path and not (markdown.parent / local_path).exists():
                errors.append(f"{markdown}: broken link {target!r}")
    return errors


def main() -> int:
    directories = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    errors = [error for directory in directories for error in check_skill(directory)]
    if not directories:
        errors.append("skills/: no skill directories found")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(directories)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
