#!/bin/bash
# GCP VM起動スクリプト

VM_NAME="falcon-test"
ZONE="asia-northeast1-b"

echo "🚀 Starting VM: $VM_NAME"
gcloud compute instances start $VM_NAME --zone=$ZONE

echo "⏳ Waiting for VM to be ready..."
sleep 10

# 外部IPを取得して表示
IP=$(gcloud compute instances describe $VM_NAME --zone=$ZONE --format='get(networkInterfaces[0].accessConfigs[0].natIP)')
echo "✅ VM started successfully!"
echo "📍 External IP: $IP"
echo ""
echo "To connect:"
echo "  ssh falcon-ai-agent@$IP"
