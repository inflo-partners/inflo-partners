# VSL Script Only

Write VSL script for client: $ARGUMENTS

## What This Does

Creates a single VSL script without running the full Phase 3 workflow.

## Prerequisites

- [ ] Client research complete (`context/clients/$ARGUMENTS/profile.md`)
- [ ] Avatar research complete (`context/clients/$ARGUMENTS/avatar.md`)
- [ ] Strategy approved (`context/clients/$ARGUMENTS/strategy.md`)

## Execution

1. **Load skill bibles**
   - `context/skills/vsl_bible.md`
   - `context/skills/copywriting_bible.md`

2. **Follow directive**
   `directives/vsl_scripting.md`

3. **Validate output**
   ```
   python .claude/hooks/quality_gate.py vsl context/clients/$ARGUMENTS/assets/vsl_script.md
   ```

## Output

- `context/clients/$ARGUMENTS/assets/vsl_script.md`
- `context/clients/$ARGUMENTS/assets/vsl_summary.md`

## Quality Requirements

- Minimum 3,500 words
- 4th-5th grade reading level
- All required sections present
- Uses avatar language
