#!/usr/bin/env python3
"""
Agent Limiter Hook
Enforces maximum number of concurrent sub-agents to prevent session crashes.

Usage:
- Pre-hook: Checks if launching new agent would exceed limit
- Can be called with --status to check current state
- Can be called with --reset to clear tracked agents
"""

import json
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
MAX_AGENTS = 3
STATE_FILE = Path(__file__).parent / ".agent_state.json"
AGENT_TIMEOUT_MINUTES = 30  # Consider agent dead if no update for this long


def load_state():
    """Load current agent state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"agents": [], "last_updated": None}
    return {"agents": [], "last_updated": None}


def save_state(state):
    """Save agent state to file."""
    state["last_updated"] = datetime.now().isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def cleanup_stale_agents(state):
    """Remove agents that have timed out."""
    cutoff = datetime.now() - timedelta(minutes=AGENT_TIMEOUT_MINUTES)
    active_agents = []

    for agent in state.get("agents", []):
        agent_time = datetime.fromisoformat(agent["started"])
        if agent_time > cutoff:
            active_agents.append(agent)

    state["agents"] = active_agents
    return state


def register_agent(agent_id, description):
    """Register a new agent as running."""
    state = load_state()
    state = cleanup_stale_agents(state)

    # Check limit
    if len(state["agents"]) >= MAX_AGENTS:
        return False, f"BLOCKED: Cannot launch agent. {len(state['agents'])}/{MAX_AGENTS} agents already running."

    # Register new agent
    state["agents"].append({
        "id": agent_id,
        "description": description,
        "started": datetime.now().isoformat()
    })

    save_state(state)
    return True, f"Agent registered. {len(state['agents'])}/{MAX_AGENTS} agents running."


def complete_agent(agent_id):
    """Mark an agent as completed."""
    state = load_state()
    state["agents"] = [a for a in state["agents"] if a.get("id") != agent_id]
    save_state(state)
    return True, f"Agent completed. {len(state['agents'])}/{MAX_AGENTS} agents running."


def get_status():
    """Get current agent status."""
    state = load_state()
    state = cleanup_stale_agents(state)
    save_state(state)

    status = f"Active agents: {len(state['agents'])}/{MAX_AGENTS}\n"
    for agent in state["agents"]:
        status += f"  - {agent['id']}: {agent['description']} (started: {agent['started']})\n"

    return status


def reset():
    """Reset all agent tracking."""
    save_state({"agents": [], "last_updated": None})
    return "Agent tracking reset."


def main():
    if len(sys.argv) < 2:
        print("Usage: agent_limiter.py [--status|--reset|--register <id> <desc>|--complete <id>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--status":
        print(get_status())

    elif command == "--reset":
        print(reset())

    elif command == "--register":
        if len(sys.argv) < 4:
            print("Usage: agent_limiter.py --register <agent_id> <description>")
            sys.exit(1)
        agent_id = sys.argv[2]
        description = " ".join(sys.argv[3:])
        success, message = register_agent(agent_id, description)
        print(message)
        sys.exit(0 if success else 1)

    elif command == "--complete":
        if len(sys.argv) < 3:
            print("Usage: agent_limiter.py --complete <agent_id>")
            sys.exit(1)
        agent_id = sys.argv[2]
        success, message = complete_agent(agent_id)
        print(message)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
