# Phase 4: Implementation

Execute Phase 4 for client: $ARGUMENTS

## What This Does

Phase 4 implements the backend infrastructure: CRM setup, automations, and delivery SOPs.

## Prerequisites

Phase 3 must be complete:
- [ ] All marketing assets created
- [ ] Delivery approved: `python execution/approve.py --check "$ARGUMENTS" delivery`

## Execution Steps

1. **Validate prerequisites**
   ```
   python execution/execute_directive.py --directive crm_architecture --client "$ARGUMENTS" --dry-run
   ```

2. **Load skill bibles**
   - `context/skills/crm_bible.md`

3. **Run CRM architecture directive**
   Follow `directives/crm_architecture.md` exactly

4. **Create implementation deliverables**

## Outputs

- `context/clients/$ARGUMENTS/assets/crm_architecture.md`
- `context/clients/$ARGUMENTS/assets/crm_setup_checklist.md`
- `context/clients/$ARGUMENTS/assets/integration_map.md`
- `context/clients/$ARGUMENTS/assets/crm_daily_workflow.md`
- `context/clients/$ARGUMENTS/assets/automation_sops.md`

## Implementation Checklist

### Close.io Setup
- [ ] Pipeline created with correct stages
- [ ] Custom fields configured
- [ ] Lead statuses defined
- [ ] Smart views created
- [ ] Sequences built

### Integrations
- [ ] Calendly → Close.io (Zapier)
- [ ] Website form → Close.io (Zapier)
- [ ] Close.io → Slack notifications (Zapier)

### Automations
- [ ] New lead welcome sequence
- [ ] Call booked notification
- [ ] No-show recovery
- [ ] Closed won onboarding trigger

### Documentation
- [ ] Daily workflow guide complete
- [ ] Team training materials ready
- [ ] Client handoff documentation

## Handoff

Upon completion:
1. Review all assets with client
2. Train team on CRM workflow
3. Document any customizations
4. Schedule 30-day check-in
