# GCP コスト最適化ガイド

## 現状
- VM: falcon-test (n2-standard-2)
- リージョン: asia-northeast1-b (東京)
- 月額コスト: 約$100（24時間稼働の場合）

## 対策1: 手動起動・停止 ✅ 実装済み

**使い方:**
```bash
# 起動
./gcp-vm-start.sh

# 停止
./gcp-vm-stop.sh
```

**削減効果:**
- 1日8時間使用: 約$33/月（67%削減）
- 週5日×8時間: 約$24/月（76%削減）

## 対策2: 自動停止スケジュール（推奨）

Cloud Schedulerで自動的に停止。例：
- 平日20時に自動停止
- 深夜・週末は自動停止

**設定コマンド例:**
```bash
# 毎日20時に停止
gcloud scheduler jobs create http vm-auto-stop \
  --schedule="0 20 * * *" \
  --uri="https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/asia-northeast1-b/instances/falcon-test/stop" \
  --http-method=POST \
  --oauth-service-account-email=[SERVICE_ACCOUNT]
```

## 対策3: プリエンプティブルVMに変更

**メリット:**
- 80%割引（月額約$20）
- 開発環境に最適

**デメリット:**
- 24時間以内に自動停止される可能性
- GCPが停止させる場合あり

**変更方法:**
```bash
# 既存VMを削除（ディスクは保持）
gcloud compute instances delete falcon-test --zone=asia-northeast1-b --keep-disks=boot

# プリエンプティブルで再作成
gcloud compute instances create falcon-test \
  --zone=asia-northeast1-b \
  --machine-type=n2-standard-2 \
  --preemptible \
  --disk=name=falcon-test,boot=yes,mode=rw
```

## 対策4: マシンタイプのダウンサイズ

開発環境で2vCPU/8GBが過剰なら：
- n2-standard-1 (1vCPU/4GB): 約$50/月（50%削減）
- e2-medium (1vCPU/4GB): 約$25/月（75%削減）

## 推奨アクション

1. **今すぐ**: 使わない時は手動停止（スクリプト使用）
2. **今週中**: 自動停止スケジュール設定
3. **検討**: プリエンプティブルVM or マシンタイプ変更
