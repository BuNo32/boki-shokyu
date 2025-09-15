# instructions ディレクトリ（エージェント向け指示書 保管用）

このディレクトリは、プロジェクトの「指示書（AGENTS 系含む）」を保管・配布するための場所です。

## 覚書（今後の運用）

- 本プロジェクトの指示書はすべて `instructions/` に集約します。
- 形式は Markdown（例: `AGENTS.*.md` や `YYYYMMDD_トピック.md`）または ZIP（説明 `.md`＋必要ファイル）を想定します。
- ZIP 配布時は、サイト反映用のファイルは ZIP 内で `content/` 配下に置いてください（例: `content/ch04/...`）。
- 指示に「RUN/EDIT」ブロックが含まれる場合は、その手順に従って作業し、原則 PR ベースで反映します。
- 作業後は `pnpm verify`（lint/typecheck/test）→ `mkdocs build --strict` を通してから必要に応じて `pnpm run deploy` で公開します。

## 補足

- 置き場所: このフォルダ直下（例: `instructions-20250915.zip`）
- 内容例: `README.md` や `*.md` の説明ファイル、補足の画像/図表 等
- 推奨: 指示の Markdown は `pnpm textlint` で日本語校正
- 注意: API キー・個人情報などの機密は含めないでください

必要であれば、ZIP 内の `.md` を `content/` へ展開してサイトに反映する運用も可能です（展開前に構成をご相談ください）。
