# Client Research Directive

## PURPOSE
Conduct comprehensive discovery research to understand a new client's business, market, avatar, and competitive landscape. This research feeds all subsequent deliverables.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client onboarding form/intake received
- [ ] Discovery call completed (or scheduled)
- [ ] Access to client's existing materials (website, ads, funnels)
- [ ] Client folder created at `context/clients/{Client_Name}/`

**If any item is missing, STOP and request the missing input.**

---

## REQUIRED INPUTS

| Input | Source | Description |
|-------|--------|-------------|
| Onboarding Form | Client submission | Business basics, goals, challenges |
| Discovery Call | Recorded call | Deep dive conversation |
| Existing Materials | Client shares | Website, ads, past funnels |
| Competitor List | Client provides | Who they compete against |

---

## HARD RULES

1. **No assumptions** - Every insight must be sourced (client said, research showed)
2. **Avatar language verbatim** - Capture exact phrases, not paraphrases
3. **Quantify when possible** - Numbers over adjectives
4. **Identify gaps** - Note what's missing for follow-up
5. **Structure for reuse** - Output must feed other directives

---

## WORKFLOW

### Step 1: Process Onboarding Form

**Extract and document:**
```
BUSINESS BASICS:
- Company name
- Industry/niche
- Years in business
- Revenue range
- Team size

OFFER DETAILS:
- Primary offer
- Price point
- Delivery method
- Timeline/duration
- Guarantee (if any)

GOALS:
- Revenue goal
- Lead volume goal
- Conversion goal
- Timeline for goals

CURRENT STATE:
- Traffic sources
- Lead volume
- Conversion rate
- Sales process
```

### Step 2: Review Discovery Call

**Listen/read for:**
```
ORIGIN STORY:
- How did they start?
- What was the catalyst?
- What makes them different?

IDEAL CLIENT:
- Who do they love working with?
- Who gets the best results?
- Who should they NOT work with?

UNIQUE MECHANISM:
- What's their method/framework?
- Why does it work?
- What makes it different?

RESULTS & PROOF:
- Best client results
- Common results
- Timeline to results

CURRENT CHALLENGES:
- Where are they stuck?
- What's not working?
- What have they tried?

COMPETITION:
- Who do they compare to?
- How do they position vs. competitors?
- What are competitors missing?
```

### Step 3: Conduct Avatar Research

**Create detailed avatar profile:**

```
DEMOGRAPHICS:
- Age range
- Gender (if relevant)
- Location
- Income level
- Role/title
- Industry

PSYCHOGRAPHICS:
- Values
- Beliefs about the problem
- Beliefs about solutions
- Risk tolerance
- Decision-making style

SITUATION:
- Where are they now? (current state)
- Where do they want to be? (desired state)
- What's stopping them? (obstacles)
- What have they tried? (failed solutions)

PAIN POINTS (capture exact language):
1. "[Pain point in their words]"
2. "[Pain point in their words]"
3. "[Pain point in their words]"

DESIRES (capture exact language):
1. "[Desire in their words]"
2. "[Desire in their words]"
3. "[Desire in their words]"

OBJECTIONS:
1. "[Why they hesitate - their words]"
2. "[Why they hesitate - their words]"
3. "[Why they hesitate - their words]"

TRIGGER EVENTS:
- What makes them search for a solution NOW?
- What finally pushes them to take action?
```

**Research sources for avatar language:**
- Client testimonials and reviews
- Reddit/Facebook groups in niche
- Amazon reviews of related books
- Competitor testimonials
- Discovery call transcripts

### Step 4: Competitive Analysis

**For top 3-5 competitors, document:**
```
COMPETITOR: [Name]

Website: [URL]
Offer: [What they sell]
Price Point: [If known]
Positioning: [How they position themselves]

MESSAGING ANALYSIS:
- Main headline
- Key hooks used
- Proof elements
- Unique claim

STRENGTHS:
- What they do well

WEAKNESSES:
- What's missing/weak

DIFFERENTIATION OPPORTUNITY:
- How client can stand apart
```

### Step 5: Market Analysis

**Document market context:**
```
MARKET SIZE:
- TAM (Total Addressable Market)
- Growth trends

MARKET SOPHISTICATION:
- Level 1: Unaware of problem
- Level 2: Aware of problem, not solutions
- Level 3: Aware of solutions, not your solution
- Level 4: Aware of your solution, not convinced
- Level 5: Fully aware, need push to act

Current avatar sophistication level: [1-5]

MARKET TRENDS:
- What's changing in this market?
- What's becoming outdated?
- What's the emerging opportunity?

BUYING TRIGGERS:
- When do people buy in this market?
- Seasonal patterns?
- Business cycle patterns?
```

### Step 6: Synthesize Findings

**Create strategic summary:**
```
KEY INSIGHT #1:
[Most important discovery about avatar/market]

KEY INSIGHT #2:
[Second most important discovery]

KEY INSIGHT #3:
[Third most important discovery]

BIGGEST OPPORTUNITY:
[Where client can win]

BIGGEST RISK:
[What could go wrong]

POSITIONING RECOMMENDATION:
[Initial positioning direction]

MESSAGING ANGLES TO EXPLORE:
1. [Angle based on research]
2. [Angle based on research]
3. [Angle based on research]
```

---

## QUALITY GATES

Before marking complete, validate:

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Avatar language | ≥ 10 verbatim quotes | Research more sources |
| Pain points | ≥ 5 documented | Dig deeper |
| Competitors | ≥ 3 analyzed | Add more competitors |
| Proof points | Client results documented | Request from client |
| Gaps identified | Missing info noted | List for follow-up |

---

## DELIVERABLES

### 1. Client Profile (`context/clients/{name}/profile.md`)
```markdown
# Client Profile: [Company Name]

## Business Overview
[2-3 paragraphs]

## Offer Details
[Structured list]

## Unique Mechanism
[What makes them different]

## Credentials & Proof
[Why they're credible]

## Goals
[What they want to achieve]
```

### 2. Avatar Research (`context/clients/{name}/avatar.md`)
```markdown
# Avatar Research: [Avatar Name]

## Demographics
[Structured list]

## Current State
[Where they are now]

## Desired State
[Where they want to be]

## Pain Points (Verbatim)
1. "[Quote]"
2. "[Quote]"
...

## Desires (Verbatim)
1. "[Quote]"
2. "[Quote]"
...

## Objections
[List with handling notes]

## Trigger Events
[What makes them act]

## Language Bank
[Key phrases to use in copy]
```

### 3. Competitive Analysis (`context/clients/{name}/competitive.md`)
```markdown
# Competitive Analysis

## Competitor 1: [Name]
[Analysis]

## Competitor 2: [Name]
[Analysis]

## Competitor 3: [Name]
[Analysis]

## Positioning Map
[Where client fits vs. competitors]

## Differentiation Opportunities
[How to stand apart]
```

### 4. Strategic Summary (`context/clients/{name}/strategy_brief.md`)
```markdown
# Strategic Brief: [Client Name]

## Key Insights
[Numbered list]

## Recommended Positioning
[Direction]

## Messaging Angles
[Options to explore]

## Next Steps
[What to do with this research]
```

---

## RESEARCH SOURCES

### For Avatar Language
- G2/Capterra reviews (B2B)
- Reddit communities
- Facebook groups
- Amazon book reviews
- Podcast comments
- YouTube comments on relevant videos
- Quora questions
- Twitter/X threads

### For Competitive Analysis
- Competitor websites
- Competitor ads (Facebook Ad Library)
- SimilarWeb for traffic
- LinkedIn for company info
- Review sites

### For Market Analysis
- Industry reports
- Google Trends
- News articles
- Trade publications

---

## EDGE CASES

### Limited Client Information
→ Use discovery call to fill gaps. Create list of specific questions.

### No Existing Testimonials
→ Ask client for informal results. Interview past clients if possible.

### Crowded Market (Many Competitors)
→ Focus on 3-5 most similar. Look for underserved positioning.

### New Market (Few Competitors)
→ Research adjacent markets. Focus on avatar research over competitive.

### B2B Complex Sale
→ Research multiple stakeholders. Map decision-making unit.

---

## RELATED DIRECTIVES

- `offer_positioning.md` - Uses this research as input
- `vsl_scripting.md` - Uses avatar research
- `landing_page_copy.md` - Uses avatar research
- `email_sequence.md` - Uses avatar research
