# David Williams Book Assistance: Internal Work Packages

This directory is the internal execution layer for the David Williams book-assistance program. It governs research, source recovery, manuscript development, review, and integration work performed in support of David's book.

## Authority boundary

David Williams is the lead author and owns the book's argument, geological judgments, and final manuscript decisions. J.D. Longmire provides research, architecture, editorial, citation, and drafting assistance. AI-assisted work is subordinate to human review.

Material developed here does not become a Biblical WorldModel conclusion merely because the collaboration is hosted in the BWM repository. Any transfer into BWM requires separate evaluation and explicit adoption.

## Canonical program artifacts

- `../sources/` preserves supplied source material and provenance.
- `../research/` contains evidence and citation work, including the evidence ledger.
- `../chapters/` contains canonical manuscript drafts in Markdown.
- `methods-approach/README.md` defines the governing research and drafting method.
- `work-packages/` decomposes program work into bounded, reviewable efforts.

## Work-package convention

Local work packages use the namespace `WP-DWBA-####-slug`. The namespace is local to this collaboration and must not be confused with repository-level `WP-BWM-####` identifiers.

Before allocating a new DWBA UID, check this directory and any open program issues for both numeric collision and semantic duplication.

Each work package should state:

1. objective and research question;
2. scope and exclusions;
3. inputs and provenance;
4. claims or evidence under examination;
5. primary-source recovery requirements;
6. manuscript deliverables;
7. verification and acceptance criteria;
8. unresolved questions and disposition.

## Initial work-package map

- `WP-DWBA-0001-chapter-1-integration`: integrate, verify, and prepare Chapter 1 for David's first review.
- Future chapter packages should normally be created when their research basis is sufficiently mature to begin manuscript development.
- Cross-cutting source-recovery efforts may receive their own work packages when they span multiple chapters or require substantial investigation.

## Status model

Use: `proposed`, `active`, `blocked`, `author-review`, `revision`, `complete`, or `retired`.

A manuscript work package is not `complete` merely because prose exists. Completion requires source integrity, artifact integrity, internal review, and the intended author-review disposition.
