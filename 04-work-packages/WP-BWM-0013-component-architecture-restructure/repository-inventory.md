# BWM Component Repository Inventory

Status: Draft inventory under WP-BWM-0013
Scope: Current `main` plus active candidate work in open PRs relevant to the component-architecture restructure

## Purpose

Inventory current substantive Biblical WorldModel artifacts by semantic role before any file movement. This inventory distinguishes lifecycle location from intellectual classification.

The current canonical systems baseline is intentionally sparse. `02-systems-baseline/2.2-architecture/` presently contains only `BWM-CANON-0001-worldmodel-interpretive-families.md` as substantive architecture content. Most of the developing conceptual model remains staged in `04-work-packages/`.

## Baseline inventory

| Current path | Current role | Proposed architectural classification | Proposed disposition |
|---|---|---|---|
| `02-systems-baseline/2.2-architecture/BWM-CANON-0001-worldmodel-interpretive-families.md` | Canonical interpretive-family architecture | Integration / comparative architecture | Retain canonical status; move or cross-link into `2.2-architecture/integration/` only after link-impact review |
| `02-systems-baseline/2.1-requirements/README.md` | Requirements surface index | Lifecycle infrastructure | Retain; update index after approved taxonomy implementation |
| `02-systems-baseline/2.2-architecture/README.md` | Architecture surface index | Lifecycle infrastructure | Retain; update to expose Foundations / Historical Frameworks / World Domains / Integration |
| `02-systems-baseline/2.3-behavior/README.md` | Behavior surface index | Lifecycle infrastructure | Retain; no conceptual relocation |
| `02-systems-baseline/2.4-interfaces/README.md` | Interfaces surface index | Lifecycle infrastructure | Retain; likely host formal cross-component interface specifications later |
| `02-systems-baseline/2.5-verification/README.md` | Verification surface index | Lifecycle infrastructure | Retain; later add component-level verification references |
| `02-systems-baseline/2.5-verification/layout-evidence.md` | Repository-layout verification evidence | Lifecycle infrastructure | Retain unchanged unless paths change |

## Active work-package inventory

### WP-BWM-0005 — Accessible Narrative

Current substantive artifacts include:

- `bwm-epistemic-hierarchy.md`
- `abiogenic-state-selection-problem.md`
- `brain-consciousness-state-selection-problem.md`
- `tier-2-starting-conditions-and-model-symmetry.md`
- public/narrative tier artifacts

Proposed classification:

- `bwm-epistemic-hierarchy.md` -> Foundations / epistemology candidate, governed by WP-BWM-0009 for canonicalization.
- `abiogenic-state-selection-problem.md` -> World Domain / biology, with Integration relevance.
- `brain-consciousness-state-selection-problem.md` -> World Domain / anthropology, with Foundations and Integration relevance.
- `tier-2-starting-conditions-and-model-symmetry.md` -> Integration / model-comparison methodology, with DFM interface.
- narrative-tier/public artifacts remain publication-layer work and should not be relocated merely because they discuss BWM concepts.

Disposition: retain in WP-BWM-0005 until each substantive artifact has an explicit promotion owner. Do not wholesale-migrate the package.

### WP-BWM-0007 — Hugh Ross / RTB DFM Harvest

Role: evidence discovery and comparative source harvesting for DFM across cosmology, fine-tuning, initial conditions, stellar nucleosynthesis, habitability, and methodology.

Classification:

- Primary: Historical Framework / DFM research input.
- Secondary: World Domain / cosmology.
- Secondary: Integration / evidence ledger and comparative-model analysis.

Disposition: retain as research/staging work. Promote individual accepted findings to DFM, cosmology, or Integration artifacts rather than moving the package itself.

### WP-BWM-0009 — Canonical Epistemic Hierarchy

Role: claim-level epistemic hierarchy, Operator governance, canonicalization flow, dependency testing, symmetry testing, adversarial review.

Classification:

- Primary: Foundations / epistemology and governance.
- Secondary: Integration / evidence and model-comparison discipline.

Proposed canonical target after acceptance:

`02-systems-baseline/2.2-architecture/foundations/epistemology/`

or, if treated as a hard methodological requirement rather than architecture:

`02-systems-baseline/2.1-requirements/foundations/epistemology/`

Decision required before migration: whether the hierarchy is architectural methodology, normative requirement, or split into both surfaces.

### WP-BWM-0010 — Story Visual Narrative

Role: public visual communication.

Classification: publication/solution delivery, not a canonical component-architecture owner.

Disposition: retain in work-package / publication lifecycle. It may consume canonical component definitions but should not be relocated into the new conceptual taxonomy.

### WP-BWM-0011 — Cosmology Retrodiction and DFM Harvest

Role: cosmology retrodiction, initialization/boundary-condition analysis, JWST early maturity, stellar formation, distant starlight, DFM/UTE comparison.

Classification:

- Primary: World Domain / cosmology.
- Primary interface: Historical Framework / DFM.
- Secondary: Integration / retrodiction and evidence methodology.

Candidate promotion split after research maturity:

- generic DFM retrodiction propositions -> `historical-frameworks/dfm/`;
- cosmology-specific findings -> `world-domains/cosmology/`;
- generic observation-to-history stack and symmetry rules -> `integration/` or Foundations/epistemology, depending on final authority status.

Disposition: do not move package wholesale. Split accepted claims by semantic ownership.

### WP-BWM-0012 — Pre-Fall History (PFH), open PR #14

Role: human-creation-to-Fall historical framework; extended pre-Fall development is an initial hypothesis under the framework.

Classification:

- Primary: Historical Framework / PFH.
- Primary interfaces: Anthropology; Archaeology / Chronology.
- Secondary interfaces: Biology / ecology; Covenant / Redemptive History at the Fall boundary.

Candidate canonical target after acceptance:

`02-systems-baseline/2.2-architecture/historical-frameworks/pfh/`

Chronology hard constraints, if separately canonicalized, belong under `2.1-requirements/chronology/` rather than being embedded only in PFH architecture.

### WP-BWM-0013 — Component Architecture Restructure, open PR #16

Role: architecture definition and migration planning.

Classification: Integration / repository architecture governance.

Candidate promotion targets after acceptance:

- `bwm-component-architecture.md` -> `02-systems-baseline/2.2-architecture/bwm-component-architecture.md`
- `framework-domain-matrix.md` -> `02-systems-baseline/2.2-architecture/integration/framework-domain-matrix.md`

Current disposition: remain in work package until JD approves taxonomy and migration plan.

### WP-BWM-0014 — Human Mortality Chronology / Chronological Contamination, open PR #12

Role: post-Fall human mortality chronology, retrodictive-age conflicts, chronological-contamination discipline.

Classification:

- Primary: Requirements / chronology hard constraint.
- Secondary: World Domain / archaeology and chronology.
- Secondary: Integration / retrodictive-age methodology.
- Historical-framework interfaces: PFH at the Fall boundary; DFM and CHFM where inherited or disturbed state is proposed.

Candidate canonical target already proposed by its package:

`02-systems-baseline/2.1-requirements/chronological-contamination.md`

Under the proposed taxonomy, preferred target is:

`02-systems-baseline/2.1-requirements/chronology/chronological-contamination.md`

Disposition: preserve current canonical-candidate status; path refinement should be coordinated with WP-BWM-0013 before merge/promotion.

## Major conceptual components not yet represented as dedicated canonical BWM artifacts

The following architectural components are recognized by the proposed BWM architecture but do not yet have dedicated canonical files under `02-systems-baseline`:

- TRT
- LRT
- Semantic Actualism
- consolidated epistemology / hermeneutics
- DFM framework definition
- PFH framework definition
- CHFM framework definition
- cosmology domain architecture
- Earth-history domain architecture
- biology domain architecture
- anthropology domain architecture
- archaeology / chronology domain architecture
- covenant / redemptive-history domain architecture
- consolidated chronology model
- evidence-ledger model
- open-problems register
- prediction / falsifier register

These are gaps in canonical architecture, not evidence that the underlying research is absent elsewhere.

## Key inventory conclusions

1. The current `02-systems-baseline` contains very little substantive BWM intellectual architecture, so the restructure is primarily a controlled promotion and classification exercise rather than a mass relocation of existing canonical files.
2. Most substantive content currently exists in `04-work-packages`, and those packages frequently span more than one proposed category.
3. Whole-package moves would create false ownership. Accepted content should be split by semantic role at promotion time.
4. The highest-value first promotions are the component architecture, framework-domain matrix, epistemic methodology, PFH framework, chronology requirement, and selected DFM retrodiction propositions.
5. TRT/LRT and CHFM require explicit source-of-truth identification before BWM creates canonical derivative artifacts, because BWM should reference their authoritative programme repositories rather than silently fork them.
6. Publication and site-delivery packages should consume canonical architecture without being forced into the conceptual taxonomy.

## Inventory status

This inventory is sufficient for migration planning of the currently visible canonical baseline and active major conceptual work packages. Implementation still requires path-level link/reference checks immediately before each move because open PR state may continue to change.

Human-Curated, AI-Enabled (HCAE)
