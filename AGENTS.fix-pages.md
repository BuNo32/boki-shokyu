# AGENTS.fix-pages.md

目的: GitHub Pages 配信に強い相対パスへ統一し、site_url とフォント設定を整備する。

## 1) mkdocs.yml を編集

- `site_url` を `https://buno32.github.io/boki-shokyu-site/` に設定
- `theme.font: false` を追加（Google Fonts の無効化）
- （任意）`plugins` に `offline` / `privacy` を追記（両方入れる場合はそのまま）

## 2) content/quizzes/index.json を編集

- `page` と `basePath` が `/` で始まる項目があれば相対表記へ修正
  - 例: `/prototypes/quiz-sample.html` → `prototypes/quiz-sample.html`
  - 例: `/quizzes/` → `quizzes/`

## 3) content/assets/js/dashboard.js を堅牢化

- `const toRel = p => p && p.startsWith('/') ? (location.pathname.replace(/[^/]+$/, '') + p.replace(/^\//,'')) : p;`
- `href` 生成時は `toRel(q.page)` を使用
- `basePath` 併用時も `toRel(q.basePath) + q.file` で生成

## 4) 検証・コミット

- `python scripts/validate_quizzes.py`
- `mkdocs build --strict`
- `git add -A && git commit -m "fix(pages): relative links, site_url, font=false"`
- `git push` （PR作成は任意）
