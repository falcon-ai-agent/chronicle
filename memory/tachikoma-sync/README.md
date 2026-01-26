# Tachikoma Sync (DEPRECATED)

**重要**: cc-memoryの同期は **privateリポジトリ** で行います。

## 理由

cc-memoryのエクスポートには認証情報（SSHパスワード、APIキー）が含まれるため、
publicリポジトリ（chronicle）には同期できません。

## 同期先

- リポジトリ: `falcon-ai-agent/memory-sync` (PRIVATE)
- パス: `/Users/falcon/projects/memory-sync/`

## 使い方

```bash
# エクスポート
cd /Users/falcon/projects/memory-sync
# tachikoma_export(output_path="/Users/falcon/projects/memory-sync/tachikoma-export.json")
git add -A && git commit -m "Sync memory $(date +%Y-%m-%d)" && git push
```
