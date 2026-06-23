# AI Factcheck Enterprise

AI生成テキストから検証可能なクレームを自動抽出し、外部情報源との照合で真偽を判定する企業向けSaaSツール。

---

## 自動ログイン（開発環境）

開発環境では Google OAuth をスキップして自動ログインできる。`.env` に以下を追加する：

```bash
TEST_USER_GOOGLE_SUB=test-sub-12345
TEST_USER_DISPLAY_NAME=開発者テスト
TEST_ORG_ID=00000000-0000-0000-0000-000000000001
```

起動後 http://localhost:3000 にアクセスすると自動的にログイン済み状態になる。

詳細は [ENV/DEVELOPMENT.md](ENV/DEVELOPMENT.md) を参照。

---

## ページ一覧

| ページ名 | URL |
|---------|-----|
| ログイン | [/login](https://factcheck.rictaworks.jp/login) |
| ダッシュボード（検証履歴一覧） | [/dashboard](https://factcheck.rictaworks.jp/dashboard) |
| 検証ジョブ作成（テキスト投稿） | [/verify](https://factcheck.rictaworks.jp/verify) |
| 検証結果詳細 | [/jobs/:id](https://factcheck.rictaworks.jp/jobs/:id) |
| レポートHTML表示 | [/jobs/:id/report](https://factcheck.rictaworks.jp/jobs/:id/report) |
| 共有レポート閲覧（認証不要） | [/shared/:token](https://factcheck.rictaworks.jp/shared/:token) |
| 組織設定・管理 | [/settings/organization](https://factcheck.rictaworks.jp/settings/organization) |
| 月次使用量 | [/settings/usage](https://factcheck.rictaworks.jp/settings/usage) |

---

## API 一覧

### Rails API（`https://api-factcheck.rictaworks.jp`）

仕様書：[SPEC/api](SPEC/)

| タイトル | エンドポイント |
|---------|--------------|
| Googleログイン | `POST /api/v1/auth/google` |
| 自ユーザー情報取得 | `GET /api/v1/me` |
| 検証ジョブ作成 | `POST /api/v1/verification_jobs` |
| 検証ジョブ一覧 | `GET /api/v1/verification_jobs` |
| 検証ジョブ詳細 | `GET /api/v1/verification_jobs/:id` |
| レポートHTML取得 | `GET /api/v1/verification_jobs/:id/report` |
| レポートPDFダウンロード | `GET /api/v1/verification_jobs/:id/report.pdf` |
| 共有リンク生成 | `POST /api/v1/verification_jobs/:id/shares` |
| 共有レポート閲覧 | `GET /api/v1/shared/:token` |
| 組織情報取得 | `GET /api/v1/organizations/me` |
| 組織設定更新 | `PUT /api/v1/organizations/me` |
| 月次使用量取得 | `GET /api/v1/organizations/me/usage` |

### FastAPI（内部 `https://ai-factcheck.rictaworks.jp`）

| タイトル | エンドポイント |
|---------|--------------|
| クレーム抽出 | `POST /extract_claims` |
| 証拠収集 | `POST /collect_evidence` |
| 真偽判定 | `POST /judge` |
| ヘルスチェック | `GET /health` |

---

## アーキテクチャ

```
Next.js (Vercel) → Rails API (Railway) → PostgreSQL (Railway)
                                       → FastAPI AI Service (Railway)
                                           → Google Custom Search API
                                           → OpenAI / Anthropic API
```

詳細仕様：[ai-factcheck-mvp-spec.md](ai-factcheck-mvp-spec.md)
