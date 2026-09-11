# WP-BRIDGE-0002 Landing-Page Asset Workspace

**Status:** PRELIMINARY / ACTIVE  
**Parent:** [`WP-BRIDGE-0002-biblical-worldmodel-publication.md`](../WP-BWM-0001-public-site-standup/requirements.md)  
**Primary static-visual producer:** ChatGPT  
**Operational integrator:** ThinxAI / thinx

## Purpose

This workspace decomposes the approved Biblical WorldModel landing-page concept into reusable production assets suitable for a dynamic, responsive GitHub Pages implementation.

The generated desktop and mobile landing-page mockups are **design references only**. They must not be deployed as full-page raster images.

The production site should use semantic HTML/CSS/MkDocs components for headings, body text, quotations, navigation, calls to action, cards, links, status labels, community actions, and other interactive or explanatory content. Raster or vector graphics should provide visual substrate where graphics add explanatory or atmospheric value.

## Governing Rule

> **Do not bake into a generated image explanatory text, navigation, buttons, status labels, citations, or other content that can reasonably be rendered as responsive HTML.**

This rule exists to preserve accessibility, responsiveness, searchability, maintainability, localization potential, source synchronization, and mobile adaptation.

## Preliminary Asset Classes

### 1. Hero

- `BWM-HERO-DESKTOP` — wide landscape visual substrate for desktop/tablet hero.
- `BWM-HERO-MOBILE` — portrait/mobile crop or composition from the same visual language.

Hero assets contain no title, quotation, button, navigation, or explanatory copy.

### 2. Audience / Reader-Journey Cards

- `BWM-AUD-SEEKER`
- `BWM-AUD-CURIOUS`
- `BWM-AUD-DEEP`
- `BWM-AUD-SKEPTIC`

Each is an independent image without embedded title, description, CTA, or icon labels. HTML owns the card semantics.

### 3. Conceptual Assets

- `BWM-CONCEPT-LAYERS` — standalone layered WorldModel illustration.
- `BWM-CONCEPT-OBS-INF-HIST` — observation → inference → historical reconstruction.
- `BWM-CONCEPT-PROGRAMMES` — DFM / CHFM / TRT relationship map.
- `BWM-CONCEPT-FALSIFICATION` — objection/anomaly/falsification status progression.

Conceptual assets may contain minimal diagram labels when the label is intrinsic to the graphic, but should prefer SVG or HTML/CSS-rendered labels where practical.

### 4. Atmospheric / Support Assets

- footer or section landscape treatment;
- optional subtle textures/backgrounds;
- social/share derivatives;
- thumbnails supporting ThinxAI narrated-media artifacts.

These should remain subordinate to the site's information architecture.

## Preliminary Folder Model for Target Repository

```text
assets/
├── hero/
│   ├── hero-desktop.webp
│   └── hero-mobile.webp
├── audiences/
│   ├── seeker.webp
│   ├── curious-mind.webp
│   ├── deep-thinker.webp
│   └── skeptic-reviewer.webp
├── concepts/
│   ├── worldmodel-layers.svg|webp
│   ├── observation-inference-history.svg
│   ├── programme-map.svg
│   └── falsification-status.svg
├── support/
├── social/
└── sources/
```

Physical paths may be adjusted by ThinxAI to match the final MkDocs build conventions.

## Responsive Composition Model

The intended hero implementation is conceptually:

```text
responsive hero image substrate
        +
HTML/CSS overlay
├── H1
├── explanatory copy
├── Scripture quotation
├── primary CTA
├── secondary CTA
└── optional status/tagline
```

Desktop and mobile may use different image crops while preserving the same semantic HTML content.

Audience cards follow the same principle:

```text
image substrate
        +
HTML card content
├── audience title
├── orientation statement
├── short description
└── actual linked CTA
```

## Production Priorities

Initial asset generation should proceed in this order:

1. Hero desktop substrate.
2. Hero mobile substrate.
3. Four audience-card substrates.
4. WorldModel layered conceptual graphic.
5. Observation/inference/history conceptual graphic.
6. Programme relationship graphic.
7. Falsification/status graphic.

## Quality Constraints

Production assets should:

- contain no watermarks;
- avoid embedded prose except where intrinsic to a technical diagram;
- avoid human depictions of Christ;
- preserve adequate negative space for responsive overlays where specified;
- avoid visual elements whose crop would materially change the theological or scientific meaning;
- use a coherent visual language across desktop/mobile variants;
- support compression to web-suitable formats;
- retain source/provenance information in the asset manifest;
- be reviewed for mobile crop safety before promotion.

## Design Reference Handling

The existing generated desktop and desktop/mobile mockups should be retained as composition references when practical, with a visible designation equivalent to:

**REFERENCE / DO NOT DEPLOY AS PAGE**

Their purpose is to communicate visual direction, hierarchy, and composition to ThinxAI and future collaborators.

## Handoff Rule

ChatGPT may generate and refine the static visual assets. ThinxAI owns integration into the responsive site, build validation, optimization, and publication plumbing. Any visual requiring changes to fit the responsive implementation should be returned through the bridge with the affected viewport/component and requested constraint clearly identified.
