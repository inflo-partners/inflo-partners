# Email Sequence Directive

## PURPOSE
Create high-converting email sequences for high-ticket sales funnels: nurture sequences, follow-up sequences, and sales sequences that move leads toward booking calls.

---

## STEP 0: PRE-FLIGHT (HARD STOP)

Before proceeding, verify ALL items:

- [ ] Client profile exists at `context/clients/{Client_Name}/profile.md`
- [ ] Avatar research exists at `context/clients/{Client_Name}/avatar.md`
- [ ] Offer details exist at `context/clients/{Client_Name}/offer.md`
- [ ] Sequence type specified (nurture, follow-up, sales, re-engagement)
- [ ] Email Bible loaded from `context/skills/email_bible.md`
- [ ] Copywriting Bible loaded from `context/skills/copywriting_bible.md`

**If any item is missing, STOP and request the missing input.**

---

## REQUIRED INPUTS

| Input | Location | Description |
|-------|----------|-------------|
| Client Profile | `context/clients/{name}/profile.md` | Business details |
| Avatar Research | `context/clients/{name}/avatar.md` | Pain points, desires, objections |
| Offer Details | `context/clients/{name}/offer.md` | What's included |
| Sequence Type | Specified in request | nurture/follow-up/sales/re-engage |
| Trigger Event | Specified in request | What starts this sequence |

---

## HARD RULES

1. **Subject lines under 50 characters** - Mobile optimization
2. **Single CTA per email** - One action, one link
3. **Preview text optimized** - First 90 characters matter
4. **Plain text friendly** - Must work without images
5. **Personal tone** - From a person, not a company
6. **Value before ask** - Earn the right to sell
7. **Mobile-first formatting** - Short paragraphs, scannable

---

## SEQUENCE TYPES

### Type 1: Lead Nurture Sequence (5-7 emails)
**Trigger**: Lead magnet download, quiz completion
**Goal**: Build trust, establish authority, generate call bookings
**Timeline**: Daily for 5-7 days

### Type 2: Call Follow-Up Sequence (3-5 emails)
**Trigger**: Booked call, call completed
**Goal**: Reduce no-shows, handle objections post-call
**Timeline**: Varies based on call status

### Type 3: Sales Sequence (5-10 emails)
**Trigger**: Launch, promotion, time-sensitive offer
**Goal**: Drive immediate action
**Timeline**: Daily during launch window

### Type 4: Re-Engagement Sequence (3-4 emails)
**Trigger**: Inactive for 30+ days
**Goal**: Reactivate cold leads
**Timeline**: Every 2-3 days

---

## WORKFLOW

### Step 1: Define Sequence Architecture

**For each sequence, determine:**
- Entry trigger (what puts someone in this sequence)
- Exit conditions (what removes them)
- Sequence length (number of emails)
- Timing (delay between emails)
- Primary CTA (what action you want)

### Step 2: Map the Narrative Arc

**Lead Nurture Arc:**
```
Email 1: Deliver value, set expectations
Email 2: Share insight/framework
Email 3: Tell origin story, build connection
Email 4: Case study/proof
Email 5: Address objections
Email 6: Create urgency, make offer
Email 7: Final push/scarcity
```

**Follow-Up Arc:**
```
Email 1: Confirmation + what to expect
Email 2: Pre-call prep + value
Email 3: Reminder (24 hours before)
Email 4: Post-call recap (if no decision)
Email 5: Handle specific objection
```

### Step 3: Write Each Email

**Email Structure:**
```
Subject: [Under 50 chars, curiosity or benefit]
Preview: [First 90 chars that complement subject]

[Opening hook - 1-2 sentences]

[Body - 3-5 short paragraphs]

[Single CTA]

[Sign-off]

P.S. [Reinforce CTA or add urgency]
```

### Step 4: Optimize Subject Lines

**Subject Line Formulas:**
1. **Curiosity Gap**: "The [thing] no one talks about"
2. **Direct Benefit**: "How to [achieve result]"
3. **Question**: "Quick question about [their situation]"
4. **Personal**: "I noticed something"
5. **Story Tease**: "What happened when [scenario]"
6. **Contrarian**: "Stop doing [common thing]"

**Test: Would YOU open this?**

### Step 5: Add Personalization

**Required personalization tokens:**
- `{{first_name}}` - Always use
- `{{company}}` - When B2B
- `{{pain_point}}` - If captured
- `{{source}}` - How they found you

### Step 6: Set Up Timing & Triggers

**Recommended timing:**
- Nurture: 24 hours between emails
- Follow-up: Varies (see templates below)
- Sales: 24 hours, then 12 hours near deadline
- Re-engagement: 48-72 hours between

---

## EMAIL TEMPLATES BY SEQUENCE

### Lead Nurture Sequence (7 Emails)

#### Email 1: Welcome + Deliver
**Subject**: Here's your [lead magnet] + a quick note
**Purpose**: Deliver value, set expectations
```
Hey {{first_name}},

Your [lead magnet] is ready: [link]

Before you dive in, quick heads up on what's coming...

Over the next few days, I'm going to share [what they'll learn].

This isn't generic advice. It's the same [framework/approach] that's helped [result] for [avatar type].

Talk soon,
[Name]

P.S. Reply to this email if you have questions. I read everything.
```

#### Email 2: Key Insight
**Subject**: The real reason [problem persists]
**Purpose**: Share unique perspective, build authority
```
Hey {{first_name}},

Most [avatars] think their problem is [surface problem].

It's not.

The real issue is [deeper insight]...

[Explain the insight in 3-5 paragraphs]

Here's what this means for you:
[Actionable takeaway]

Tomorrow I'll share [next topic teaser].

[Name]
```

#### Email 3: Origin Story
**Subject**: How I figured this out (the hard way)
**Purpose**: Build connection through vulnerability
```
Hey {{first_name}},

I wasn't always [current position].

[Share relevant origin story - struggle to success]

The turning point was when I realized [key insight].

That's when I developed [mechanism/approach].

Since then, [results achieved].

Reason I'm sharing this: [tie to their situation]

[Name]

P.S. [Teaser for next email or soft CTA]
```

#### Email 4: Case Study
**Subject**: How [client name] got [specific result]
**Purpose**: Proof through story
```
Hey {{first_name}},

Quick story about [client type]...

[Client] came to me with [problem - similar to reader's].

They'd already tried [failed approaches].

Within [timeframe], they [achieved result].

Here's what made the difference:
1. [Key change 1]
2. [Key change 2]
3. [Key change 3]

Want to see if this could work for you?

[CTA: Book a call link]

[Name]
```

#### Email 5: Handle Objections
**Subject**: "I'm not sure this is right for me"
**Purpose**: Overcome hesitation
```
Hey {{first_name}},

Got a question I hear a lot:

"How do I know this will work for MY situation?"

Fair question. Here's my honest answer...

[Address objection directly]

The truth is, this approach works best for:
- [Qualifier 1]
- [Qualifier 2]
- [Qualifier 3]

If that's you, [CTA].

If it's not, no worries. These emails might still be helpful.

[Name]
```

#### Email 6: The Offer
**Subject**: Wanted to share something with you
**Purpose**: Clear offer presentation
```
Hey {{first_name}},

Over the past few days, I've shared:
- [Summary of value delivered]

Now I want to offer you something...

[Explain the offer clearly]

Here's what happens when you [CTA]:

1. [Step 1 - what happens]
2. [Step 2 - what they get]
3. [Step 3 - the outcome]

No pressure. No pitch on the call. Just a conversation to see if I can help.

[CTA: Book your call]

[Name]

P.S. [Urgency if legitimate - limited spots, etc.]
```

#### Email 7: Final Push
**Subject**: Last call (then I'll stop emailing about this)
**Purpose**: Create urgency, final conversion push
```
{{first_name}},

This is my last email about [offer/opportunity].

If you've been on the fence, here's my honest take:

[Restate the core value proposition in 2-3 sentences]

If that's what you want, [CTA].

If not, totally fine. I'll keep sending valuable content either way.

But I didn't want you to miss this because you "meant to get around to it."

[CTA: Last chance to book]

[Name]
```

---

### Call Follow-Up Sequence (No-Show)

#### Email 1: Missed You (Send immediately)
**Subject**: Hey, everything okay?
```
Hey {{first_name}},

We had a call scheduled for [time] but I didn't see you there.

No worries at all - life happens.

Want to reschedule? [Calendly link]

Or if something came up and this isn't the right time, just let me know.

[Name]
```

#### Email 2: Reschedule (24 hours later)
**Subject**: Still want to chat?
```
{{first_name}},

Following up on our missed call.

If you're still interested in [solving problem/achieving result], here's my calendar: [link]

If the timing isn't right, no pressure. Just reply and let me know.

[Name]
```

---

## QUALITY GATES

Before delivery, validate:

| Check | Requirement | Fail Action |
|-------|-------------|-------------|
| Subject length | ≤ 50 characters | Shorten |
| Preview text | Intentionally written | Add preview |
| Single CTA | One link/action per email | Remove extras |
| Personalization | {{first_name}} minimum | Add tokens |
| Mobile format | Short paragraphs | Break up text |
| Spam words | None (free, guarantee, etc.) | Replace |

---

## DELIVERABLES

1. **Email Sequence Document** (`assets/email_sequence_{type}.md`)
   - All emails in order
   - Subject lines + preview text
   - Timing between emails
   - Trigger and exit conditions

2. **Automation Setup Guide** (`assets/email_automation_setup.md`)
   - Trigger configuration
   - Tag/segment requirements
   - Exit conditions

3. **A/B Test Variants** (optional)
   - 2-3 subject line alternatives
   - Key body copy variations

---

## EDGE CASES

### No Lead Magnet
→ Adjust Email 1 to focus on "thanks for your interest" + immediate value delivery

### B2B vs. B2C
→ B2B: More formal, company-focused, longer consideration. B2C: More personal, emotion-driven

### Multiple Products/Offers
→ Segment by interest. One offer per sequence. Don't confuse with options.

### High-Volume List (10K+)
→ Add more segmentation triggers. Personalize based on engagement.

### Compliance Requirements (Finance/Health)
→ Add disclaimers, soften claims, remove income/result promises

---

## RELATED DIRECTIVES

- `landing_page_copy.md` - Often delivers traffic to email opt-in
- `crm_architecture.md` - Email sequences live in CRM
- `client_research.md` - Avatar research required
