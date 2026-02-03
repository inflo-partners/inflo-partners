#!/usr/bin/env python3
"""
Approval Token System
Manages approval tokens for critical decisions.

Usage:
    # Grant approval
    python approve.py "Client_Name" strategy

    # Check approval
    python approve.py --check "Client_Name" strategy

    # List approvals
    python approve.py --list "Client_Name"

    # Revoke approval
    python approve.py --revoke "Client_Name" strategy
"""

import argparse
import json
import os
import sys
import hashlib
import hmac
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
CLIENTS_DIR = BASE_DIR / "context" / "clients"

# Secret for HMAC (in production, load from environment)
SECRET_KEY = os.environ.get("APPROVAL_SECRET", "agency-approval-secret-key")

# Valid approval types
APPROVAL_TYPES = [
    "strategy",      # Strategy/angle selection
    "offer",         # Offer structure approval
    "delivery",      # Final delivery to client
    "pricing",       # Pricing recommendations
    "scope_change",  # Scope modifications
]


def get_approval_file(client_name):
    """Get path to client's approval file."""
    client_dir = CLIENTS_DIR / client_name.replace(" ", "_")
    return client_dir / ".approvals.json"


def load_approvals(client_name):
    """Load existing approvals for client."""
    approval_file = get_approval_file(client_name)

    if not approval_file.exists():
        return {}

    with open(approval_file, 'r') as f:
        return json.load(f)


def save_approvals(client_name, approvals):
    """Save approvals for client."""
    approval_file = get_approval_file(client_name)

    # Ensure client directory exists
    approval_file.parent.mkdir(parents=True, exist_ok=True)

    with open(approval_file, 'w') as f:
        json.dump(approvals, f, indent=2)


def generate_token(client_name, approval_type, timestamp):
    """Generate HMAC token for approval."""
    message = f"{client_name}:{approval_type}:{timestamp}"
    token = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()[:16]
    return token


def verify_token(client_name, approval_type, timestamp, token):
    """Verify an approval token."""
    expected_token = generate_token(client_name, approval_type, timestamp)
    return hmac.compare_digest(token, expected_token)


def grant_approval(client_name, approval_type, notes=""):
    """Grant approval for a decision type."""
    if approval_type not in APPROVAL_TYPES:
        return False, f"Invalid approval type. Valid types: {', '.join(APPROVAL_TYPES)}"

    approvals = load_approvals(client_name)
    timestamp = datetime.now().isoformat()
    token = generate_token(client_name, approval_type, timestamp)

    approvals[approval_type] = {
        "approved": True,
        "timestamp": timestamp,
        "token": token,
        "notes": notes
    }

    save_approvals(client_name, approvals)

    return True, f"Approval granted: {approval_type} for {client_name}\nToken: {token}"


def check_approval(client_name, approval_type):
    """Check if approval exists and is valid."""
    approvals = load_approvals(client_name)

    if approval_type not in approvals:
        return False, f"No approval found for: {approval_type}"

    approval = approvals[approval_type]

    if not approval.get("approved"):
        return False, f"Approval revoked for: {approval_type}"

    # Verify token integrity
    is_valid = verify_token(
        client_name,
        approval_type,
        approval["timestamp"],
        approval["token"]
    )

    if not is_valid:
        return False, "Approval token invalid - possible tampering"

    return True, f"Approval valid: {approval_type} (granted: {approval['timestamp']})"


def revoke_approval(client_name, approval_type):
    """Revoke an existing approval."""
    approvals = load_approvals(client_name)

    if approval_type not in approvals:
        return False, f"No approval to revoke for: {approval_type}"

    approvals[approval_type]["approved"] = False
    approvals[approval_type]["revoked_at"] = datetime.now().isoformat()

    save_approvals(client_name, approvals)

    return True, f"Approval revoked: {approval_type}"


def list_approvals(client_name):
    """List all approvals for a client."""
    approvals = load_approvals(client_name)

    if not approvals:
        return f"No approvals found for: {client_name}"

    output = [f"Approvals for {client_name}:", ""]

    for approval_type, data in approvals.items():
        status = "✓ APPROVED" if data.get("approved") else "✗ REVOKED"
        timestamp = data.get("timestamp", "unknown")
        notes = data.get("notes", "")

        output.append(f"  {approval_type}: {status}")
        output.append(f"    Timestamp: {timestamp}")
        if notes:
            output.append(f"    Notes: {notes}")
        output.append("")

    return "\n".join(output)


def require_approval_hmac(client_name, approval_type):
    """
    Function for Claude to call to verify approval before proceeding.
    Returns tuple: (approved: bool, message: str)
    """
    return check_approval(client_name, approval_type)


def main():
    parser = argparse.ArgumentParser(description="Manage approval tokens")
    parser.add_argument("client", help="Client name")
    parser.add_argument("approval_type", nargs="?", help="Type of approval")
    parser.add_argument("--check", action="store_true", help="Check if approval exists")
    parser.add_argument("--list", action="store_true", help="List all approvals")
    parser.add_argument("--revoke", action="store_true", help="Revoke approval")
    parser.add_argument("--notes", default="", help="Notes for approval")

    args = parser.parse_args()

    if args.list:
        print(list_approvals(args.client))
        sys.exit(0)

    if not args.approval_type:
        print("Error: approval_type required (unless using --list)")
        print(f"Valid types: {', '.join(APPROVAL_TYPES)}")
        sys.exit(1)

    if args.check:
        valid, message = check_approval(args.client, args.approval_type)
        print(message)
        sys.exit(0 if valid else 1)

    elif args.revoke:
        success, message = revoke_approval(args.client, args.approval_type)
        print(message)
        sys.exit(0 if success else 1)

    else:
        # Grant approval
        success, message = grant_approval(args.client, args.approval_type, args.notes)
        print(message)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
