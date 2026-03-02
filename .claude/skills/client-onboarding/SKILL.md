---
name: client-onboarding
description: SOP for onboarding new partners, building PARTNER.md, and initializing partner workspaces
---

# Client Onboarding — SOP

## Steps

### 1. Client Fills Out Tally Onboarding Form
Client completes the 23-question Tally form covering:
- Business info (name, address, phone, logo)
- Target audience + ideal client profile
- Pain points + dream outcomes
- Product/service description + offer structure
- USP / unique mechanism
- Founder story + growth timeline
- Proof / case studies + average results
- Market context + industry trends

### 2. Export & Run Onboarding Script
Export the Tally submissions as CSV, then run:
```
python3 execution/onboard_client.py <path_to_tally_csv>
```

This automatically:
- Parses all new client submissions from the CSV
- Auto-detects the output style (financial-advisory / coaching-fitness / saas-b2b / real-estate-capital)
- Creates the full client folder structure from `_template`
- Generates a populated `PARTNER.md` with all Tally responses mapped to the correct fields

### 3. Review PARTNER.md
Fill in any remaining `[To be confirmed]` fields:
- Monthly revenue
- Website (if not captured in form)
- Brand colors (primary + secondary hex)
- Booking URL (Calendly/link)
- CTA type (Book a call / Watch VSL / Apply)
- Top 3 objections (or use `objection-handling` skill to generate)

### 4. Plan the Funnel
Use `@funnel-strategist` to map the full conversion path:
- Traffic source → Landing page → Nurture → Call → Close
- Identify which agents build each piece

### 5. Build Assets (in order)
1. **Landing page** → `@landing-page-builder`
2. **VSL script** (if applicable) → `@vsl-scriptwriter`
3. **Email sequences** → `@email-sequence-writer`
4. **Ad copy** → `@ad-copy-writer`

### 6. Review & Deploy
- Review all assets against PARTNER.md
- Check output style consistency
- Deploy landing page (v0 → Vercel)
- Set up email in CRM (Close.io / GoHighLevel)
- Launch ads

## Folder Structure After Onboarding
```
partners/[partner-name]/
├── PARTNER.md
├── funnels/
├── emails/
└── vsl/
```

## Output Style Auto-Detection

The onboarding script detects the appropriate output style by scanning all form responses for industry-specific keywords:

| Style | Trigger Keywords |
|---|---|
| `real-estate-capital` | real estate, fund, syndication, investor, accredited, equity, self storage |
| `coaching-fitness` | coach, athlete, training, fitness, strength, performance, gym |
| `saas-b2b` | saas, software, platform, b2b, enterprise, subscription, mrr |
| `financial-advisory` | wealth, tax, financial, advisory, fiduciary, portfolio, retirement |
| `default` | Fallback if no keywords match |
