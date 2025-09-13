# AGENTS.split-ch05.md

## 目的

第5章「現金・預金」を以下の 5 ページ構成に分割し、MkDocs のナビを更新する。

- 章トップ（目次）
- 節ページ × 3
- 章末クイズ

## 完了条件

- `content/ch05/` に以下のファイルが存在すること
  - `index.md`（章目次）
  - `01-basics.md`（1節）
  - `02-patterns.md`（2節）
  - `03-transfers.md`（3節）
  - `99-quiz.md`（章末クイズ）

- `mkdocs.yml` のナビが第5章の入れ子になっており、Material の標準フッターで「前へ / 次へ」が機能すること

- クイズは `99-quiz.md` のみで読み込まれ、4列仕訳UI（既存機能）で採点可能であること

- `mkdocs build --strict` と `scripts/validate_quizzes.py` が成功すること
