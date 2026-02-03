#!/usr/bin/env python3
"""
Unified Scanner
Scans all business systems and produces prioritized action list.

Scans:
- Gmail: Unread emails requiring response
- Slack: Conversations needing attention
- Close.io: Tasks, overdue follow-ups, pipeline changes
- Calendar: Today's meetings and prep requirements

Usage:
    python unified_scanner.py --comprehensive  # Full scan
    python unified_scanner.py --quick          # High-priority only
    python unified_scanner.py --source gmail   # Single source
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

# Try to import integrations (may not all be configured)
try:
    from close_io.client import CloseClient, get_today_tasks, get_overdue_tasks
    CLOSE_AVAILABLE = True
except ImportError:
    CLOSE_AVAILABLE = False


@dataclass
class ActionItem:
    """Represents a prioritized action item."""
    source: str           # gmail, slack, close, calendar
    type: str            # email, message, task, meeting
    title: str           # Brief description
    description: str     # Details
    priority_score: int  # 0-100
    due_date: Optional[str]
    link: Optional[str]
    raw_data: Optional[Dict]

    def to_dict(self):
        return asdict(self)


class UnifiedScanner:
    """Scans all business systems for actionable items."""

    def __init__(self):
        self.items: List[ActionItem] = []

    def scan_all(self, comprehensive: bool = True) -> List[ActionItem]:
        """Run all scanners and return prioritized list."""
        self.items = []

        # Gmail
        try:
            self._scan_gmail(comprehensive)
        except Exception as e:
            print(f"Gmail scan error: {e}", file=sys.stderr)

        # Slack
        try:
            self._scan_slack(comprehensive)
        except Exception as e:
            print(f"Slack scan error: {e}", file=sys.stderr)

        # Close.io
        if CLOSE_AVAILABLE:
            try:
                self._scan_close(comprehensive)
            except Exception as e:
                print(f"Close.io scan error: {e}", file=sys.stderr)

        # Calendar
        try:
            self._scan_calendar()
        except Exception as e:
            print(f"Calendar scan error: {e}", file=sys.stderr)

        # Sort by priority
        self.items.sort(key=lambda x: x.priority_score, reverse=True)

        return self.items

    def _scan_gmail(self, comprehensive: bool = True):
        """Scan Gmail for unread emails requiring response."""
        # In production, use Gmail API
        # For now, create placeholder structure

        # Priority scoring for emails:
        # - Client email: +30
        # - Contains "urgent" or "asap": +20
        # - Contains question: +10
        # - Over 24 hours old: +15
        # - From VIP sender: +25

        # Placeholder - in production, integrate with Gmail API
        gmail_available = os.environ.get("GMAIL_CREDENTIALS_PATH")

        if not gmail_available:
            # Add a placeholder item indicating Gmail not configured
            return

        # TODO: Implement actual Gmail scanning
        pass

    def _scan_slack(self, comprehensive: bool = True):
        """Scan Slack for messages needing response."""
        # Priority scoring for Slack:
        # - Direct message: +25
        # - Mention: +20
        # - Client channel: +15
        # - Contains question: +10
        # - Unanswered for >2 hours: +15

        slack_available = os.environ.get("SLACK_BOT_TOKEN")

        if not slack_available:
            return

        # TODO: Implement actual Slack scanning
        pass

    def _scan_close(self, comprehensive: bool = True):
        """Scan Close.io for tasks and follow-ups."""
        if not CLOSE_AVAILABLE:
            return

        try:
            client = CloseClient()

            # Get today's tasks
            today_tasks = get_today_tasks()
            for task in today_tasks:
                self.items.append(ActionItem(
                    source="close",
                    type="task",
                    title=task.get("text", "Task")[:50],
                    description=task.get("text", ""),
                    priority_score=self._score_close_task(task),
                    due_date=task.get("due_date"),
                    link=f"https://app.close.com/lead/{task.get('lead_id')}",
                    raw_data=task if comprehensive else None
                ))

            # Get overdue tasks
            overdue_tasks = get_overdue_tasks()
            for task in overdue_tasks:
                self.items.append(ActionItem(
                    source="close",
                    type="task",
                    title=f"OVERDUE: {task.get('text', 'Task')[:40]}",
                    description=task.get("text", ""),
                    priority_score=self._score_close_task(task, overdue=True),
                    due_date=task.get("due_date"),
                    link=f"https://app.close.com/lead/{task.get('lead_id')}",
                    raw_data=task if comprehensive else None
                ))

            # Get hot leads (qualified, recent activity)
            if comprehensive:
                hot_leads = client.search('lead_status:"Qualified"')[:10]
                for lead in hot_leads:
                    self.items.append(ActionItem(
                        source="close",
                        type="lead",
                        title=f"Follow up: {lead.get('display_name', 'Lead')}",
                        description=f"Qualified lead - last updated: {lead.get('date_updated', 'unknown')[:10]}",
                        priority_score=40,  # Base score for qualified leads
                        due_date=None,
                        link=f"https://app.close.com/lead/{lead.get('id')}",
                        raw_data=None
                    ))

        except Exception as e:
            print(f"Close.io error: {e}", file=sys.stderr)

    def _scan_calendar(self):
        """Scan calendar for today's meetings."""
        # Priority scoring for meetings:
        # - Client meeting: +50
        # - Within next 2 hours: +30
        # - Needs prep: +20

        # TODO: Implement calendar integration (Google Calendar API)
        pass

    def _score_close_task(self, task: Dict, overdue: bool = False) -> int:
        """Calculate priority score for Close.io task."""
        score = 50  # Base score for any task

        if overdue:
            score += 30

        # Check task text for priority indicators
        text = task.get("text", "").lower()
        if "urgent" in text or "asap" in text:
            score += 20
        if "client" in text:
            score += 15
        if "proposal" in text or "contract" in text:
            score += 10

        return min(100, score)


def format_action_list(items: List[ActionItem], format_type: str = "text") -> str:
    """Format action items for display."""
    if format_type == "json":
        return json.dumps([item.to_dict() for item in items], indent=2, default=str)

    # Text format
    output = []
    output.append("=" * 60)
    output.append(f"ACTION ITEMS - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    output.append("=" * 60)
    output.append("")

    if not items:
        output.append("No action items found!")
        return "\n".join(output)

    # Group by priority
    critical = [i for i in items if i.priority_score >= 80]
    high = [i for i in items if 60 <= i.priority_score < 80]
    medium = [i for i in items if 40 <= i.priority_score < 60]
    low = [i for i in items if i.priority_score < 40]

    if critical:
        output.append("🔴 CRITICAL (80-100)")
        output.append("-" * 40)
        for item in critical:
            output.append(f"  [{item.source.upper()}] {item.title}")
            if item.due_date:
                output.append(f"      Due: {item.due_date}")
            if item.link:
                output.append(f"      Link: {item.link}")
        output.append("")

    if high:
        output.append("🟠 HIGH (60-79)")
        output.append("-" * 40)
        for item in high:
            output.append(f"  [{item.source.upper()}] {item.title}")
            if item.due_date:
                output.append(f"      Due: {item.due_date}")
        output.append("")

    if medium:
        output.append("🟡 MEDIUM (40-59)")
        output.append("-" * 40)
        for item in medium:
            output.append(f"  [{item.source.upper()}] {item.title}")
        output.append("")

    if low:
        output.append("🟢 LOW (<40)")
        output.append("-" * 40)
        for item in low:
            output.append(f"  [{item.source.upper()}] {item.title}")
        output.append("")

    output.append("=" * 60)
    output.append(f"Total: {len(items)} items")
    output.append(f"  Critical: {len(critical)} | High: {len(high)} | Medium: {len(medium)} | Low: {len(low)}")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="Scan business systems for action items")
    parser.add_argument("--comprehensive", action="store_true", help="Full detailed scan")
    parser.add_argument("--quick", action="store_true", help="Quick high-priority scan")
    parser.add_argument("--source", choices=["gmail", "slack", "close", "calendar"],
                       help="Scan single source only")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    scanner = UnifiedScanner()

    # Determine scan type
    comprehensive = args.comprehensive or not args.quick

    # Run scan
    items = scanner.scan_all(comprehensive=comprehensive)

    # Filter by source if specified
    if args.source:
        items = [i for i in items if i.source == args.source]

    # Filter to high priority only for quick scan
    if args.quick:
        items = [i for i in items if i.priority_score >= 60]

    # Output
    format_type = "json" if args.json else "text"
    print(format_action_list(items, format_type))


if __name__ == "__main__":
    main()
