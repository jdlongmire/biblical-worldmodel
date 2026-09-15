# WP-DWBA-0001: Chapter 1 Integration

**Status:** blocked-mechanical-assembly  
**Program:** David Williams Book Assistance  
**Chapter:** 1, `The Timing Problem`

## Objective

Produce one complete, internally verified canonical Markdown draft of Chapter 1 suitable for David Williams' first substantive author review.

## Current condition

The substantive Chapter 1 Draft 0.1 is complete across three ordered Markdown source segments. The initial large GitHub write truncated mid-sentence, so continuation files were used to preserve the remainder without further loss. The joins and final ending have now been inspected directly from repository state.

A chapter integration manifest is maintained at `../../../chapters/01-the-timing-problem-MANIFEST.md`. It defines the authoritative source order and exact assembly rule.

## Inputs

- `../../../chapters/01-the-timing-problem.md`
- `../../../chapters/01-the-timing-problem-continuation-a.md`
- `../../../chapters/01-the-timing-problem-continuation-b.md`
- `../../../chapters/01-the-timing-problem-MANIFEST.md`
- `../../../research/evidence-ledger.md`
- David Williams' supplied hydrocarbon-migration/source-rock notes
- verified primary and secondary literature recovered during citation research

## Completed work

- Inspected all three manuscript segments from current GitHub state.
- Verified the exact truncation point in the original canonical file.
- Verified that continuation A reconstructs the interrupted sentence and continues through Section 10.
- Verified that continuation B begins Section 11 and completes Sections 11-19, the conclusion, and working references.
- Verified that the Adkins quantitative claim remains quarantined.
- Verified that serious alternative mechanisms remain represented.
- Created a formal integration manifest with deterministic assembly instructions.

## Remaining work

1. Mechanically assemble the three source segments into one canonical `../../../chapters/01-the-timing-problem.md` without passing the entire manuscript through a connector-sized generative rewrite.
2. Remove continuation headers and integration notes during assembly.
3. Re-fetch the resulting canonical file and verify opening metadata, all Sections 1-19, conclusion, references, and final paragraph.
4. Record word count.
5. Only then change chapter disposition to `author-review` and retire the continuation files.

## Blocker

The GitHub connector accepts normal text writes but the first book-length replacement was truncated in transit. Repeating a full-manuscript generative replacement through the same path would create an avoidable integrity risk. The remaining task is therefore classified as mechanical assembly rather than manuscript drafting.

## Acceptance criteria

- One canonical Chapter 1 Markdown file.
- No truncation.
- No continuation dependency.
- Coherent book-length chapter from opening through conclusion.
- Sections 1-19 and references intact.
- Load-bearing evidence either verified or visibly qualified.
- Artifact re-fetched and ending verified.
- Chapter status changed to `author-review` only after artifact-integrity verification.

## Authority boundary

David Williams retains final authority over geological interpretation and manuscript content. Completion of this work package means the chapter is ready for his review, not that it is final or publication-ready.
