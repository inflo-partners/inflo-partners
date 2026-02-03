# Offer Positioning Directive

## PURPOSE
Transform client research into strategic positioning: angles, hooks, unique mechanism framing, and messaging hierarchy. This is the strategic bridge between research and asset creation.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client profile exists at `context/clients/{Client_Name}/profile.md`
- [ ] Avatar research exists at `context/clients/{Client_Name}/avatar.md`
- [ ] Competitive analysis exists at `context/clients/{Client_Name}/competitive.md`
- [ ] Strategic brief exists at `context/clients/{Client_Name}/strategy_brief.md`
- [ ] Client has reviewed research and confirmed accuracy

**If any item is missing, STOP and run `client_research` directive first.**

---

## REQUIRED INPUTS

| Input | Location | Description |
|-------|----------|-------------|
| Client Profile | `context/clients/{name}/profile.md` | Business and offer details |
| Avatar Research | `context/clients/{name}/avatar.md` | Pain points, desires, language |
| Competitive Analysis | `context/clients/{name}/competitive.md` | Market positioning context |
| Strategic Brief | `context/clients/{name}/strategy_brief.md` | Initial insights |

---

## HARD RULES

1. **Strategy before execution** - Never write copy without approved positioning
2. **One primary angle** - Everything supports the main angle
3. **Avatar-first** - Positioning must resonate with avatar, not client ego
4. **Differentiation required** - Must stand apart from competitors
5. **Provable claims** - Every positioning claim must be supportable
6. **Approval required** - Strategy requires explicit sign-off before Phase III

---

## WORKFLOW

### Step 1: Identify Positioning Opportunities

**Review research for:**
```
AVATAR GAPS:
- What does the avatar want that competitors don't offer?
- What frustrations with current solutions?
- What unmet needs?

MARKET GAPS:
- What positioning is overcrowded?
- What positioning is underserved?
- What's emerging that no one owns?

CLIENT STRENGTHS:
- What does client do better than competitors?
- What unique experience/method do they have?
- What proof do they have that others don't?
```

### Step 2: Develop Positioning Options

**Create 3-5 positioning directions:**

```
POSITIONING OPTION A:
Name: [Short label]
Core Claim: [One sentence]
Target: [Specific avatar segment]
Differentiation: [How it's different]
Proof Points: [What supports this]
Risk Level: [Low/Medium/High]

Example:
Name: "The Systematizer"
Core Claim: "Replace founder-dependent delivery with repeatable systems"
Target: Coaches stuck at $50K/month due to capacity
Differentiation: Focus on systems vs. just more leads
Proof Points: Client results showing scale without hiring
Risk Level: Low (matches client strength)
```

### Step 3: Define Unique Mechanism

**For each positioning option, articulate:**
```
MECHANISM NAME:
[Branded name for the approach]

MECHANISM DEFINITION:
[What it is in one sentence]

WHY IT WORKS:
[The logic behind it]

WHY IT'S DIFFERENT:
[Contrast with common approaches]

MECHANISM COMPONENTS:
1. [Step/element 1]
2. [Step/element 2]
3. [Step/element 3]

PROOF IT WORKS:
[Evidence supporting the mechanism]
```

### Step 4: Generate Hooks and Angles

**For each positioning option, create:**

```
PRIMARY HOOK:
[Main attention-grabbing statement]

SUPPORTING ANGLES:
1. [Angle that supports primary hook]
2. [Angle that supports primary hook]
3. [Angle that supports primary hook]

HEADLINE OPTIONS:
1. [Outcome-focused]
2. [Curiosity-focused]
3. [Contrarian]
4. [Direct benefit]
5. [Question-based]

HOOK TYPES:
- Story Hook: [Personal story opener]
- Stat Hook: [Surprising statistic]
- Contrarian Hook: [Challenge common belief]
- Question Hook: [Provocative question]
- Prediction Hook: [Future-focused]
```

### Step 5: Create Messaging Hierarchy

**Organize messaging by importance:**

```
LEVEL 1: CORE MESSAGE (Used everywhere)
- Primary positioning statement
- Unique mechanism name
- Main transformation promise

LEVEL 2: SUPPORTING MESSAGES (Used frequently)
- 3-5 key benefits
- Main proof points
- Primary objection handler

LEVEL 3: DETAIL MESSAGES (Used selectively)
- Feature explanations
- Process details
- Secondary proof points
- Minor objection handlers
```

### Step 6: Develop Objection Strategy

**For each major objection:**
```
OBJECTION: "[Exact objection language]"

Root Cause: [Why they have this objection]

Prevention: [How to prevent it from arising]

Response Framework:
1. Acknowledge: [Validate the concern]
2. Reframe: [Change how they see it]
3. Evidence: [Proof that addresses it]
4. Bridge: [Move forward]

Where to Address:
- [ ] VSL (specify section)
- [ ] Landing page (specify section)
- [ ] Email sequence (specify email)
- [ ] Sales call (talk track)
```

### Step 7: Create Positioning Document

**Compile final strategy document:**

```
# [Client Name] Positioning Strategy

## Approved Positioning
[Selected option with full details]

## Unique Mechanism
[Complete mechanism documentation]

## Messaging Hierarchy
[All three levels]

## Hook Library
[All hooks and angles]

## Headline Options
[Ranked by recommendation]

## Objection Strategy
[Complete objection handling]

## Creative Direction
[Tone, style, visual direction]

## Next Steps
[What to create with this strategy]
```

---

## QUALITY GATES

Before requesting approval, validate:

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Differentiation | Clearly distinct from competitors | Revise positioning |
| Avatar alignment | Uses avatar language | Adjust messaging |
| Provable claims | Evidence exists for all claims | Remove or soften |
| Mechanism clarity | Can explain in one sentence | Simplify |
| Hook strength | Pattern interrupt present | Rewrite hooks |
| Complete hierarchy | All three levels documented | Fill gaps |

---

## APPROVAL PROCESS

**This directive requires approval token before Phase III begins.**

```python
# To request approval
python execution/request_approval.py "Client_Name" strategy

# Client reviews positioning document
# Client approves or requests changes

# Upon approval
python execution/approve.py "Client_Name" strategy
```

**Approval meeting agenda:**
1. Present research summary (2 min)
2. Present positioning options (5 min)
3. Recommend preferred option (2 min)
4. Discuss and decide (10 min)
5. Confirm angle and hooks (5 min)
6. Document decisions (2 min)

---

## DELIVERABLES

### 1. Positioning Options (`assets/positioning_options.md`)
```markdown
# Positioning Options: [Client Name]

## Option A: [Name]
[Full option documentation]

## Option B: [Name]
[Full option documentation]

## Option C: [Name]
[Full option documentation]

## Recommendation
[Which option and why]
```

### 2. Approved Strategy (`context/clients/{name}/strategy.md`)
```markdown
# Approved Strategy: [Client Name]

## Positioning
[Approved positioning]

## Unique Mechanism
[Mechanism details]

## Messaging Hierarchy
[All levels]

## Hook Library
[Approved hooks]

## Objection Strategy
[Handling approaches]

## Approved: [Date]
## Approved By: [Name]
```

### 3. Creative Brief (`assets/creative_brief.md`)
```markdown
# Creative Brief: [Client Name]

## Project Overview
[What we're creating]

## Target Avatar
[Summary from research]

## Positioning
[From approved strategy]

## Key Messages
[Priority order]

## Tone & Style
[Voice guidelines]

## Mandatories
[Must-include elements]

## Constraints
[What to avoid]
```

---

## POSITIONING FRAMEWORKS

### Framework 1: Contrast Positioning
"We're the [category] for people who [frustration with alternatives]"

Example: "We're the business coaching for people who are tired of motivational fluff and want actual systems"

### Framework 2: Specialization Positioning
"We only work with [specific avatar] who want [specific outcome]"

Example: "We only work with coaches at $30K+/month who want to hit $100K without burning out"

### Framework 3: Method Positioning
"The [method name] that [mechanism] to [outcome]"

Example: "The Revenue Engine Method that systematizes your backend to collect cash on autopilot"

### Framework 4: Against Positioning
"Unlike [alternative], we [differentiation]"

Example: "Unlike agencies that give you more leads you can't handle, we build the backend that converts those leads"

### Framework 5: Transformation Positioning
"From [current state] to [desired state] in [timeframe]"

Example: "From founder-dependent chaos to predictable $100K+ months in 90 days"

---

## EDGE CASES

### Client Attached to Weak Positioning
→ Present data showing market saturation. Show competitor examples. Propose test.

### Multiple Valid Positions
→ Recommend one. Offer to test others later. Don't split focus.

### No Clear Differentiation
→ Go deeper on mechanism. Find the "how" that's different even if "what" is similar.

### Positioning Requires Unmet Claims
→ Soften claims. Focus on process/method over outcomes. Build proof first.

### Market Too Small for Position
→ Widen target. Find adjacent markets. Test broader positioning.

---

## RELATED DIRECTIVES

- `client_research.md` - Must complete before this
- `vsl_scripting.md` - Uses approved strategy
- `landing_page_copy.md` - Uses approved strategy
- `email_sequence.md` - Uses approved strategy
