# SOP-RSCH-001: Reproducible Research Notebooks and Evidence Traceability

**Status:** Proposed cross-programme standard; review required before adoption.
**Version:** 0.1 (2026-10-10)
**Applies to:** Active research programmes governed by the principal, with programme-specific extensions.

## Governing principle

Any conclusion materially dependent on computation must be traceable from claim through evidence, assumptions, code, execution, results and review. A notebook is an executable research record, **not** an authority to promote a hypothesis. Conceptual, textual and theological work may use structured Markdown instead of an artificial notebook.

## Required research package

```text
research/<study-id>/
  README.md                  # research question, status, owner, scope
  hypotheses.md              # competing models, warrants, falsifiers
  evidence-ledger.csv        # source, observation, uncertainty, provenance
  assumptions.yaml           # IDs, values, ranges, rationale, evidence
  data-manifest.yaml         # licenses, URLs, checksums, access limitations
  notebooks/
    00-research-design.ipynb
    01-evidence-audit.ipynb
    02-baseline.ipynb
    03-sensitivity.ipynb
    04-severe-tests.ipynb
    05-comparative-appraisal.ipynb
  src/                       # importable, typed research methods
  tests/                     # independent unit, property, regression tests
  results/README.md          # reproducible artifact manifest, not opaque outputs
  environment/               # locked dependencies, runtime and execution steps
```

Adapt notebook names and count to the study. Large restricted data stay outside Git with accession, license and checksum in the manifest. Do not commit credentials, protected data or large binaries.

## Standard notebook contract

Each notebook records: (1) question and study ID; (2) competing hypotheses and independent predictions; (3) warrant and epistemic class [textual premise / observation / inference / auxiliary]; (4) dataset provenance and quality controls; (5) assumptions with stable IDs and uncertainty; (6) methods and executable analysis; (7) plots with units and confidence or uncertainty; (8) negative and null findings; (9) limitations and alternative explanations; (10) run metadata and conclusion disposition.

Use deterministic seeds where applicable; report stochastic variation across seeds. Pin runtime and dependencies. Parameterize instead of editing code to obtain desired results. Separate observed data, synthetic test data, and model output unmistakably.

## Verification gates

- **G0 Registration:** hypotheses, competing models, expected discriminators and adverse outcomes written before fitting.
- **G1 Data:** sources, licensing, sample selection, checksum and transformations verified.
- **G2 Execution:** notebooks run top-to-bottom from a clean environment without hidden state; automated execution in CI where feasible.
- **G3 Software:** calculations in tested `src/` modules; boundary, negative and regression tests.
- **G4 Robustness:** sensitivity to priors, time calibration, rates, sample choice and model structure; distinguish identifiable from non-identifiable parameters.
- **G5 Independent challenge:** held-out predictions and strongest counterevidence reported; failures preserved.
- **G6 Review:** reviewer and principal approve promotion; merge or publication is not implied by a successful notebook run.

## Nonuniform historical processes

Uniformitarian rate assumptions are hypotheses to test, not unquestioned axioms. Alternative time-varying rates require explicit functional forms, mechanisms or independent constraints, plausible parameter ranges, and severe tests. Do not use unrestricted historical rate acceleration as an all-purpose escape. Equally, do not assume current rates were necessarily constant.

## Cross-programme implementation

Programme registries should link this SOP and list applicability, exceptions, owners and adoption status. Use dedicated branches and draft PRs for rollout. Preserve local repository conventions. Initial targets for review include Biblical WorldModel, Designed Functional Maturity, Post-Flood Diversity, Triadic Reality Theory, Creation Cosmology Programmes, and Global Flood Hydrotectonic Model. Confirm each repository's active status and governance before adoption. Philosophical-only studies use equivalent traceable argument/evidence records without mandatory computation.

## Minimum acceptance checklist

- [ ] All research claims linked to provenance and assumption IDs
- [ ] Every computational result reproducible from a clean checkout or documented data-access procedure
- [ ] Versioned dependencies, seeds, and execution metadata
- [ ] Sensitivity and counterexample analyses
- [ ] Negative findings retained
- [ ] No claim of empirical confirmation from synthetic-only demonstrations
- [ ] Review and promotion decisions recorded

## Pilot

WP-BWM-0035 Antediluvian Human Diversity: founder-genotype inverse reconstruction, pedigree-aware forward simulation, and nonuniform-rate sensitivity. Pilot findings and SOP refinements are proposed through reviewed PRs.
