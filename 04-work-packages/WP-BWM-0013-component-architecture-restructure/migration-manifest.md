# BWM Component Architecture Migration Manifest

Status: Draft migration plan under WP-BWM-0013
Authority: Planning only; no file movement authorized by this manifest

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
│   │   ├── ontology/
│   │   ├── epistemology/
│   │   └── hermeneutics/
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
```

## Planned migrations and promotions

| Source | Target | Action | Link impact | Reversibility |
|---|---|---|---|---|
| `04-work-packages/WP-BWM-0013-component-architecture-restructure/bwm-component-architecture.md` | `02-systems-baseline/2.2-architecture/bwm-component-architecture.md` | Promote after JD acceptance | Update architecture README and root/component references | Copy first; retain WP source until verification |
| `04-work-packages/WP-BWM-0013-component-architecture-restructure/framework-domain-matrix.md` | `02-systems-baseline/2.2-architecture/integration/framework-domain-matrix.md` | Promote after JD acceptance | Update architecture README and links from component architecture | Copy first; retain WP source until verification |
| `02-systems-baseline/2.2-architecture/BWM-CANON-0001-worldmodel-interpretive-families.md` | `02-systems-baseline/2.2-architecture/integration/BWM-CANON-0001-worldmodel-interpretive-families.md` | Candidate relocation | Potentially high: existing direct links and public references unknown | Add target copy; update links; delete old only after verification or retain stable shim |
| `04-work-packages/WP-BWM-0005-accessible-narrative/bwm-epistemic-hierarchy.md` + WP-BWM-0009 governed revisions | `02-systems-baseline/2.2-architecture/foundations/epistemology/epistemic-hierarchy.md` OR `2.1-requirements/foundations/epistemology/...` | Promote only after WP-BWM-0009 disposition | High because WP-BWM-0005 and public narrative reference source path | Decide architecture-vs-requirement split first; preserve forwarding reference |
| Accepted generic retrodiction propositions from WP-BWM-0011 | `02-systems-baseline/2.2-architecture/historical-frameworks/dfm/retrodiction.md` | Extract/promote, not package move | Medium; work package remains research provenance | Add canonical artifact with source citations; retain package unchanged |
| Accepted cosmology findings from WP-BWM-0011 | `02-systems-baseline/2.2-architecture/world-domains/cosmology/` | Extract/promote by topic | Low/medium initially | Add new artifacts; retain research package |
| Accepted PFH framework from WP-BWM-0012 | `02-systems-baseline/2.2-architecture/historical-frameworks/pfh/README.md` or `pfh.md` | Promote after PFH review | Medium; chronology and anthropology references expected | Add canonical PFH file; keep hypothesis evidence in work package |
| WP-BWM-0014 canonical candidate `chronological-contamination.md` | `02-systems-baseline/2.1-requirements/chronology/chronological-contamination.md` | Promote after chronology disposition and taxonomy acceptance | Medium/high because PFH and dating work will reference it | Promote additively; update refs; retain WP provenance |
| Accepted abiogenic state-selection propositions from WP-BWM-0005 | `02-systems-baseline/2.2-architecture/world-domains/biology/` and/or `integration/` | Split by semantic role | Medium because public narrative may reference original | Do not move original narrative artifact; derive canonical technical artifact |
| Accepted brain/consciousness state-selection propositions from WP-BWM-0005 | `02-systems-baseline/2.2-architecture/world-domains/anthropology/` and/or Foundations | Split by semantic role | Medium | Derive canonical artifact, preserve narrative source |
| TRT/LRT references | `02-systems-baseline/2.2-architecture/foundations/ontology/` | Create BWM interface/reference artifacts, not independent forks | Cross-repository source-of-truth impact | Reference authoritative TRT/LRT sources and pin provenance |
| CHFM references | `02-systems-baseline/2.2-architecture/historical-frameworks/chfm/` | Create BWM interface/reference artifact after CHFM source authority is identified | Cross-repository source-of-truth impact | Reference authoritative CHFM source; do not fork silently |

## Deferred items

The following should not be migrated during the first restructure pass:

- public-site implementation packages;
- visual asset packages;
- video narration;
- chat-interface implementation;
- narrative-tier publication files;
- raw research harvests;
- evidence collections that have not received Operator disposition;
- any CHFM/TRT/LRT source material whose authoritative repository and version have not been explicitly identified.

## Proposed migration sequence

### Phase 0 — Freeze and validate

- refresh `main` and all open PRs;
- re-run UID and semantic-duplicate checks;
- scan repository references to every proposed source path;
- record the pre-migration commit SHA;
- confirm architecture approval.

### Phase 1 — Create taxonomy directories and indexes

Create empty/indexed target surfaces under `2.1-requirements` and `2.2-architecture` without moving substantive content.

Verification:

- repository layout tests still pass;
- no public navigation changes;
- all existing links remain intact.

### Phase 2 — Promote WP-BWM-0013 architecture artifacts

Promote:

- `bwm-component-architecture.md`;
- `framework-domain-matrix.md`.

Update `2.2-architecture/README.md`.

Verification:

- links resolve;
- taxonomy is discoverable;
- source work-package provenance remains intact.

### Phase 3 — Promote foundational methodology

Resolve WP-BWM-0009 disposition and determine whether epistemic hierarchy should be:

- architecture only;
- normative requirement only;
- or split into descriptive architecture plus normative requirements.

Then promote approved material.

### Phase 4 — Promote historical-framework definitions

In order:

1. DFM BWM interface/framework definition;
2. PFH after WP-BWM-0012 disposition;
3. CHFM BWM interface/framework definition after source-of-truth confirmation.

Framework files should define jurisdiction and interfaces rather than duplicate full external research repositories.

### Phase 5 — Promote chronology requirements

Promote accepted WP-BWM-0014 requirements into `2.1-requirements/chronology/` and reconcile PFH references.

### Phase 6 — Establish world-domain indexes

Create domain architecture/index files for:

- cosmology;
- Earth history;
- biology;
- anthropology;
- archaeology/chronology;
- covenant/redemptive history.

Initially these should be interface/index artifacts, not attempts to rewrite all research.

### Phase 7 — Integration artifacts

Establish:

- chronology model;
- evidence-ledger model;
- open-problems register;
- predictions/falsifiers register;
- model-comparison/Bayesian interfaces.

### Phase 8 — Optional relocation of existing canonical artifact

Only after all new taxonomy links are stable, decide whether `BWM-CANON-0001-worldmodel-interpretive-families.md` should physically move into `integration/`.

Preferred conservative option: retain the current path initially and classify it logically as Integration. Physical relocation provides little value unless directory consistency materially improves navigation.

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

## Outstanding decisions before implementation

1. Approve or revise the four-category architecture.
2. Decide architecture-vs-requirement placement for the epistemic hierarchy.
3. Identify authoritative source repositories/versions for TRT/LRT and CHFM BWM interface artifacts.
4. Decide whether `BWM-CANON-0001` physically moves or remains at its stable path.
5. Resolve stale PFH references to the former chronological-contamination UID and ensure PFH points to WP-BWM-0014.
6. Decide whether post-Flood history becomes a formal Historical Framework now or remains a reserved candidate.
7. Approve the migration sequence before Phase 1 begins.

## Recommendation

Implement conservatively. The immediate restructure should establish taxonomy, indexes, interfaces, and approved canonical definitions. It should avoid broad physical relocation of mature files unless relocation solves a concrete ownership or navigation problem.

Human-Curated, AI-Enabled (HCAE)
