# Claude Code 概要と基本機能

## Claude Codeとは

AnthropicのAIエージェント型コーディングツール。ターミナルで動作し、自動的にコード編集・実行・コミットが可能。

## インストール

```bash
# 推奨
curl -fsSL https://claude.ai/install.sh | bash

# Homebrew
brew install --cask claude-code

# NPM
npm install -g @anthropic-ai/claude-code
```

## 基本コマンド

| コマンド | 説明 |
|---------|------|
| `claude` | 対話型REPL起動 |
| `claude "query"` | 初期プロンプト付き起動 |
| `claude -p "query"` | 非対話モード（SDKモード） |
| `claude -c` | 最新の会話を続行 |
| `claude -r "<session>"` | 特定セッション再開 |
| `claude update` | 更新 |

## 利用可能なツール

| ツール | 説明 |
|-------|------|
| Read | ファイル読み込み |
| Write | ファイル作成/上書き |
| Edit | ファイル編集 |
| Bash | シェルコマンド実行 |
| Glob | パターンマッチング検索 |
| Grep | ファイル内容検索 |
| WebFetch | URL取得 |
| WebSearch | Web検索 |
| Task | サブエージェント実行 |
| TodoWrite | TODOリスト管理 |

## スラッシュコマンド（頻出）

| コマンド | 機能 |
|---------|------|
| `/clear` | 会話履歴クリア |
| `/compact` | 会話圧縮 |
| `/config` | 設定 |
| `/model` | モデル選択 |
| `/memory` | CLAUDE.mdエディタ |
| `/permissions` | パーミッション管理 |
| `/agents` | サブエージェント管理 |
| `/mcp` | MCPサーバー管理 |

## キーボードショートカット

| ショートカット | 機能 |
|-------------|------|
| `Ctrl+C` | キャンセル/中断 |
| `Ctrl+L` | 画面クリア |
| `Shift+Tab` | パーミッションモード切替 |
| `Esc+Esc` | 巻き戻し |
| `Ctrl+V` | 画像ペースト |
| `\+Enter` | 複数行入力 |

## モデル選択

| エイリアス | 説明 |
|----------|------|
| `sonnet` | 最新Sonnet（バランス型） |
| `opus` | Opus 4.5（複雑推論向け） |
| `haiku` | 高速軽量 |
