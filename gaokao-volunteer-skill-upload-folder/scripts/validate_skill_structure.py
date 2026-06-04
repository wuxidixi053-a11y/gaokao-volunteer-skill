from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md not found")

    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter")

    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("front matter block is incomplete")

    frontmatter = match.group(1)
    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"missing {field} in front matter")

    if "gaokao-volunteer-due-diligence" not in frontmatter:
        fail("unexpected skill name")

    if len(text.splitlines()) < 20:
        fail("SKILL.md looks too short")

    print("OK: skill structure is valid")


if __name__ == "__main__":
    main()

