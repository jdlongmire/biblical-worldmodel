# WP-BWM-0013 — BWM Component Architecture Restructure

Status: Active / implementation underway
Owner: JD Longmire
Working branch: `work/bwm-component-architecture-restructure`

## Objective

Implement a content-taxonomy refactor for Biblical WorldModel so the repository distinguishes foundational commitments, historical/explanatory frameworks, world domains, and cross-domain integration without replacing the existing `00`–`06` repository lifecycle structure.

## Governing architecture

Canonical BWM content is organized conceptually into four categories:

1. Foundations
2. Historical Frameworks
3. World Domains
4. Integration

The repository lifecycle structure remains unchanged.

## Operator disposition

Principal Operator JD Longmire authorized proceeding with the recommended architecture and phased implementation on 2026-09-13.

Working decisions:

- epistemic hierarchy belongs under Foundations / Epistemology;
- TRT/LRT remain external authoritative sources consumed through pinned BWM interfaces;
- CHFM follows the same interface/source-of-truth pattern;
- `BWM-CANON-0001-worldmodel-interpretive-families.md` remains at its stable path and is logically classified as Integration;
- PFH mortality chronology references point to `WP-BWM-0014`;
- Post-Flood History remains a reserved framework candidate;
- architecture and framework-domain matrix promote before substantive framework/domain content;
- taxonomy surfaces receive semantic contracts before substantive promotion;
- work packages remain provenance records after promotion.

## Source authorities

See `source-authorities.md`.

Current pinned planning sources:

- TRT/LRT: `jdlongmire/triadic-reality-theory` @ `491cb32ac3e937125a4844fb9417e1ea50a0e489`
- LRT formal source: `formalization/lrt/` inside the TRT repository
- CHFM: `jdlongmire/catastrophic-hydrotectonic-flood-model` @ `22dcdea8126861f3c9d7ecca89f71cf586287cd0`
- legacy CHFM predecessor: `jdlongmire/global-flood-hydrotectonic-model`, provenance only unless explicitly cited

## Current artifacts

Planning/provenance artifacts retained under this work package:

- `bwm-component-architecture.md`
- `framework-domain-matrix.md`
- `repository-inventory.md`
- `migration-manifest.md`
- `source-authorities.md`

Promoted baseline artifacts now exist on this branch:

- `02-systems-baseline/2.2-architecture/bwm-component-architecture.md`
- `02-systems-baseline/2.2-architecture/integration/framework-domain-matrix.md`

## Phase status

### Phase 0 — Freeze and validate

Complete for current implementation pass. The chronology UID collision was repaired by moving chronological contamination to `WP-BWM-0014`; PFH stale references were corrected.

### Phase 1 — Taxonomy directories and semantic contracts

Complete on this branch.

Semantic contracts now exist for:

- `2.2-architecture/foundations/`
- `2.2-architecture/historical-frameworks/`
- `2.2-architecture/world-domains/`
- `2.2-architecture/integration/`
- `2.1-requirements/foundations/`
- `2.1-requirements/biblical-historical-constraints/`
- `2.1-requirements/chronology/`

### Phase 2 — Architecture promotion

Complete on this branch.

The component architecture and framework-domain matrix have been promoted additively into `02-systems-baseline` while their source work-package artifacts remain for provenance.

### Phase 3 — Foundational methodology

Pending WP-BWM-0009 disposition and canonical derivative construction.

### Phase 4 — Foundation/framework interfaces

Next implementation phase. Create pinned BWM interface artifacts for TRT, LRT, DFM, PFH, and CHFM according to the interface contract in `migration-manifest.md`.

### Phase 5+ — Chronology, domains, integration

Pending preceding dispositions and interfaces.

## Architectural boundaries

Do not create root-level peers such as `DFM/`, `PFH/`, `CHFM/`, `cosmology/`, or `biology/`.

Active hypotheses and unfinished research remain in `04-work-packages/` until accepted for promotion. Whole work packages are not migrated merely because portions map to the conceptual taxonomy.

## Verification requirements

Before merge or each later migration phase:

- refresh live repository/PR state;
- re-run UID and semantic-duplicate checks;
- validate references and public navigation impacts;
- preserve immutable source provenance;
- keep each migration phase independently revertible;
- run repository-layout and site/build verification where applicable.

## Current disposition

Active. Architecture accepted for implementation. Phases 1 and 2 complete on the restructure branch. Phase 4 interface construction is the next architectural implementation task; Phase 3 foundational-methodology promotion remains gated by WP-BWM-0009 disposition.

Human-Curated, AI-Enabled (HCAE)
