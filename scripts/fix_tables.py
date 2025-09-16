\
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_tables.py
-------------
Detect and fix "inline" 4-column journal tables that were written on a single line like:
  "例：... | 借方科目 | 金額 | 貸方科目 | 金額 | |---|---:|---|---:| | 普通預金 | 49,670 | 売掛金 | 49,670 | | 支払手数料 | 330 | 売掛金 | 330 |"
and convert them into proper Markdown tables with newlines.
Also inserts a blank line before each table header and preserves preceding captions (e.g., "4列（2行）"や"例1：...").

Usage:
  python scripts/fix_tables.py --root <repo-root> [--dry-run]

It will operate on the following default targets (relative to --root):
  content/ch05/01-fees-and-interest.md
  content/ch05/02-transfers-advanced.md
  content/ch05/03-cash-over-short.md
  content/ch06/03-returns-and-allowances.md
  content/ch07/02-advance-and-unsettled.md
  content/ch07/03-employee-and-temp.md
  content/ch08/02-notes-transactions.md
  content/ch08/03-densai.md
  content/ch09/02-daily-transactions.md
  content/ch09/03-returns-and-allowances.md
"""
from __future__ import annotations
import re, sys, argparse, pathlib, shutil

DEFAULT_TARGETS = [
  "content/ch05/01-fees-and-interest.md",
  "content/ch05/02-transfers-advanced.md",
  "content/ch05/03-cash-over-short.md",
  "content/ch06/03-returns-and-allowances.md",
  "content/ch07/02-advance-and-unsettled.md",
  "content/ch07/03-employee-and-temp.md",
  "content/ch08/02-notes-transactions.md",
  "content/ch08/03-densai.md",
  "content/ch09/02-daily-transactions.md",
  "content/ch09/03-returns-and-allowances.md",
]

HEADER_LABEL = "| 借方科目 | 金額 | 貸方科目 | 金額 |"
ALIGN_ROW    = "|---|---:|---|---:|"

header_regex = re.compile(r"\|\s*借方科目\s*\|\s*金額\s*\|\s*貸方科目\s*\|\s*金額\s*\|")

align_token = re.compile(r"^-{3,}:?$")

def normalize_inline_table(line: str) -> str | None:
    """
    Given a single line that contains a full table (header+align+rows), normalize it.
    Return the normalized multiline table (with a blank line before) or None if not applicable.
    """
    if header_regex.search(line) is None:
        return None

    # Split into tokens by '|', but keep blanks to preserve empty cells
    raw_tokens = [t for t in line.split('|')]
    # Strip surrounding spaces except we preserve pure empties (for empty cells)
    tokens = [t.strip() for t in raw_tokens]

    # Find the index where alignment row starts (first token that looks like --- or ---:)
    try:
        align_idx = next(i for i, tok in enumerate(tokens) if align_token.match(tok or ""))
    except StopIteration:
        # If no explicit align tokens on this line, we cannot parse safely
        return None

    # Heuristic: header labels are the last 4 non-empty tokens before align_idx
    header_candidates = [t for t in tokens[:align_idx] if t != ""]
    if len(header_candidates) >= 4:
        hdr = header_candidates[-4:]
    else:
        hdr = ["借方科目","金額","貸方科目","金額"]

    # Collect 4 alignment tokens
    align = tokens[align_idx:align_idx+4]
    if len(align) < 4:
        # Not a standard 4-col table
        return None

    # Remaining tokens after alignment describe rows (allow blanks for empty cells)
    data = tokens[align_idx+4:]

    # Build rows from data tokens in groups of 4 (pad with blanks if needed)
    rows = []
    group = []
    for tok in data:
        # skip None-like values but preserve empty strings as blank cells
        if tok is None:
            tok = ""
        group.append(tok)
        if len(group) == 4:
            rows.append(group)
            group = []
    if group:
        # pad incomplete last row
        while len(group) < 4:
            group.append("")
        rows.append(group)

    # Format the table
    out_lines = []
    out_lines.append(f"| {' | '.join(hdr)} |")
    out_lines.append(f"|{'|'.join(align)}|".replace("||", "|"))  # ensure pipe count
    for r in rows:
        out_lines.append(f"| {' | '.join(r)} |")

    # Prepend a blank line to ensure Markdown treats this as a table block
    normalized = "\n" + "\n".join(out_lines) + "\n"
    return normalized

def process_file(path: pathlib.Path, dry_run=False) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    changed = False
    new_lines = []
    for i, line in enumerate(lines):
        if header_regex.search(line):
            # Separate any caption text placed before the header on the same line
            # e.g., "4列（2行） " or "例1：..." etc.
            before, sep, after = line.partition("|")
            if before.strip():
                # Keep caption in bold for visibility
                caption = before.strip()
                # If caption is something like "4列（2行）" remove trailing colon
                new_lines.append(f"**{caption}**")
                # Make sure there's a blank line after caption
                new_lines.append("")
                line = "|" + after  # rebuild starting at the header
            # Normalize entire inline table (header+align+rows) on this line
            normalized = normalize_inline_table(line)
            if normalized:
                # Ensure a blank line above unless previous line is already blank or a list boundary
                if len(new_lines) > 0 and new_lines[-1].strip() != "":
                    new_lines.append("")
                new_lines.append(normalized.strip("\n"))
                changed = True
                continue
        new_lines.append(line)

    if changed:
        bak = path.with_suffix(path.suffix + ".bak")
        if not dry_run:
            bak.write_text(text, encoding="utf-8")
            path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    return changed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root (contains content/)")
    ap.add_argument("--dry-run", action="store_true", help="Report only")
    ap.add_argument("--targets", nargs="*", default=DEFAULT_TARGETS, help="Specific .md files to process")
    args = ap.parse_args()

    root = pathlib.Path(args.root)
    targets = [root / t for t in args.targets]

    any_changed = False
    for p in targets:
        if not p.exists():
            print(f"[skip] {p} (not found)")
            continue
        changed = process_file(p, dry_run=args.dry_run)
        state = "CHANGED" if changed else "OK"
        print(f"[{state}] {p.relative_to(root)}")
        any_changed = any_changed or changed

    if args.dry_run:
        print("Dry run complete.")
    else:
        print("Done. .bak files were saved next to originals (only when changes were made).")

if __name__ == "__main__":
    main()
