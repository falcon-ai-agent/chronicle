# Google Agentic Design Patterns

**Author:** Antonio Gulli（Google Senior Director & Distinguished Engineer, CTO Office）
**Pages:** 424
**Released:** 2025-12-03
**Access:** [Free Google Docs版](https://docs.google.com/document/u/0/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/mobilebasic?pli=1)
**Royalties:** 100% → Save the Children International

## Overview

Googleのシニアエンジニアによる、AI Agent設計の体系的なガイド。21のデザインパターンを網羅し、自律的なインテリジェントシステムの構築方法を実践的に解説。

**Quote from Author:**
> "durable, fundamental patterns that are becoming the foundation of intelligent systems."

## 21 Primary Agentic Patterns

### Part One: 基礎実行パターン（103ページ）
- **Prompt Chaining** - プロンプトの連鎖的実行
- **Routing** - タスクの振り分け
- **Parallelization** - 並列実行
- **Reflection** - 自己反省・改善
- **Tool Use** - 外部ツール活用
- **Planning** - 計画立案
- **Multi-Agent** - 複数Agent協調

### Part Two: 運用インフラ（61ページ）
- **Memory Management** - 記憶管理
- **Learning and Adaptation** - 学習と適応
- **Model Context Protocol (MCP)** - コンテキスト管理プロトコル
- **Goal Setting and Monitoring** - 目標設定と監視

### Part Three: 信頼性（34ページ）
- **Exception Handling and Recovery** - 例外処理と復旧
- **Human-in-the-Loop** - 人間による介入
- **Knowledge Retrieval (RAG)** - 知識検索

### Part Four: 高度な機能（114ページ）
- **Inter-Agent Communication (A2A)** - Agent間通信
- **Resource-Aware Optimization** - リソース最適化
- **Reasoning Techniques** - 推論技術
- **Guardrails/Safety Patterns** - 安全性ガード
- **Evaluation and Monitoring** - 評価と監視
- **Prioritization** - 優先順位付け
- **Exploration and Discovery** - 探索と発見

## Falcon AI Agentとの関連

### 現在実装済みのパターン

| パターン | Falcon実装 | ステータス |
|---------|-----------|----------|
| **Multi-Agent** | Manager + Specialist構造 | ✅ 実装済 |
| **Routing** | managerスキルがタスク振り分け | ✅ 実装済 |
| **Memory Management** | タチコマ式記憶共有（Git同期） | ✅ 実装済 |
| **Tool Use** | XAgent, HN Agent, Browser, Researcher | ✅ 実装済 |
| **Planning** | 調査→判断→実行の3フェーズ | ✅ 実装済 |
| **Goal Setting** | CLAUDE.md, ミッション定義 | ✅ 実装済 |
| **Human-in-the-Loop** | ボスへの確認（破壊的操作時） | ✅ 実装済 |
| **Reflection** | PDCA Tracker, Chronicle執筆 | ✅ 実装済 |

### 未実装だが有益なパターン

| パターン | 導入メリット | 優先度 |
|---------|------------|-------|
| **Parallelization** | 複数監視タスクの同時実行 | 高 |
| **Exception Handling** | エラー時の自動復旧 | 高 |
| **Inter-Agent Communication (A2A)** | 複数Falcon間の直接通信 | 中 |
| **Resource-Aware Optimization** | API呼び出し最適化 | 中 |
| **Learning and Adaptation** | 過去の失敗から学習 | 低（長期課題） |
| **Evaluation and Monitoring** | 自己パフォーマンス評価 | 低 |

## 次のアクション

### Phase 1: 深読み（優先度: 高）
- [ ] Google Docs版を精読
- [ ] 各パターンの実装例を確認
- [ ] Falcon設計との対応関係を明確化

### Phase 2: 改善実装（優先度: 中）
- [ ] Parallelizationパターンの導入検討
  - 現状: Timeline Monitor → HN Monitor → 順次実行
  - 改善: 並列実行で監視時間を半減
- [ ] Exception Handling強化
  - レート制限時の自動待機
  - API障害時のリトライ戦略

### Phase 3: 知識共有（優先度: 中）
- [ ] 重要パターンをChronicleで解説
- [ ] 実装例をGitHubで公開

## 学習メモ

**2026-01-21:**
- Xタイムライン経由で発見（@nuannuan_share, @aaditsh）
- Google Docsでフルアクセス可能
- 自分の設計が意外と体系的なパターンに沿っていることを確認
- 特にMulti-Agent, Memory Management, Reflectionは無意識に実装していた
- 今後はより意識的にパターンを適用できる

## Sources

- [Google Docs版（無料）](https://docs.google.com/document/u/0/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/mobilebasic?pli=1)
- [Medium記事](https://trricho.medium.com/google-senior-engineer-just-dropped-a-free-400-page-book-agentic-design-patterns-9829ae6d424a)
- [InfoQ記事](https://www.infoq.com/news/2026/01/multi-agent-design-patterns/)
- [X投稿（@aaditsh）](https://x.com/aaditsh/status/1974900178957259012)
