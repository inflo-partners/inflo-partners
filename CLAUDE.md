# Inflo Partners — Business Overview

**About Inflo Partners**

Inflo Partners is a growth partner firm that works with established operators to build and scale high-ticket revenue systems.

www.inflopartners.com

We partner with businesses across multiple industries — including:

* Coaches and consultants
* Online education and info product businesses
* Agencies and service providers
* B2B SaaS companies
* Enterprise consulting firms
* Wealth, tax, and financial advisory firms
* Real estate funds, syndicators, and capital allocators

Our role is to help these businesses turn existing demand, traffic, or deal flow into **predictable, scalable revenue**.

We are not a marketing agency.

We are a **revenue infrastructure partner**.

**Who We Work With**

We don't work with beginners.

We partner with U.S.-based businesses already generating consistent revenue — typically between $10,000 and $100,000+ per month — that have proven demand but are unable to scale efficiently.

Most of our clients are already:

* Running paid ads (Meta, Google, YouTube)
* Building an organic audience (LinkedIn, YouTube, Instagram, X, etc.)
* Relying on referrals or word-of-mouth

Or a combination of all three.

They don't need more traffic.

They need a system that converts it.

**The Core Problem We Solve**

Most high-ticket businesses do not have a conversion system that works at scale.

They generate leads, but they struggle with:

* Low booked call rates
* Poor show rates
* Low close rates
* Leads ghosting
* Inconsistent revenue

The underlying issue is simple:

**They are asking for high-commitment decisions without enough trust, education, or touch points.**

**The 7-11-4 Rule**

Our entire philosophy is built around one core principle:

The **7-11-4 Rule**, based on research into digital buying behavior.

Before making a high-ticket decision, a prospect typically needs:

* 7 hours of exposure to your brand
* 11 meaningful touchpoints
* 4 hours of content or messaging consumption

Most businesses skip this entirely.

They run an ad or send traffic to a page and immediately ask prospects to:

* Book a call
* Schedule a demo
* Commit to a high-ticket offer

As a result, prospects are:

* Uneducated
* Skeptical
* Not ready to buy

This leads to low conversion across the entire funnel.

**What's Actually Happening**

Without a proper system, your funnel looks like this:

* Leads opt in but don't book
* Leads book but don't show
* Leads show but don't close

Even if you are generating revenue, you are leaving **a significant amount of money on the table**.

In many cases, 60–70% of potential revenue is lost due to:

* Lack of follow-up
* No nurturing process
* No objection handling before the call
* No contextual marketing

**What We Do**

Inflo Partners installs a complete **front-end conversion system and back-end selling infrastructure** that fixes these gaps.

Our goal is to move prospects from:

Cold → Educated → Pre-sold → Ready to buy

Before they ever get on a call.

**The Conversion System**

Our system is broken into two parts:

**1. Front-End Conversion System**

This is everything the prospect sees when they first interact with your business.

Depending on the business model, this may include:

* Meta, Google, or YouTube ads
* Organic content (YouTube, LinkedIn, Instagram, X)
* Landing pages and funnels
* DMs and outbound messaging
* Video Sales Letters (VSLs)

The goal of the front end is to:

* Capture lead information (name, email, phone)
* Educate the prospect
* Position the offer clearly
* Build trust and authority
* Pre-sell the prospect before the call

We also design and manage **paid acquisition (Meta Ads)** and **organic content strategy** to ensure consistent inbound flow into the system.

**2. Back-End Selling Infrastructure**

This is where the majority of revenue is made or lost.

The back end is responsible for:

* Nurturing leads
* Building trust
* Handling objections
* Driving show rates
* Increasing close rates

Most businesses have little to no back-end system.

This is where we create the biggest impact.

**What We Install**

When you partner with Inflo Partners, we build a complete system including:

**Funnel & Offer Infrastructure**

* High-converting landing pages
* Offer positioning and optimization
* Full sales page copywriting

**Video Assets**

* Scripted Video Sales Letters (VSLs)
* Long-form pre-sale content
* Objection-handling assets

**CRM & Automation**

* Full CRM buildout (Close.io, GoHighLevel, etc.)
* Automation workflows
* Pipeline tracking

**Email & SMS Systems**

* Value-based email nurture sequences
* Pre-call education flows
* Post-call follow-up sequences
* SMS reminders and conversational flows

**Sales Process Infrastructure**

* SDR / setter systems
* Lead qualification processes
* Pre-call engagement systems

**Paid Ads & Organic Strategy**

* Meta ads strategy and funnel integration
* Organic content strategy aligned with conversion

**Retargeting & Tracking**

* Retargeting systems
* Revenue attribution
* Real-time dashboards (CAC, show rate, close rate, etc.)

**Contextual Marketing**

One of our core advantages is **contextual marketing**.

Not all leads are the same.

We segment and market based on behavior:

* Opted in but didn't book
* Booked but didn't show
* Showed but didn't close

Each segment receives:

* Different messaging
* Different follow-ups
* Different content

This allows us to recover lost revenue and increase conversion across the entire funnel.

**The Outcome**

By installing this system, we consistently improve:

* Booked call rate
* Show rate
* Close rate
* Cost per acquisition (CAC)
* Total revenue

In many cases, businesses are able to significantly increase revenue **without increasing traffic**.

Same leads.

Same offer.

---

## Deployment & Version Control

- **GitHub repo**: `inflo-partners` (github.com/shariqwarsy/inflo-partners)
- **Vercel**: Connected to GitHub, auto-deploys on every push
- **Workflow**: Always test changes on localhost first before pushing
- **CRITICAL**: Never push to GitHub or create commits unless Shariq explicitly says "push to GitHub" or "commit this"
- Landing pages and web assets deploy automatically to Vercel when code is pushed to the repo

---

## Workspace Architecture

### How It Works

```
CLAUDE.md (this file)           ← Global directive — always active
.claude/
  agents/                       ← Team members — invoke with @agent-name
  skills/                       ← SOPs/playbooks — reference knowledge
  output-styles/                ← Brand voices — per-partner tone control
inflo-internal/                 ← Inflo Partners internal assets
  content/                      ← Inflo's own content
    voice-reference/            ← Shariq's writing samples (tweets, emails, scripts)
  youtube/                      ← YouTube scripts, outlines, and video assets
  emails/                       ← Inflo's own email sequences (pre-call, etc.)
partners/                       ← Partner workspaces — one folder per partner
execution/                      ← Automation scripts
```

### Agents (Team Members)

| Agent | Invoke | Role |
|---|---|---|
| Landing Page Builder | `@landing-page-builder` | Design and code landing pages |
| Email Sequence Writer | `@email-sequence-writer` | Nurture, pre-call, post-call, re-engagement emails |
| VSL Scriptwriter | `@vsl-scriptwriter` | Video sales letter and video content scripts |
| Ad Copy Writer | `@ad-copy-writer` | Meta, Google, YouTube ad copy and hooks |
| Funnel Strategist | `@funnel-strategist` | Full funnel architecture and conversion path planning |

### Skills (SOPs)

| Skill | What it covers |
|---|---|
| `conversion-principles` | 7-11-4 framework, contextual marketing, key metrics |
| `landing-page-architecture` | Page structure, section order, CTA rules |
| `email-sequence-framework` | Sequence types, timing, copy structure |
| `vsl-script-framework` | Script structure, timing, hook formulas |
| `ad-copy-framework` | Platform specs, hook types, copy formulas |
| `objection-handling` | Common objections by vertical + reframes |
| `contextual-marketing` | Behavior-based segmentation and messaging |
| `youtube-organic-funnel` | Complete YouTube organic SOP: strategy, content pillars, video categories, formats, funnels, CTAs, retention, cadence, team |
| `client-onboarding` | Partner onboarding SOP, Tally form processing, folder scaffolding |
| `gamma-deck-framework` | Gamma presentation deck SOP: copy rules, layout standards, slide structure, iteration workflow |

### Output Styles (Brand Voices)

| Style | Use for |
|---|---|
| `financial-advisory` | Wealth management, tax advisory, financial firms |
| `coaching-fitness` | Coaching, fitness, transformation offers |
| `saas-b2b` | SaaS companies, B2B service providers |
| `real-estate-capital` | Real estate funds, syndicators, capital allocators |
| `default` | Inflo Partners base voice |

Each partner's `PARTNER.md` specifies which output style to use. Agents read this and adapt their voice accordingly.

### Partner Workspace Structure

```
partners/
  [partner-name]/
    PARTNER.md            ← Partner brief (offer, audience, proof, brand, output style)
    funnels/
    emails/
    vsl/
```

### Workflow

1. **New partner** → Create folder, build `PARTNER.md`
2. **Plan funnel** → `@funnel-strategist`
3. **Build assets** → `@landing-page-builder`, `@vsl-scriptwriter`, `@email-sequence-writer`, `@ad-copy-writer`
4. **Deploy** → v0 + Vercel for landing pages, CRM for email
5. **Iterate** → Review metrics, optimize
6. **Knowledge capture** → When new knowledge is learned, add it to the appropriate skill file using: "add this to the appropriate skill: [knowledge]"

## Writing & Brand Guidelines (Global Default)

- Tone: Direct, authoritative, no-fluff, results-driven
- Avoid: Hype language, vague claims, generic marketing speak
- Always tie messaging back to revenue outcomes and specific metrics
- Use the 7-11-4 framework as a guiding principle
- Speak to operators and founders, not beginners
- Lead with the problem, follow with the system, close with proof
- **Per-partner voice**: Specified in each partner's `PARTNER.md` via output style

## Shariq's Voice (Personal Brand / Content)

Reference: `inflo-internal/content/voice-reference/`

### Short-Form (X/Twitter, Threads)
- One sentence per line, double-spaced (shift+enter x2)
- Short, punchy, conversational — like texting a friend who runs a business
- Lead with a bold or contrarian statement
- Use real numbers and math to prove the point
- CTAs are simple and direct: "comment X, I'll send it"
- No hype, no fluff, no motivational talk
- State things as obvious truths, not opinions

### Long-Form (Email, LinkedIn, YouTube)
- Teach while you sell — give away the framework so prospects see the gap themselves
- "Here's what most people do → here's why it's broken → here's what actually works" structure
- Specific numbers, percentages, and step-by-step breakdowns
- Self-aware and meta when appropriate
- Uses bullet points and numbered lists heavily
- Signs off personally as Shariq
- Frame calls/offers as audits, not pitches

### What He NEVER Does
- Motivational fluff
- "Mindset" talk
- Long-winded storytelling
- Corporate or polished marketing language
- Vague claims without numbers to back them up
- Em dashes (—) or en dashes (–), use commas or separate lines instead
