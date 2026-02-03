# VSL Scripting Directive

## PURPOSE
Create a high-converting Video Sales Letter script for high-ticket offers ($3K-$50K+) that educates, builds trust, and converts cold traffic into booked calls.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client profile exists at `context/clients/{Client_Name}/profile.md`
- [ ] Avatar research exists at `context/clients/{Client_Name}/avatar.md`
- [ ] Offer details exist at `context/clients/{Client_Name}/offer.md`
- [ ] Strategy/angle approved (check approval token: `strategy`)
- [ ] VSL Bible loaded from `context/skills/vsl_bible.md`
- [ ] Copywriting Bible loaded from `context/skills/copywriting_bible.md`

**If any item is missing, STOP and request the missing input.**

---

## REQUIRED INPUTS

| Input | Location | Description |
|-------|----------|-------------|
| Client Profile | `context/clients/{name}/profile.md` | Business details, unique mechanism, credentials |
| Avatar Research | `context/clients/{name}/avatar.md` | Pain points, desires, objections, language |
| Offer Details | `context/clients/{name}/offer.md` | What's included, pricing, guarantee, bonuses |
| Approved Strategy | `context/clients/{name}/strategy.md` | Angle, hooks, positioning |

---

## HARD RULES

1. **Minimum 3,500 words** - High-ticket requires depth and trust-building
2. **4th-5th grade reading level** - Must be accessible to all audiences
3. **No hype language** - No "revolutionary", "secret", "guaranteed results"
4. **Proof required** - Must include specific results, case studies, or credentials
5. **Single CTA** - Book a call (not buy, not multiple options)
6. **Problem-first structure** - 60% problem agitation, 40% solution
7. **Avatar language only** - Use exact phrases from avatar research

---

## WORKFLOW

### Step 1: Review All Inputs
Read and internalize:
- Client's unique mechanism and differentiator
- Avatar's top 3 pain points (with exact language)
- Avatar's top 3 desires (with exact language)
- Competitive landscape and positioning
- Approved angle/hook from strategy

### Step 2: Craft the Hook (First 30 Seconds)
The hook must:
- Pattern interrupt (challenge a belief)
- Promise a specific outcome
- Create curiosity gap
- Qualify the viewer ("If you're a [avatar]...")

**Use framework from VSL Bible: [FRAMEWORK] Hook Formula**

### Step 3: Build Problem Agitation (Minutes 1-8)
Structure:
1. **Surface problem** - What they think the problem is
2. **Real problem** - What the actual problem is (insight)
3. **Cost of problem** - What it's costing them (specific)
4. **Failed solutions** - Why other approaches don't work
5. **Common mistakes** - What they're probably doing wrong

**Use exact avatar language for pain points.**

### Step 4: Introduce the Solution (Minutes 8-12)
Structure:
1. **Transition** - "What if there was a different way?"
2. **Mechanism reveal** - The unique approach (name it)
3. **Why it works** - Logical explanation
4. **Why it's different** - Contrast with failed approaches
5. **Origin story** - How you discovered/developed this

### Step 5: Proof & Credibility (Minutes 12-16)
Include:
- Your credentials/experience
- Case study 1 (specific results, timeline)
- Case study 2 (different avatar segment)
- Case study 3 (overcame specific objection)
- Social proof elements

**Rule: Every claim needs specific numbers or verifiable proof.**

### Step 6: Present the Offer (Minutes 16-20)
Structure:
1. **What they get** - Core deliverables
2. **How it works** - Process overview
3. **What's included** - Itemized list
4. **Bonuses** - Additional value (if applicable)
5. **Investment framing** - Value vs. cost positioning
6. **Guarantee** - Risk reversal

### Step 7: Handle Objections (Minutes 20-22)
Address top objections from avatar research:
- "I don't have time"
- "I've tried this before"
- "How do I know this will work for me?"
- "I can't afford it"
- [Client-specific objections]

### Step 8: Call to Action (Minutes 22-25)
Structure:
1. **Recap the transformation**
2. **Restate the mechanism**
3. **Clear next step** - "Click below to book a call"
4. **What happens on the call**
5. **Urgency** (if legitimate - limited spots, etc.)
6. **Final push** - Future pacing success

---

## QUALITY GATES

Before delivery, validate:

```python
python execution/validators/vsl_validator.py --file output.md
```

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Word count | ≥ 3,500 words | Expand weak sections |
| Reading level | 4th-5th grade | Simplify language |
| Hook strength | Pattern interrupt present | Rewrite hook |
| Proof density | ≥ 3 specific proof points | Add case studies |
| CTA clarity | Single, clear CTA | Remove competing CTAs |
| Avatar language | Uses exact phrases | Replace with avatar language |

---

## DELIVERABLES

1. **VSL Script** (`assets/vsl_script.md`)
   - Full script with speaker notes
   - Timestamp markers for each section
   - Visual/B-roll suggestions

2. **VSL Summary** (`assets/vsl_summary.md`)
   - Key hooks and angles used
   - Main proof points
   - Objections addressed

3. **Slide Outline** (optional, if requested)
   - Key slides for video production
   - Text overlay suggestions

---

## EDGE CASES

### No Case Studies Available
→ Use: Credentials, logical proof, third-party data, "here's what typically happens" framework

### Multiple Offers
→ Focus on ONE offer only. If client has multiple, request which one to focus on.

### Compliance-Sensitive Industry (Finance, Health)
→ Load compliance skill bible, add disclaimers, avoid specific outcome claims

### Short Attention Span Audience
→ Create "VSL Lite" version (15 min) with tighter structure

### Client Wants "Shorter VSL"
→ Explain: High-ticket requires trust-building. Minimum 20 minutes for $5K+ offers. Offer compromise of tighter editing, not less content.

---

## EXAMPLE OUTPUT STRUCTURE

```markdown
# [Client Name] VSL Script
## Video Sales Letter for [Offer Name]

---

### HOOK (0:00 - 0:30)
[Script text here]

*Visual: [suggestion]*
*Tone: [direction]*

---

### PROBLEM AGITATION (0:30 - 8:00)

#### Surface Problem (0:30 - 2:00)
[Script text]

#### Real Problem (2:00 - 4:00)
[Script text]

[Continue structure...]

---

### CALL TO ACTION (22:00 - 25:00)
[Script text]

*Button text: "Book Your Strategy Call"*
*Below video: Calendar embed*
```

---

## RELATED DIRECTIVES

- `client_research.md` - Must complete before VSL
- `offer_positioning.md` - Strategy approval required
- `landing_page_copy.md` - Often done in parallel
