# boki-shokyu

簿記（初級）向けの学習用リポジトリ雛形です。Node.js（LTS 20+）/ pnpm / TypeScript を採用し、ESLint + Prettier、Vitest、Husky + lint-staged、textlint を設定しています。

## セットアップ

```sh
pnpm install --frozen-lockfile
```

## スクリプト

- `pnpm build` — TypeScript を `dist/` にビルド
- `pnpm test` — テスト実行（Vitest）
- `pnpm lint` — ESLint 実行
- `pnpm format` — Prettier チェック
- `pnpm format:write` — Prettier 修正
- `pnpm typecheck` — 型チェック（noEmit）
- `pnpm verify` — Lint / Typecheck / Test 一括実行

## コード例

UI 文言は i18n ファイルに集約しています。例として `greet(name, lang)` を実装し、`src/i18n/` に日本語・英語の辞書を配置しています。

```ts
import { greet } from './src/index';
console.log(greet('太郎')); // => こんにちは、太郎！
```

## コミット前フック

`pnpm install` 後に `husky` が有効化され、`lint-staged` により整形/静的解析が走ります。

## ライセンス

（未設定）

