# WP-BWM-0019 Repository Tune-Up Findings

Audit date: 2026-09-15
Branch: `wp-bwm-0019-repository-tuneup`

## Executive finding

The repository has a substantial BWM-specific root README. The problem is drift and front-door density rather than absence. The current README mixes durable orientation with a dated delivery snapshot, detailed build/run instructions, and a partial roadmap. Several repository-local README files also retain upstream/template language that no longer accurately describes this product.

The recommended tune-up is targeted rather than structural: preserve the accepted `00`–`06` layout and BWM component architecture, replace stale template text, make the root README durable and navigational, repair the work register, and add the one materially missing local entry point at `05-mxm-construct/README.md`.

## Findings

### F1 — Root README exists and is BWM-specific, but has become too operational

Severity: medium
Disposition: revise

The root README correctly identifies Biblical WorldModel, the live site, project ownership, repository ownership boundaries, build tooling, the `00`–`06` layout, contribution paths, and licensing. It is therefore not a generic template README.

Drift identified:

- status date is fixed at 2026-09-12;
- roadmap is partial and stops at WP-BWM-0017 while current work has advanced through WP-BWM-0019;
- roadmap contains status language that conflicts with the work register, including WP-BWM-0009;
- detailed browser/build/publication instructions duplicate the site README and operations runbooks;
- the accepted post-WP-BWM-0013 intellectual architecture is not presented as a first-class orientation surface;
- PFH and the Foundations / Historical Frameworks / World Domains / Integration taxonomy are difficult to discover from the front door;
- the README is long enough that the project identity and intellectual architecture compete with delivery mechanics.

Recommendation: replace dated status/roadmap material with durable project-status language and links to the work register; add a concise component-architecture section; retain a minimal quick-build section and route detailed procedures to site/operations documentation.

### F2 — Work-package register is incomplete

Severity: high
Disposition: correct

`04-work-packages/README.md` omits:

- WP-BWM-0015 — Observation, Purpose, and the Unobserved Past;
- WP-BWM-0018 — Sixth Day Artifacts Revision and Integration;
- WP-BWM-0019 — Repository Tune-Up and Front Door.

The register also contains stale status prose, including WP-BWM-0009 being described in the table as canonicalized while later prose still describes it as active/proposed for canonicalization in the root README.

Recommendation: add 0015, 0018, 0019 and make the register the single front-door status index rather than duplicating a roadmap in root README.

### F3 — `.github/README.md` is stale template text and factually false

Severity: high
Disposition: replace

The file states that `.github/` is empty of workflows/templates by design. The directory now contains `workflows/`, including the live GitHub Pages publication workflow. This is clear template residue.

Recommendation: replace with BWM-specific GitHub automation documentation and point to the workflow/runbook.

### F4 — `03-solutions-baseline/README.md` contains wrong product language

Severity: high
Disposition: replace

The file says: "The aide implementation lives in 05-mxm-construct." BWM is a publication product, and the acting aide/runtime is external. This conflicts with `MXM.md` and the repository mission.

Recommendation: redefine Solutions Baseline as the implemented BWM publication product, principally the MkDocs site under `site/`, and point operational/harness material to their actual locations without calling them the product implementation.

### F5 — `05-mxm-construct/` lacks a local README

Severity: medium
Disposition: add

The directory contains `meta-harness/`, `memory/`, and `means/` but no local README. Because this directory has a specific repository-working-guidance boundary and is easily mistaken for a deployed aide/runtime, a local entry point materially improves correctness.

Recommendation: add a concise README stating that this is repository-scoped MxM guidance, not a new aide or deployment identity; route to root `MXM.md`, meta-harness, memory, and means.

### F6 — Major baseline README coverage is otherwise adequate

Severity: none
Disposition: retain

`00-meta-model`, `01-strategic-baseline`, `02-systems-baseline`, `03-solutions-baseline`, `04-work-packages`, and `06-operations` all have root-level README/index files. The architecture directory has a useful canonical index, and publication articles have an index. No broad README proliferation is warranted.

### F7 — Accepted intellectual architecture is stronger than the root front door implies

Severity: medium
Disposition: expose

The accepted component architecture defines four substantive categories:

1. Foundations
2. Historical Frameworks
3. World Domains
4. Integration

It places DFM, PFH, and CHFM under Historical Frameworks and TRT/LRT/Semantic Actualism under Foundations, while retaining external source-of-truth discipline for designated technical programmes.

Recommendation: surface this architecture concisely in root README and link directly to `bwm-component-architecture.md` and the framework-domain matrix.

### F8 — Public article index is current for the Sixth Day work

Severity: none
Disposition: retain

The article index includes both `The Sixth Day` and `The Naming of the Animals within the Sixth Day` under Creation and Pre-Fall History. No correction is required there for this WP.

### F9 — Site README is detailed and product-specific

Severity: none
Disposition: retain as detailed implementation guide

`03-solutions-baseline/site/README.md` accurately documents the MkDocs implementation, build, publication, assets, SEO, browser verification, and product boundaries. Root README should link to it instead of reproducing equivalent detail.

### F10 — Operations README is concise and appropriately bounded

Severity: low
Disposition: retain

`06-operations/README.md` correctly routes onboarding, capability inventory, recovery, and machine-local scratch. Detailed publication procedures remain in runbooks.

## Planned edits

1. Rewrite root `README.md` as a durable BWM front door.
2. Repair `04-work-packages/README.md` and add 0015, 0018, 0019.
3. Replace stale `.github/README.md` template text.
4. Replace stale `03-solutions-baseline/README.md` aide language.
5. Add `05-mxm-construct/README.md`.
6. Avoid changing accepted component architecture or creating unnecessary local README files.
7. Verify links/build/workflow before PR acceptance.

## Metadata observation

The repository content clearly identifies the canonical site as `https://worldmodel.thinxai.net/`. Repository-administration metadata such as GitHub description/homepage/topics should be inspected separately if connector permissions expose those fields. No administrative metadata change is claimed by this audit.

Human-Curated, AI-Enabled (HCAE)
