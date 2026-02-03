# Phase 3: Asset Creation

Execute Phase 3 for client: $ARGUMENTS

## What This Does

Phase 3 creates all marketing assets: VSL script, landing page copy, and email sequences.

## Prerequisites

Phases 1 & 2 must be complete:
- [ ] Client research complete
- [ ] Strategy approved: `python execution/approve.py --check "$ARGUMENTS" strategy`

## Execution Steps

1. **Validate prerequisites**
   ```
   python execution/execute_directive.py --directive vsl_scripting --client "$ARGUMENTS" --dry-run
   ```

2. **Load skill bibles**
   - `context/skills/vsl_bible.md`
   - `context/skills/copywriting_bible.md`
   - `context/skills/email_bible.md`

3. **Create assets in parallel** (using sub-agents)

   **Agent 1: VSL Script**
   - Follow `directives/vsl_scripting.md`
   - Output: `context/clients/$ARGUMENTS/assets/vsl_script.md`

   **Agent 2: Landing Page**
   - Follow `directives/landing_page_copy.md`
   - Output: `context/clients/$ARGUMENTS/assets/landing_page_copy.md`

   **Agent 3: Email Sequence**
   - Follow `directives/email_sequence.md`
   - Output: `context/clients/$ARGUMENTS/assets/email_sequence.md`

4. **Quality validation**
   ```
   python .claude/hooks/quality_gate.py vsl context/clients/$ARGUMENTS/assets/vsl_script.md
   python .claude/hooks/quality_gate.py landing_page context/clients/$ARGUMENTS/assets/landing_page_copy.md
   ```

5. **Collect and summarize** (one at a time)

## Outputs

- `context/clients/$ARGUMENTS/assets/vsl_script.md` (3,500+ words)
- `context/clients/$ARGUMENTS/assets/vsl_summary.md`
- `context/clients/$ARGUMENTS/assets/landing_page_copy.md`
- `context/clients/$ARGUMENTS/assets/v0_prompt.md`
- `context/clients/$ARGUMENTS/assets/email_sequence.md`
- `context/clients/$ARGUMENTS/assets/email_automation_setup.md`

## Quality Gates

All assets must pass validation before delivery:
- VSL: 3,500+ words, 4th-5th grade reading level
- Landing page: All required sections present
- Emails: Subject lines under 50 chars, single CTAs

## Request Delivery Approval

After assets pass quality gates:
```
python execution/approve.py --request "$ARGUMENTS" delivery
```
