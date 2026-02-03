# CRM Architecture Directive

## PURPOSE
Design and document Close.io CRM architecture for high-ticket sales operations: pipelines, lead routing, automations, and attribution tracking.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client profile exists at `context/clients/{Client_Name}/profile.md`
- [ ] Offer structure documented at `context/clients/{Client_Name}/offer.md`
- [ ] Sales process understood (how they currently sell)
- [ ] Traffic sources identified (where leads come from)
- [ ] Team structure known (who handles what)
- [ ] CRM Bible loaded from `context/skills/crm_bible.md`

**If any item is missing, STOP and request the missing input.**

---

## REQUIRED INPUTS

| Input | Location | Description |
|-------|----------|-------------|
| Client Profile | `context/clients/{name}/profile.md` | Business details |
| Offer Structure | `context/clients/{name}/offer.md` | Products, pricing, upsells |
| Sales Process | Discovery conversation | Current sales flow |
| Traffic Sources | Discovery conversation | Lead origins |
| Team Structure | Discovery conversation | Roles and responsibilities |

---

## HARD RULES

1. **One pipeline per distinct sales process** - Don't mix different sales flows
2. **Lead status reflects reality** - Stages must match actual process
3. **Every lead has a source** - Attribution is non-negotiable
4. **Automation before manual** - Automate all repetitive tasks
5. **Follow-up is systematic** - No lead forgotten
6. **Clean data in, clean data out** - Validation at entry points
7. **Reporting from day one** - Build with analytics in mind

---

## CLOSE.IO ARCHITECTURE COMPONENTS

### Component 1: Pipelines
Distinct sales processes (e.g., "High-Ticket Consulting", "Group Program")

### Component 2: Lead Statuses
Stages within each pipeline (e.g., "New", "Qualified", "Call Scheduled")

### Component 3: Custom Fields
Data captured per lead (e.g., "Lead Source", "Offer Interest", "Budget")

### Component 4: Smart Views
Filtered lists for daily actions (e.g., "Today's Follow-ups", "Hot Leads")

### Component 5: Automations (Workflows)
Triggered actions based on events (e.g., "Send email when status changes")

### Component 6: Sequences
Automated outreach cadences (e.g., "Booked Call Sequence")

### Component 7: Integrations
Connections to other tools (Zapier, Calendly, etc.)

---

## WORKFLOW

### Step 1: Map the Current Sales Process

**Document the journey:**
```
1. Lead Source → How do leads enter?
2. Qualification → How are they vetted?
3. Nurture → What happens before sales conversation?
4. Sales Conversation → How does the call work?
5. Follow-Up → What happens after the call?
6. Closed → Won or Lost, what's tracked?
7. Onboarding → (If Won) What's the handoff?
```

**Identify decision points:**
- What moves someone forward?
- What disqualifies someone?
- What triggers follow-up?

### Step 2: Design Pipeline Structure

**Standard High-Ticket Pipeline:**
```
PIPELINE: High-Ticket Sales

STAGES:
1. New Lead
   └─ Entry: Any new lead
   └─ Exit: Qualification complete

2. Qualified
   └─ Entry: Meets criteria
   └─ Exit: Call scheduled OR disqualified

3. Call Scheduled
   └─ Entry: Calendly booking
   └─ Exit: Call completed

4. Call Completed
   └─ Entry: After call
   └─ Exit: Proposal sent OR not a fit

5. Proposal Sent
   └─ Entry: Pricing/terms shared
   └─ Exit: Decision made

6. Closed Won
   └─ Entry: Payment received
   └─ Action: Trigger onboarding

7. Closed Lost
   └─ Entry: Declined
   └─ Action: Add to nurture sequence
```

### Step 3: Define Custom Fields

**Required Fields:**
```
LEAD INFORMATION:
- Lead Source (dropdown): How they found you
- Lead Source Detail (text): Specific campaign/ad/referrer
- Offer Interest (dropdown): Which product/service
- Budget Range (dropdown): Qualified budget
- Timeline (dropdown): When they want to start

QUALIFICATION:
- Qualified (yes/no): Meets criteria
- Disqualification Reason (dropdown): Why not a fit

SALES PROCESS:
- Call Date (date): Scheduled call
- Call Outcome (dropdown): Result of call
- Proposal Amount (currency): Deal value
- Follow-Up Date (date): Next action

ATTRIBUTION:
- UTM Source (text): Traffic source
- UTM Medium (text): Traffic medium
- UTM Campaign (text): Campaign name
```

### Step 4: Create Smart Views

**Daily Action Views:**
```
VIEW: Today's Calls
- Filter: Call Date = Today
- Sort: Call time ascending

VIEW: Follow-Up Due
- Filter: Follow-Up Date ≤ Today
- Sort: Follow-Up Date ascending

VIEW: Hot Leads
- Filter: Status = Qualified, Last Activity < 3 days
- Sort: Last Activity descending

VIEW: Stale Leads
- Filter: Status = Qualified, Last Activity > 7 days
- Sort: Last Activity ascending

VIEW: New Leads (Unworked)
- Filter: Status = New, Activities = 0
- Sort: Created date ascending
```

### Step 5: Design Automations

**Automation Templates:**

```yaml
AUTOMATION: New Lead Welcome
Trigger: Lead created
Conditions: Source = [website, ad]
Actions:
  - Send email: "Welcome" template
  - Create task: "Review new lead" (assigned to owner)
  - Add to sequence: "Lead Nurture"

AUTOMATION: Call Booked
Trigger: Calendly booking (via Zapier)
Actions:
  - Update status: "Call Scheduled"
  - Update field: Call Date = booking date
  - Remove from sequence: "Lead Nurture"
  - Add to sequence: "Pre-Call Prep"

AUTOMATION: No Show
Trigger: Call Date passed + Status still "Call Scheduled"
Actions:
  - Update status: "No Show"
  - Add to sequence: "No Show Recovery"
  - Create task: "Follow up on no-show"

AUTOMATION: Closed Won
Trigger: Status → Closed Won
Actions:
  - Send email: "Welcome Client"
  - Create task: "Onboarding kickoff"
  - Update field: Won Date = today
  - Trigger Zapier: Create in project management tool
```

### Step 6: Set Up Sequences

**Close.io Sequence Structure:**
```
SEQUENCE: Lead Nurture (7 steps)
Step 1: Day 0 - Welcome email
Step 2: Day 1 - Value email
Step 3: Day 3 - Insight email
Step 4: Day 5 - Case study email
Step 5: Day 7 - CTA email
Step 6: Day 10 - Follow-up email
Step 7: Day 14 - Final push

EXIT CONDITIONS:
- Replies to any email
- Status changes to "Call Scheduled"
- Unsubscribes
```

### Step 7: Configure Integrations

**Required Integrations:**
```
CALENDLY → CLOSE.IO (via Zapier)
- Trigger: New Calendly booking
- Action: Update lead status, add Call Date

WEBSITE FORM → CLOSE.IO (via Zapier)
- Trigger: Form submission
- Action: Create lead with UTM data

CLOSE.IO → SLACK (via Zapier)
- Trigger: New lead created
- Action: Post to #leads channel

CLOSE.IO → GOOGLE SHEETS (optional)
- Trigger: Status = Closed Won
- Action: Add to revenue tracker
```

### Step 8: Document Attribution Model

**Source Tracking:**
```
LEAD SOURCE OPTIONS:
- Paid Ad (Facebook)
- Paid Ad (Google)
- Paid Ad (YouTube)
- Organic Social
- Referral
- Podcast
- Speaking/Event
- Cold Outreach
- Website Direct
- Other

CAPTURE METHOD:
1. UTM parameters on all links
2. "How did you hear about us?" on forms
3. Manual entry during qualification call
```

**Attribution Report:**
```
Monthly report shows:
- Leads by source
- Calls by source
- Close rate by source
- Revenue by source
- Cost per acquisition by source
```

---

## QUALITY GATES

Before delivery, validate:

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Pipeline stages | Match actual sales process | Revise with client |
| Lead sources | All sources captured | Add missing sources |
| Automations | No manual tasks automatable | Create automation |
| Smart views | Cover daily workflows | Add missing views |
| Attribution | Every lead has source | Add required fields |
| Data validation | Required fields enforced | Configure requirements |

---

## DELIVERABLES

1. **CRM Architecture Document** (`assets/crm_architecture.md`)
   - Pipeline structure diagram
   - Custom field definitions
   - Automation logic
   - Smart view configurations

2. **Setup Checklist** (`assets/crm_setup_checklist.md`)
   - Step-by-step implementation guide
   - Field configurations
   - Automation triggers

3. **Integration Map** (`assets/integration_map.md`)
   - All tool connections
   - Zapier configuration details
   - Data flow diagram

4. **Daily Workflow Guide** (`assets/crm_daily_workflow.md`)
   - Morning routine in CRM
   - Smart view usage
   - Task management

---

## CLOSE.IO SPECIFIC NOTES

### API Access
```python
# Close.io API base
BASE_URL = "https://api.close.com/api/v1"

# Common endpoints
GET /lead/              # List leads
POST /lead/             # Create lead
GET /lead/{id}          # Get lead
PUT /lead/{id}          # Update lead
GET /status/lead/       # List lead statuses
GET /customfield/lead/  # List custom fields
```

### Workflow Limitations
- Close.io workflows are powerful but have limits
- Complex logic may require Zapier
- Multi-step conditional logic = use Zapier

### Best Practices
- Use lead statuses, not custom fields, for pipeline stages
- Keep pipelines under 8 stages
- Use activities for all communication
- Log calls as "Call" activity type

---

## EDGE CASES

### Multiple Offers/Products
→ Option A: One pipeline with "Offer Interest" field
→ Option B: Separate pipelines per offer (if sales process differs)

### Multiple Sales Reps
→ Use lead assignment automation based on territory, round-robin, or lead score

### High Volume (100+ leads/day)
→ Add lead scoring, automated qualification, segment-based routing

### Complex Approval Process
→ Add "Pending Approval" stage, manager assignment field, approval automation

### Subscription/Recurring Revenue
→ Track MRR field, renewal dates, churn risk scoring

---

## RELATED DIRECTIVES

- `client_research.md` - Understand client before CRM design
- `email_sequence.md` - Sequences implemented in CRM
- `automation_sop.md` - Zapier integration details
