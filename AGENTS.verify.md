# AGENTS.verify.md

## 目的

`boki-shokyu/` 内で、以下の項目を自動的に点検し、その結果をレポートとして `VERIFY_REPORT.md` にまとめ、PR を作成する。

- サイトが正常にビルドできること
- 必要なファイルが揃っていること
- クイズの妥当性が保たれていること
- CI 状況が良好であること

## 完了条件

以下の条件が満たされたとき、このタスクを完了とする。

- [ ] リポジトリ直下に `VERIFY_REPORT.md` が作成され、以下の主要チェック結果が掲載されている
  - [ ] `mkdocs build --strict` の実行結果
  - [ ] `scripts/validate_quizzes.py` の実行結果
  - [ ] `site/` 生成物の主要ファイル一覧
- [ ] 上記成果物がブランチ `chore/verify-report` にコミットされ、Push 済み
- [ ] PR が作成済み（`gh` コマンド利用可能な場合）
