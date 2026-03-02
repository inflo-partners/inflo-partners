---
name: gamma-deck-framework
description: SOP for turning YouTube video scripts into Gamma presentation decks, covering copy rules, layout standards, slide structure, and iteration workflow
---

# Gamma Deck Framework — SOP

## Purpose

Turn a YouTube video script or plan into a Gamma presentation deck. The deck serves two functions:

1. Visual companion during recording (screen share slides while talking head)
2. Standalone reference asset viewers can revisit after watching

## Copy Rules

Write at a Hemingway reading level (grade 5-6). Short sentences. Simple words. Conversational tone.

**Exceptions**: Keep technical terms and unique selling mechanisms as-is. If it's a moat (7-11-4 Rule, contextual marketing, PARTNER.md), don't dumb it down.

**Rules**:
- Every slide must be scannable: quick summary at the top, then detail below
- No tech jargon for non-technical audiences. Use relatable business terms.
- "Agents" becomes "AI employees." "Skills" becomes "SOPs and playbooks." "CLAUDE.md" becomes "your business brain."
- Lead with the problem. Follow with the system. Close with proof.
- No hype. No motivational fluff. No vague claims without numbers.
- No em dashes or en dashes. Use commas or separate lines.

## Headline Format

Every headline must be instantly understandable to someone with zero context about the topic.

**Layer/concept slides use a two-line title**:
- Line 1 (small label): The technical term — "Layer 1: CLAUDE.md"
- Line 2 (big headline): The plain-English explanation — "Your Business Brain"

The viewer sees the relatable headline first. The technical label provides context for people following along.

**Non-layer slides**: Single clear headline. Test it by asking: "Would someone who has never heard of this topic understand what this slide is about from the headline alone?"

## Layout Rules

**Density**: Use compact card layouts with minimal padding. Minimize white space throughout all slides. Information density matters more than visual breathing room.

**Grids**: Match the item count exactly. Never create empty placeholder boxes.
- 5 items = 3 on top row, 2 centered on bottom row
- 9 items = 3x3 grid
- 4 items = 2x2 grid
- 6 items = 3x2 grid or 2x3 grid

**Funnels and stacks**: Always flow top-down. Broadest/most general at the top. Narrowest/most specific at the bottom.

**Enforcing layout**: Use the `additionalInstructions` parameter in the Gamma generate call to explicitly tell Gamma the item count per slide and the grid structure. Gamma will create empty boxes if not told otherwise.

## Gamma Generate Settings

| Setting | Value | Why |
|---|---|---|
| format | `presentation` | Slide-based deck |
| textMode | `preserve` | Content is pre-written, don't rewrite |
| textOptions.amount | `detailed` | Preserve the full depth of each slide |
| imageOptions.source | `noImages` | Screenshots and visuals added manually after |
| themeId | Partner or Inflo theme ID | Use `get_themes` to find by name |
| numCards | Match slide count | One card per slide |
| additionalInstructions | Layout rules | Enforce compact cards, grid structures, funnel direction |

**Always use `additionalInstructions`** to enforce:
- Exact item counts per slide (no empty boxes)
- Grid layouts (3+2, 3x3, etc.)
- Compact card sizing
- Funnel/stack direction (top-down)
- Minimal white space

## Slide Structure Pattern

This is the proven structure from iterating across multiple video decks. Adapt as needed but follow the general arc.

### 1. Title Slide
- Hook headline that would make someone stop scrolling
- 1-2 sentence summary of what the video covers and what the viewer will see

### 2. Problem Slide
- Relatable pain point in simple language
- Frame it as something the viewer has experienced personally
- Use "you" language. Make them feel seen.
- End with a pivot: "What if [the fix]?"

### 3. Solution Slide
- What fixes the problem, high-level
- Don't go deep yet. Set up the detail slides.
- Introduce the system/tool/method in plain English

### 4. Detail Slides (one per concept or layer)
- Each slide has: small label + big headline + scannable body
- Start with a 1-2 sentence summary of what this piece is and why it matters
- Then detail: what it contains, how it works, what it does
- Use bullet points and short descriptions. Dense but readable.

### 5. Connection Slide
- How all the pieces fit together
- Visual: funnel, stack, or flow diagram (top-down, broad to specific)
- Quick description per layer. One line each.

### 6. Transition Slide
- "Now let me prove it" or "Let's see this in action"
- Summarize what you're about to do in 2-3 sentences
- Set expectations: what input goes in, what comes out

### 7. Demo/Proof Slides
- What happened during the live build
- What the input was (onboarding info, a single command, etc.)
- What came out (landing page sections, VSL script sections, etc.)
- Reinforce that no manual prompting or context-setting was needed

### 8. CTA Slide
- Clear ask. One sentence.
- What you're offering. Link reference.
- Optional: secondary CTA (watch another video)

## Iteration Workflow

Building a Gamma deck is not a one-shot process. Expect 3-5 iterations.

**V1 — Structure**: Get all slides in with the right content. Don't worry about layout, headline polish, or white space. Focus on completeness.

**V2 — Depth and Tone**: Add detail where slides feel thin. Fix copy tone to match Hemingway level. Make sure every slide is scannable with a summary at the top.

**V3+ — Layout and Polish**: Fix empty boxes, white space, headline clarity, and card sizing. This is where `additionalInstructions` becomes critical. Each regeneration should target specific layout problems.

**Rules across iterations**:
- Always use `textMode: preserve` so Gamma doesn't rewrite your content
- Copy changes go in the `inputText`. Layout changes go in `additionalInstructions`.
- Don't change both copy and layout in the same iteration. Fix one at a time so you can isolate what's working.

## Integration with Other Skills

| Skill | When to reference |
|---|---|
| `youtube-organic-funnel` | Video strategy, CTA placement (mid-video at ~30%, double outro CTA), content pillars |
| `vsl-script-framework` | When the video includes VSL content or the deck accompanies a VSL |
| `conversion-principles` | When the deck explains conversion frameworks or the 7-11-4 rule |
| `landing-page-architecture` | When the deck includes landing page build demos |

## Checklist Before Sharing

- [ ] All slides present with no missing content
- [ ] Headlines pass the "zero context" test (anyone can understand them)
- [ ] No empty boxes or wasted white space
- [ ] Grids match item counts exactly
- [ ] Funnels/stacks flow top-down
- [ ] Copy is Hemingway level (short, simple, conversational)
- [ ] Technical terms preserved, everything else in plain English
- [ ] Screenshot placeholders noted for manual addition
- [ ] CTA slide has a clear ask
