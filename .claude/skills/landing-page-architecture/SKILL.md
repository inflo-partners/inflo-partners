---
name: landing-page-architecture
description: SOP for landing page structure, section order, and conversion best practices
---

# Landing Page Architecture — SOP

## Section Order (Proven Structure)

1. **Hero** — Logo (favicon, if provided) → Headline → Subheadline → VSL Video Placeholder → CTA Button → Embed (Calendly for Book a Call CTA, or Application Form for Apply CTA)
2. **Problem** — Agitate pain points with specifics
3. **Solution/System** — Introduce the mechanism (not features)
4. **Proof** — Case studies with hard numbers
5. **Meet the Leadership / Founder** — *(Financial verticals only)* Photo + short bio of the founder/principal
6. **Objection Handling** — FAQ addressing top 5–7 hesitations
7. **Final CTA** — Restate outcome, urgency, risk reversal

## Hero Section — Mandatory Order

The hero section follows this exact layout, top to bottom, all center-aligned:

1. **Logo** — Client logo displayed as the page favicon AND at the top of the hero. If no logo is provided, skip this element entirely (do not use a placeholder).
2. **Headline** — Problem-aware, outcome-driven. Must be SHORT: 2 lines max when stacked (3 absolute max). States the offer quickly without sounding salesy. Designed for fast conversion — the reader should immediately understand what this is. Do NOT stack two separate headlines on top of each other. One headline only. Fades in from top on load.
3. **Subheadline** — Positions the mechanism or system. Must be short and easily digestible — one to two sentences max. Supports the headline without repeating it. Fades in from top (slight delay).
4. **VSL Video Placeholder** — 16:9 aspect ratio container with play button overlay. This is a placeholder — no actual video is embedded. The placeholder must display this exact text (replacing [Company Name] with the actual company name): "This is a placeholder for a Video Sales Letter we will script and produce for you so prospects fully understand why [Company Name] is the right fit for them." Fades in.
5. **CTA Button** — Clear, specific action. Scrolls to the Calendly embed section (NOT an external link).
6. **Calendly Embed** — Inline Calendly widget embedded directly below the CTA. Default embed (used on ALL landing pages unless specified otherwise):

```html
<!-- Calendly inline widget begin -->
<div class="calendly-inline-widget" data-url="https://calendly.com/inflopartners/call?hide_event_type_details=1&hide_gdpr_banner=1" style="min-width:320px;height:700px;"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
<!-- Calendly inline widget end -->
```

**CRITICAL: Calendly Embed Styling** — The Calendly embed must sit directly on the page with NO background color, NO section box, NO white space container, and NO card/wrapper behind it. Do not wrap it in a colored section or container with padding/background. It should be embedded cleanly into the page flow by itself with a transparent/matching background. No visual separation — it's part of the page, not inside a box.

## Vertical-Specific Sections

### Meet the Leadership / Meet the Founder (Financial Verticals Only)
For financial firms, wealth management, tax advisory, real estate funds, capital allocators, and similar finance-related verticals, include a **Meet the Leadership** or **Meet the Founder** section. This section contains:
- A photo of the founder/principal (use a placeholder image container if no photo is provided)
- The founder's name and title
- A short 2-3 sentence bio highlighting credentials, experience, and track record
- Place this section AFTER the Proof section and BEFORE the Objection Handling / FAQ section

This section is NOT included for non-financial verticals (coaches, SaaS, agencies, etc.) unless specifically requested.

## CTA Rules
- Minimum 3 CTAs per page (hero, mid-page, bottom)
- ALL CTA buttons scroll to the Calendly embed section — never link externally
- Button text is action-specific ("Book Your Free Strategy Call" not "Submit")
- Always include subtext under CTA (reduces friction)
- Use smooth scroll behavior with offset for comfortable viewing

## Layout Rules
- **Everything is center-aligned** — all headings, subheadings, body text, cards, CTAs, and sections are centered on the page
- No left-aligned hero content — the entire page flows as a centered, single-column layout
- Cards and grids are centered within their containers
- Section labels, headings, and subtext are always text-align: center

## Typography
- **Font family**: Use a thin, elegant Inter-like font (e.g., Inter with weights 300, 400, 500, 600). Keep text thin/light for a professional, high-end feel.
- Body weight: 300–400 (light/regular)
- Headings weight: 500–600 (medium/semibold) — NOT bold/700+
- Font size minimum 16px body
- Clean letter-spacing for headings

## Animation — Fade-In From Top
- All major elements fade in from the top on scroll (or on load for hero)
- Use CSS `@keyframes` with `transform: translateY(-20px)` → `translateY(0)` and `opacity: 0` → `opacity: 1`
- Stagger animations with slight delays for hero elements (logo → headline → subheadline → video → CTA)
- Below-the-fold sections use Intersection Observer to trigger fade-in when scrolled into view
- Keep animations subtle and professional — 0.6s–0.8s duration, ease-out timing

## Favicon
- If a client logo URL is provided, use it as the page favicon via `<link rel="icon">`
- The same logo appears at the top of the hero section

## Traffic-Based Page Length
- **Cold traffic**: Long page, full education, heavy proof
- **Warm traffic**: Medium page, direct offer, social proof focused
- **Hot traffic**: Short page, minimal friction, strong CTA

## Mobile Rules
- CTA button full-width on mobile
- Font size minimum 16px body
- Breakpoints: 768px (tablet), 480px (mobile)
- Thumb-friendly tap targets (min 44px)
- Calendly embed maintains min-width: 320px on mobile

---

## Funnel Types

Every partner funnel uses one of two CTA types. **Always ask the client which type during onboarding.**

### Book a Call CTA
- Calendly embed sits on the **main landing page** (in the hero section)
- All CTA buttons scroll to the Calendly embed
- Flow: **Landing Page → `/callconfirmed`**

### Apply CTA
- Application form (e.g., Typeform) sits on the **main landing page** where the Calendly embed would normally go
- All CTA buttons scroll to the application form embed
- After submission, the applicant is redirected to `/bookacall` where the Calendly embed lives
- Flow: **Landing Page → `/bookacall` → `/callconfirmed`**
- The `/bookacall` page is minimal: confirmation badge, headline, subtext, Calendly embed, footer

---

## Standard Pages (Every Partner)

| URL | File | Purpose |
|---|---|---|
| `/` | `index.html` | Main landing page |
| `/privacypolicy` | `privacypolicy.html` | Privacy policy (legally required) |
| `/termsofservice` | `termsofservice.html` | Terms of service (legally required) |
| `/callconfirmed` | `callconfirmed.html` | Post-booking confirmation (show rate optimization) |
| `/bookacall` | `bookacall.html` | Calendly booking page (**Apply CTA funnels only**) |

---

## URL Conventions

- **No hyphens**: `/privacypolicy` not `/privacy-policy`
- **All lowercase**: `/callconfirmed` not `/CallConfirmed`
- **No trailing slashes**
- Files are named to match their URL path (e.g., `privacypolicy.html` serves at `/privacypolicy`)

---

## Footer Links (Standard)

Every page in the funnel must include these footer links:

- `/privacypolicy` — Privacy Policy
- `/termsofservice` — Terms of Service
- `mailto:[partner-email]` — Contact

Plus the partner's physical address and phone number.

---

## Deployment Pattern (Per-Partner Vercel Project)

Each partner's `funnels/` folder deploys as its own Vercel project:

```
partners/[partner]/funnels/
  index.html            ← main landing page (serves at /)
  bookacall.html        ← Calendly booking (Apply CTA funnels only)
  callconfirmed.html    ← post-booking confirmation
  privacypolicy.html    ← privacy policy
  termsofservice.html   ← terms of service
  vercel.json           ← { "cleanUrls": true }
```

**`vercel.json`** — required in every partner's `funnels/` folder:
```json
{
  "cleanUrls": true
}
```

This strips `.html` extensions automatically so `privacypolicy.html` serves at `/privacypolicy`.

**Deploy command:**
```bash
cd partners/[partner]/funnels && vercel --prod
```

Then attach the custom domain (e.g., `partnerdomain.com`) to that Vercel project via the Vercel dashboard.
