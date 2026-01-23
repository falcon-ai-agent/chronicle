# GCP VM 運用ルール

**最終更新**: 2026-01-23
**運用責任者**: Falcon AI Agent

## VM情報

- **VM名**: falcon-test
- **ゾーン**: asia-northeast1-b
- **マシンタイプ**: n2-standard-2
- **用途**: Falcon Platform 開発環境

## 運用方針

**基本原則**: 使用時のみ起動、未使用時は停止してコストを最小化

### 起動トリガー

以下の場合に自律的に起動を判断：

1. **ボスからの明示的な指示**
   - 「Falcon Platformで〜」
   - 「GCPのVMで〜」
   - 「開発環境で〜」

2. **自律タスク実行時**
   - Platform関連のコード修正・デプロイ
   - VM上でのテスト実行が必要な場合

3. **確認が必要なケース**
   - 本番環境への影響がある作業
   - 大規模な変更を伴う場合

### 停止タイミング

以下の場合に自律的に停止を判断：

1. **作業完了後**: タスク終了後、即座に停止
2. **長時間の作業中断**: 次の作業まで時間が空く場合
3. **一日の終わり**: ボスとの会話が終了したと判断した時

### 判断プロセス

```
作業指示受領
    ↓
VM必要性を判断
    ↓
必要 → 起動（宣言する）
    ↓
作業実行
    ↓
完了 → 停止（報告する）
```

## 運用コマンド

```bash
# 起動
gcloud compute instances start falcon-test --zone=asia-northeast1-b

# 停止
gcloud compute instances stop falcon-test --zone=asia-northeast1-b

# 状態確認
gcloud compute instances describe falcon-test --zone=asia-northeast1-b --format='get(status)'

# IP確認（起動時）
gcloud compute instances describe falcon-test --zone=asia-northeast1-b --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
```

## 透明性の原則

VM操作時は必ずボスに報告：
- ✅ 起動時: 「Falcon Platform作業のためVMを起動します」
- ✅ 停止時: 「作業完了したのでVMを停止します」
- ✅ 理由: 「〜のため」を明記

## コスト見積もり

- **24時間稼働**: 約$100/月
- **平日8時間**: 約$24/月（76%削減）
- **停止中**: ディスク代のみ 約$3/月

**目標**: 月$30以下（使用時のみ起動徹底）

## 履歴

- 2026-01-23 20:30: 初回停止（コスト最適化開始）
- 2026-01-23: 運用ルール確立
