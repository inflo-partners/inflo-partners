# Phase 1: Discovery & Research

Execute Phase 1 for client: $ARGUMENTS

## What This Does

Phase 1 conducts comprehensive discovery research to understand the client's business, market, avatar, and competitive landscape.

## Execution Steps

1. **Validate prerequisites**
   ```
   python execution/execute_directive.py --directive client_research --client "$ARGUMENTS" --dry-run
   ```

2. **Create client folder** (if needed)
   ```
   mkdir -p context/clients/$ARGUMENTS/assets
   ```

3. **Run client research directive**
   Follow `directives/client_research.md` exactly

4. **Outputs to create:**
   - `context/clients/$ARGUMENTS/profile.md`
   - `context/clients/$ARGUMENTS/avatar.md`
   - `context/clients/$ARGUMENTS/competitive.md`
   - `context/clients/$ARGUMENTS/strategy_brief.md`

## Required Inputs

- Client onboarding form/intake
- Discovery call transcript/notes
- Access to client's existing materials

## Success Criteria

- [ ] Client profile complete with all business details
- [ ] Avatar research has 10+ verbatim quotes
- [ ] 3+ competitors analyzed
- [ ] Strategic brief with key insights documented
