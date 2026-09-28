# Biblical WorldModel Component Architecture

Status: Accepted architecture; gateway refinement proposed under `WP-BWM-0026`
Authority: Principal Operator disposition, 2026-09-13
Source work package: `WP-BWM-0013`

## Purpose

Define the intellectual architecture of Biblical WorldModel (BWM) independently from the repository lifecycle structure.

BWM retains the `00`–`06` repository operating model. This artifact defines how substantive worldmodel content is categorized inside that operating model.

## Governing architecture

BWM content is organized conceptually into four categories:

1. **Foundations**
2. **Historical Frameworks**
3. **World Domains**
4. **Integration**

These categories are not interchangeable. They answer different classes of questions.

Cross-domain invariants are maintained under Integration as governing constraints that preserve consistency when claims move among these four categories. See `integration/cross-domain-invariants.md`.

## 1. Foundations

Foundations govern the entire worldmodel. They define the ontological, epistemological, and hermeneutical commitments within which historical and domain-specific models are evaluated.

### Ontology and metaphysics

- **TRT — Triadic Reality Theory**: externally authoritative foundational-ontology research programme. BWM consumes its governed ontological outputs through a pinned interface.
- **LRT — Logic Realism Theory**: externally authoritative foundational research programme. TRT's canonical source situates LRT within TRT's broader ontology and identifies LRT as formalizing TRT's L3 constituent; LRT retains its own source authority and repository.
- **Semantic Actualism (SA)**: externally authoritative foundational-ontology research programme in philosophy of mind. Its canonical source states that SA and TRT share a constrained-information-in-action form while neither is derived from the other there.

TRT, LRT, and SA source authority remains external to BWM and shall be consumed through pinned BWM interface artifacts rather than forked. BWM Foundation is their integration role, not their source type.

### Epistemology

- Scripture is the primary epistemic authority for biblical-historical claims.
- Nature is secondary evidence and is interpreted rather than treated as a self-interpreting authority.
- Observation, operational measurement, model inference, retrodiction, and actual elapsed history must remain distinct.
- Operational regularity warrants defeasible extrapolation; it does not entail generation of an initial state or actual prior history across a boundary event.

### Hermeneutics

- Scripture interprets Scripture first.
- Immediate context and canonical warrant constrain model formation.
- Historical-grammatical analysis follows canonical constraints.
- Scientific and historical reconstructions are tested within the scriptural boundary.

## 2. Historical Intervals, Boundaries, and Hypotheses

BWM distinguishes the historical categories it owns from externally authoritative research programmes that inform them. A programme's BWM role does not transfer source ownership to BWM.

### Creation / initialization boundary

Historical jurisdiction:

`creation / initialization boundary -> operational created order`

**DFM — Designed Functional Maturity** is the externally authoritative cross-domain research programme supplying the general functional-maturity, constrained-initialization, and retrodiction framework used here. BWM consumes DFM through a pinned interface.

Primary integration questions include the initialized state of the created system, sufficient functional maturity, the warrant of backward extrapolation across an initialization boundary, and the distinction between retrodictive age and actual elapsed history.

### Pre-Fall historical interval

Historical jurisdiction:

`human creation -> Fall boundary`

The interval is a BWM historical category. **PFH — Pre-Fall Hypothesis** is the BWM-owned hypothesis space for proposed reconstructions of underdetermined content within that interval.

PFH may investigate duration, demography, geography, settlement, culture, technology, and related development. Inclusion in PFH does not convert a proposal into established history. Extended pre-Fall duration is one hypothesis within PFH, not a defining commitment of the interval.

### Flood boundary and catastrophic interval

Historical jurisdiction:

`pre-Flood terrestrial order -> Flood catastrophe -> immediate post-Flood terrestrial state`

**CHFM — Catastrophic Hydrotectonic Flood Model** is the externally authoritative historical/physical research programme supplying detailed Flood-mechanism research. BWM consumes CHFM through a pinned interface.

### Post-Flood History

Reserved BWM historical-framework candidate only. It shall not be formalized until distinct explanatory content justifies a separate framework.

### Comparative interpretive families

DFM may also appear as a perspective in BWM comparative model-family analysis. **DTE — Designed Time and Emergence** and **UTE — Undirected Time and Emergence** are comparative interpretive/model families only. They are not Longmire research programmes and are not programme-registry entries.

## 3. World Domains

World Domains are subject-matter areas. Foundations constrain every domain, while one or more Historical Frameworks may apply to each domain.

### Cosmology and Physical Order

Scope includes Day Four cosmology, starlight and observational reach, redshift and expansion, low initial entropy, early galaxy maturity, Hubble tension, dark-component model questions, physical-law regularity, and initial conditions.

### Earth History and Geology

Scope includes tectonics, sedimentation, stratigraphy, fossilization, geochemistry, hydrothermal alteration, radiometric systems, catastrophic restructuring, and post-Flood normalization.

### Biology and Life Systems

Scope includes created kinds, biological information, systems biology, genomic function, adaptation and variation, abiogenesis critiques, and biological maturity/initialization.

### Anthropology

Scope includes imago Dei, Adam and Eve, human nature and personhood, consciousness, language, symbolism, engineering and architecture, Neanderthal/Denisovan classification, and human/non-human boundary questions.

### Archaeology and Chronology

Scope includes human antiquity, archaeological context, tools, structures, symbolic artifacts, settlement traces, human mortality chronology, dating systems, chronological contamination, and the distinction between retrodictive age and actual elapsed history.

### Covenant and Redemptive History

Scope includes the Fall and covenantal curse, Noahic/Abrahamic/Mosaic/Davidic/New Covenant structures, Israel, Christ, Church, kingdom, resurrection, and consummation.

Eschatology remains a subdomain unless later content volume justifies separation.

## 4. Integration

Integration evaluates whether foundations, historical intervals/boundaries, hypotheses, externally sourced programme outputs, and world-domain models cohere without hiding tensions.

Primary integration artifacts include cross-domain invariants, framework-domain mapping, chronology integration, evidence-ledger architecture, Bayesian/model-comparison ledgers, interface definitions, open-problems tracking, predictions/falsifiers, and contradiction/dependency tracking.

Cross-domain invariants define commitments that must remain stable across domain boundaries unless explicitly revised through dependency analysis. They function as constraints and interface conditions, not as substitutes for domain evidence or exegesis.

Integration must distinguish doctrinal/scriptural constraint, foundation, historical framework, domain model, hypothesis, empirical proposition, observation, and unresolved tension.

## Historical sequence

The current BWM historical backbone is:

`Foundations -> creation/initialization boundary [DFM interface] -> pre-Fall historical interval [PFH hypothesis space] -> Fall -> post-Fall/pre-Flood history -> Flood catastrophe [CHFM interface] -> post-Flood history -> covenant/redemptive history -> consummation`

This sequence is historical, not hierarchical. Foundations apply across every stage.

## Architectural rules

1. Foundations shall not be represented as world domains.
2. Historical intervals and boundaries shall not be represented as subject-matter domains.
3. Source type and BWM role are independent dimensions. A research programme may supply a Foundation, historical-boundary, or World Domain role without BWM acquiring source ownership.
4. World Domains may consume multiple programme interfaces, historical categories, and hypotheses.
5. Active research remains in `04-work-packages/` until accepted for promotion.
6. Canonical architecture belongs primarily under `02-systems-baseline/2.2-architecture/`.
7. Requirements and hard constraints belong primarily under `02-systems-baseline/2.1-requirements/`.
8. Repository lifecycle structure remains independent from intellectual taxonomy.
9. Cross-cutting relationships are represented by interfaces, matrices, and invariants rather than forced directory nesting.
10. External foundational/research programmes are consumed through pinned BWM interfaces, preserving source-of-truth ownership.
11. Work packages remain provenance records after promoted derivatives are created.
12. Physical relocation of stable canonical artifacts requires a concrete ownership/navigation benefit and explicit migration control.
13. New cross-domain claims must identify the invariants that constrain them before promotion into canonical BWM requirements.
14. Changes to an invariant require explicit dependency analysis because multiple frameworks or domains may rely on it.

Human-Curated, AI-Enabled (HCAE)
