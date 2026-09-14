# Video Highlights Requirement

**Status:** ADDITIVE REQUIREMENT
**Added:** 2026-09-11
**Authority:** JD Longmire
**Parent:** WP-BWM-0001 Public Site Standup

## Requirement

The Biblical WorldModel public site shall include a **Video Highlights** section for curated third-party and project-produced videos that materially illuminate topics addressed by the WorldModel.

This is distinct from the existing narrated-explainer pipeline. Narrated explainers are BWM-produced media. Video Highlights is a curated resource surface that may point to external primary or secondary audiovisual material.

## Reader Experience

The site should support:

- a homepage or landing-page highlight for one or more current/recommended videos;
- a durable `/media/video-highlights/` collection or equivalent;
- responsive YouTube/video embeds where licensing and platform behavior permit;
- thumbnail, title, speaker/creator, publication date, runtime where available, and source link;
- a short BWM editorial note explaining why the video is relevant;
- topic/programme tags such as `DFM`, `cosmology`, `fine-tuning`, `biology`, `epistemology`, `CHFM`, or `foundations`;
- optional links from a highlight to the relevant BWM page, canonical research resource, or evidential ledger;
- clear separation between **source claims** and **BWM assessment**;
- an explicit external-resource alignment disclosure on every third-party video highlight.

## WorldModel Alignment Disclosure

Every third-party video highlight must make clear that inclusion does not imply full agreement with the creator's broader worldview, chronology, interpretive framework, scientific model, theological conclusions, or other claims outside the specific material being highlighted.

### Card-level label

Use a compact visible label on third-party video cards, such as:

**External Resource · Partial Alignment**

Equivalent wording is acceptable if it preserves the same meaning and remains visually distinct from project-produced media.

### Full disclosure

Each third-party video detail page or expanded highlight should include substantially the following disclosure:

> **WorldModel Note:** This video is included because it contains material relevant to the Biblical WorldModel research programme. Inclusion does not imply endorsement of the creator's broader worldview, chronology, interpretive framework, scientific model, or theological conclusions. Specific claims highlighted here may be compatible with or useful to DFM or another BWM programme while other positions held by the creator may differ materially from the Biblical WorldModel.

The disclosure should appear near the embed or in a clearly visible expandable section such as **Why we included this**. It should not be buried in a global footer or generic site disclaimer.

### Alignment assessment

Where useful, the editorial metadata may identify the specific scope of agreement and divergence. This is especially important when a creator's evidential argument is useful to DFM while the creator's broader model materially differs from DFM.

For example, Hugh Ross's cosmological fine-tuning arguments may be relevant to DFM evidential analysis while Ross's old-earth/progressive-creation framework differs substantially from DFM. The site should preserve that distinction explicitly.

## Epistemic Discipline

Inclusion in Video Highlights does not constitute blanket endorsement of a speaker, organization, argument, or every claim in the video. Each entry should identify its relevance and, where needed, qualify claims that are technically imprecise, disputed, or differently framed by BWM.

Prefer primary video sources and official creator/channel uploads. Reposts and excerpt channels should be used only when the primary source is unavailable and should be labeled accordingly.

## Initial Highlight

### The Fine-Tuning of the Universe for Life

- **Speakers:** Dr. James Tour and Hugh Ross
- **Published:** 2026-08-11
- **Platform:** YouTube
- **URL:** https://www.youtube.com/watch?v=HTF4y_9i3AY
- **Relevant domains:** DFM, cosmology, fine-tuning, initial conditions, Bayesian comparison
- **BWM relevance:** Provides an accessible discussion of cosmological fine-tuning, including the relationship among cosmic mass density, expansion history, stellar nucleosynthesis, and the availability of life-permitting elements.
- **Technical qualification:** The frequently cited `1 part in 10^60` figure should be presented specifically in relation to early-universe mass-density/critical-density or expansion-condition fine-tuning, rather than as an unrestricted statement that changing total universe mass by that fraction necessarily eliminates life.
- **Alignment:** Partial. Fine-tuning material is relevant to DFM; Hugh Ross's broader old-earth/progressive-creation framework is not DFM.
- **DFM resource record:** `jdlongmire/chatgpt-bridge/weltmodell/dfm/resources/fine-tuning-tour-ross-2026.md`

## Recommended Highlight: Genesis, Geology, and Uniformitarianism

### What EVERY Christian Today NEEDS to Realize About Genesis

- **Speaker:** Calvin Smith
- **Source creator:** Answers in Genesis Canada
- **Published:** 2025-10-31
- **Platform:** YouTube
- **URL:** https://www.youtube.com/watch?v=TtkmzlIHHFs
- **Video ID:** `TtkmzlIHHFs`
- **Relevant domains:** foundations, epistemology, earth history, Genesis, historical geology, uniformitarianism, catastrophism, retrodiction
- **BWM relevance:** Recommended primarily for its historical discussion of Charles Hodge, Charles Lyell, the rise of uniformitarian geology, Lyell's influence on Darwin, and the later re-entry of catastrophic processes into mainstream geology. It also provides a useful case study in distinguishing operational regularity from historical retrodiction.
- **Technical qualification:** The presentation contains historical and geological claims of differing evidential status. Significant quotations are to be traced to primary sources, and geological examples such as paraconformities, fossilization rates, and Grand Canyon contacts are to be evaluated separately before use as BWM evidence.
- **Alignment:** Partial. The video's high-level commitment to biblical authority and its critique of naive rate-uniformity overlap materially with BWM concerns. Inclusion does not imply that BWM adopts every geological inference, rhetorical characterization, chronology claim, or theological formulation in the presentation.
- **BWM research record:** `04-work-packages/WP-BWM-0018-historical-geology-harvest/`
- **Preserved transcript:** `04-work-packages/WP-BWM-0018-historical-geology-harvest/sources/TtkmzlIHHFs-transcript.md`

## Implementation Guidance

Treat highlights as structured content rather than hard-coded homepage markup. A small metadata record per video should drive both the collection page and any homepage featured-video component. This permits highlights to be added, retired, reordered, filtered by topic, and reused on relevant subject pages without duplicating content.

Suggested metadata fields:

```yaml
title:
speakers:
source_creator:
published:
runtime:
platform:
url:
video_id:
thumbnail:
topics: []
programmes: []
featured: false
resource_type: external | project-produced
alignment_status: aligned | partial | divergent | not-assessed
alignment_note:
editorial_note:
technical_qualification:
related_pages: []
canonical_resources: []
```

For any `resource_type: external` record, `alignment_status` and `alignment_note` are required. The rendering layer should automatically show the card-level external-resource label and full WorldModel disclosure rather than relying on an editor to remember to add boilerplate manually.

ThinxAI should incorporate this requirement into the site information architecture and media implementation without creating a parallel source-of-truth system.
