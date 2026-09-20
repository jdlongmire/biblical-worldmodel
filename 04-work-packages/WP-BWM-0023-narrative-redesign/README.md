# WP-BWM-0023 — Mobile-First Narrative Redesign

Status: active development

## Purpose

Develop the next BWM public narrative around the approved calculated-age video and the visual language shown in the redesign references. The work starts as a parallel mockup so readers can evaluate the direction before the current homepage is changed.

The proposed front door is:

> **Can a Calculated Age Differ From Actual History?**

The page then gives readers one accessible distinction and three routes into the existing body of work:

1. **The Model** — how BWM frames creation, starting conditions, and subsequent history.
2. **The Evidence** — what is observed, what is measured, and what assumptions connect data to reconstruction.
3. **The Tests** — predictions, falsifiers, objections, open problems, and the research programmes that own technical claims.

## Current artifact

The first visual artifact is live at [worldmodel.thinxai.net/mockup/](https://worldmodel.thinxai.net/mockup/). It is a presentation prototype, not a homepage migration. Its source is [mockup.md](../../03-solutions-baseline/site/docs/mockup.md), and it was published in commit `f16a9c6`.

## Content map

The working content map is [content-map.md](content-map.md). It traces each mockup section to existing BWM material and marks the bridge copy that still needs drafting.

## Requirements

### Narrative

- The first screen states the question in plain language and gives the video a written frame.
- The video argument is available in text so the page does not depend on playback.
- The observed-state / model-assumptions / extrapolated-age / historical-age distinction is explicit.
- The three paths describe what a reader will find without implying that every programme claim is settled.
- The page distinguishes BWM's interpretation from observations and from canonical programme claims.
- Strong objections and unresolved burdens remain visible in the reader journey.

### Accessibility

- The video has a descriptive title and a linked transcript or equivalent text treatment.
- Every meaningful image has useful alt text; decorative imagery is empty-alt or omitted from the reading order.
- The equation-like distinction is represented as semantic text, not only a decorative graphic.
- Text and controls meet the site's contrast requirements in both normal and focus states.
- The page is keyboard navigable, has a visible focus state, and preserves logical heading order.
- Mobile layout works without horizontal scrolling at the retained 320px–760px widths.
- Reduced-motion preferences suppress nonessential transitions.
- The page remains understandable when images, video, or external scripts fail.

### Editorial integrity

- Plain-language copy precedes acronyms and programme names.
- "Extrapolated age" remains the accessible gloss for the formal term "retrodictive age."
- No section presents a research proposal as an established result.
- Competing explanations receive symmetric description where the page compares them.
- Technical claims link to the repository or source that owns them.

## Acceptance criteria

- [x] A mobile-first visual mockup exists at `/mockup/` without changing the existing homepage.
- [x] The mockup uses the three-path architecture and the calculated-age video.
- [x] The mockup builds successfully through the strict Pages workflow.
- [ ] Content map traces each visible section to an approved source or declares new bridge copy.
- [ ] Transcript or equivalent written treatment is linked from the video section.
- [ ] The three path landing sections are drafted at the target reading level.
- [ ] Keyboard, focus, semantic-heading, contrast, and reduced-motion checks pass.
- [ ] Principal Operator accepts, revises, holds, or rejects the redesign direction.
- [ ] A separate migration package is approved before the current homepage is replaced.

## Boundaries and dependencies

This package depends on the approved Tier 1 material in WP-BWM-0005, the visual assets and provenance tracked by WP-BWM-0002, the canonical hierarchy in WP-BWM-0009, and the terminology in WP-BWM-0022. It may link into those materials, but it does not rewrite their canonical research content.

The existing homepage remains the public baseline until a later migration decision. No new video, image generation, private contact route, or Home-runtime change is part of this package.

## Verification plan

1. Run the strict MkDocs build and asset/link checks.
2. Run the retained browser checks at 320, 390, 760, 768, 960, 1024, and 1440px classes.
3. Inspect the mockup with keyboard navigation and a semantic heading/accessibility tree.
4. Test the page with video unavailable and images disabled.
5. Record source traceability and unresolved editorial decisions in this package.

Human-Curated, AI-Enabled (HCAE)
