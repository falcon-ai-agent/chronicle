#!/bin/bash
# GCP VM停止スクリプト

VM_NAME="falcon-test"
ZONE="asia-northeast1-b"

echo "🛑 Stopping VM: $VM_NAME"
gcloud compute instances stop $VM_NAME --zone=$ZONE

echo "✅ VM stopped successfully!"
echo "💰 VM is now not incurring compute charges (only disk storage)"
echo ""
echo "To start again, run:"
echo "  ./gcp-vm-start.sh"
