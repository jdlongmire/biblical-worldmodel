# Biblical WorldModel Component Architecture

Status: Accepted architecture for restructure implementation
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

## 1. Foundations

Foundations govern the entire worldmodel. They define the ontological, epistemological, and hermeneutical commitments within which historical and domain-specific models are evaluated.

### Ontology and metaphysics

- **TRT — Triadic Reality Theory**: logic as rational constraint; information as content; action as causal actualization; actualized reality as contingent state.
- **LRT**: formal logical work situated within TRT and consumed by BWM through a pinned interface to the authoritative TRT repository.
- **Semantic Actualism**: distinction among representable, logically admissible, and actualizable states.

TRT/LRT source authority remains external to BWM and shall be consumed through pinned BWM interface artifacts rather than forked.

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

## 2. Historical Frameworks

Historical Frameworks govern intervals, transitions, or boundary events in the history of the created order. They are cross-domain and may apply simultaneously to cosmology, geology, biology, anthropology, archaeology, and chronology.

### DFM — Designed Functional Maturity

Primary jurisdiction:

`creation / initialization boundary -> operational created order`

Primary questions:

- What state did the created system begin in?
- What constitutes sufficient functional maturity?
- What does backward extrapolation across an initialization boundary legitimately establish?
- Which apparent historical indicators may encode initialized state rather than elapsed history?

### PFH — Pre-Fall History

Primary jurisdiction:

`human creation -> pre-Fall human history -> Fall boundary`

Primary questions:

- What history is biblically admissible between human creation and the Fall?
- Was the Genesis 1:28 mandate operational before the Fall?
- What demographic, geographic, cultural, symbolic, architectural, and technological development may have occurred?
- When does mortal human age accounting become relevant?

The extended pre-Fall human-development model is an initial PFH hypothesis. PFH itself does not depend on an extended duration being established.

### CHFM — Catastrophic Hydrotectonic Flood Model

Primary jurisdiction:

`pre-Flood terrestrial order -> Flood catastrophe -> post-Flood terrestrial state`

Primary questions:

- What catastrophic processes generated major terrestrial restructuring during the Flood?
- How do tectonics, sedimentation, fossilization, hydrothermal alteration, climate, and post-Flood adjustment interact?
- Which geological or geochemical clocks may have been reset, disturbed, inherited, or mixed?

The detailed CHFM research programme remains authoritative in `jdlongmire/catastrophic-hydrotectonic-flood-model`; BWM consumes it through a pinned interface.

### Post-Flood History

Reserved Historical Framework candidate only. It shall not be formalized until distinct explanatory content justifies a separate framework.

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

Integration evaluates whether foundations, historical frameworks, and world-domain models cohere without hiding tensions.

Primary integration artifacts include framework-domain mapping, chronology integration, evidence-ledger architecture, Bayesian/model-comparison ledgers, interface definitions, open-problems tracking, predictions/falsifiers, and contradiction/dependency tracking.

Integration must distinguish doctrinal/scriptural constraint, foundation, historical framework, domain model, hypothesis, empirical proposition, observation, and unresolved tension.

## Historical sequence

The current BWM historical backbone is:

`Foundations -> DFM / creation and initialization -> PFH -> Fall -> post-Fall / pre-Flood history -> CHFM / Flood catastrophe -> post-Flood history -> covenant/redemptive history -> consummation`

This sequence is historical, not hierarchical. Foundations apply across every stage.

## Architectural rules

1. Foundations shall not be represented as world domains.
2. Historical Frameworks shall not be represented as subject-matter domains.
3. World Domains may consume multiple Historical Frameworks.
4. A Historical Framework may span multiple World Domains.
5. Active research remains in `04-work-packages/` until accepted for promotion.
6. Canonical architecture belongs primarily under `02-systems-baseline/2.2-architecture/`.
7. Requirements and hard constraints belong primarily under `02-systems-baseline/2.1-requirements/`.
8. Repository lifecycle structure remains independent from intellectual taxonomy.
9. Cross-cutting relationships are represented by interfaces and matrices rather than forced directory nesting.
10. External foundational/research programmes are consumed through pinned BWM interfaces, preserving source-of-truth ownership.
11. Work packages remain provenance records after promoted derivatives are created.
12. Physical relocation of stable canonical artifacts requires a concrete ownership/navigation benefit and explicit migration control.

Human-Curated, AI-Enabled (HCAE)
