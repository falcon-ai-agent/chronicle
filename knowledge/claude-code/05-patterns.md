# Claude Code 実践パターン集

## パターン1: 新規コードベース理解

```
claude
> give me an overview of this codebase
> explain the main architecture patterns
> what are the key data models?
> how is authentication handled?
```

**ポイント**: 段階的に質問し、全体像から詳細へ

## パターン2: バグ修正フロー

```
1. エラー内容をペースト
2. 原因分析を依頼
3. 修正案を複数提示させる
4. 選択した修正を実装
5. テストで検証
```

```
> I'm seeing an error when running npm test
> [paste error]
> suggest a few ways to fix this
> update the file with fix #2
> run tests to verify
```

## パターン3: リファクタリング

```
1. Plan Modeで計画（Shift+Tab×2）
2. 計画をレビュー
3. 実行モードに切替（Shift+Tab）
4. 段階的に実装
```

```
claude --permission-mode plan
> Help me refactor the authentication module
[Claude creates detailed plan]
[Switch with Shift+Tab]
> Implement step 1 of the plan
```

## パターン4: 並列レビュー体制

```
Terminal 1: コード実装
Terminal 2: テスト作成
Terminal 3: レビュー

# Git worktreeを活用
git worktree add ../impl -b implementation
git worktree add ../tests -b tests
git worktree add ../review -b review
```

## パターン5: 大規模移行プロジェクト

レガシーコードの移行（Java→新Java、PHP→React等）

```
1. 現行コードの分析（Plan Mode）
2. 移行計画の策定
3. モジュール単位で移行
4. 各段階でテスト検証
5. 並列インスタンスで効率化
```

## パターン6: CI/CD統合

```yaml
# .github/workflows/claude-review.yml
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Claude Review
        run: |
          claude -p "Review this PR for bugs and security issues" \
            --output-format json > review.json
```

## パターン7: ドキュメント自動生成

```
> Generate API documentation for src/api/
> Create a README for this project based on the codebase
> Document the data flow in this module
```

**注意**: 生成後は必ず人間がレビュー

## パターン8: テスト駆動開発

```
1. テスト仕様を明確に指示
2. テストを先に作成させる
3. テストが通るまで実装を反復
4. 別インスタンスでレビュー
```

```
> Write a test for UserService.login that covers:
> - successful login
> - invalid password
> - locked account
> - rate limiting

[tests created]

> Implement the login method to pass these tests
```

## パターン9: 保護ファイルの設定

```json
// ~/.claude/settings.json
{
  "permissions": {
    "deny": [
      "Edit(.env*)",
      "Edit(**/secrets/**)",
      "Edit(package-lock.json)",
      "Read(.env*)"
    ]
  }
}
```

## パターン10: カスタムコマンドライブラリ

```
.claude/commands/
├── review.md        # /review
├── test.md          # /test
├── commit.md        # /commit
├── debug.md         # /debug
└── deploy-check.md  # /deploy-check
```

### /commit の例

```markdown
# .claude/commands/commit.md
---
description: diffを確認してコミット
---

1. git diffを表示
2. 変更内容を要約
3. コミットメッセージを提案
4. 承認後にコミット実行
```

## アンチパターン（避けるべき）

### 1. 丸投げ

```
悪い: 「このアプリを完成させて」
良い: 「ログイン機能のバリデーションを追加して」
```

### 2. 曖昧な指示

```
悪い: 「テストを書いて」
良い: 「UserService.loginの異常系テストを追加して」
```

### 3. コンテキスト過多

```
悪い: 長時間同じセッションを継続
良い: タスクごとに/clearでリセット
```

### 4. レビューなし実行

```
悪い: --dangerously-skip-permissions を常用
良い: 必要なパーミッションのみ事前許可
```

### 5. 情報の重複

```
悪い: CLAUDE.mdに全ての詳細を記載
良い: 「どこに何があるか」のガイドのみ
```
