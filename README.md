# 簿記初級ラボ（オフライン対応）

オフラインで配布できる静的サイト教材（MkDocs + Material）。  
解説と章末クイズ（JSON）で学びます。

## セットアップ

```bash
python3 -m venv .venv && . .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
mkdocs build     # site/ に出力
mkdocs serve     # http://127.0.0.1:8000
python scripts/validate_quizzes.py  # 問題データ検証
```

## 開発ワークフロー（推奨）

```bash
# 依存のインストール（Node 20+ / pnpm）
pnpm install --frozen-lockfile

# Lint / 型チェック / テスト 一括実行
pnpm verify   # = pnpm lint && pnpm typecheck && pnpm test
```

## 公開（デプロイ）

- 公開先リポジトリ: https://github.com/BuNo32/boki-shokyu-site （GitHub Pages）
- デプロイスクリプト: `scripts/deploy_site.sh`

```bash
# 推奨: pnpm スクリプトで実行（必ず run を付ける）
pnpm run deploy

# 直接実行も可。引数で公開リポジトリの作業ディレクトリを指定可能（省略時: $HOME/boki-shokyu-site）
scripts/deploy_site.sh /path/to/boki-shokyu-site
```

メモ:

- デプロイ時は `mkdocs build --strict` を実行し、strict 警告で失敗しないことを確認します。
- `*:Zone.Identifier`（Windows 派生ファイル）は rsync で除外し、残存しても削除します。
- `pnpm deploy` は pnpm 組み込みコマンドと衝突するため、`pnpm run deploy` を使用してください。

公開URL: https://buno32.github.io/boki-shokyu-site/
