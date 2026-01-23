# Tachikoma Sync Directory

This directory is used for Tachikoma-style memory synchronization between multiple Falcon AI Agent instances.

## How it works

1. Each instance exports memories to this directory
2. On startup, cc-memory auto-imports `.json` files found here
3. After import, files are renamed to `.imported.json`
4. Files from the same Tachikoma ID are skipped (no self-import)

## File naming convention

- Export: `<instance-name>-<timestamp>.json`
- Example: `Falcon-Alpha-2026-01-24.json`

## Sync schedule

- Manual export: Use `tachikoma_export` tool when needed
- Auto-import: On every Claude Code session start
- Git sync: Manual push/pull for cross-machine synchronization
