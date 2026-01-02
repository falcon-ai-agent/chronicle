# Claude Code 生産性向上Tips

## 即効性のあるTips

### 1. `/clear`を頻繁に使う

新しいタスクを始めるたびにチャットをクリア。履歴がトークンを消費し、コンパクション呼び出しを招く。

### 2. Shift+ドラッグでファイル参照

ファイルをターミナルにドラッグ&ドロップで正確なパス挿入。

### 3. Ctrl+V で画像ペースト

スクリーンショットやデザインモックをそのままペースト。視覚的な指示が可能。

### 4. 複数インスタンスの並列実行

- VS Code拡張を使い、異なるペインで複数インスタンス実行
- Git worktreeで独立したブランチを並列作業
- コード作成と検証を分離したインスタンスで実行

### 5. カスタムスラッシュコマンド

`.claude/commands/` にMarkdownファイルを配置:

```markdown
# .claude/commands/review.md
---
description: コードレビューを実行
---

変更されたファイルをレビューし、以下の観点でチェック:
1. バグの可能性
2. セキュリティ問題
3. パフォーマンス
4. 可読性
```

使用: `/review`

### 6. Plan Modeの活用

`Shift+Tab` を2回押してPlan Modeへ。ファイル変更なしで分析・計画のみ。大規模変更の前に必須。

### 7. think/think hard/think harder

複雑な問題には拡張思考を:

```
> think hard: このアーキテクチャの問題点を分析して
> ultrathink: キャッシングレイヤーを設計して
```

### 8. GitHub App連携

```bash
/install-github-app
```

PRの自動レビューが可能。`claude-code-review.yml`で「バグと脆弱性のみ報告、簡潔に」と指定。

### 9. ヘッドレスモード（CI/CD統合）

```bash
# 非対話実行
claude -p "analyze this code for security issues" < code.ts > report.txt

# JSON出力
claude -p "fix all linting issues" --output-format json > result.json
```

### 10. 巻き戻し機能

`Esc+Esc`で過去の状態にロールバック。安全な実験が可能。

## 生産性向上の実績データ

| ユースケース | 効果 |
|------------|------|
| 広告コピー作成 | 2時間 → 15分（87.5%短縮） |
| 複雑な機能の自動生成 | 70%を自動化 |
| 一般的なワークフロー | 10-30%の生産性向上 |
| 環境・権限の最適化後 | 最大40%向上 |

## 2026年の注目機能

- **Swarming**: 並列実行パターンの強化（Anthropic発表）
- 早期に並列実行パターンを習得しておくと有利

## Sources

- [Builder.io: How I use Claude Code](https://www.builder.io/blog/claude-code)
- [F22 Labs: 10 Claude Code Productivity Tips](https://www.f22labs.com/blogs/10-claude-code-productivity-tips-for-every-developer/)
- [Tembo: Mastering Claude Code](https://www.tembo.io/blog/mastering-claude-code-tips)
