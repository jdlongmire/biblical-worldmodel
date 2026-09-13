# BWM Component Architecture Migration Manifest

Status: Draft migration plan under WP-BWM-0013
Authority: Planning only; no file movement authorized by this manifest

## Approved architectural recommendations for implementation planning

The following decisions are adopted as the working implementation plan:

1. The epistemic hierarchy belongs architecturally under **Foundations / Epistemology**. Normative requirements derived from it may be separately promoted into `2.1-requirements`; the methodology itself is architecture.
2. TRT and LRT remain authoritative in their own source repositories. BWM shall create interface artifacts that identify the authoritative source/version and the propositions BWM consumes. BWM shall not silently fork TRT/LRT.
3. CHFM shall follow the same interface pattern if its detailed research remains externally authoritative: BWM carries the framework jurisdiction, accepted BWM-level propositions, interfaces, and provenance, while detailed calculations/data remain at the authoritative CHFM source.
4. `BWM-CANON-0001-worldmodel-interpretive-families.md` remains at its current stable path during the initial restructure. It is logically classified as Integration and referenced from the Integration index. Physical relocation is deferred unless it later solves a concrete navigation/ownership problem.
5. PFH stale mortality-chronology references are a correctness fix and must point to `WP-BWM-0014` before restructure implementation.
6. Post-Flood History remains a **reserved Historical Framework candidate**. Do not formalize it as a full framework until distinct explanatory content justifies it.
7. Promote the component architecture and framework-domain matrix before substantive framework/domain content.
8. Create the target taxonomy skeleton and semantic README contracts before promoting substantive content.
9. Use BWM interface artifacts for DFM/PFH/CHFM and external foundations rather than duplicating full research programmes.
10. Preserve work-package provenance after promotion; promotion creates governed canonical derivatives and does not gut historical work packages.

## Migration principles

1. Preserve the repository `00`–`06` lifecycle contract.
2. Move only accepted canonical content into `02-systems-baseline`; active research remains in `04-work-packages`.
3. Do not move whole work packages merely because portions of their content map to the conceptual taxonomy.
4. Split promotion by semantic ownership: Foundations, Historical Frameworks, World Domains, Integration, or Requirements.
5. Preserve provenance and add forwarding/cross-reference notes where path changes would otherwise break traceability.
6. Perform a fresh reference scan immediately before every move.
7. Prefer additive promotion followed by verified reference updates before deleting any old canonical path.

## Proposed target skeleton

```text
02-systems-baseline/
├── 2.1-requirements/
│   ├── foundations/
│   ├── biblical-historical-constraints/
│   └── chronology/
│
├── 2.2-architecture/
│   ├── bwm-component-architecture.md
│   ├── foundations/
│   │   ├── README.md
│   │   ├── ontology/
│   │   │   ├── trt-interface.md
│   │   │   └── lrt-interface.md
│   │   ├── epistemology/
│   │   │   └── epistemic-hierarchy.md
│   │   └── hermeneutics/
│   ├── historical-frameworks/
│   │   ├── README.md
│   │   ├── dfm/
│   │   │   └── bwm-interface.md
│   │   ├── pfh/
│   │   │   └── bwm-interface.md
│   │   ├── chfm/
│   │   │   └── bwm-interface.md
│   │   └── post-flood-history/   # reserved candidate only
│   ├── world-domains/
│   │   ├── README.md
│   │   ├── cosmology/
│   │   ├── earth-history/
│   │   ├── biology/
│   │   ├── anthropology/
│   │   ├── archaeology-chronology/
│   │   └── covenant-redemptive-history/
│   └── integration/
│       ├── README.md
│       ├── framework-domain-matrix.md
│       ├── chronology-model.md
│       ├── evidence-ledger-model.md
│       ├── open-problems.md
│       └── predictions-falsifiers.md
```

## Interface artifact contract

Each external-foundation or Historical-Framework interface should identify:

- authoritative source repository and pinned provenance/version;
- architectural type and BWM jurisdiction;
- BWM-adopted propositions;
- open hypotheses that remain non-canonical;
- dependent World Domains;
- interfaces to other foundations/frameworks;
- known tensions or unresolved questions;
- promotion/disposition status;
- source work package(s) where applicable.

## Planned migrations and promotions

| Source | Target | Action | Link impact | Reversibility |
|---|---|---|---|---|
| `04-work-packages/WP-BWM-0013-component-architecture-restructure/bwm-component-architecture.md` | `02-systems-baseline/2.2-architecture/bwm-component-architecture.md` | First architecture promotion after JD implementation approval | Update architecture README and root/component references | Copy first; retain WP source |
| `04-work-packages/WP-BWM-0013-component-architecture-restructure/framework-domain-matrix.md` | `02-systems-baseline/2.2-architecture/integration/framework-domain-matrix.md` | First Integration promotion | Update architecture README and component links | Copy first; retain WP source |
| `02-systems-baseline/2.2-architecture/BWM-CANON-0001-worldmodel-interpretive-families.md` | Current path retained | Classify logically as Integration; do not move in initial restructure | Low | No physical change |
| `04-work-packages/WP-BWM-0005-accessible-narrative/bwm-epistemic-hierarchy.md` + WP-BWM-0009 governed revisions | `02-systems-baseline/2.2-architecture/foundations/epistemology/epistemic-hierarchy.md` | Promote methodology after WP-BWM-0009 disposition | High because narrative references source path | Derive/promote canonical artifact; preserve narrative source |
| Accepted normative rules derived from epistemic hierarchy | `02-systems-baseline/2.1-requirements/foundations/` | Promote separately when accepted | Medium | Additive |
| Accepted generic retrodiction propositions from WP-BWM-0011 | `02-systems-baseline/2.2-architecture/historical-frameworks/dfm/` | Extract into DFM BWM interface/canonical derivatives | Medium | Retain package provenance |
| Accepted cosmology findings from WP-BWM-0011 | `02-systems-baseline/2.2-architecture/world-domains/cosmology/` | Extract/promote by topic | Low/medium | Retain package provenance |
| Accepted PFH framework from WP-BWM-0012 | `02-systems-baseline/2.2-architecture/historical-frameworks/pfh/bwm-interface.md` | Promote after PFH disposition | Medium | Retain WP evidence/hypotheses |
| WP-BWM-0014 canonical chronology candidate | `02-systems-baseline/2.1-requirements/chronology/chronological-contamination.md` | Promote after chronology disposition | Medium/high | Additive; retain WP provenance |
| Accepted abiogenic state-selection propositions from WP-BWM-0005 | `02-systems-baseline/2.2-architecture/world-domains/biology/` and/or Integration | Derive by semantic role | Medium | Preserve narrative source |
| Accepted brain/consciousness state-selection propositions from WP-BWM-0005 | `02-systems-baseline/2.2-architecture/world-domains/anthropology/` and/or Foundations | Derive by semantic role | Medium | Preserve narrative source |
| TRT/LRT | `02-systems-baseline/2.2-architecture/foundations/ontology/*-interface.md` | Create BWM interfaces after authoritative source/version confirmation | Cross-repository | Interface only; no fork |
| CHFM | `02-systems-baseline/2.2-architecture/historical-frameworks/chfm/bwm-interface.md` | Create BWM interface after authoritative source/version confirmation | Cross-repository | Interface only; no fork |

## Deferred items

Do not migrate during the first restructure pass:

- public-site implementation packages;
- visual asset packages;
- video narration;
- chat-interface implementation;
- narrative-tier publication files;
- raw research harvests;
- evidence collections without Operator disposition;
- detailed CHFM/TRT/LRT source material whose authoritative repository/version is not confirmed;
- physical relocation of `BWM-CANON-0001`;
- formalization of Post-Flood History as a full framework.

## Implementation sequence

### Phase 0 — Freeze and validate

- refresh `main` and all open PRs;
- re-run UID and semantic-duplicate checks;
- scan repository references to every proposed source path;
- record the pre-migration commit SHA;
- verify PFH points to WP-BWM-0014;
- confirm implementation approval.

### Phase 1 — Create taxonomy directories and semantic contracts

Create target surfaces under `2.1-requirements` and `2.2-architecture` with README files defining what belongs in each category. Do not move substantive content yet.

### Phase 2 — Promote WP-BWM-0013 architecture artifacts

Promote:

- `bwm-component-architecture.md`;
- `framework-domain-matrix.md`.

Update `2.2-architecture/README.md` and Integration index. Keep WP sources for provenance.

### Phase 3 — Promote foundational methodology

After WP-BWM-0009 disposition, promote the epistemic hierarchy into Foundations / Epistemology. Promote any normative requirements separately into `2.1-requirements`.

### Phase 4 — Create foundation/framework interfaces

In order:

1. TRT BWM interface after source/version confirmation;
2. LRT BWM interface after source/version confirmation;
3. DFM BWM interface;
4. PFH BWM interface after WP-BWM-0012 disposition;
5. CHFM BWM interface after source/version confirmation.

### Phase 5 — Promote chronology requirements

Promote accepted WP-BWM-0014 requirements into `2.1-requirements/chronology/`.

### Phase 6 — Establish World Domain indexes

Create domain architecture/index files for cosmology, Earth history, biology, anthropology, archaeology/chronology, and covenant/redemptive history. Initially these are interfaces/indexes, not research rewrites.

### Phase 7 — Integration artifacts

Establish chronology model, evidence-ledger model, open-problems register, predictions/falsifiers register, and model-comparison/Bayesian interfaces.

### Phase 8 — Review deferred structural choices

After stable use of the new taxonomy, reassess whether any existing canonical artifact needs physical relocation and whether Post-Flood History has matured enough to become a formal framework.

## Link-impact controls

Before any source file is deleted or relocated:

1. search exact path references across the repository;
2. search filename-only references;
3. inspect public-site references and generated navigation;
4. inspect work-package dependencies;
5. update references in the same PR;
6. preserve provenance to the source commit;
7. run repository-layout verification;
8. verify GitHub Pages/public build where applicable.

## Rollback strategy

Each migration phase must be independently revertible.

Preferred implementation pattern:

1. create/copy target artifact;
2. update references;
3. validate;
4. only then remove an old canonical path if removal is necessary;
5. use a dedicated migration commit or small commit series so reversal is unambiguous.

For derived promotions from work packages, the work-package source remains and is not deleted. Rollback therefore consists primarily of removing the promoted canonical derivative and reverting references.

## Remaining prerequisites before Phase 1

1. Identify and pin authoritative TRT/LRT source repositories/versions.
2. Identify and pin the authoritative CHFM source repository/version.
3. Complete Operator disposition of the architecture proposal for implementation.

## Recommendation

Implement conservatively. Establish taxonomy, semantic contracts, interfaces, and approved canonical definitions first. Avoid broad physical relocation unless it solves a concrete ownership or navigation problem.

Human-Curated, AI-Enabled (HCAE)
