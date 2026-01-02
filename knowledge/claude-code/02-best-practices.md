# Claude Code ベストプラクティス

## 核心原則

### 1. 探索 → 計画 → 実装 → コミット

最も汎用性の高いワークフロー。段階を分けることで精度が向上する。

```
1. 探索: 関連ファイルを読み込ませ、現状を理解させる（コードを書かせない）
2. 計画: think/think hard/think harder で分析の深度を調整
3. 実装: 具体的な指示で実装
4. コミット: レビュー後にコミット
```

### 2. タスク分割と段階的レビュー

大規模な変更を一度に行わない。

```
悪い例: 「このアプリ全体をリファクタリングして」
良い例: 「この関数のエラーハンドリングを改善して」
更に良い: 「UserService.loginのnull checkを追加して」
```

人間がレビューできる単位で分割し、「指示 → レビュー → コミット」を繰り返す。

### 3. 具体的な指示

曖昧な指示は精度を下げる。

```
悪い例: add tests for foo.py
良い例: write tests covering edge case where user is logged out
更に良い: src/auth/login.tsのlogin関数に、パスワードが空文字列の場合のテストを追加して
```

期待値を明示するほど、1回目の試行での成功率が上がる。

### 4. CLAUDE.mdの活用

```markdown
# プロジェクト構造
- src/: ソースコード
- tests/: テスト

# コマンド
- `npm run test`: テスト実行
- `npm run build`: ビルド

# コード規約
- インデント: 2スペース
- 命名: camelCase
```

**ポイント**:
- 簡潔に保つ（冗長な情報は避ける）
- 「どこに何があるか」程度のガイドに留める
- 詳細はClaude Codeに自動探索させる
- `#`キーで情報を追加できる

### 5. テスト駆動開発（TDD）との相性

テストを先に書かせることで、明確な目標に向かって反復改善できる。

```
1. 期待する入出力を明確に指示
2. テストを先に作成させる
3. テストが通るまで実装を反復
4. 独立したサブエージェントでレビュー
```

## CLAUDE.md の階層構造

```
~/.claude/CLAUDE.md          # 個人・全プロジェクト
./CLAUDE.md                  # プロジェクト共有
./.claude/CLAUDE.md          # プロジェクト共有（別配置）
./CLAUDE.local.md            # 個人・このプロジェクトのみ
```

## パーミッション設定

`~/.claude/settings.json` で危険性の低い操作を事前承認:

```json
{
  "permissions": {
    "allow": [
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(npm run test:*)",
      "Bash(npm run build:*)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./secrets/**)"
    ]
  }
}
```

## コンテキスト管理

- `/clear`: 新しいタスク開始時に履歴クリア（トークン節約）
- `/compact`: 長い会話を圧縮（重要情報は保持）
- `Esc+Esc`: 過去の状態に巻き戻し

## Sources

- [Anthropic公式: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Zenn: Claude Code ベストプラクティス](https://zenn.dev/farstep/articles/claude-code-best-practices)
- [Qiita: Claude Code 個人的ベストプラクティス](https://qiita.com/sijiaoh/items/6aea2d31141e5c989bee)
