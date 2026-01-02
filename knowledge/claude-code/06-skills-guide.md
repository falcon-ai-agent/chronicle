# Claude Code Skills 実践ガイド

## Skillsとは

Claudeに特定タスクの遂行方法を教えるMarkdownファイル。リクエストに応じて**自動発動**する。

## Subagentsとの違い

| | Skills | Subagents |
|---|---|---|
| 起動 | 自動（意味マッチ） | 明示的 |
| コンテキスト | 共有 | 独立 |
| 用途 | 知識・標準を追加 | タスクを隔離実行 |

## 基本構造

```
~/.claude/skills/my-skill/
└── SKILL.md
```

```yaml
---
name: my-skill
description: 説明と使用場面（1024文字以下）
allowed-tools: Read, Grep, Glob  # オプション
---

# My Skill

## Instructions
1. ステップ1
2. ステップ2

## Examples
- 例1
- 例2
```

## 配置場所

| 場所 | パス | 範囲 |
|------|------|------|
| 個人 | `~/.claude/skills/` | 全プロジェクト |
| プロジェクト | `.claude/skills/` | チーム共有 |

## 実用Skills事例

### 公式（anthropics/skills）

- **docx, pdf, pptx, xlsx** - ドキュメント操作
- **algorithmic-art** - p5.js生成アート
- **frontend-design** - UIデザイン支援

### コミュニティ（obra/superpowers）

- **test-driven-development** - TDDサイクル
- **systematic-debugging** - 4フェーズ根本原因分析
- **brainstorming** - ソクラテス式設計改善
- **writing-plans** - 実装計画書作成
- **dispatching-parallel-agents** - 並列エージェント管理

## ベストプラクティス

### 1. 説明は具体的に

```yaml
# Good
description: PRをレビューし、セキュリティ・パフォーマンス・可読性をチェック。コードレビュー時に使用。

# Bad
description: コードをチェック
```

### 2. 単一責任

```yaml
# Good - 1つの責任
name: pdf-text-extraction

# Bad - 責任が多すぎ
name: pdf-everything
```

### 3. 5回以上繰り返すタスクをSkill化

> "5回以上やったことがあり、今後10回以上やるなら、Skillにする価値がある"

### 4. Progressive Disclosure

```
my-skill/
├── SKILL.md        # 500行以下（必須情報のみ）
├── REFERENCE.md    # 詳細（必要時のみ読み込み）
└── scripts/        # 実行スクリプト
```

## インストール方法

```bash
# 公式Skillsプラグイン
/plugin marketplace add anthropics/skills

# 個別インストール
/plugin install document-skills@anthropic-agent-skills
```

## Sources

- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [Simon Willison: Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
