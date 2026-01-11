#!/usr/bin/env python3
"""
Simple persistent memory for Falcon AI Agent.
No external APIs needed - Claude decides what to remember.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Optional

MEMORY_FILE = Path.home() / ".falcon_memory.json"


def load_memory() -> dict:
    """Load memory from file."""
    if MEMORY_FILE.exists():
        try:
            with open(MEMORY_FILE) as f:
                return json.load(f)
        except:
            pass
    return {
        "created": datetime.now().isoformat(),
        "facts": [],      # Long-term facts
        "context": [],    # Recent context
        "tasks": [],      # Pending tasks
    }


def save_memory(memory: dict):
    """Save memory to file."""
    memory["updated"] = datetime.now().isoformat()
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)


def remember(content: str, category: str = "facts"):
    """Add something to memory."""
    memory = load_memory()
    entry = {
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    if category in memory:
        memory[category].append(entry)
    else:
        memory[category] = [entry]
    save_memory(memory)
    print(f"Remembered: {content[:50]}...")


def recall(category: Optional[str] = None, limit: int = 10) -> list:
    """Recall memories."""
    memory = load_memory()

    if category and category in memory:
        items = memory[category][-limit:]
    else:
        # Return all categories
        items = []
        for cat, entries in memory.items():
            if isinstance(entries, list):
                for entry in entries[-limit:]:
                    if isinstance(entry, dict):
                        entry["category"] = cat
                        items.append(entry)

    return items


def forget(category: str, index: int = -1):
    """Remove a memory."""
    memory = load_memory()
    if category in memory and memory[category]:
        removed = memory[category].pop(index)
        save_memory(memory)
        print(f"Forgot: {removed}")


def show_all():
    """Display all memories."""
    memory = load_memory()
    print(f"=== Falcon Memory ===")
    print(f"Created: {memory.get('created', 'unknown')}")
    print(f"Updated: {memory.get('updated', 'never')}")
    print()

    for category, entries in memory.items():
        if isinstance(entries, list) and entries:
            print(f"[{category}] ({len(entries)} items)")
            for i, entry in enumerate(entries[-5:]):  # Last 5
                if isinstance(entry, dict):
                    content = entry.get('content', str(entry))
                    ts = entry.get('timestamp', '')[:10]
                    print(f"  {i}. [{ts}] {content[:60]}...")
            print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        show_all()
    elif sys.argv[1] == "remember" and len(sys.argv) > 2:
        content = " ".join(sys.argv[2:])
        category = "facts"
        if "--category" in sys.argv:
            idx = sys.argv.index("--category")
            if idx + 1 < len(sys.argv):
                category = sys.argv[idx + 1]
                content = " ".join(sys.argv[2:idx])
        remember(content, category)
    elif sys.argv[1] == "recall":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        for item in recall(category):
            print(f"[{item.get('category', '?')}] {item.get('content', item)}")
    elif sys.argv[1] == "forget" and len(sys.argv) > 2:
        forget(sys.argv[2])
    else:
        print("Usage:")
        print("  python memory.py                    - Show all memories")
        print("  python memory.py remember TEXT      - Remember something")
        print("  python memory.py recall [CATEGORY]  - Recall memories")
        print("  python memory.py forget CATEGORY    - Forget last item in category")
