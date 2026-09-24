# WP-BWM-0026 — Research Programme Gateway Architecture

## Status

Proposed / active architecture investigation

## Purpose

Formalize Biblical WorldModel (BWM) as the integration and publication gateway for associated authoritative research programmes while preserving source-of-truth ownership, epistemic classification, and conflict visibility.

This work package begins from the live authoritative repositories rather than reconstructing programme identity from conversational or duplicated BWM summaries.

## Problem

BWM already distinguishes Foundations, Historical Frameworks, World Domains, and Integration and already consumes several external programmes through interfaces. The research ecosystem has matured beyond the taxonomy currently encoded in BWM:

- Logic Realism Theory (LRT) is an established, independently authoritative research programme and repository.
- Triadic Reality Theory (TRT) is an established foundational-ontology research programme. Its canonical repository states that TRT is the broader ontology within which LRT is situated and that LRT formalizes TRT's L3 constituent.
- Designed Functional Maturity (DFM) has become an independently authoritative research programme and repository rather than merely BWM-owned historical-framework content.
- Catastrophic Hydrotectonic Flood Model (CHFM) is already an independently authoritative research programme consumed by BWM.
- PFH is to be renamed **Pre-Fall Hypothesis**, distinguishing the hypothesis from the biblically bounded pre-Fall historical interval.
- DTE and UTE are comparative interpretive/model families only. They are not Longmire research programmes and are not intended to become research programmes.

## Initial authoritative inventory

| Construct | Initial classification | Source authority | BWM relationship |
|---|---|---|---|
| BWM | integration and publication gateway | this repository | owns integration, interfaces, synthesis, publication |
| TRT | foundational research programme | `jdlongmire/triadic-reality-theory` | consumed through governed interface |
| LRT | foundational research programme | `jdlongmire/logic-realism-theory` | consumed through governed interface; relationship to TRT represented from source |
| DFM | research programme | `jdlongmire/designed-functional-maturity` | consumed and integrated through governed interface |
| CHFM | research programme | `jdlongmire/catastrophic-hydrotectonic-flood-model` | consumed and integrated through governed interface |
| PFH | Pre-Fall Hypothesis | BWM pending ownership review | hypothesis concerning underdetermined content within the pre-Fall interval |
| DTE | comparative interpretive/model family | BWM canonical comparison artifact | comparison/reference model only |
| UTE | comparative interpretive/model family | BWM canonical comparison artifact | comparison/reference model only |
| Semantic Actualism | foundation/construct, classification pending source audit | to verify | do not reclassify until audited |

## Gateway authority verbs

### OWNS
The authoritative repository controls the research claim, proof/evidence, status, revision, and failure conditions.

### CONSUMES
BWM imports a governed output from an authoritative source without taking ownership of its proof or research history.

### INTEGRATES
BWM relates outputs from multiple programmes, hypotheses, frameworks, and domains; tracks dependencies and conflicts; and evaluates world-model coherence.

### PUBLISHES
BWM translates governed integrated results into reader-facing WorldModel material without silently strengthening source claims.

## Source-of-truth rule

BWM shall not silently fork externally authoritative research.

If BWM integration exposes a conflict with an imported proposition, BWM records the conflict and returns it to the owning programme for disposition. The owning programme may revise, reject, retain with qualification, or record unresolved accounting. BWM consumes the resulting governed state.

## Proposed gateway contract

Each externally authoritative programme should expose or permit BWM to maintain a pinned interface containing:

- programme identity and canonical repository;
- interface/version or commit pin;
- scope and jurisdiction;
- hard-core commitments where applicable;
- exported propositions used by BWM;
- assumptions and boundary conditions;
- dependencies on other programmes;
- unresolved questions and tensions;
- predictions, discriminators, falsifiers, or failure conditions where applicable;
- BWM implications and cross-domain constraints;
- canonical source links.

The interface is BWM-owned integration metadata. The underlying research remains programme-owned.

## Relationship discipline

Programme association, ontological containment, formalization relationship, evidential support, and logical dependency are different relations and shall not be collapsed into a single hierarchy.

In particular, BWM shall represent the TRT/LRT relationship using their canonical repositories. Current TRT source states that TRT is the broader ontology within which LRT is situated, while LRT retains its own authoritative programme and repository.

## PFH terminology decision to implement

Use:

- **pre-Fall historical interval** for the bounded historical category from human creation to the Fall;
- **PFH, Pre-Fall Hypothesis** for proposed reconstructions of underdetermined content within that interval.

PFH may address duration, demography, geography, settlement, culture, technology, and related questions without those proposals becoming canonical history merely by inclusion in BWM.

## DFM / DTE / UTE rule

DFM has two legitimate roles:

1. an independently authoritative research programme;
2. the DFM perspective used within BWM comparative model-family analysis.

DTE and UTE have only the second kind of role. They are comparative interpretive/model families and shall not be represented as peer research programmes.

## Work plan

### Tranche A — authoritative inventory
Audit BWM, TRT, LRT, DFM, CHFM, and relevant canonical artifacts. Classify named constructs by type and authority.

### Tranche B — gateway contract
Define interface schema, authority verbs, source pinning, dependency semantics, and conflict-return protocol.

### Tranche C — canonical taxonomy corrections
Prepare controlled changes to BWM component architecture, including LRT/TRT wording, DFM external authority, PFH terminology/classification, and DTE/UTE non-programme status.

### Tranche D — programme interfaces
Establish or update BWM-facing interfaces for TRT, LRT, DFM, and CHFM without forcing common internal repository structures.

### Tranche E — verification
Check public navigation, work-package dependencies, canonical links, terminology, and absence of duplicated source-of-truth research.

## Acceptance criteria

This WP succeeds when:

1. every associated programme/construct has an explicit type and authority;
2. BWM's gateway role is formally defined;
3. external programme research remains externally authoritative;
4. imported claims are pinned and traceable;
5. integration conflicts have a governed return path;
6. PFH means Pre-Fall Hypothesis throughout canonical BWM material;
7. DTE and UTE cannot reasonably be mistaken for Longmire research programmes;
8. DFM is represented as an authoritative research programme while remaining usable in comparative model-family analysis;
9. TRT/LRT relationships match their authoritative repositories;
10. public synthesis cannot silently strengthen programme claims.

Human-Curated, AI-Enabled (HCAE)
