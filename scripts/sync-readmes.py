#!/usr/bin/env python3
"""Regenerate wiki README mirrors from wiki/index.md.

The wiki index is the source of truth.
The repo root README mirrors it with repo-root links.
The wiki README mirrors it with wiki-local links.
"""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "wiki" / "index.md"
ROOT_README = ROOT / "README.md"
WIKI_README = ROOT / "wiki" / "README.md"


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def rewrite_root_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        if target.startswith(("http://", "https://", "#", "wiki/", "../", "./", "/")):
            return match.group(0)
        return f"[{label}](wiki/{target})"

    return LINK_RE.sub(repl, text)


def write_if_changed(path: pathlib.Path, content: str) -> bool:
    if path.is_symlink():
        path.unlink()
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    index = INDEX.read_text(encoding="utf-8")
    write_if_changed(ROOT_README, rewrite_root_links(index))
    write_if_changed(WIKI_README, index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
