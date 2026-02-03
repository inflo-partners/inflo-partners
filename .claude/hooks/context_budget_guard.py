#!/usr/bin/env python3
"""
Context Budget Guard Hook
Monitors and enforces context window usage limits.

Thresholds:
- 60% usage: WARNING - recommend completing current task and checkpointing
- 85% usage: BLOCK - no new major operations allowed

Usage:
- Called to check if new operation should proceed
- Can be called with --status to see current estimate
- Can be called with --reset after session restart
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Configuration
WARN_THRESHOLD = 0.60  # 60% - warn and recommend checkpoint
BLOCK_THRESHOLD = 0.85  # 85% - block new operations
MAX_TOKENS = 200000  # Claude's context window

STATE_FILE = Path(__file__).parent / ".context_state.json"

# Token estimation (rough approximations)
TOKEN_ESTIMATES = {
    "file_read": 500,  # Average file read
    "file_read_large": 2000,  # Large file
    "agent_launch": 1000,  # Agent prompt + overhead
    "agent_result": 1500,  # Average agent result
    "skill_bible": 5000,  # Skill bible load
    "directive": 1000,  # Directive load
    "message": 200,  # Average message
}


def load_state():
    """Load current context state."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {
        "estimated_tokens": 0,
        "operations": [],
        "session_start": datetime.now().isoformat()
    }


def save_state(state):
    """Save context state."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def add_operation(operation_type, description=""):
    """Track a new operation's token cost."""
    state = load_state()

    tokens = TOKEN_ESTIMATES.get(operation_type, 500)
    state["estimated_tokens"] += tokens
    state["operations"].append({
        "type": operation_type,
        "description": description,
        "tokens": tokens,
        "timestamp": datetime.now().isoformat()
    })

    save_state(state)
    return check_budget(state)


def check_budget(state=None):
    """Check current budget status."""
    if state is None:
        state = load_state()

    usage = state["estimated_tokens"] / MAX_TOKENS
    remaining = MAX_TOKENS - state["estimated_tokens"]

    if usage >= BLOCK_THRESHOLD:
        return {
            "status": "BLOCKED",
            "usage_percent": usage * 100,
            "estimated_tokens": state["estimated_tokens"],
            "remaining_tokens": remaining,
            "message": f"BLOCKED: Context at {usage*100:.1f}%. Complete current work and checkpoint before new operations."
        }
    elif usage >= WARN_THRESHOLD:
        return {
            "status": "WARNING",
            "usage_percent": usage * 100,
            "estimated_tokens": state["estimated_tokens"],
            "remaining_tokens": remaining,
            "message": f"WARNING: Context at {usage*100:.1f}%. Consider checkpointing soon."
        }
    else:
        return {
            "status": "OK",
            "usage_percent": usage * 100,
            "estimated_tokens": state["estimated_tokens"],
            "remaining_tokens": remaining,
            "message": f"OK: Context at {usage*100:.1f}%. {remaining:,} tokens remaining."
        }


def get_status():
    """Get detailed status report."""
    state = load_state()
    budget = check_budget(state)

    report = f"""
Context Budget Status
=====================
Status: {budget['status']}
Usage: {budget['usage_percent']:.1f}%
Estimated Tokens: {budget['estimated_tokens']:,}
Remaining: {budget['remaining_tokens']:,}
Session Start: {state['session_start']}

Recent Operations:
"""
    for op in state["operations"][-10:]:  # Last 10 operations
        report += f"  - {op['type']}: +{op['tokens']} tokens\n"

    return report


def reset():
    """Reset context tracking for new session."""
    save_state({
        "estimated_tokens": 0,
        "operations": [],
        "session_start": datetime.now().isoformat()
    })
    return "Context tracking reset for new session."


def can_proceed(operation_type):
    """Check if an operation should proceed."""
    state = load_state()

    # Estimate what usage would be after this operation
    tokens = TOKEN_ESTIMATES.get(operation_type, 500)
    projected_usage = (state["estimated_tokens"] + tokens) / MAX_TOKENS

    if projected_usage >= BLOCK_THRESHOLD:
        return False, f"BLOCKED: This operation would push context to {projected_usage*100:.1f}%"

    return True, "OK"


def main():
    if len(sys.argv) < 2:
        print("Usage: context_budget_guard.py [--status|--reset|--add <type> [desc]|--check <type>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--status":
        print(get_status())

    elif command == "--reset":
        print(reset())

    elif command == "--add":
        if len(sys.argv) < 3:
            print("Usage: context_budget_guard.py --add <operation_type> [description]")
            sys.exit(1)
        op_type = sys.argv[2]
        description = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        result = add_operation(op_type, description)
        print(result["message"])
        if result["status"] == "BLOCKED":
            sys.exit(1)

    elif command == "--check":
        if len(sys.argv) < 3:
            print("Usage: context_budget_guard.py --check <operation_type>")
            sys.exit(1)
        op_type = sys.argv[2]
        can_do, message = can_proceed(op_type)
        print(message)
        sys.exit(0 if can_do else 1)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
