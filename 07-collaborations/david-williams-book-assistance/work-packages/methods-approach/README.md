# Methods and Approach

**Program:** David Williams Book Assistance (DWBA)  
**Status:** governing internal method  
**Lead author:** David Williams  
**Research/editorial assistance:** J.D. Longmire

## Purpose

This document defines how the DWBA program converts David Williams' notes, field observations, bibliographic leads, and technical argument into a source-grounded book manuscript. The method is designed to preserve authorship, expose uncertainty, prevent citation laundering, and keep observation distinct from interpretation.

## 1. Epistemic layers

Every substantive claim should be traceable to one of four layers:

1. **Source observation:** what a primary publication, dataset, field report, or supplied source actually reports.
2. **David Williams interpretation:** the geological inference David draws from those observations.
3. **Editorial/research inference:** an inference introduced during assistance, which must be labeled and remain open to David's correction.
4. **BWM interpretation:** any later use inside Biblical WorldModel. This is outside the authority of the book program unless separately adopted through BWM governance.

These layers must not be silently collapsed.

## 2. Source hierarchy and citation recovery

Primary sources are preferred. An author/year fragment in David's notes is a lead, not a verified citation.

For each material claim:

1. search for the primary source;
2. verify bibliographic identity;
3. inspect the relevant passage, figure, table, or dataset when accessible;
4. record exactly what the source supports;
5. record what it does not establish;
6. identify later interpretation separately;
7. record contradictory or qualifying literature;
8. assign a confidence state in the evidence ledger.

If a primary source is inaccessible but a reliable secondary source gives usable page-level evidence, cite it explicitly as secondary and use `as cited in` when it is the route to the primary claim. Never fabricate missing bibliographic fields.

Confidence states:

- **HIGH:** verified against the primary source.
- **MEDIUM:** supported by a reliable secondary source with sufficiently specific evidence.
- **LOW:** tertiary, incomplete, or weakly documented support.
- **UNCERTAIN:** unresolved or not yet assessable.

## 3. Observation before thesis

Research begins with the geological observation rather than with the desired conclusion. Examples include source-reservoir geochemical correlation, measured permeability, inferred expulsion efficiency, diagenetic relationships, paleostructure, dry-hole history, fracture chronology, and carrier-bed architecture.

The next question is what histories are physically compatible with the observation. David's early-migration and trap-timing interpretation is then compared with serious alternatives such as generation-induced overpressure, transient microfracturing, fault-assisted migration, episodic charge, remigration, leakage, and late structural development.

The purpose is discriminating evidence. A case that can equally support several histories carries less weight than one whose chronology excludes important alternatives.

## 4. Temporal reconstruction

The program treats petroleum systems as evolving state histories. For each major case, reconstruct as far as evidence permits:

`deposition -> burial/compaction -> maturation -> generation -> expulsion -> migration -> trap availability -> preservation/remigration`

These events may overlap or recur. The sequence is an analytical scaffold, not an assumption of a single linear episode.

Particular attention should be paid to the hydraulic state of the system at the inferred time of migration: matrix permeability, fractures, faults, bedding-plane pathways, carrier beds, overpressure, seal competence, and diagenetic modification.

## 5. Falsification and competing explanations

A case is strengthened when independent evidence converges on the same chronology. A case is weakened when the chronology depends on one ambiguous proxy or when a competing mechanism explains the observations equally well.

For each major case study ask:

- What observation would be expected if David's interpretation is correct?
- What would be expected under the strongest competing explanation?
- Which evidence can distinguish them?
- What result would force qualification or rejection of the proposed interpretation?

Weak examples should be downgraded or removed rather than defended for rhetorical completeness.

## 6. Evidence ledger

`../../research/evidence-ledger.md` is the program's claim-level control artifact. Material quantitative or historical claims should enter the ledger before they become load-bearing manuscript claims.

The ledger should capture claim ID, wording, source lead, verification state, confidence, manuscript use, and material caveats. Where one sentence contains separable claims with different evidentiary status, split them.

Quarantined claims may be discussed internally but should not be written into manuscript prose as established facts.

## 7. Manuscript development

Markdown is the canonical manuscript format. Each chapter is developed as a book-length chapter, with enough geological explanation for a technically literate reader to follow the argument without already sharing David's interpretation.

Drafting sequence:

1. establish the chapter question and role in the book;
2. identify load-bearing claims;
3. mature the relevant evidence ledger entries;
4. construct the chapter argument from verified observations outward;
5. present competing explanations fairly;
6. distinguish established result, inference, and open question;
7. perform citation and artifact-integrity review;
8. send to David for geological and authorial review;
9. revise from David's corrections and redirection.

Draft prose should not wait for every background citation to be perfected, but unresolved claims must not masquerade as verified evidence.

## 8. Author review

David's review is substantive, not ceremonial. He may correct geological interpretation, reject framing, add field experience, change emphasis, or redirect the argument. Draft assistance does not transfer authorship.

Review should occur chapter by chapter so the program does not accumulate large amounts of prose on an incorrect interpretation.

## 9. Artifact integrity

A successful write is not sufficient evidence that a manuscript artifact is complete. After any substantial chapter write or integration:

1. re-fetch the committed file;
2. verify the opening metadata;
3. verify expected major headings;
4. verify the final paragraph and reference section;
5. check for truncation or duplicated continuation text;
6. record approximate word count when feasible.

Large GitHub writes should be handled in controlled increments or by a verified integration method. The Chapter 1 truncation event established this as a mandatory control.

## 10. References and bibliography

References should be built from verified bibliographic records. Primary sources should be cited as primary only when actually recovered or directly verified. Secondary routes must remain visible.

Reference formatting can be normalized late in the drafting process, but source identity and provenance must be correct from the beginning.

## 11. Relationship to BWM

The book program may discover evidence relevant to BWM geology, DFM, or Flood-related research. Such relevance should be recorded as a possible transfer candidate. It does not alter the evidentiary status of the book claim and does not authorize importing BWM assumptions into David's argument.

The book should be capable of standing on its geological evidence and explicit interpretive reasoning.

## 12. Definition of ready for author review

A chapter is ready for David when:

- the chapter is structurally complete and book-length for its role;
- the canonical Markdown artifact passes integrity checks;
- load-bearing citations are verified or visibly qualified;
- unresolved high-risk claims are quarantined or identified;
- major competing explanations are represented;
- the chapter has a coherent transition into the next chapter;
- the draft is clearly marked as working material for David's review.

This is the minimum gate for author review, not the publication-ready standard.
