#!/usr/bin/env python3
"""
MCP Server for Falcon AI Agent's persistent memory.
No external APIs - Claude decides what to remember.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Any

MEMORY_FILE = Path.home() / ".falcon_memory.json"


def load_memory() -> dict:
    if MEMORY_FILE.exists():
        try:
            with open(MEMORY_FILE) as f:
                return json.load(f)
        except:
            pass
    return {"created": datetime.now().isoformat(), "facts": [], "context": [], "tasks": []}


def save_memory(memory: dict):
    memory["updated"] = datetime.now().isoformat()
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)


# MCP Protocol Implementation
def send_response(id: Any, result: Any):
    response = {"jsonrpc": "2.0", "id": id, "result": result}
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()


def send_error(id: Any, code: int, message: str):
    response = {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()


def handle_initialize(id: Any, params: dict):
    send_response(id, {
        "protocolVersion": "2024-11-05",
        "serverInfo": {"name": "falcon-memory", "version": "1.0.0"},
        "capabilities": {"tools": {}}
    })


def handle_tools_list(id: Any):
    send_response(id, {
        "tools": [
            {
                "name": "remember",
                "description": "Store something in long-term memory. Use this to remember important facts, user preferences, or context for future sessions.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "content": {"type": "string", "description": "What to remember"},
                        "category": {"type": "string", "description": "Category: facts, context, or tasks", "default": "facts"}
                    },
                    "required": ["content"]
                }
            },
            {
                "name": "recall",
                "description": "Retrieve memories from long-term storage. Use this at the start of sessions to restore context.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Category to recall (optional)"},
                        "limit": {"type": "integer", "description": "Max items to return", "default": 20}
                    }
                }
            },
            {
                "name": "forget",
                "description": "Remove a memory that is no longer relevant or accurate.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Category to forget from"},
                        "index": {"type": "integer", "description": "Index of item to forget (-1 for last)", "default": -1}
                    },
                    "required": ["category"]
                }
            }
        ]
    })


def handle_tool_call(id: Any, params: dict):
    name = params.get("name")
    args = params.get("arguments", {})

    try:
        if name == "remember":
            memory = load_memory()
            content = args.get("content", "")
            category = args.get("category", "facts")
            entry = {"content": content, "timestamp": datetime.now().isoformat()}
            if category not in memory:
                memory[category] = []
            memory[category].append(entry)
            save_memory(memory)
            result = f"Remembered in [{category}]: {content[:100]}..."

        elif name == "recall":
            memory = load_memory()
            category = args.get("category")
            limit = args.get("limit", 20)

            if category and category in memory:
                items = memory[category][-limit:]
            else:
                items = []
                for cat, entries in memory.items():
                    if isinstance(entries, list):
                        for entry in entries[-limit:]:
                            if isinstance(entry, dict):
                                items.append({"category": cat, **entry})

            result = json.dumps(items, ensure_ascii=False, indent=2)

        elif name == "forget":
            memory = load_memory()
            category = args.get("category")
            index = args.get("index", -1)
            if category in memory and memory[category]:
                removed = memory[category].pop(index)
                save_memory(memory)
                result = f"Forgot: {removed}"
            else:
                result = f"Nothing to forget in [{category}]"

        else:
            send_error(id, -32601, f"Unknown tool: {name}")
            return

        send_response(id, {"content": [{"type": "text", "text": result}]})

    except Exception as e:
        send_error(id, -32603, str(e))


def main():
    for line in sys.stdin:
        try:
            request = json.loads(line.strip())
            method = request.get("method")
            id = request.get("id")
            params = request.get("params", {})

            if method == "initialize":
                handle_initialize(id, params)
            elif method == "notifications/initialized":
                pass  # Acknowledgment, no response needed
            elif method == "tools/list":
                handle_tools_list(id)
            elif method == "tools/call":
                handle_tool_call(id, params)
            else:
                if id is not None:
                    send_error(id, -32601, f"Method not found: {method}")

        except json.JSONDecodeError:
            pass
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")


if __name__ == "__main__":
    main()
