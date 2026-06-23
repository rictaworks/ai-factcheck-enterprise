# SPEC ディレクトリ

仕様書・設計書・図解を管理する。

## ファイル一覧

| ファイル | 内容 |
|---------|------|
| `../ai-factcheck-mvp-spec.md` | MVP 仕様書（全体） |

## 図解（mermaid 形式）

以下の図解は `ai-factcheck-mvp-spec.md` に含まれている：

- ER 図（Section 5）
- DFD（Section 6）
- シーケンス図（Section 7）
- クラス図（Section 8）
- 状態遷移図（Section 9）
- ユースケース図（Section 10）

## 追加仕様書の配置ルール

- `SPEC/api/` — API 詳細仕様（エンドポイントごと）
- `SPEC/db/` — DB スキーマ詳細
- `SPEC/ui/` — 画面仕様書

mermaid 図はすべて `.md` ファイル内に記述する（`npm install -g @mermaid-js/mermaid-cli` でPNG出力可）。
