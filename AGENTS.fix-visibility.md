# AGENTS.fix-visibility.md

## 目的

クイズが表示されない環境差を解消（`loadQuiz` 実行順問題）。

## 完了条件

- ch05 など各ページで、再読込後に必ずクイズが描画されること。
- `mkdocs build --strict` および `scripts/validate_quizzes.py` が成功すること。
