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
- clear separation between **source claims** and **BWM assessment**.

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
- **DFM resource record:** `jdlongmire/chatgpt-bridge/weltmodell/dfm/resources/fine-tuning-tour-ross-2026.md`

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
editorial_note:
technical_qualification:
related_pages: []
canonical_resources: []
```

ThinxAI should incorporate this requirement into the site information architecture and media implementation without creating a parallel source-of-truth system.
