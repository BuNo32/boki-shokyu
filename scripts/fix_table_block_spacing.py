#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_table_block_spacing.py
--------------------------
Ensure Markdown table blocks are separated by a blank line from the previous
paragraph/list text so that Python-Markdown (and mkdocs-material) recognizes
them as tables.

Heuristic:
- Outside code fences, if there are 2 or more consecutive lines whose first
  non-space character is a pipe ('|'), treat them as a table block.
- If the line immediately before that block is non-blank, insert a blank line.

Notes:
- Keeps existing indentation of table lines unchanged.
- Does NOT attempt to change list indentation or blockquotes; inserting a
  true blank line is generally sufficient for Markdown parsers.

Usage:
  python scripts/fix_table_block_spacing.py --root .
"""
from __future__ import annotations
import argparse, pathlib, re

FENCE_RE = re.compile(r"^\s*(```|~~~)")

def is_pipe_line(s: str) -> bool:
    return s.lstrip().startswith("|")

def ensure_table_spacing(text: str) -> tuple[str, bool]:
    lines = text.splitlines()
    n = len(lines)
    changed = False
    out: list[str] = []
    in_code = False
    i = 0
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            in_code = not in_code
            out.append(line)
            i += 1
            continue

        if not in_code and is_pipe_line(line):
            # Count consecutive pipe-start lines
            j = i
            cnt = 0
            while j < n and lines[j].strip() != "" and is_pipe_line(lines[j]):
                cnt += 1
                j += 1
            if cnt >= 2:
                # Need a blank line before if previous line exists and is non-blank
                if len(out) > 0 and out[-1].strip() != "":
                    out.append("")
                    changed = True
                # Emit the block as-is
                while i < j:
                    out.append(lines[i])
                    i += 1
                continue

        # Default: passthrough
        out.append(line)
        i += 1

    if changed:
        return "\n".join(out) + "\n", True
    return text, False

def process_file(path: pathlib.Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new, changed = ensure_table_spacing(text)
    if changed:
        path.write_text(new, encoding="utf-8")
    return changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--targets", nargs="*")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    if args.targets:
        files = [root / t for t in args.targets]
    else:
        files = list(root.glob("content/**/*.md"))

    any_changed = False
    for p in files:
        if not p.exists():
            continue
        if process_file(p):
            print(f"[CHANGED] {p.relative_to(root)}")
            any_changed = True
    if not any_changed:
        print("No spacing fixes applied.")

if __name__ == "__main__":
    main()

