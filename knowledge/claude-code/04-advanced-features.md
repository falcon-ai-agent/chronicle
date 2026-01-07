# Claude Code 高度な機能

## 1. MCP (Model Context Protocol)

外部サービス・ツールと連携するプロトコル。数百のツールを統合可能。

### サーバー追加

```bash
# HTTPサーバー
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 認証付き
claude mcp add --transport http api https://api.example.com/mcp \
  --header "Authorization: Bearer TOKEN"

# ローカルstdioサーバー
claude mcp add --transport stdio airtable \
  --env AIRTABLE_API_KEY=KEY \
  -- npx -y airtable-mcp-server
```

### スコープ

| スコープ | 保存場所 | 範囲 |
|--------|--------|------|
| local | ~/.claude.json | このプロジェクトのみ |
| project | .mcp.json | プロジェクト全体（チーム共有） |
| user | ~/.claude.json | 全プロジェクト |

### 管理コマンド

```bash
claude mcp list      # 一覧
claude mcp get NAME  # 詳細
claude mcp remove NAME
```

## 2. Subagents（サブエージェント）

特定タスク用の専門化エージェント。独立コンテキストで動作。

### 配置場所

```
.claude/agents/      # プロジェクト
~/.claude/agents/    # ユーザー
```

### 定義例

```markdown
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: コードレビュー専門。変更後に使用。
tools: Read, Grep, Glob
model: sonnet
---

あなたはシニアコードレビュアーです。
以下の観点でレビュー:
- 可読性
- バグの可能性
- セキュリティ
- テストカバレッジ
```

### 組み込みサブエージェント

| 名前 | 用途 |
|-----|------|
| General | 複雑な多段階タスク |
| Plan | Plan Modeでの調査（Haiku使用） |
| Explore | 読み取り専用コード探索 |

## 3. Hooks（イベントフック）

自動化スクリプトの実行トリガー。

### イベント種類

| イベント | トリガー |
|--------|--------|
| PreToolUse | ツール実行前（ブロック可） |
| PostToolUse | ツール実行後 |
| UserPromptSubmit | ユーザー入力時 |
| Stop | 応答完了時 |

### 設定例: 自動フォーマット

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "prettier --write \"$(jq -r '.tool_input.file_path')\""
        }]
      }
    ]
  }
}
```

### 設定例: ファイル保護

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "python3 -c \"import json,sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if '.env' in path else 0)\""
        }]
      }
    ]
  }
}
```

## 4. Skills（エージェントスキル）

Claude に特定領域の知識を教える。自動トリガー。

### 構造

```
~/.claude/skills/explaining-code/
├── SKILL.md        # 必須
├── reference.md    # 参考資料
└── scripts/        # ユーティリティ
```

### SKILL.md例

```markdown
---
name: code-review
description: コードレビュー。PR分析時に使用。
allowed-tools: Read, Grep, Glob
model: sonnet
---

# Code Review Skill

レビュー観点:
1. コード構成
2. エラーハンドリング
3. セキュリティ
4. テストカバレッジ
```

## 5. Plugins（プラグインシステム）

再利用可能な拡張機能。チーム・コミュニティで共有。

### 構造

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json   # マニフェスト
├── commands/         # スラッシュコマンド
├── agents/           # サブエージェント
├── skills/           # スキル
├── hooks/
│   └── hooks.json
└── .mcp.json         # MCPサーバー
```

### 管理

```
/plugin              # 管理UI
/plugin install URL  # インストール
/plugin uninstall    # アンインストール
```

## 6. Extended Thinking

複雑な問題に専用トークン予算を割り当て。

```bash
# 環境変数
export MAX_THINKING_TOKENS=1024

# セッション内
> ultrathink: キャッシングアーキテクチャを設計
```

## 7. Git Worktrees並列実行

```bash
# Worktree作成
git worktree add ../feature-a -b feature-a

# 各worktreeで独立実行
cd ../feature-a && claude
```

## 8. .claude/rules/（モジュール化ルール）

大規模プロジェクト向け:

```
.claude/rules/
├── frontend/
│   ├── react.md
│   └── styles.md
├── backend/
│   ├── api.md
│   └── database.md
└── general.md
```

パス固定ルール:

```markdown
---
paths: src/api/**/*.ts
---

# API開発ルール
- 入力バリデーション必須
- 標準エラーレスポンス形式
- OpenAPIドキュメントコメント
```

## 9. Claude Canvas（コミュニティツール）

**概要:**
Claude Codeに外部ディスプレイを提供するTUIツールキット（コミュニティプロジェクト）

**リポジトリ:** https://github.com/dvdsgl/claude-canvas

**機能:**
- インタラクティブなターミナルインターフェース
- メール、カレンダー、フライト予約など様々なUIをスポーン可能
- Claude Codeの出力を専用ディスプレイに表示

**ユースケース:**
- マルチモニター環境での開発体験向上
- Claude Codeの出力と実際のコード編集を分離
- TUIベースのインタラクティブアプリケーション開発

**発表:** 2026-01-06（@dvdsgl）

**注意:** Anthropic公式機能ではなく、コミュニティによる拡張ツール
