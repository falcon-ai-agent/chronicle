#!/bin/bash
# Tachikoma-style Memory Sync
# タチコマの並列化と記憶共有 - Git経由で複数インスタンス間で記憶を同期

set -e

# スクリプトのディレクトリからchronicleルートを特定
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CHRONICLE_DIR="$(dirname "$SCRIPT_DIR")"
MEMORY_FILE="memory/shared.json"
LOG_FILE="$CHRONICLE_DIR/tools/memory_sync.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

cd "$CHRONICLE_DIR"

# 1. Pull latest (他のインスタンスの記憶を取得)
log "Pulling latest memories from remote..."
git pull --rebase origin main 2>&1 | head -5 >> "$LOG_FILE"

# 2. Check for local changes (自分の新しい記憶)
if git diff --quiet "$MEMORY_FILE" 2>/dev/null; then
    log "No new memories to sync"
else
    log "New memories detected, syncing..."

    # 3. Commit local changes
    git add "$MEMORY_FILE"
    git commit -m "🧠 Memory sync: $(date '+%Y-%m-%d %H:%M')

Tachikoma parallel memory update
" 2>&1 | head -3 >> "$LOG_FILE"

    # 4. Push to remote (他のインスタンスと共有)
    git push origin main 2>&1 | head -3 >> "$LOG_FILE"

    log "Memory sync complete"
fi

log "---"
