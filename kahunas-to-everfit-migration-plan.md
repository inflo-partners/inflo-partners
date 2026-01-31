# Kahunas to Everfit Migration Plan

## Executive Summary

Kahunas has **no public API, no CSV export, and no bulk data download**. The only programmatic interface is a narrow Zapier integration (Growth+ plans only) that exposes check-in forms and client creation -- nothing else. This means the migration is fundamentally a **manual rebuild with assisted data capture**, not a data pipeline. The plan below is designed around that constraint.

---

## 1. Full Inventory of Kahunas Data Types

| # | Data Type | Subtypes / Details | Volume Estimate Method |
|---|-----------|-------------------|----------------------|
| 1 | **Clients** | Name, email, phone, birthdate, start/current weight, measurement prefs (kg/lbs), package assignment, enrollment weeks, last activity | Count in Kahunas client list |
| 2 | **Workout Programs** | Simple, Detailed, PDF/Excel upload types. Training phases/blocks, workout days with warmup/workout/cooldown sections | Count per client (up to 5 per client) |
| 3 | **Exercises (Library)** | 1,000+ built-in + custom. Name, video (upload/YT/Vimeo), type (time/sets&reps/distance/calories), RIR, RPE, intensity, tempo, male/female variants | Count custom exercises in library |
| 4 | **Exercise Videos** | Direct uploads to Kahunas, YouTube links, Vimeo links | Audit library for upload vs. link |
| 5 | **Workout Logs** | Client-entered performance data: weights, reps, volume per session | Per-client history depth |
| 6 | **Nutrition Plans** | Macro/micronutrient targets, TDEE-based, supplement plans | Per-client count |
| 7 | **Nutrition Logs** | Client food entries with calorie/macro adherence from 1.6M food DB | Per-client history depth |
| 8 | **Check-in Forms** | Custom templates with rating scales, text, file uploads, metric-designated fields | Count form templates |
| 9 | **Check-in Submissions** | Client responses to check-in forms (weekly/biweekly/monthly) | Per-client history |
| 10 | **Daily Habit Forms** | Walking, meditation, steps, HRV, hunger, stress, sleep, custom fields | Count templates + submissions |
| 11 | **Initial Questionnaires** | One-time onboarding Q&A presented on first login | Count templates + responses |
| 12 | **Messages** | 1:1 in-app messages, voice notes, group messages (Growth+) | Per-client thread depth |
| 13 | **Progress Photos** | Client uploads with side-by-side comparison and overlay features | Per-client count |
| 14 | **Body Metrics / Charts** | Any form field designated as "metric" generates graphs over time | Per-client data points |
| 15 | **Billing / Payments** | Packages (recurring/one-off), Stripe/PayPal integration, payment history | Count in Stripe dashboard |
| 16 | **The Vault (Content)** | Videos, PDFs, ebooks, audio, documents with time-release/drip scheduling | Count items in Vault |
| 17 | **Lead Generation Forms** | Capture forms for prospects (Growth+) | Count forms |
| 18 | **Automations** | Email, chat, push notification sequences (Growth+) | Count automation rules |
| 19 | **Calendar Events** | Appointments, goals, training phase scheduling | Per-client count |
| 20 | **Goals** | Motivational targets with countdown dates | Per-client count |
| 21 | **Wearable Data** | Apple Health, Google Fit synced metrics (cardio, sleep, HRV, body comp) | Per-client, auto-re-syncs on Everfit |

---

## 2. Kahunas-to-Everfit Data Mapping

### 2A. Direct Equivalents

| # | Kahunas Data Type | Everfit Equivalent | Mapping Notes |
|---|-------------------|-------------------|---------------|
| 1 | Client profile (name, email, phone) | Client profile | Direct 1:1. Category field maps to Hybrid/In-Person/Online. |
| 2 | Workout Programs (Detailed) | Programs (Program Library) | Kahunas phases/blocks = Everfit multi-week calendar. Warmup/Workout/Cooldown sections = Everfit Regular sections. |
| 3 | Custom exercises | Custom exercises in Exercise Library | Map type (time/reps/distance/calories) to Everfit category (Strength/Bodyweight/Timed/Distance-short/Distance-long). Tracking fields must be reconfigured (max 3 in Everfit). |
| 4 | Exercise videos (YouTube/Vimeo links) | Exercise videos (YouTube/Vimeo links) | Direct link transfer. |
| 5 | Exercise videos (direct uploads) | Exercise videos (direct upload, max 300MB) | Must re-download from Kahunas and re-upload to Everfit. |
| 6 | Nutrition plans (macros) | Macro Goals (calories/protein/carbs/fats) + Meal Plans | Kahunas macro targets map to Everfit Macro Goals. Detailed meal plans must be rebuilt. |
| 7 | Check-in forms | Check-In Forms / Questionnaires | Rebuild form templates manually. Field types may differ. |
| 8 | Daily habits | Habits & Tasks | Map Kahunas habits (steps, sleep, water, etc.) to Everfit built-in habits + custom tasks. |
| 9 | Initial questionnaire | Welcome Form / Custom Questionnaire | Rebuild as Everfit form template. |
| 10 | Messages | Private Messaging / Broadcast | History does NOT transfer. Start fresh in Everfit. |
| 11 | Progress photos | Progress Photos | Must be re-uploaded or client re-submits. No bulk transfer path. |
| 12 | Body metrics | Body Metrics (default + custom) | Metric names/types must be mapped. Custom metrics created in Everfit. Historical data does NOT transfer unless manually entered. |
| 13 | Packages (billing) | Packages (Stripe-powered) | Recreate pricing tiers. Payment history stays in Stripe. |
| 14 | The Vault (content) | Resource Collections | Reorganize into Everfit's collection/section structure (max 25 resources per collection). |
| 15 | Supersets / Circuits / EMOMs | Supersets (in Regular sections) / Interval sections / AMRAP sections | Circuits map to supersets. EMOMs map to Interval/Timed sections. |
| 16 | Lead generation forms | Onboarding Flows + Packages with Sequences | Rebuild using Everfit's onboarding system. |
| 17 | Automations (email/chat/push) | Autoflows (Exact Date or By Day Sequence) | Rebuild automation logic. Autoflows support workouts, tasks, messages, announcements. |
| 18 | Calendar events | Client training calendar + Tasks | Training events = program calendar. Appointments = manual tasks. |
| 19 | Goals | Goals (bidirectional text) | Simplified in Everfit -- text-based, shared between coach and client. |
| 20 | Wearable data | Wearable Integrations (Apple Health, Google Fit, Fitbit, Garmin, Oura) | Client re-connects wearable on Everfit app. Historical data re-syncs automatically for supported data types. |

### 2B. No Direct Equivalent (Requires Workaround or Omission)

| Kahunas Data Type | Issue | Workaround |
|-------------------|-------|-----------|
| Workout logs (historical) | Everfit has no bulk import for historical workout data | Export key PRs/maxes manually, enter as notes or initial metric entries |
| Nutrition logs (historical) | Everfit has no import for food journal history | Summarize key trends in client notes. Client starts fresh. |
| Check-in submission history | No import path | Screenshot/PDF critical submissions before migration. Store in Resource Collections. |
| Voice notes | No transfer mechanism | Not transferable. Archive critical ones locally. |
| Health Score AI | Kahunas proprietary feature | No equivalent. Use Everfit's wearable data + manual tracking. |
| Progress photo overlay | Kahunas proprietary feature | Everfit has standard progress photos but no overlay comparison tool. |
| Supplement plans | No dedicated feature in Everfit | Use Resource Collections or client notes to store supplement protocols. |

---

## 3. Extraction Methods by Data Type

### CRITICAL CONSTRAINT
Kahunas has no API, no CSV export, and no bulk download. Every extraction method below works around this limitation.

| # | Data Type | Extraction Method | Tool / Process | Effort |
|---|-----------|------------------|----------------|--------|
| 1 | **Client list** | **GDPR data request** + manual screenshot | Email support@kahunas.io requesting all client data in machine-readable format (GDPR Art. 20). Supplement with manual export: open client list in Chrome, screenshot or copy-paste into spreadsheet. | Low-Medium |
| 2 | **Client contact info** | **Zapier trigger** (if Growth+ plan) | Use Zapier "Get Packages" trigger to pull client associations. Or manually copy from each client profile. | Low |
| 3 | **Workout programs** | **Manual screen capture + PDF rebuild** | For each program: (1) Open in Kahunas, (2) Screenshot or copy every workout day's exercises/sets/reps into a structured spreadsheet or Google Doc, (3) Use Everfit's AI PDF import to recreate. | HIGH |
| 4 | **Custom exercises** | **Manual inventory** | Open exercise library in Kahunas, list every custom exercise (name, type, video source). For YouTube/Vimeo-linked exercises, copy the URL. For direct uploads, screen-record or re-download if possible. | HIGH |
| 5 | **Exercise videos (uploaded)** | **Browser download or screen record** | Right-click video in browser > Inspect Element > find video URL in Network tab > download. If DRM-protected, screen-record each video. | HIGH |
| 6 | **Exercise videos (YT/Vimeo)** | **Copy link** | Just copy the URL from each exercise. These work directly in Everfit. | LOW |
| 7 | **Nutrition plans** | **PDF download** (native) | Kahunas supports PDF download of nutrition plans. Download each client's plan. Rebuild macro targets in Everfit. | Medium |
| 8 | **Check-in form templates** | **Manual copy** or **Zapier** | Zapier exposes check-in form structure (Growth+). Otherwise, screenshot each form template and rebuild in Everfit. | Medium |
| 9 | **Check-in submissions** | **Zapier** (partial) or **manual screenshot** | Zapier can pull form data. For completeness, screenshot important historical submissions. | Medium |
| 10 | **Daily habit templates** | **Zapier** or **manual copy** | Zapier exposes daily check-in forms. Copy template structure and rebuild. | Low |
| 11 | **Initial Q&A templates** | **Zapier** or **manual copy** | Zapier exposes Q&A forms. Copy and rebuild. | Low |
| 12 | **Initial Q&A responses** | **Manual screenshot** | Open each client's Q&A responses, screenshot/copy critical answers. | Medium |
| 13 | **Messages** | **Not extractable** | No export path. Screenshot critical conversations if needed. Accept data loss. | N/A |
| 14 | **Progress photos** | **Manual download** | Open each client's progress photos, right-click save or screenshot. | HIGH (if many clients) |
| 15 | **Body metrics history** | **Manual screenshot** | Screenshot metric charts for key clients. Enter current values in Everfit as baseline. | Medium |
| 16 | **Billing / payment history** | **Stripe/PayPal dashboard** | Export transaction history directly from Stripe or PayPal (independent of Kahunas). Recreate packages in Everfit. | Low |
| 17 | **The Vault content** | **Manual download** | Download every file (video, PDF, ebook, audio) from The Vault. Re-upload to Everfit Resource Collections. | Medium-High |
| 18 | **Automations** | **Manual documentation** | Document each automation rule (trigger, action, timing). Rebuild as Everfit Autoflows. | Medium |
| 19 | **Lead gen forms** | **Manual copy** | Screenshot form fields. Rebuild using Everfit Onboarding Flows + Packages. | Low |
| 20 | **Wearable data** | **No extraction needed** | Client reconnects wearable to Everfit. Data re-syncs from Apple Health / Google Fit / Fitbit / Garmin / Oura. | None |

### Extraction Workflow Summary

```
Phase A: Automated/Bulk (do first)
  1. Submit GDPR data request to support@kahunas.io
  2. Export Stripe/PayPal transaction history
  3. Set up Zapier to pull all available form templates (if on Growth+ plan)
  4. Copy all YouTube/Vimeo exercise video URLs into a spreadsheet

Phase B: Systematic Manual Capture (browser-based)
  5. Inventory custom exercises (name, type, video source) into spreadsheet
  6. Screenshot/copy each workout program structure per client
  7. Download nutrition plan PDFs
  8. Download all Vault content files
  9. Download progress photos for active clients
  10. Screenshot body metric charts for active clients

Phase C: Accept Loss
  11. Message history -- not recoverable, inform clients
  12. Historical workout logs -- capture key PRs only
  13. Historical nutrition logs -- summarize trends in notes
  14. Voice notes -- archive critical ones locally, accept loss on rest
```

---

## 4. Everfit Build Order

**Dependencies dictate this sequence. Items higher in the list are prerequisites for items below.**

### Phase 1: Foundation (Days 1-2)

| Step | Action | Dependency | Notes |
|------|--------|------------|-------|
| 1.1 | **Set up Everfit workspace** | None | Configure coach account, branding, timezone, measurement units |
| 1.2 | **Configure custom body metrics** | None | Create all custom metrics that existed in Kahunas (beyond Everfit defaults) |
| 1.3 | **Build exercise library** | None | Create all custom exercises with correct category, tracking fields, muscle groups, video links/uploads. This is the longest single task. |
| 1.4 | **Upload exercise videos** | 1.3 | Attach re-downloaded videos or YouTube/Vimeo links to each exercise |
| 1.5 | **Set up Stripe integration** | None | Connect Stripe account to Everfit for payments |

### Phase 2: Templates & Content (Days 3-5)

| Step | Action | Dependency | Notes |
|------|--------|------------|-------|
| 2.1 | **Build form templates** | None | Recreate check-in forms, daily habit forms, welcome/Q&A forms |
| 2.2 | **Create nutrition ingredients** | None | Use CSV bulk upload (up to 500 at a time) for any custom ingredients |
| 2.3 | **Build recipes and recipe books** | 2.2 | Recreate meal plan recipes if applicable |
| 2.4 | **Build workout templates** | 1.3 | Create reusable workouts in Workout Library. Use Everfit AI PDF import where possible. |
| 2.5 | **Build program templates** | 2.4 | Assemble workouts into multi-week programs in Program Library |
| 2.6 | **Upload Resource Collections** | None | Re-upload Vault content (PDFs, videos, docs) into Everfit Resource Collections |
| 2.7 | **Create packages** | 1.5 | Set up billing packages (recurring/one-time) with pricing |

### Phase 3: Automation & Flows (Days 5-7)

| Step | Action | Dependency | Notes |
|------|--------|------------|-------|
| 3.1 | **Build Autoflows** | 2.4, 2.5, 2.1 | Recreate automation sequences (program delivery, tasks, messages, announcements) |
| 3.2 | **Build Onboarding Flows** | 2.1, 2.5, 2.6 | Set up new-client onboarding: forms, welcome messages, auto-assignments |
| 3.3 | **Create Sequences** | 2.7, 3.1 | Link package purchases to onboarding + program delivery |
| 3.4 | **Set up Forums** (if applicable) | None | Create community spaces |

### Phase 4: Client Migration (Days 7-10)

| Step | Action | Dependency | Notes |
|------|--------|------------|-------|
| 4.1 | **Bulk upload clients via CSV** | All above | Upload client list (name, email, category). Do NOT send invites yet. |
| 4.2 | **Configure individual clients** | 4.1 | For each active client: assign program, set macro goals, add notes/injuries/limitations, enter current body metrics as baseline |
| 4.3 | **Assign content and forms** | 4.1, 2.1, 2.6 | Assign Resource Collections, Recipe Books, Check-in Forms, Habits to each client |
| 4.4 | **Assign Autoflows** | 4.1, 3.1 | Enroll clients in appropriate Autoflows |
| 4.5 | **Upload progress photos** (if critical) | 4.1 | Re-upload key progress photos per client if retention is important |
| 4.6 | **Enter baseline metrics** | 4.1, 1.2 | Enter current weight, body fat, key measurements as starting point |

### Phase 5: Testing & Cutover (Days 10-14)

| Step | Action | Dependency | Notes |
|------|--------|------------|-------|
| 5.1 | **Internal testing** | All above | Coach walks through every client's Everfit profile as if they were the client |
| 5.2 | **Beta test with 2-3 clients** | 5.1 | Invite select clients, collect feedback |
| 5.3 | **Fix issues from beta** | 5.2 | Adjust based on client feedback |
| 5.4 | **Send invites to all clients** | 5.3 | Batch send Everfit invites |
| 5.5 | **Decommission Kahunas** | 5.4 + 30 days | Keep Kahunas active for at least 30 days as fallback |

---

## 5. Risk Checklist

### Data Loss Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|-----------|------------|
| **Historical workout logs lost** | Medium | CERTAIN | Capture key PRs/maxes before migration. Communicate to clients that history starts fresh. |
| **Historical nutrition logs lost** | Low | CERTAIN | Summarize trends in client notes. Clients restart food logging in Everfit. |
| **Message history lost** | Medium | CERTAIN | Screenshot critical coaching conversations. Inform clients this will not transfer. |
| **Progress photos lost** | High | HIGH | Download all photos before decommissioning Kahunas. Re-upload critical ones to Everfit. |
| **Check-in submission history lost** | Medium | HIGH | PDF/screenshot critical submissions. Store in Resource Collections if needed. |
| **Custom exercise videos lost** | High | MEDIUM | Download all directly-uploaded videos from Kahunas before account closes. Verify each video plays in Everfit after upload. |
| **GDPR request returns incomplete data** | Medium | MEDIUM | Do not rely solely on GDPR request. Manually extract critical data in parallel. |
| **Kahunas terminates account early** | Critical | LOW | Per their TOS, they can terminate "without notice." Extract all data before notifying them of departure. |
| **Vault content inaccessible after migration** | Medium | MEDIUM | Download all Vault files immediately. Do not wait until cutover. |

### Client Disruption Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|-----------|------------|
| **Clients confused by new app** | Medium | HIGH | Send advance notice 2 weeks before cutover. Create a video walkthrough of the new app. |
| **Active program mid-cycle interrupted** | High | HIGH | Time migration to align with program phase transitions where possible. For mid-cycle clients, rebuild their current week + remaining weeks only. |
| **Clients lose access during transition** | High | LOW | Run both platforms simultaneously for 2-4 weeks during cutover. |
| **Client fails to install new app** | Medium | MEDIUM | Send step-by-step install instructions. Follow up individually with non-responsive clients within 48 hours. |
| **Billing disruption** | High | MEDIUM | Pre-configure all Everfit packages. Transition billing on the client's next renewal date, not mid-cycle. |
| **Wearable data gap** | Low | MEDIUM | Prompt clients to connect wearables to Everfit immediately upon onboarding. |

### Technical / Edge Case Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|-----------|------------|
| **Exercise name mismatches** | Medium | HIGH | Build a canonical exercise name mapping spreadsheet. Verify every custom exercise is correctly recreated. |
| **Workout structure differences** | Medium | HIGH | Kahunas EMOMs/circuits may not map 1:1 to Everfit sections. Test each complex workout type manually. |
| **Everfit AI PDF import errors** | Medium | MEDIUM | Always manually verify AI-imported workouts against source. Do not trust AI output without review. |
| **Video format incompatibility** | Low | LOW | Everfit accepts .mp4/.mov/.flv/.3gp/.avi, max 300MB. Convert files if needed before upload. |
| **Metric unit mismatches** | Medium | MEDIUM | Verify kg/lbs and metric/imperial settings per client before entering data. |
| **Autoflow timing drift** | Medium | LOW | Test Autoflow delivery dates with a test client before live rollout. |
| **Stripe subscription duplication** | High | MEDIUM | Cancel Kahunas-linked Stripe subscriptions only after Everfit subscriptions are confirmed active. Never leave a client double-billed. |

---

## 6. Testing and Validation Plan

### 6A. Pre-Migration Validation (Before Inviting Any Clients)

| Test | Method | Pass Criteria |
|------|--------|--------------|
| **Exercise library completeness** | Compare Kahunas custom exercise list vs. Everfit library side-by-side | Every custom exercise exists in Everfit with correct name, type, video, and tracking fields |
| **Exercise video playback** | Open every custom exercise in Everfit, play video | All videos play correctly. No broken links, no buffering failures. |
| **Workout structure accuracy** | For each program template, compare Kahunas workout day-by-day against Everfit | Exercise order, sets, reps, rest, tempo, RPE match source. Supersets/circuits/EMOMs structured correctly. |
| **Program calendar accuracy** | View each program in Everfit calendar view | Correct number of weeks, workouts on correct days, rest days correct |
| **Form template accuracy** | Compare each Kahunas form template to Everfit form | All fields present, correct field types, correct order |
| **Nutrition accuracy** | Compare macro targets per client | Calories, protein, carbs, fats match Kahunas values |
| **Resource Collections** | Open every resource in Everfit | All PDFs render, videos play, links resolve |
| **Package pricing** | Compare Kahunas package prices to Everfit packages | Amounts, frequency, trial periods match |
| **Autoflow delivery** | Create test client, enroll in each Autoflow, advance through timeline | Correct content delivered on correct days |
| **Onboarding flow** | Simulate new client signup through each Onboarding Flow | Forms, messages, assignments trigger correctly |

### 6B. Beta Client Validation (2-3 Volunteer Clients)

| Test | Method | Pass Criteria |
|------|--------|--------------|
| **App install and login** | Client installs Everfit app, logs in | Smooth onboarding, no errors |
| **Workout visibility** | Client opens today's workout | Correct exercises, sets, reps displayed. Videos play. |
| **Workout logging** | Client completes a workout and logs results | Data saves correctly. Coach sees logged data. |
| **Check-in submission** | Client submits a check-in form | Coach receives submission. All fields captured. |
| **Habit tracking** | Client logs daily habits for 3 days | Data appears in coach dashboard. |
| **Messaging** | Client sends message to coach | Message delivered. Coach can reply. |
| **Nutrition tracking** | Client logs a meal | Macros calculate correctly. Coach can view food journal. |
| **Wearable sync** | Client connects Apple Health / Google Fit | Activity, sleep, HRV data appears in Everfit |
| **Notification delivery** | Client receives push notifications | Workout reminders, check-in reminders, messages arrive |
| **Client feedback** | Ask: "Is anything missing compared to the old app?" | No critical gaps reported |

### 6C. Post-Cutover Validation (First 7 Days After Full Migration)

| Check | Frequency | Action if Failed |
|-------|-----------|-----------------|
| All clients have logged in | Day 1, Day 3, Day 7 | Follow up individually with non-responsive clients |
| No duplicate billing | Day 1 | Audit Stripe for overlapping Kahunas + Everfit charges. Refund immediately if found. |
| Workout completion rates normal | Day 7 | Compare to Kahunas baseline. Investigate drops > 20%. |
| Check-in submission rates normal | Day 7 | Follow up with clients who missed check-ins. |
| Zero support tickets about missing data | Day 7 | Remediate any missing exercises, programs, or content. |
| Autoflows delivering correctly | Day 3, Day 7 | Spot-check 5 clients' upcoming schedules. |

---

## 7. Cutover Strategy

### Timeline: 14-Day Transition Window

```
Day -14:  ANNOUNCE migration to clients (email + in-app message via Kahunas)
          "We're upgrading to a new, better coaching app. Here's what to expect."

Day -14:  BEGIN data extraction from Kahunas (Phase A + B from Section 3)
          Submit GDPR data request
          Export Stripe history
          Start manual data capture (programs, exercises, content)

Day -10:  COMPLETE Everfit foundation build (exercise library, workspace config)

Day -7:   COMPLETE template build (workouts, programs, forms, content)

Day -5:   COMPLETE automation build (Autoflows, Onboarding, Sequences)

Day -4:   BULK UPLOAD clients to Everfit (no invites yet)
          Configure each active client's profile, programs, metrics

Day -3:   INTERNAL TESTING - coach validates every client's Everfit setup

Day -2:   BETA LAUNCH - invite 2-3 volunteer clients
          Collect feedback, fix issues

Day 0:    CUTOVER DAY
          ├── Morning: Send Everfit invites to all remaining clients
          ├── Morning: Send detailed onboarding email with:
          │   ├── App download links (iOS + Android)
          │   ├── Login instructions
          │   ├── Video walkthrough of new app
          │   └── "What changed" FAQ
          ├── Afternoon: Follow up with clients who haven't installed
          └── Evening: Verify all clients can access their programs

Day +1:   MONITOR - Check login rates, workout completions, messages

Day +3:   FOLLOW UP with any clients who haven't engaged

Day +7:   FIRST FULL VALIDATION - Run all post-cutover checks from 6C

Day +14:  SECOND VALIDATION - Confirm all metrics stable

Day +30:  DECOMMISSION KAHUNAS
          ├── Final data extraction pass (anything missed)
          ├── Download all remaining content
          ├── Cancel Kahunas subscription
          └── Archive Kahunas login credentials
```

### Client Communication Templates

**Day -14 Announcement (send via Kahunas messaging + email):**
> We're moving to a new coaching app called Everfit starting [DATE]. This upgrade gives you a better workout tracking experience, improved nutrition tools, and a smoother app. Your programs, nutrition plans, and check-in forms will all be set up and waiting for you. You'll receive an invite email from Everfit on [CUTOVER DATE] with instructions to download the app and log in. No action needed from you until then.

**Day 0 Invite Email:**
> Your new coaching app is ready. Here's how to get started:
> 1. Download Everfit: [iOS link] | [Android link]
> 2. Open the email invitation from Everfit and tap "Accept"
> 3. Log in and you'll see your current program ready to go
> 4. Connect your wearable (Apple Watch, Fitbit, etc.) in Settings
> If you have any questions, message me directly in the new app.

**Day +3 Non-Responsive Follow-Up:**
> Hey [NAME], just checking in -- have you had a chance to download the Everfit app yet? I want to make sure you don't miss any workouts. Let me know if you need help getting set up.

### Billing Cutover Rules

1. **Do NOT cancel Kahunas subscriptions until Everfit subscriptions are confirmed active for each client**
2. **Align transition to each client's billing cycle** -- switch on their next renewal date, not mid-cycle
3. **If a client is billed on both platforms**, refund the Kahunas charge immediately
4. **Keep Stripe connected to both platforms during the 30-day overlap** -- monitor for duplicates daily
5. **For clients on annual plans**, prorate the Kahunas remainder and credit toward Everfit if needed

---

## Assumptions and Unknowns

### Assumptions
- You are on Kahunas Growth ($69/mo) or Ultimate ($99/mo) plan, giving access to Zapier integration
- Your Stripe account is independent and can be connected to Everfit without disrupting existing subscriptions
- You have fewer than 100 active clients (affects effort estimates for manual extraction)
- Custom exercise count is under 200 (affects exercise library rebuild time)
- Workout programs are primarily "Detailed" type (not PDF uploads)
- You own all uploaded video content and can legally re-host it on Everfit

### Unknowns
- **GDPR response time and format** -- Kahunas may take up to 30 days to respond, and the format is undocumented
- **Direct-upload video retrievability** -- unclear if you can download videos you uploaded to Kahunas, or if they are locked in their CDN
- **Kahunas account termination behavior** -- their TOS allows termination without notice; extract data before announcing departure
- **Everfit API token availability** -- API tokens require contacting Everfit; availability may depend on your plan tier
- **Everfit plan tier** -- some features (Autoflows, On-Demand Collections, Forums) require specific Everfit plan tiers

---

## Priority Matrix: What to Migrate vs. What to Restart Fresh

| Priority | Data Type | Action |
|----------|-----------|--------|
| **P0 - Must migrate** | Client profiles, active workout programs, current nutrition targets, exercise library (custom), exercise videos, billing packages, content library (Vault) | Full rebuild in Everfit |
| **P1 - Should migrate** | Check-in form templates, daily habit templates, initial Q&A templates, automation rules, onboarding flows | Rebuild templates; historical data is nice-to-have |
| **P2 - Nice to have** | Progress photos, body metric history, check-in submission history, initial Q&A responses | Capture snapshots; client starts fresh in Everfit |
| **P3 - Accept loss** | Message history, historical workout logs, historical nutrition logs, voice notes, Health Score AI data | Not recoverable. Document for clients. |
