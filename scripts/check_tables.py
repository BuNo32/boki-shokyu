\
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_tables.py
---------------
Scan target files and report lines where the table header appears inline
(i.e., on the same line as other text) which often prevents Markdown
from rendering tables.

Usage:
  python scripts/check_tables.py --root <repo-root>
"""
from __future__ import annotations
import re, argparse, pathlib

HEADER_RE = re.compile(r"\|\s*借方科目\s*\|\s*金額\s*\|\s*貸方科目\s*\|\s*金額\s*\|")

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

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--root", default=".", help="Repo root (contains content/)")
  ap.add_argument("--targets", nargs="*", default=DEFAULT_TARGETS)
  args = ap.parse_args()

  root = pathlib.Path(args.root)
  total = 0
  for rel in args.targets:
    p = root / rel
    if not p.exists():
      print(f"[skip] {rel} (not found)")
      continue
    with p.open(encoding="utf-8") as f:
      for i, line in enumerate(f, start=1):
        if HEADER_RE.search(line):
          # If the first non-space char is a pipe, this is a proper table header line; skip.
          first = line.lstrip()[:1]
          if first == "|":
            continue
          print(f"[warn] {rel}:{i} Possible inline table header → {line.strip()[:96]}...")
          total += 1

  if total == 0:
    print("No suspicious inline table headers found.")
  else:
    print(f"Detected {total} suspicious lines. Run fix_tables.py to reformat.")

if __name__ == "__main__":
  main()
