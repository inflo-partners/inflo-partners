# Landing Page Copy Directive

## PURPOSE
Create high-converting landing page copy for high-ticket offers that drives visitors to book a call. Optimized for v0.dev implementation.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client profile exists at `context/clients/{Client_Name}/profile.md`
- [ ] Avatar research exists at `context/clients/{Client_Name}/avatar.md`
- [ ] Offer details exist at `context/clients/{Client_Name}/offer.md`
- [ ] Strategy/angle approved (check approval token: `strategy`)
- [ ] Landing page type specified (VSL page, long-form, quiz funnel, etc.)
- [ ] Copywriting Bible loaded from `context/skills/copywriting_bible.md`

**If any item is missing, STOP and request the missing input.**

---

## REQUIRED INPUTS

| Input | Location | Description |
|-------|----------|-------------|
| Client Profile | `context/clients/{name}/profile.md` | Business details, credentials |
| Avatar Research | `context/clients/{name}/avatar.md` | Pain points, desires, objections |
| Offer Details | `context/clients/{name}/offer.md` | What's included, pricing |
| Approved Strategy | `context/clients/{name}/strategy.md` | Angle, hooks, positioning |
| Page Type | Specified in request | VSL, long-form, quiz, webinar |

---

## HARD RULES

1. **Single CTA focus** - Book a call (one action, repeated)
2. **Mobile-first** - All sections must work on mobile
3. **Above-fold clarity** - Visitor knows what this is in 3 seconds
4. **No navigation** - Remove distractions, one path only
5. **Proof before ask** - Credibility established before CTA
6. **Avatar language** - Headlines use exact avatar phrases
7. **Scannable** - Subheads tell the story alone

---

## LANDING PAGE TYPES

### Type A: VSL Page (Recommended for High-Ticket)
```
- Headline + subhead
- VSL embed
- Below-video CTA
- Proof section (logos, testimonials)
- FAQ
- Final CTA
```

### Type B: Long-Form Sales Page
```
- Hook headline
- Problem agitation
- Solution introduction
- How it works
- What's included
- Proof/testimonials
- FAQ/objections
- CTA
```

### Type C: Application Page
```
- Headline
- Brief value prop
- "Who this is for" qualifier
- Application form
- Trust elements
```

---

## WORKFLOW

### Step 1: Define Page Strategy
Determine:
- Primary traffic source (cold, warm, retargeting)
- Page type (A, B, or C)
- Primary objection to overcome
- Key proof element to feature

### Step 2: Craft Above-Fold Section

**Headline Formula Options:**
1. **Outcome + Timeframe**: "Get [Result] in [Time] Without [Pain]"
2. **Question Hook**: "What If You Could [Desire] Without [Obstacle]?"
3. **Contrarian**: "Why [Common Approach] Is Keeping You From [Result]"
4. **Direct**: "[Specific Result] for [Specific Avatar]"

**Subhead**: Expand on headline, add specificity

**Above-fold must include:**
- Clear headline
- Supporting subhead
- Visual element (video thumbnail or hero image)
- Primary CTA button

### Step 3: Build Problem Section
- Identify with their current state
- Agitate the pain (use avatar language)
- Show cost of inaction
- Transition to solution

### Step 4: Present the Solution
- Introduce unique mechanism
- Explain why it's different
- Show the transformation path
- Keep focus on outcomes, not features

### Step 5: Create "How It Works" Section
Three-step framework:
1. Step 1: [Simple Action] → [Immediate Benefit]
2. Step 2: [Core Process] → [Key Result]
3. Step 3: [Final Action] → [Ultimate Outcome]

### Step 6: Build Proof Section

**Required elements:**
- Testimonials (3-5 minimum)
- Case study highlights
- Credentials/experience
- Media mentions or logos (if available)

**Testimonial structure:**
```
"[Specific result achieved]"
- Name, Title/Company
  [Context: where they started]
```

### Step 7: Write FAQ Section

**Standard FAQs for high-ticket:**
1. "Who is this for?" → Qualify ideal client
2. "How is this different?" → Differentiation
3. "What results can I expect?" → Realistic outcomes
4. "What's the investment?" → Frame value (or "discussed on call")
5. "What if it doesn't work?" → Guarantee/risk reversal
6. "How long does it take?" → Timeline expectations

### Step 8: Craft CTA Sections

**CTA Button Text Options:**
- "Book Your Strategy Call"
- "Apply Now"
- "Get Your Free [Value Prop]"
- "Schedule Your Consultation"

**Below CTA:**
- What happens next
- No obligation statement
- Urgency element (if legitimate)

---

## QUALITY GATES

Before delivery, validate:

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Single CTA | One action only | Remove competing CTAs |
| Mobile scan | Works on mobile | Restructure sections |
| Headline clarity | Understood in 3 seconds | Simplify |
| Proof present | ≥ 3 testimonials | Request or create placeholder |
| Avatar language | Headlines match research | Rewrite with avatar words |
| No jargon | Plain English | Simplify technical terms |

---

## DELIVERABLES

1. **Landing Page Copy Document** (`assets/landing_page_copy.md`)
   - All copy sections in order
   - Placeholder notes for images/video
   - Mobile considerations noted

2. **v0.dev Prompt** (`assets/v0_prompt.md`)
   - Structured prompt for v0.dev
   - Design direction
   - Component requirements

3. **Copy Variations** (optional)
   - 2-3 headline alternatives for testing
   - CTA button text variations

---

## V0.DEV INTEGRATION

### Prompt Structure for v0.dev

```
Create a high-converting landing page with the following:

BRAND:
- Primary color: [color]
- Font style: [modern/classic/bold]
- Tone: [professional/friendly/authoritative]

STRUCTURE:
[Paste the page structure from workflow]

COPY:
[Paste each section's copy]

REQUIREMENTS:
- Mobile responsive
- Single CTA focus
- Clean, minimal design
- Fast loading (no heavy animations)
```

---

## EDGE CASES

### No Testimonials Available
→ Use: Credentials section, "What clients typically experience", methodology proof

### Multiple Traffic Sources
→ Create traffic-specific variants (cold vs. warm have different awareness levels)

### Client Wants Pricing on Page
→ For high-ticket ($5K+): Recommend NOT showing price. Explain: Price without context = objection. Call allows proper framing.

### Compliance-Sensitive Industry
→ Add required disclaimers, soften claims, use "typical results" language

### Short-Form Requested
→ Minimum viable page: Headline + Video + CTA + 3 Proof Points + FAQ

---

## SECTION-BY-SECTION COPY TEMPLATES

### Hero Section Template
```markdown
## HERO

**Headline:**
[Outcome-focused headline using avatar language]

**Subhead:**
[Expand with specificity - who it's for, what they get]

**CTA Button:**
[Action verb + benefit]

**Below CTA:**
[Micro-commitment text: "Free 30-minute strategy session"]
```

### Problem Section Template
```markdown
## PROBLEM

**Lead-in:**
If you're like most [avatar]...

**Pain Point 1:**
[Specific pain in their words]

**Pain Point 2:**
[Another pain point]

**Pain Point 3:**
[Third pain point]

**Agitation:**
[Cost of staying stuck]

**Transition:**
But what if there was a different way?
```

### Proof Section Template
```markdown
## PROOF

**Section Header:**
[Don't Take Our Word For It / Results That Speak]

**Testimonial 1:**
"[Result in their words]"
- [Name], [Context]

**Testimonial 2:**
[Different result type]

**Testimonial 3:**
[Overcomes specific objection]

**Credentials:**
[Your credibility elements]
```

---

## RELATED DIRECTIVES

- `vsl_scripting.md` - Often created together
- `client_research.md` - Must complete first
- `email_sequence.md` - Follow-up sequences
