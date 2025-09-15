#!/usr/bin/env bash
set -euo pipefail

# MkDocs のビルド成果物 (site/) を公開用リポジトリに同期してデプロイします。
# 使い方:
#   scripts/deploy_site.sh [公開リポジトリの作業ディレクトリ (省略時: "$HOME/boki-shokyu-site")]

TARGET_DIR="${1:-"$HOME/boki-shokyu-site"}"

echo "[deploy] Building site with mkdocs --strict"
mkdocs build --strict

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "[deploy] Target repo not found. Cloning to: $TARGET_DIR"
  git clone https://github.com/BuNo32/boki-shokyu-site.git "$TARGET_DIR"
fi

echo "[deploy] Rsync to target (excluding .git/.github and *:Zone.Identifier)"
rsync -av --delete \
  --exclude=.git/ \
  --exclude=.github/ \
  --exclude='*:Zone.Identifier' \
  site/ "$TARGET_DIR/"

echo "[deploy] Removing any leftover *:Zone.Identifier files"
find "$TARGET_DIR" -type f -name '*:Zone.Identifier' -delete || true

echo "[deploy] Commit & push"
pushd "$TARGET_DIR" >/dev/null

# Fallback identity (必要ならローカル設定)
if ! git config user.name >/dev/null; then
  git config user.name "nm3284"
fi
if ! git config user.email >/dev/null; then
  git config user.email "nm3284@users.noreply.github.com"
fi

git add -A
if ! git diff --cached --quiet; then
  git commit -m "chore(deploy): MkDocs ビルドを反映（Zone.Identifier 除外）"
  git push origin main
  echo "[deploy] Pushed to origin/main"
else
  echo "[deploy] No changes to commit"
fi

popd >/dev/null
echo "[deploy] Done. Public URL: https://buno32.github.io/boki-shokyu-site/"

