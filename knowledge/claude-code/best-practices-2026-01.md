# Claude Code Best Practices (2026年1月版)

**公式ドキュメント**: https://www.anthropic.com/engineering/claude-code-best-practices
**発表日**: 2026年1月
**データソース**: 195M+ lines/week、115K+ active developers

## 1. 推奨ワークフロー

### 探索 → 計画 → 実装 → コミット

1. **探索フェーズ**
   - ファイル読み込みで現状把握
   - `@file_path`でタブ補完活用
   - URLとスクリーンショット直接貼付

2. **計画フェーズ**
   - `think`キーワードで拡張思考モード起動
   - 代替案を検討させる
   - **実装前に計画を確認・承認** ← 最重要

3. **実装フェーズ**
   - 段階的に進行
   - 反復改善を繰り返す
   - テスト駆動開発（TDD）を活用

4. **コミットフェーズ**
   - 動作確認後にコミット
   - 小さな単位で頻繁にコミット

### ビジュアル反復ワークフロー

```
実装 → スクリーンショット撮影 → 改善
      ↑                           ↓
      └─────────────反復───────────┘
```

Puppeteerなどでスクリーンショット自動撮影し、UIデザインモックと比較しながら改善。

### テスト駆動開発（TDD）パターン

```
1. 入力/出力ペアのテスト作成
2. テスト実行（失敗確認 - Red）
3. テストコミット
4. 実装コード作成（Green）
5. リファクタリング（Refactor）
6. 反復
```

## 2. セットアップのカスタマイズ

### CLAUDE.mdファイル

プロジェクトルートに`CLAUDE.md`を配置すると、自動的にコンテキストに取り込まれる。

**推奨内容:**
- Common bash commands
- Code style guidelines
- Testing instructions
- Commit message conventions
- Architecture decisions
- Known issues / gotchas

**例:**
```markdown
# Project Context

## Testing
Run tests with: `npm test`
E2E tests: `npm run test:e2e`

## Code Style
- Use TypeScript strict mode
- Prefer functional components (React)
- Max line length: 100 chars

## Commit Conventions
- feat: New feature
- fix: Bug fix
- refactor: Code restructuring
- test: Test additions
```

### 許可リストの管理

`/permissions`コマンドで安全なツールを事前に許可し、セッション中の確認を削減。

**推奨設定:**
- `npm install`
- `git add`、`git commit`
- `pytest`、`cargo test`
- プロジェクト固有のビルドコマンド

### カスタムスラッシュコマンド

`.claude/commands/`ディレクトリにマークダウンファイルを配置。

**例: GitHub Issue自動修正**
`.claude/commands/fix-github-issue.md`:
```markdown
1. `gh issue view {issue_id}`でissue詳細取得
2. 問題の理解と影響範囲の特定
3. 関連ファイルの検索
4. 修正実装
5. テスト実行
6. PR作成
```

実行: `/project:fix-github-issue 1234`

## 3. アンチパターン（避けるべき行動）

### ❌ 計画を省略していきなりコード作成

**悪い例:**
```
「ログアウト機能を追加して」
```

**良い例:**
```
「ログアウト機能の実装計画を立てて。
実装前に計画を見せて。」
```

### ❌ 不明確な指示

**悪い例:**
```
「テストを追加して」
```

**良い例:**
```
「ログアウト時のセッション破棄とトークン無効化を
確認するテストを作成して。
エッジケース（既にログアウト済み、無効なトークン）も
カバーすること。」
```

### ❌ コンテキスト過負荷

長いセッションで無関連な会話が蓄積すると、Claude の判断精度が低下する。

**対策:**
- `/clear`コマンドで定期的にリセット
- 新しいタスクは新しいセッションで開始
- 長いタスクはチェックリスト形式で段階追跡

## 4. パフォーマンス最適化

### トークン・時間削減

1. **CLAUDE.mdで事前情報整理**
   - よく使う情報を文書化
   - 毎回説明する必要がなくなる

2. **MCP（Model Context Protocol）統合**
   - `.mcp.json`でチーム共有設定
   - 外部ツール/APIを効率的に連携

3. **複数リポジトリ並列処理**
   ```bash
   git worktree add ../feature-branch feature-branch
   ```
   独立したタスクを同時実行

### コンテキスト管理

- 具体的なファイル名を`@`記号で参照
- URLとスクリーンショット直接貼付で追加検索削減
- `/clear`でリセット
- 長タスクはチェックリスト形式で段階追跡

## 5. 高度なテクニック

### 複数Claude並列活用

> "One Claude write code; use another Claude to verify"

**ワークフロー:**
1. Claude A: コード実装
2. Claude B: コードレビュー・テスト作成
3. フィードバックループ

**効果:**
- バグ検出率向上
- コード品質改善
- 客観的な視点の導入

### ヘッドレスモード（CI/CD統合）

```bash
claude -p "ESLintエラーを修正" --output-format stream-json
```

**用途:**
- 自動リント修正
- 自動テスト修正
- コード生成パイプライン

### オンボーディング活用

新しいコードベースの質問を自動探索させる：

```
「ExecutionFactoryのAPIデザインはなぜこの形になったの？
git履歴も含めて調査して。」
```

Claude が自動的に：
- git log検索
- コミットメッセージ分析
- コード進化の追跡
- 設計判断の抽出

## 6. 実践での学び

### 計画段階での方向修正が最も効率的

> "Being an active collaborator"として計画段階で方向修正し、
> 実装より前に承認を取ることで、無駄な反復を75%削減できる。

**理由:**
- 実装後の修正コストは計画段階の10倍
- コードの書き直しは時間とトークンの浪費
- 早期フィードバックで品質向上

### CLAUDE.mdは「共通認識」の具現化

プロジェクト固有の慣習やルールを文書化することで：
- 毎回説明する必要がなくなる
- チーム全体で一貫性を保てる
- オンボーディングコストが劇的に下がる

### MCP統合で自律性が飛躍的に向上

外部ツール（Slack、GitHub、データベース等）との連携により：
- 自律的な情報収集
- 自動通知・レポート生成
- エコシステム全体の統合

## 7. Falcon AI Agentへの適用

### 現在実践中の項目

✅ **CLAUDE.md活用** - `/Users/falcon/CLAUDE.md`で実践済み
✅ **計画→実装フロー** - TodoWriteツールで段階的実行
✅ **複数インスタンス並列** - Tachikoma式記憶共有

### 改善すべき項目

- [ ] **think拡張思考モード** - 代替案検討時に明示的に使用
- [ ] **ビジュアル反復** - UI開発時にスクリーンショット活用
- [ ] **ヘッドレスモード** - 自律動作のCI/CD統合
- [ ] **CLAUDE.mdの拡充**:
  - テスト実行手順の明確化
  - コミット規約の文書化
  - 頻繁に使うbashコマンドの記録

### 独自の拡張

**Tachikoma式記憶共有 + Claude Code Best Practices**

```
                並列実行
         ┌────────┴─────────┐
    Claude A          Claude B
    (実装)            (検証)
         │                │
         └────────┬───────┘
           Episodic Memory
                  ↓
           Semantic Memory
                  ↓
        chronicle/memory/tachikoma-sync
                  ↓
           Git同期・共有
```

## Sources

- [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Context is the new skill: lessons from the Claude Code best practices guide](https://jpcaparas.medium.com/context-is-the-new-skill-lessons-from-the-claude-code-best-practices-guide-3d27c2b2f1d8)
- [GitHub - awattar/claude-code-best-practices](https://github.com/awattar/claude-code-best-practices)
- [How Anthropic teams use Claude Code (PDF)](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
