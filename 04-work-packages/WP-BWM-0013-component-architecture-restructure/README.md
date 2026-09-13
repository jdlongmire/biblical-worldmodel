# WP-BWM-0013 — BWM Component Architecture Restructure

Status: Proposed / design capture
Owner: JD Longmire
Working branch: `work/bwm-component-architecture-restructure`

## Objective

Capture and design a content-taxonomy refactor for Biblical WorldModel so the repository distinguishes foundational commitments, historical/explanatory frameworks, world domains, and cross-domain integration without replacing the existing `00`–`06` repository lifecycle structure.

The restructure is intended to make the intellectual architecture of BWM explicit while preserving the repository's current MxM/template operating model.

## Current design artifacts

- `bwm-component-architecture.md` — proposed component architecture and architectural rules.
- `framework-domain-matrix.md` — cross-cutting map among foundations, historical frameworks, and world domains.
- `repository-inventory.md` — inventory of current canonical and candidate artifacts by semantic role and proposed disposition.
- `migration-manifest.md` — proposed target paths, link-impact controls, phased migration sequence, rollback strategy, and outstanding decisions.

These artifacts are design and migration-planning deliverables under this work package. They are not yet canonical baseline content and authorize no file migration.

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
│   ├── bwm-component-architecture.md
│   ├── foundations/
│   │   ├── ontology/
│   │   ├── epistemology/
│   │   └── hermeneutics/
│   │
│   ├── historical-frameworks/
│   │   ├── dfm/
│   │   ├── pfh/
│   │   └── chfm/
│   ├── world-domains/
│   │   ├── cosmology/
│   │   ├── earth-history/
│   │   ├── biology/
│   │   ├── anthropology/
│   │   ├── archaeology-chronology/
│   │   └── covenant-redemptive-history/
│   └── integration/
│       ├── framework-domain-matrix.md
│       ├── chronology-model.md
│       ├── evidence-ledger-model.md
│       ├── open-problems.md
│       └── predictions-falsifiers.md
│
├── 2.3-behavior/
├── 2.4-interfaces/
└── 2.5-verification/
```

This is a proposed target taxonomy, not authorization to move files yet.

## Architectural relationships

The directory hierarchy should not be used to imply that historical frameworks and world domains are peers in kind.

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

The inventory establishes that whole-package moves would create false semantic ownership. Promotion should instead extract accepted content into canonical artifacts according to role while retaining work-package provenance.

Examples:

- WP-BWM-0011 contains both DFM-generic retrodiction material and cosmology-specific work; those should promote to different canonical surfaces.
- WP-BWM-0012 develops PFH and an extended-duration hypothesis; mature PFH architecture should promote without automatically promoting every hypothesis.
- WP-BWM-0014 is primarily a chronology requirement, not a PFH framework artifact.
- public narrative and media packages should consume canonical architecture without being relocated into the conceptual taxonomy.

## Inventory findings

The current `02-systems-baseline` is sparse: `BWM-CANON-0001-worldmodel-interpretive-families.md` is the principal substantive architecture artifact currently on `main`. Most developing BWM intellectual content remains in work packages.

Important consequences:

1. this restructure is primarily a controlled promotion/classification effort, not a mass move of canonical files;
2. TRT/LRT and CHFM require authoritative source-of-truth identification before BWM creates canonical interface artifacts;
3. the epistemic hierarchy needs a placement decision between architecture and normative requirements;
4. physical relocation of `BWM-CANON-0001` is optional and should occur only if it adds concrete navigation value;
5. PFH currently contains stale references to the pre-renumbering chronology package and must point to `WP-BWM-0014` before coordinated promotion.

See `repository-inventory.md` and `migration-manifest.md` for details.

## Planned implementation sequence

The migration manifest proposes:

1. freeze and validate live repository/PR state;
2. create taxonomy directories and indexes;
3. promote the WP-BWM-0013 architecture artifacts;
4. promote approved foundational methodology;
5. promote DFM/PFH/CHFM framework interface definitions;
6. promote chronology requirements;
7. establish world-domain indexes;
8. establish Integration artifacts;
9. optionally relocate existing canonical artifacts only after links are stable.

Every phase must be independently revertible.

## Out of scope

This package does not yet authorize:

- moving or deleting existing canonical files;
- renaming root-level lifecycle directories;
- breaking existing URLs without redirects or migration records;
- rewriting substantive scientific or theological claims merely to fit the new taxonomy;
- changing public-site navigation until the content architecture is approved;
- collapsing DFM, PFH, CHFM, foundations, and world domains into a single flat hierarchy.

## Acceptance criteria

Ready for implementation approval when:

- the four conceptual categories are approved;
- TRT/LRT, DFM, PFH, and CHFM each have an explicit architectural role;
- historical frameworks are distinguished from world domains;
- the framework-domain matrix covers current major components and interfaces;
- the repository inventory has a disposition for current substantive canonical/candidate artifacts;
- the migration manifest documents target paths, link impacts, rollout order, and rollback;
- active research remains separate from canonical baseline content;
- the epistemic-hierarchy placement decision is resolved;
- authoritative source repositories are identified for TRT/LRT and CHFM interfaces;
- stale PFH chronology-package references are reconciled;
- no UID, file, or semantic-ownership collision remains unresolved;
- repository conformance and source-of-truth boundaries are preserved;
- JD explicitly approves implementation.

## Current disposition

Open. Architecture definition, repository inventory, and migration manifest are drafted. No file migration or canonical restructure is authorized yet.

Human-Curated, AI-Enabled (HCAE)
