# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 削除系コマンドの禁止（重要）

以下のルールはこのワークスペース内のすべての会話で絶対に守られる：

- Claude はファイルまたはディレクトリを削除するコマンドを一切生成してはならない。
  例：rm, rm -rf, rm *, rmdir, unlink, cache --delete,
      lftp mirror --delete, rsync --delete, git clean -df, find -delete 等。
- 削除が必要な場合でも、Claude は削除コマンドを提案せず、「手動で削除してください」といった説明に留めること。
- 削除の推奨・削除操作の自動判断も禁止。
- ssh / lftp / デプロイ系スクリプトを生成する場合でも、削除コマンドの生成は禁止。

---

## AI 役割分担

| フェーズ | 担当 |
|---|---|
| 設計・Issue 発行 | Claude Sonnet |
| 1次実装 | Antigravity 3.5Flash（`.agents/agents.md` 参照） |
| コードレビュー | Claude Sonnet |
| テスト作成・実行 | Claude Sonnet |
| セキュリティレビュー | Codex GPT5.5（`@AGENTS.md` 参照） |

エージェント別の指示は `.agents/` に配置する。

---

## ブランチ・PR ルール

- **main ブランチでの作業禁止**
- `src/*` の変更は必ず PR を作成すること（main への直接 push 禁止）
- `src/*` 以外は main ブランチへの push を許可する
- commit 前に必ず security review を実施すること
- PR 本文に**非エンジニア向けユーザーテスト手順**を丁寧に記載すること

---

## ディレクトリ管理

| ディレクトリ | 用途 |
|---|---|
| `TASKS/` | タスク管理 |
| `DEBUG/` | バグ報告 |
| `CLIENT/` | クライアント要望 |
| `WORK/` | 作業報告 |
| `ENV/DEVELOPMENT.md` | 開発環境 |
| `ENV/PRODUCTION.md` | 本番環境 |
| `SPEC/` | 仕様書・図解（ER図・DFD・シーケンス図・クラス図・状態遷移図・ユースケース図） |
| `DELETE/` | ゴミ箱（削除対象ファイルはここへ移動すること） |
| `test/pr***/` | PR 対応テスト |

図解は mermaid を使用すること。

---

## UI デザイン

- `app-ui/` にモックが配置されている場合、必ずそれに従うこと
- デフォルトアイコンは **Font Awesome** を使用すること
- 絵文字を使用禁止
- ネイティブの `alert()` / `confirm()` / `prompt()` はプロジェクト全体で使用禁止
- UI 変更時は `@.claude/CRAP.md`（Contrast・Repetition・Alignment・Proximity）に照らして評価すること

---

## コーディング規約

- **フォールバック禁止** — 例外処理をしっかり書くこと
- デバッグトレースできるようにコードを書くこと
- 制御構文・条件構文以外は必ずクラスまたは関数に書くこと
- **グローバル変数禁止**（セキュリティ観点）
- 文字列リテラルは設定ファイルに分離すること（ハードコード禁止・ハードコードチェックのテストを書くこと）
- 環境変数は `.env` を参照すること
- **環境判定**（development/production）を必ず実装して分岐できるようにすること
- 開発環境は認証済み状態に分岐すること（テスト可能性のため）
- 時刻は **JST**、エンコードは **UTF-8**

---

## 多言語対応

開発当初から多言語対応すること（7言語）：

> 日本語・英語・フランス語・中国語・ロシア語・スペイン語・アラビア語

ただし、**開発者用の管理画面は日本語のみ**。

---

## TDD

`plan → red test → coding → green test` を厳守する。

| 対象 | フレームワーク |
|---|---|
| Ruby | RSpec |
| TypeScript/JS | Jest |
| Python | pytest |
| フロントエンド確認 | `curl`・`wget --mirror`・Playwright |

テスト対象は開発サーバーとすること。

---

## テックスタック

- **フロントエンド**: Next.js 14, TypeScript, TailwindCSS, SWR（3秒ポーリング）
- **バックエンド**: Rails 7 (API mode), Ruby 3.3
- **AI/ML**: FastAPI, Python, LangChain, LangGraph, LangSmith
- **DB**: PostgreSQL 16（本番）/ SQLite（開発）
- **キュー**: Sidekiq + Redis
- **認証**: Google OAuth 2.0（OmniAuth + Devise）
- **デプロイ**: Vercel（フロント）/ Railway（バックエンド・DB・AI）
- **ドメイン**: rictaworks.jp のサブドメイン
- FastAPI・Gin は必要な場合のみ追加可（AI処理・画像加工・リアルタイム通信）

---

## エージェント構成

規模に応じて以下のエージェントを作成すること：

`director` / `project-manager` / `designer` / `debugger` / `tester` / `data-scientist` / `deployer` / `writer` / `service-manager`

---

## Sub Agent 指示

### pr-checker
- 全 PR を日本語にすること
- 非エンジニア向けユーザーテストを PR 本文に丁寧に記載すること

### tester
- 全 PR に書かれたユーザーテスト手順の実行スクリプトを作成すること
- `@.claude/TM.md` に記載されたテストを作成すること（jest, rspec 等）
- テストは `test/pr***/` に作成すること
- テスト対象は開発サーバーとすること

---

## README 要件

README.md に以下を必ず記載すること：
- 自動ログイン手順
- ページ一覧（ページ名・URL リンク）
- API 一覧（タイトル・エンドポイント URL・`SPEC/api` リンク）

---

## 参照ファイル

コーディング・レビュー時に必ず参照すること：

- `@.claude/development-principles.md` — YAGNI, KISS, DRY, SOLID
- `@.claude/TM.md` — テスト方法・フレームワーク
- `@.claude/QC10.md` — 品質チェックリスト（10項目）
- `@.claude/OWASP10.md` — セキュリティチェックリスト
- `@.claude/CC.md` — コンプライアンスチェックリスト（商標・著作権・個人情報等）
- `@.claude/CRAP.md` — UI デザイン原則（UI作業時）
- `@AGENTS.md` — Codex セキュリティレビュー指示
- `@ai-factcheck-mvp-spec.md` — MVP 仕様書（全機能・API・データモデル・テスト）
