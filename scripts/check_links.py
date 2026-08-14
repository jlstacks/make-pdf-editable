"""Fail when a repository Markdown link points to a missing local file."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []

    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue

            path_text = target.split("#", 1)[0]
            resolved = (markdown.parent / path_text).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")

    if failures:
        print("Broken local Markdown links:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("All local Markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
