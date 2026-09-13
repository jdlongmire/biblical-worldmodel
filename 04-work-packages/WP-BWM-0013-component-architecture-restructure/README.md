# WP-BWM-0013 — BWM Component Architecture Restructure

Status: Proposed / design capture
Owner: JD Longmire
Working branch: `work/bwm-component-architecture-restructure`

## Objective

Capture and design a content-taxonomy refactor for Biblical WorldModel so the repository distinguishes foundational commitments, historical/explanatory frameworks, world domains, and cross-domain integration without replacing the existing `00`–`06` repository lifecycle structure.

The restructure is intended to make the intellectual architecture of BWM explicit while preserving the repository's current MxM/template operating model.

## Core architectural decision

Do **not** create new root-level peers such as `DFM/`, `PFH/`, `CHFM/`, `cosmology/`, or `biology/`.

Retain the existing root structure:

`00-meta-model/`
`01-strategic-baseline/`
`02-systems-baseline/`
`03-solutions-baseline/`
`04-work-packages/`
`05-mxm-construct/`
`06-operations/`

The conceptual BWM architecture should be expressed primarily inside `02-systems-baseline`, especially `2.2-architecture`, while `04-work-packages` remains the staging area for active investigation and proposed changes.

## Proposed conceptual taxonomy

Within `02-systems-baseline/2.2-architecture/`, organize BWM content around four categories:

### 1. Foundations

Global commitments and grounding that apply across all BWM domains.

Candidate contents:

- TRT
- LRT
- Semantic Actualism
- Logos grounding
- epistemology
- hermeneutics
- Scripture-primary / nature-secondary ordering
- observation / inference distinction
- operational / historical science distinction

### 2. Historical Frameworks

Cross-domain frameworks that govern major historical intervals or transitions.

Candidate contents:

- DFM — creation-state initialization, functional maturity, initialization boundary, retrodiction limits
- PFH — Pre-Fall History, from human creation through the Fall boundary
- CHFM — catastrophic Flood transition and Earth-history consequences
- post-Flood history framework, if/when formalized
- other alternative timing/emergence frameworks where retained for comparison

Working historical sequence:

`Foundations -> DFM / creation and initialization -> PFH -> Fall -> post-Fall / pre-Flood history -> CHFM / Flood catastrophe -> post-Flood history`

### 3. World Domains

Subject-matter domains to which foundations and historical frameworks are applied.

Candidate domains:

- cosmology / physical order
- Earth history / geology
- biology / life systems
- anthropology
- archaeology and chronology
- covenant / redemptive history
- eschatology, if treated as a separate domain

### 4. Integration

Cross-framework and cross-domain synthesis.

Candidate artifacts:

- framework-domain matrix
- chronology model
- evidence-ledger model
- Bayesian/model-comparison ledgers
- open-problems register
- predictions and falsifiers
- interface definitions among TRT/LRT, DFM, PFH, CHFM, and world domains

## Proposed file structure

```text
02-systems-baseline/
├── 2.1-requirements/
│   ├── foundations/
│   ├── biblical-historical-constraints/
│   ├── chronology/
│   └── ...
│
├── 2.2-architecture/
│   ├── foundations/
│   │   ├── trt.md
│   │   ├── lrt.md
│   │   ├── semantic-actualism.md
│   │   └── epistemology-hermeneutics.md
│   │
│   ├── historical-frameworks/
│   │   ├── dfm/
│   │   ├── pfh/
│   │   ├── chfm/
│   │   └── post-flood-history/
│   │
│   ├── world-domains/
│   │   ├── cosmology/
│   │   ├── earth-history/
│   │   ├── biology/
│   │   ├── anthropology/
│   │   ├── archaeology-chronology/
│   │   └── covenant-redemptive-history/
│   │
│   ├── integration/
│   │   ├── framework-domain-matrix.md
│   │   ├── chronology-model.md
│   │   ├── evidence-ledger-model.md
│   │   └── open-problems.md
│   │
│   └── BWM-CANON-0001-worldmodel-interpretive-families.md
│
├── 2.3-behavior/
├── 2.4-interfaces/
└── 2.5-verification/
```

This is a proposed target taxonomy, not authorization to move files yet.

## Architectural relationships

The directory hierarchy should not be used to imply that historical frameworks and world domains are peers in kind.

Examples:

```text
DFM
 ├── applies-to cosmology
 ├── applies-to biology
 ├── applies-to geology
 └── constrains chronology

PFH
 ├── applies-to anthropology
 ├── applies-to archaeology
 ├── applies-to chronology
 └── interfaces-with DFM

CHFM
 ├── applies-to earth-history
 ├── applies-to paleontology
 ├── applies-to climatology
 ├── applies-to chronology
 └── interfaces-with PFH
```

TRT/LRT remain foundational rather than domain-specific historical models.

## Promotion model

Active hypotheses and unfinished research remain under `04-work-packages/` until accepted for promotion.

Examples:

- `WP-BWM-0012` develops PFH and its extended pre-Fall hypothesis.
- mature PFH framework content would eventually be promoted into `02-systems-baseline/2.2-architecture/historical-frameworks/pfh/`.
- DFM and CHFM research should follow the same pattern.

The work-package area therefore remains a development/staging layer rather than becoming the permanent conceptual taxonomy.

## Central architecture artifact

Create, as part of implementation after approval:

`02-systems-baseline/2.2-architecture/bwm-component-architecture.md`

That artifact should define the canonical relationship:

`Foundations -> Historical Frameworks -> World Domains -> Integration`

and explicitly map TRT/LRT, DFM, PFH, CHFM, domain sciences, chronology, and redemptive history.

## Scope

This package covers:

- defining the target BWM content taxonomy;
- identifying current files that would map into the new taxonomy;
- defining framework/domain relationships;
- planning migration without breaking links or source-of-truth boundaries;
- specifying promotion rules from work packages to canonical baseline content;
- planning required updates to indexes, README files, navigation, and cross-references.

## Out of scope

This package does not yet authorize:

- moving or deleting existing canonical files;
- renaming root-level lifecycle directories;
- breaking existing URLs without redirects or migration records;
- rewriting substantive scientific or theological claims merely to fit the new taxonomy;
- changing public-site navigation until the content architecture is approved;
- collapsing DFM, PFH, CHFM, foundations, and world domains into a single flat hierarchy.

## Planned work

1. Inventory current BWM canonical and candidate content by semantic role.
2. Map each artifact to Foundations, Historical Frameworks, World Domains, Integration, or another existing lifecycle surface.
3. Identify ambiguous or cross-cutting artifacts and define interface/cross-reference treatment.
4. Produce `bwm-component-architecture.md` as the proposed canonical component map.
5. Produce a migration manifest with old path, proposed new path, disposition, and link impact.
6. Check all current work packages and open PRs for dependencies on paths proposed for movement.
7. Define promotion criteria from `04-work-packages` into canonical baseline areas.
8. Validate that the restructure preserves the `00`–`06` repository contract and MxM conformance.
9. Implement only after JD accepts the proposed taxonomy and migration plan.

## Acceptance criteria

Ready for implementation approval when:

- the four conceptual categories are clearly defined;
- TRT/LRT, DFM, PFH, and CHFM each have an explicit architectural role;
- historical frameworks are distinguished from world domains;
- active research remains separate from canonical baseline content;
- every existing canonical artifact has a proposed disposition;
- link and navigation impacts are documented;
- no UID, file, or semantic-ownership collision remains unresolved;
- repository conformance and source-of-truth boundaries are preserved;
- a reversible migration sequence is documented before file moves begin.

## Current disposition

Open. Design capture only. No file migration or canonical restructure is authorized by creation of this package.

Human-Curated, AI-Enabled (HCAE)
