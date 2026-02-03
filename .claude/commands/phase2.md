# Phase 2: Strategy & Positioning

Execute Phase 2 for client: $ARGUMENTS

## What This Does

Phase 2 transforms research into strategic positioning: angles, hooks, unique mechanism framing, and messaging hierarchy.

## Prerequisites

Phase 1 must be complete:
- [ ] `context/clients/$ARGUMENTS/profile.md` exists
- [ ] `context/clients/$ARGUMENTS/avatar.md` exists
- [ ] `context/clients/$ARGUMENTS/competitive.md` exists

## Execution Steps

1. **Validate prerequisites**
   ```
   python execution/execute_directive.py --directive offer_positioning --client "$ARGUMENTS" --dry-run
   ```

2. **Load skill bibles**
   - `context/skills/copywriting_bible.md`
   - `context/skills/vsl_bible.md`

3. **Run positioning directive**
   Follow `directives/offer_positioning.md` exactly

4. **Request approval**
   ```
   python execution/approve.py --request "$ARGUMENTS" strategy
   ```

## Outputs

- `context/clients/$ARGUMENTS/assets/positioning_options.md`
- `context/clients/$ARGUMENTS/strategy.md` (after approval)
- `context/clients/$ARGUMENTS/assets/creative_brief.md`

## Approval Required

This phase produces strategy options that MUST be approved before Phase 3.

Client reviews positioning document and selects:
- Primary positioning angle
- Unique mechanism framing
- Key messaging hierarchy

Upon approval:
```
python execution/approve.py "$ARGUMENTS" strategy
```
