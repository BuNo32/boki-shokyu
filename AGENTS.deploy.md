# AGENTS.deploy.md — 公開（デプロイ）手順

## 目的

MkDocs のビルド成果物（`site/`）を GitHub Pages 用の公開リポジトリ `BuNo32/boki-shokyu-site` に同期して公開する。

## 前提

- Python + MkDocs 環境（`pip install -r requirements.txt` 済み）
- Node.js 20+ / pnpm（`pnpm install --frozen-lockfile` 済み）

## 手順（標準）

1. 検証

- `python scripts/validate_quizzes.py`
- `mkdocs build --strict`
- `pnpm verify`（= `pnpm lint && pnpm typecheck && pnpm test`）

2. 公開

- `pnpm run deploy`
  - 内部で `scripts/deploy_site.sh` を実行
  - `site/` → `$HOME/boki-shokyu-site/` へ rsync
  - `--exclude='*:Zone.Identifier'` で Windows 派生ファイルを除外
  - 変更があれば `commit` → `push`（`origin/main`）

3. 確認

- ルート: https://buno32.github.io/boki-shokyu-site/
- プロトタイプ:
  - `prototypes/exam-sample.html`
  - `prototypes/dashboard.html`

## 注意

- pnpm の予約コマンドと衝突するため、必ず `pnpm run deploy` を使用すること（`pnpm deploy` は不可）。
- 初回のみ、公開リポジトリが無い場合はスクリプトが `$HOME/boki-shokyu-site` に clone する。
- 外部ネットワーク操作（clone/push）はプロジェクト規約に従い、事前承認を得ること。
