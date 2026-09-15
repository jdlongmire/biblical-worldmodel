# WP-BWM-0019 — Repository Tune-Up and Front Door

Status: proposed
Owner: Principal Operator / BWM
Date opened: 2026-09-15

## Intent

Tune the `biblical-worldmodel` repository so that its GitHub front door, repository documentation, navigation, metadata, governance pointers, and contributor/operator paths accurately describe the current BWM product and architecture.

The immediate trigger was concern that the repository lacked a repository-specific README. Inspection shows that a root `README.md` does exist and is BWM-specific, but it is now sufficiently important and fast-moving that it should be treated as a governed front-door artifact and audited against the current repository state rather than assumed current.

## UID and semantic-duplication validation

Before allocation:

- `WP-BWM-0018` was the latest known BWM work package after the Sixth Day integration;
- repository code search found no `WP-BWM-0019`;
- open issues were searched for repository tune-up / README / documentation-hygiene work and no semantic duplicate was found.

`WP-BWM-0019` is therefore allocated to this effort.

## Problem statement

The repository has evolved rapidly through public-site standup, component restructuring, MxM integration, PFH/DFM/CHFM architecture work, publication workflows, and research artifacts. A repository can remain structurally valid while its human-facing front door drifts from the actual product.

The root README currently contains substantial BWM-specific content, including project identity, website links, repository ownership, current status, file routing, build instructions, and the `00`–`06` structure. The tune-up must therefore begin with an audit rather than replacing it reflexively.

## Scope

### 1. Root README audit and revision

Evaluate the current `README.md` for:

- clear statement of what Biblical WorldModel is;
- distinction between the BWM public publication repository and authoritative technical programme repositories;
- current BWM component architecture, including Foundations, DFM, CHFM, PFH, and integration surfaces;
- current public-site status and canonical URL;
- correct repository ownership and disposition language;
- useful paths for readers, researchers, contributors, and AI agents;
- build/test instructions that match current CI;
- stale dates, stale status claims, stale work-package references, and obsolete future-work statements;
- appropriate links to `AGENTS.md`, `MXM.md`, work packages, architecture, operations, publications, and the public site;
- concise GitHub-front-page usability. The README should orient before it documents implementation detail.

### 2. Repository metadata audit

Inspect and, where authorized by available tooling, align:

- repository description;
- homepage URL;
- topics/tags if supported;
- default branch assumptions;
- Pages/public-site references;
- license presentation;
- issue/contribution entry points.

Metadata changes requiring repository administration beyond available connector permissions are to be recorded as explicit follow-up actions rather than guessed or silently omitted.

### 3. Documentation topology audit

Check whether each major repository area has an adequate local README or index where one materially improves navigation:

- `00-meta-model/`;
- `01-strategic-baseline/`;
- `02-systems-baseline/` and major architecture branches;
- `03-solutions-baseline/` and site root;
- `04-work-packages/`;
- `05-mxm-construct/`;
- `06-operations/`;
- `graphics-library/`;
- publication article/response directories.

Do not create README files mechanically. Add or revise them only where the directory has a meaningful contract, ownership boundary, or navigation function.

### 4. Work-package registry hygiene

Audit `04-work-packages/README.md` against the live directory:

- all active/completed WPs represented;
- UID sequence and titles accurate;
- status/disposition language consistent;
- no stale template artifacts presented as live BWM work;
- links resolve.

### 5. Architecture and terminology consistency

Check front-door documentation against the post-`WP-BWM-0013` architecture and subsequent accepted work. In particular:

- PFH is a historical framework, not merely the extended pre-Fall hypothesis;
- DFM and CHFM retain their correct jurisdictions;
- TRT/LRT remain foundational programme interfaces rather than being conflated with historical models;
- Day 6 commissioning material is represented where relevant without overloading the README;
- BWM remains the integrative publication/worldmodel layer rather than silently becoming the authoritative source for every programme.

### 6. GitHub hygiene

Audit repository-visible maintenance surfaces for obvious drift:

- `.github/` workflows and templates;
- stale branches or references where visible;
- broken internal links;
- duplicated or orphaned navigation artifacts;
- repository-local contribution/run instructions;
- generated artifacts accidentally tracked;
- obvious naming inconsistencies.

Destructive cleanup is out of scope without explicit approval. Findings can be recorded for later disposition.

### 7. Verification

Run or obtain evidence for the checks available to this harness:

- repository layout/conformance checks;
- strict MkDocs build / publication workflow;
- internal link/path checks;
- navigation consistency;
- branch-to-main comparison;
- GitHub Actions result for the PR head.

Do not claim local scripts were run if only GitHub-hosted verification was available.

## Deliverables

1. Revised root `README.md` serving as the canonical GitHub front door.
2. Repository tune-up findings and disposition record under this WP.
3. Updated work-package registry.
4. Targeted directory README/index corrections where the audit demonstrates a need.
5. Corrected repository/site navigation and cross-links where required.
6. Metadata recommendations or changes, depending on available authorization/tooling.
7. Verification evidence and a PR suitable for Principal Operator acceptance.

## README design target

The root README should answer, in this order:

1. What is Biblical WorldModel?
2. Where is the live site?
3. What does this repository own?
4. What are the major BWM components/programmes?
5. Where should a reader/researcher/contributor start?
6. How is the repository organized?
7. How is it built and verified?
8. What are the epistemic/source and contribution expectations?
9. What is the project status and license?

Detailed operator procedures should remain in `06-operations/` and MxM/harness instructions in `AGENTS.md` / `MXM.md`, with the README linking rather than duplicating them.

## Acceptance criteria

- `WP-BWM-0019` is collision-free and semantically non-duplicative.
- Root README is demonstrably BWM-specific and aligned to current repository state.
- README does not function as a stale status dump or duplicate detailed runbooks.
- Major repository ownership boundaries and programme jurisdictions are clear.
- Live site, architecture, publication, work-package, agent, and operations paths are discoverable from the front door.
- Work-package registry matches the live WP directory.
- No new unnecessary README proliferation is introduced.
- Internal links added or changed by the WP resolve.
- Available repository/site verification passes, or failures are explicitly recorded.
- A PR contains the audit evidence and acceptance mapping.

## Execution sequence

1. Reload repository governance and current architecture.
2. Inventory root and major directory documentation.
3. Audit current root README against repository state.
4. Audit WP registry and GitHub-visible maintenance surfaces.
5. Record findings before broad edits.
6. Revise root README and targeted local indexes.
7. Correct navigation/cross-links and metadata where supported.
8. Run available verification.
9. Open PR with findings and acceptance-criteria mapping.
10. Merge only after Principal Operator acceptance.

## State

Proposed: complete.
Implemented: pending.
Verified: pending.
Accepted: pending.
Deployed: pending.
