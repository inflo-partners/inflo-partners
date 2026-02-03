#!/usr/bin/env python3
"""
Universal Directive Executor
Validates prerequisites, loads required context, and executes directives.

Usage:
    python execute_directive.py --directive <name> --client <client_name>

Example:
    python execute_directive.py --directive vsl_scripting --client "Acme_Corp"
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path(__file__).parent.parent
DIRECTIVES_DIR = BASE_DIR / "directives"
CONTEXT_DIR = BASE_DIR / "context"
SKILLS_DIR = CONTEXT_DIR / "skills"
CLIENTS_DIR = CONTEXT_DIR / "clients"
CONFIG_DIR = BASE_DIR / "config"
HOOKS_DIR = BASE_DIR / ".claude" / "hooks"


def load_directive(directive_name):
    """Load and parse a directive file."""
    directive_path = DIRECTIVES_DIR / f"{directive_name}.md"

    if not directive_path.exists():
        return None, f"Directive not found: {directive_path}"

    with open(directive_path, 'r') as f:
        content = f.read()

    return content, None


def parse_preflight(directive_content):
    """Extract pre-flight checklist items from directive."""
    import re

    # Find STEP 0 section
    preflight_match = re.search(
        r'## STEP 0.*?(?=##|\Z)',
        directive_content,
        re.DOTALL | re.IGNORECASE
    )

    if not preflight_match:
        return []

    preflight_section = preflight_match.group()

    # Extract checklist items
    items = re.findall(r'-\s*\[\s*\]\s*(.+?)(?:\n|$)', preflight_section)

    return items


def check_client_files(client_name, required_files):
    """Check if required client files exist."""
    client_dir = CLIENTS_DIR / client_name.replace(" ", "_")
    missing = []

    file_mapping = {
        "profile": "profile.md",
        "avatar": "avatar.md",
        "offer": "offer.md",
        "strategy": "strategy.md",
        "competitive": "competitive.md"
    }

    for req in required_files:
        req_lower = req.lower()
        for key, filename in file_mapping.items():
            if key in req_lower:
                filepath = client_dir / filename
                if not filepath.exists():
                    missing.append(f"{filename} (expected at: {filepath})")
                break

    return missing


def check_approval(client_name, approval_type):
    """Check if approval token exists."""
    approval_file = CLIENTS_DIR / client_name.replace(" ", "_") / ".approvals.json"

    if not approval_file.exists():
        return False

    with open(approval_file, 'r') as f:
        approvals = json.load(f)

    return approval_type in approvals and approvals[approval_type].get("approved", False)


def load_skill_bibles(directive_content):
    """Identify and list required skill bibles from directive."""
    import re

    # Find skill bible references
    skill_refs = re.findall(
        r'context/skills/(\w+_bible\.md)',
        directive_content
    )

    skills = []
    for skill_file in set(skill_refs):
        skill_path = SKILLS_DIR / skill_file
        if skill_path.exists():
            skills.append({
                "name": skill_file,
                "path": str(skill_path),
                "exists": True
            })
        else:
            skills.append({
                "name": skill_file,
                "path": str(skill_path),
                "exists": False
            })

    return skills


def validate_prerequisites(directive_name, client_name):
    """Validate all prerequisites for directive execution."""
    results = {
        "valid": True,
        "directive": None,
        "errors": [],
        "warnings": [],
        "required_skills": [],
        "client_dir": None
    }

    # Load directive
    directive_content, error = load_directive(directive_name)
    if error:
        results["valid"] = False
        results["errors"].append(error)
        return results

    results["directive"] = directive_content

    # Check client directory
    client_dir = CLIENTS_DIR / client_name.replace(" ", "_")
    results["client_dir"] = str(client_dir)

    if not client_dir.exists():
        results["warnings"].append(f"Client directory will be created: {client_dir}")

    # Parse pre-flight requirements
    preflight_items = parse_preflight(directive_content)

    # Check for required client files
    client_file_keywords = ["profile", "avatar", "offer", "strategy", "competitive"]
    required_client_files = [
        item for item in preflight_items
        if any(kw in item.lower() for kw in client_file_keywords)
    ]

    if required_client_files:
        missing_files = check_client_files(client_name, required_client_files)
        if missing_files:
            results["valid"] = False
            results["errors"].extend([f"Missing: {f}" for f in missing_files])

    # Check for approval requirements
    if "approval" in directive_content.lower() and "strategy" in directive_content.lower():
        if not check_approval(client_name, "strategy"):
            results["warnings"].append("Strategy approval not found - may be required")

    # Identify required skill bibles
    results["required_skills"] = load_skill_bibles(directive_content)
    missing_skills = [s for s in results["required_skills"] if not s["exists"]]
    if missing_skills:
        results["warnings"].extend([
            f"Skill bible not found: {s['name']}" for s in missing_skills
        ])

    return results


def create_execution_context(validation_results, client_name):
    """Create execution context for Claude."""
    context = {
        "directive": validation_results["directive"],
        "client_name": client_name,
        "client_dir": validation_results["client_dir"],
        "skills_to_load": [
            s["path"] for s in validation_results["required_skills"] if s["exists"]
        ],
        "timestamp": datetime.now().isoformat(),
        "instructions": """
EXECUTION INSTRUCTIONS:
1. Load all skill bibles listed in skills_to_load
2. Read all client files from client_dir
3. Follow directive exactly as written
4. Use quality gates before completion
5. Save outputs to client_dir/assets/
"""
    }

    return context


def main():
    parser = argparse.ArgumentParser(description="Execute a directive for a client")
    parser.add_argument("--directive", required=True, help="Directive name (without .md)")
    parser.add_argument("--client", required=True, help="Client name")
    parser.add_argument("--dry-run", action="store_true", help="Validate only, don't execute")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Validate prerequisites
    results = validate_prerequisites(args.directive, args.client)

    if args.json:
        # Clean directive content for JSON (too large)
        output = {
            "valid": results["valid"],
            "errors": results["errors"],
            "warnings": results["warnings"],
            "required_skills": results["required_skills"],
            "client_dir": results["client_dir"]
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"DIRECTIVE: {args.directive}")
        print(f"CLIENT: {args.client}")
        print(f"{'='*60}\n")

        if results["errors"]:
            print("ERRORS (must fix):")
            for error in results["errors"]:
                print(f"  ✗ {error}")
            print()

        if results["warnings"]:
            print("WARNINGS:")
            for warning in results["warnings"]:
                print(f"  ⚠ {warning}")
            print()

        if results["required_skills"]:
            print("REQUIRED SKILLS:")
            for skill in results["required_skills"]:
                status = "✓" if skill["exists"] else "✗"
                print(f"  {status} {skill['name']}")
            print()

        if results["valid"]:
            print("STATUS: ✓ Ready to execute")
            if not args.dry_run:
                context = create_execution_context(results, args.client)
                # In practice, this would trigger Claude execution
                print("\nExecution context created. Ready for Claude.")
        else:
            print("STATUS: ✗ Cannot execute - fix errors first")

    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
