# Quick Business Scan

Run a quick scan of all business systems.

## What This Does

Scans Gmail, Slack, Close.io, and Calendar for high-priority action items.

## Execution

```
python execution/unified_scanner.py --quick
```

## Output

Prioritized action list showing:
- Critical items (score 80-100)
- High priority items (score 60-79)

## What Gets Scanned

- **Gmail**: Unread emails from clients/VIPs
- **Slack**: Unresponded DMs and mentions
- **Close.io**: Overdue tasks, today's follow-ups
- **Calendar**: Upcoming meetings needing prep

## For Full Scan

Use `/morning` for comprehensive scan including medium/low priority items.
