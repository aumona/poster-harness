#!/usr/bin/env python3
"""Create an independent poster project using only the reusable template files."""
import argparse
from pathlib import Path
import shutil
import sys

TEMPLATE = Path(__file__).resolve().parent.parent
FILES = (
    "AGENTS.md", "README.md", "brief.md", "main.tex", "content.tex",
    "poster-style.sty", "Makefile", ".gitignore",
    "assets", "scripts",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="new folder; must not exist")
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()
    if destination == TEMPLATE or TEMPLATE in destination.parents:
        parser.error("Choose a destination outside the template folder.")
    if destination.exists():
        parser.error(f"Destination already exists: {destination}")
    for name in FILES:
        if not (TEMPLATE / name).exists():
            parser.error(f"Template file is missing: {name}")
    try:
        destination.mkdir(parents=True, exist_ok=False)
    except OSError as error:
        parser.error(str(error))
    try:
        for name in FILES:
            source = TEMPLATE / name
            target = destination / name
            if source.is_dir():
                shutil.copytree(source, target, ignore=shutil.ignore_patterns(
                    "__pycache__", "*.pyc", ".DS_Store"))
            else:
                shutil.copy2(source, target)
    except OSError as error:
        print(f"Copy failed; incomplete project at {destination}: {error}", file=sys.stderr)
        return 1
    print(f"Created poster: {destination}")
    print("Open that folder in Codex and ask it to read AGENTS.md and help fill brief.md.")
    print("Build there with: make check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
