#!/usr/bin/env bash
set -u
REPORT="VERIFY_REPORT.md"

echo "# Repository Verification Report" > "$REPORT"
date -u +"Generated at (UTC): %Y-%m-%d %H:%M:%S" >> "$REPORT"

section () { echo -e "\n## $1\n" >> "$REPORT"; }
append ()  { echo -e "$1" >> "$REPORT"; }

section "Environment"
append "\`\`\`"
python --version 2>&1 >> "$REPORT" || true
mkdocs --version 2>&1 >> "$REPORT" || true
append "\`\`\`"

section "Validate quizzes (scripts/validate_quizzes.py)"
append "\`\`\`"
if python scripts/validate_quizzes.py; then
  echo "RESULT: OK" >> "$REPORT"
else
  echo "RESULT: NG" >> "$REPORT"
fi
append "\`\`\`"

section "MkDocs build (--strict)"
append "\`\`\`"
if mkdocs build --strict; then
  echo "RESULT: OK" >> "$REPORT"
else
  echo "RESULT: NG" >> "$REPORT"
fi
append "\`\`\`"

section "Essential files"
append "\`\`\`"
for f in content/ch05/index.md content/assets/js/quiz.js content/quizzes/ch05.json mkdocs.yml; do
  if [ -f "$f" ]; then echo "OK - $f"; else echo "NG - missing $f"; fi
done >> "$REPORT"
append "\`\`\`"

section "Quick grep checks"
append "\`\`\`"
grep -n "loadQuiz(" content/ch05/index.md >> "$REPORT" 2>/dev/null || echo "loadQuiz() not found in ch05" >> "$REPORT"
grep -n "use_directory_urls" mkdocs.yml   >> "$REPORT" 2>/dev/null || true
grep -n "extra_javascript"   mkdocs.yml   >> "$REPORT" 2>/dev/null || true
append "\`\`\`"

section "Site outputs (top-level)"
append "\`\`\`"
if [ -d site ]; then
  find site -maxdepth 2 -type f | sort | sed 's/^/ - /' >> "$REPORT"
else
  echo "site/ not found (build may have failed)" >> "$REPORT"
fi
append "\`\`\`"

section "GitHub Actions (latest 5)"
append "\`\`\`"
if command -v gh >/dev/null 2>&1; then
  gh run list -L 5 >> "$REPORT" 2>/dev/null || echo "gh run list failed" >> "$REPORT"
else
  echo "gh not found; skipping GA status" >> "$REPORT"
fi
append "\`\`\`"

append "\n---\nEnd of report.\n"
echo "Report generated: $REPORT"
