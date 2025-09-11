# Repository Verification Report

Generated at (UTC): 2025-09-11 15:35:48

## Environment

```
Python 3.12.3
mkdocs, version 1.6.1 from /home/nm3284/.venv/lib/python3.12/site-packages/mkdocs (Python 3.12)
```

## Validate quizzes (scripts/validate_quizzes.py)

```
RESULT: OK
```

## MkDocs build (--strict)

```
RESULT: OK
```

## Essential files

```
OK - content/ch05/index.md
OK - content/assets/js/quiz.js
OK - content/quizzes/ch05.json
OK - mkdocs.yml
```

## Quick grep checks

```
22:  loadQuiz('../quizzes/ch05.json','quiz-ch05');
9:use_directory_urls: false
35:extra_javascript:
```

## Site outputs (top-level)

```
 - site/404.html
 - site/ch01/index.html
 - site/ch05/index.html
 - site/index.html
 - site/prototypes/dashboard.html
 - site/prototypes/exam-sample.html
 - site/prototypes/lesson-sample.html
 - site/prototypes/quiz-sample.html
 - site/prototypes/typography.html
 - site/quizzes/ch05.json
 - site/quizzes/index.json
 - site/quizzes/prototype.json
 - site/quizzes/schema.json
 - site/search/search_index.json
 - site/sitemap.xml
 - site/sitemap.xml.gz
```

## GitHub Actions (latest 5)

```
completed	success	chore(verify): add VERIFY_REPORT.md	CI	chore/verify-report	push	17649546677	24s	2025-09-11T15:31:01Z
completed	success	UI prototypes & assets relocation	CI	feat/ui-prototypes	pull_request	17647466547	24s	2025-09-11T14:17:04Z
completed	success	feat(ui): add prototypes (lesson/quiz/exam/dashboard) and move assets…	CI	feat/ui-prototypes	push	17647463291	21s	2025-09-11T14:16:57Z
completed	success	fix(lint): avoid empty catch block in dashboard.js	CI	feat/ui-prototypes	push	17647444640	22s	2025-09-11T14:16:19Z
completed	failure	docs(mkdocs): add extra_css/js and prototypes nav	CI	feat/ui-prototypes	push	17647308942	10s	2025-09-11T14:11:36Z
```

---

End of report.
