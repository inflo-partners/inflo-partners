# YouTube Video Script — Inflo Partners
## "How I Automated My Entire Agency with Claude Code"

**Length:** ~13-15 minutes
**Audience:** Agency owners, operators, consultants doing $10k-$100k+/month
**Traffic:** Cold/Warm — Flywheel funnel (embedded selling, no hard pitch)
**Format:** Talking head + screen share (Gamma deck as visual companion)
**Funnel:** All videos feed to this as a core video, CTA to free audit call

---

## [0:00] HOOK

[SLIDE: Title/Hook Slide]

[CAMERA: talking head, direct to lens]

Most agency owners are using AI wrong.

They open ChatGPT or Claude, type a question, get an answer, and think they're using AI.

That's not automation.

That's a fancy Google search.

What I'm going to show you today is how I turned Claude into an operating system for my entire business.

Not just a writing assistant.

An actual team of AI employees that know my clients, know our frameworks, write in the right brand voice, and produce deliverables without me re-explaining anything.

This morning I used it to build a full presentation deck.

Last week it wrote a 7-email nurture sequence for a partner in about 4 minutes.

I'm going to show you the exact architecture, walk you through how it works, and show you a live demo.

By the end of this video you'll know how to build this for your own business.

Let's get into it.

---

## [0:45] PROBLEM

[SLIDE: Problem Slide]

[CAMERA: talking head]

Here's the problem most operators run into with AI.

Every single session, you start from zero.

You open a new chat, you explain who you are, who your client is, what the offer is, what the brand voice sounds like, what the audience cares about.

You spend 10 minutes prompting before you get anything useful.

And the next day, you do it again.

That's not a system.

That's just manual labor with extra steps.

I was doing this myself six months ago.

For every client deliverable, every email sequence, every landing page, every ad script, I was re-explaining context every single time.

It was burning hours.

Hours that should have taken minutes.

And the output was inconsistent because Claude only knew what I told it in that one session.

There was no memory, no continuity, no permanent context.

The moment you close the chat, everything resets.

That's the core problem.

And that's exactly what I fixed.

---

## [2:00] MID-VIDEO CTA

[CAMERA: talking head, casual delivery]

By the way, if you want my team to build a system like this for your business, the first link in the description has a spot to book a free audit call.

We'll look at your current setup and map out exactly what needs to change.

But for now, let's get back into this.

---

## [2:15] THE SOLUTION OVERVIEW

[SLIDE: Solution Overview Slide]

[CAMERA: talking head, then transition to screen share]

What I built is called a Claude Code workspace.

It's a folder structure on my computer that Claude reads every single time I open a session.

The result is an AI that already knows everything about my business before I type a single word.

It knows Inflo Partners, what we do, who we work for, our frameworks, our voice, our clients.

Every agent I invoke has full context from the start.

I never re-explain anything.

There are five layers to this system.

I'm going to walk you through each one.

[CAMERA: switch to screen share, Gamma deck visible]

---

## [3:00] LAYER 1: CLAUDE.MD

[SLIDE: Layer 1 - CLAUDE.md, "Your Business Brain"]

[CAMERA: screen share]

Layer one is a single file called CLAUDE.md.

Think of it as your business brain.

This file contains everything Claude needs to know about your business permanently.

What the business does, who the clients are, the core frameworks we use, the workspace structure, brand voice rules, what agents exist and how to invoke them.

It lives in the root of the project folder.

And because of how Claude Code works, it reads this file at the start of every single session, automatically.

You never have to re-explain your business again.

Every conversation starts with Claude already knowing you.

Here's what mine looks like.

[CAMERA: zoom into CLAUDE.md on screen, scroll briefly]

You can see the full business overview is in here.

The 7-11-4 rule, which is the core conversion framework we build every client's system around.

The partner workspace structure.

The agents, what they do, how to call them.

The output styles, which I'll explain in a minute.

This one file is the foundation everything else runs on.

Without it, Claude is a blank slate every session.

With it, Claude is a fully briefed operator.

---

## [4:30] LAYER 2: AGENTS

[SLIDE: Layer 2 - Agents, "Your AI Employees"]

[CAMERA: screen share]

Layer two is the agents folder.

These are your AI employees.

Each agent is a markdown file with a specific role, a specific set of instructions, and a specific area of expertise baked in.

I have five of them.

The landing page builder designs and codes full landing pages.

The email sequence writer handles nurture sequences, pre-call flows, post-call follow-up, re-engagement.

The VSL scriptwriter produces full video sales letter scripts with timing markers.

The ad copy writer handles Meta, Google, and YouTube ads.

And the funnel strategist plans the full architecture for any given partner before we build anything.

To use them, I just type the agent name with an @ symbol.

@email-sequence-writer, and it activates that specific agent.

That agent comes pre-loaded with its domain expertise.

And because CLAUDE.md is always active, the agent also has full business context from the start.

It already knows what Inflo does, what our framework is, and who we serve.

You combine a specialized agent with global business context, and you get output that's actually usable, not a generic template you have to rewrite from scratch.

---

## [5:45] LAYER 3: SKILLS

[SLIDE: Layer 3 - Skills, "Your SOPs & Playbooks"]

[CAMERA: screen share]

Layer three is the skills folder.

These are your SOPs and playbooks in file form.

Every methodology we use at Inflo is documented as a skill file that agents can reference automatically.

I have eight of them right now.

Conversion principles, which has the full 7-11-4 framework and contextual marketing logic.

Landing page architecture, the exact section order and CTA rules.

Email sequence framework, sequence types and timing rules.

VSL script framework, hook formulas and full script structure.

Ad copy framework, platform specs and copy formulas for Meta, Google, and YouTube.

YouTube organic funnel, which is the full channel strategy SOP including funnel types, CTA rules, retention targets, posting cadence, everything.

Client onboarding, the full partner onboarding process.

And gamma deck framework, which is a presentation deck SOP for building slide decks.

[CAMERA: scroll through skills folder briefly]

When I invoke the landing page builder, it automatically references the landing page architecture skill.

When I invoke the email writer, it references the email sequence framework.

The agents know which skills to pull from because that's written into their system prompt.

So the output isn't just good writing.

It's writing built on proven methodology.

That's the difference between getting generic copy and getting copy that's actually engineered to convert.

---

## [7:00] LAYER 4: OUTPUT STYLES

[SLIDE: Layer 4 - Output Styles, "Brand Voices Per Partner"]

[CAMERA: screen share]

Layer four is output styles.

This is how I solve the brand voice problem at scale.

Every client sounds different.

A financial advisory firm writes nothing like a fitness coach.

A B2B SaaS company sounds nothing like a real estate fund.

Without a system, you're either prompting the voice from scratch every time, or everything starts sounding the same.

I have four brand voice profiles.

Financial advisory for wealth, tax, and advisory firms.

Coaching and fitness for transformation offers.

SaaS and B2B for software companies and service providers.

Real estate and capital for fund managers and syndicators.

Each one is a detailed file with tone rules, vocabulary, what to do and what never to do, and example copy in that voice.

And here's the key part.

Each partner's workspace has a PARTNER.md file.

That file specifies which output style to use.

Every agent reads the PARTNER.md when working on that partner's deliverables, sees the output style, and automatically adapts.

No prompting for voice.

No reminding Claude what this client sounds like.

The system handles it.

---

## [8:15] LAYER 5: PARTNER WORKSPACES

[SLIDE: Layer 5 - Partners, "Partner Workspaces"]

[CAMERA: screen share, navigate to partners folder]

Layer five is the partner workspaces.

Every client gets their own folder.

Inside that folder is a PARTNER.md file.

This is the client brief.

It has the offer details, the target audience, proof points and case study numbers, the brand voice, the output style, the funnel stage, everything.

Underneath that is a folder for funnels, one for emails, and one for VSL scripts.

When a new partner joins, I run one command.

[CAMERA: open terminal briefly, show onboard_client.py reference]

There's a Python script called onboard_client.py in the execution folder.

That script creates the entire partner workspace automatically.

Folder structure, PARTNER.md template pre-populated, all of it, in one command.

From that point forward, every agent automatically has full context on that partner.

I don't brief them.

I don't re-explain the offer.

I just invoke the agent and say what I need built.

---

## [9:15] HOW IT ALL FITS

[SLIDE: Connection Slide - "How It All Fits"]

[CAMERA: talking head]

Let me connect the layers so you can see the full picture.

CLAUDE.md is always running in the background.

It holds the global business context.

Agents are your specialized team members.

Each one knows its job and has domain expertise baked in.

Skills are the methodology layer.

Agents reference skills automatically so every output is built on proven frameworks.

Output styles are the voice layer.

Every deliverable automatically matches the client's brand.

Partner workspaces are the context layer.

Every agent knows the specific client they're working on without being told.

The result is this.

I open a session, navigate to a partner folder, invoke an agent, tell it what I need, and get a fully context-aware, methodology-driven, brand-voice-correct deliverable.

No re-prompting.

No explaining.

No starting from zero.

That's the system.

---

## [10:00] DEMO TRANSITION

[SLIDE: Transition - "Let Me Show You This Live"]

[CAMERA: talking head]

Let me actually show you how this works in practice.

[CAMERA: full screen share, Claude Code terminal visible]

---

## [10:15] DEMO

[SLIDE: Demo Slides]

[CAMERA: screen share, live demo]

I'm going to show you three things.

First, I'll invoke the email sequence writer for an existing partner.

Watch how it already knows the client, the offer, the audience, the brand voice.

I don't tell it any of that.

[CAMERA: navigate to partner folder, invoke @email-sequence-writer, show the output beginning to generate]

You can see it's already pulling in the partner's offer details, their audience profile, and writing in the correct brand voice.

I didn't tell it any of that.

That's the PARTNER.md and output style doing the work.

Second, let me show you the onboarding script.

[CAMERA: navigate to execution folder, show onboard_client.py briefly]

One Python script.

One command.

It creates the entire partner workspace.

The folder structure, the PARTNER.md template, the subfolders.

Everything a new client needs to be fully set up in the system, done instantly.

Third, I want to show you the Gamma deck I built this morning.

[CAMERA: open Gamma deck or share browser with the deck visible]

This deck was built using the gamma-deck-framework skill in combination with Gamma's AI tool.

The framework told Claude exactly how to structure the slides, what copy rules to follow, how many words per slide, the layout logic.

The whole thing took less than an hour from idea to finished deck.

And it's the visual companion for this exact video.

That's the system working end to end.

---

## [11:30] PROOF

[SLIDE: Proof/Results Slide]

[CAMERA: talking head]

Now I want to show you why this matters.

Because this system isn't just an internal tool.

It's how we build and run every client system at Inflo.

The speed at which we can produce deliverables, the consistency of the output, the fact that every agent is already briefed on every client, that's what lets us move the way we do.

Here's what that looks like in practice.

One partner came to us with an audience and zero monetization system.

We installed the system.

$36,500 cash collected in 30 days.

Same audience, just added infrastructure.

Another partner launched a brand new offer.

One setter, one closer, and a system.

$30,266 cash collected in 18 days.

A third partner was doing $1,000 a month.

We installed the system.

$27,000 the following month.

That's 27x growth in 30 days.

And a micro-creator with zero previous revenue collected $14,000 in their first 7 days after we installed the system.

These results aren't from a bigger audience or a bigger ad budget.

They're from a system that moves cold leads to pre-sold before they ever get on a call.

That's what the 7-11-4 framework does when it's actually installed.

---

## [12:30] THE POINT

[CAMERA: talking head]

Here's the point I want to make for your own business.

You don't need more time.

You need a system that removes the manual repetition from everything you already do.

Every time you explain your business to an AI from scratch, you're losing time.

Every time output comes back generic because Claude didn't have context, you're losing time.

Every time a team member has to ask you for the brief, you're losing time.

The workspace I showed you today solves all three of those problems.

CLAUDE.md handles context permanently.

Agents handle specialization without extra prompting.

Skills handle methodology so you're not reinventing the wheel.

Output styles handle brand voice automatically.

Partner workspaces handle client context at scale.

The system does the operational work.

You just direct it.

---

## [13:15] OUTRO CTA

[SLIDE: CTA Slide]

[CAMERA: talking head]

You have two options from here.

Option one, take everything I showed you today and build it yourself.

The architecture is all here.

CLAUDE.md, agents, skills, output styles, partner workspaces.

You have the full framework.

Option two, if you want to talk about how we build this for your business specifically, and on top of that, build the full conversion infrastructure that turns your leads into revenue at a significantly higher rate, click the first link in the description.

It'll take you to a short form.

Fill it out, book a time, and we'll do a free audit of your current setup.

We'll show you exactly where you're leaking revenue right now and what it would look like to fix it.

No pitch.

Just an honest look at your system and a clear plan to improve it.

If we're a good fit to work together, we'll talk about what that looks like.

If not, you'll still leave with something useful.

And if you're not ready for that yet, watch this video next.

[CAMERA: gesture to on-screen end card]

It breaks down the full funnel architecture we use for high-ticket offers, including how we think about contextual marketing for leads at different stages.

It connects directly to everything I showed you today.

I'm Shariq.

See you in the next one.

---

## Shooting Notes

**Screen share segments:** Use Claude Code terminal in a clean environment. Navigate partner folder before recording so it's already open.

**Gamma deck:** Have deck open in browser tab, pre-loaded before recording. Transition to it via screen share, not a split screen.

**Demo segment:** Pre-run the email writer invocation once in a test session so you know exactly what the output looks like. Record the demo cleanly in one take if possible.

**Pacing:** The talking head sections should be direct and move quickly. No pause-and-breathe moments. This audience is operators, they want information density.

**Thumbnail direction:** Claude Code terminal visible with something like "CLAUDE.md" or "@email-sequence-writer" on screen. Real work showing. No stock imagery. No lifestyle. Something an agency owner would immediately recognize as backend operational content.

**Title options:**
- "How I Automated My Entire Agency with Claude Code"
- "The Claude Code System That Runs My Agency"
- "I Built an AI Team for My Agency (Full Walkthrough)"

**Description (first link):** Free audit call booking link. Must be the very first line.

**Pinned comment:** Same audit link, posted immediately after publishing.

**Chapter markers:**
- 0:00 The Problem with How Most People Use AI
- 2:15 The System Overview
- 3:00 Layer 1: Your Business Brain (CLAUDE.md)
- 4:30 Layer 2: Your AI Employees (Agents)
- 5:45 Layer 3: Your SOPs (Skills)
- 7:00 Layer 4: Brand Voices (Output Styles)
- 8:15 Layer 5: Partner Workspaces
- 9:15 How It All Connects
- 10:15 Live Demo
- 11:30 Results
- 13:15 What to Do Next
