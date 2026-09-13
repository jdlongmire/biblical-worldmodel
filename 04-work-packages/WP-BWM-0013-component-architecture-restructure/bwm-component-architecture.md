# Biblical WorldModel Component Architecture

Status: Draft architecture artifact under WP-BWM-0013
Authority: Design proposal only; no canonical file moves authorized

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

- **TRT — Triadic Reality Theory**
  - logic as rational constraint;
  - information as content;
  - action as causal actualization;
  - actualized reality as contingent state.
- **LRT — Logos Reality Theory**
  - grounding of logic, information, action, intelligibility, and actuality in the Logos.
- **Semantic Actualism**
  - distinction among representable, logically admissible, and actualizable states.

### Epistemology

- Scripture is the primary epistemic authority for biblical-historical claims.
- Nature is secondary evidence and is interpreted rather than treated as a self-interpreting authority.
- Observation, operational measurement, model inference, retrodiction, and actual elapsed history must remain distinct.
- Operational regularity warrants defeasible extrapolation; it does not entail generation of an initial state or actual prior history across a boundary event.

### Hermeneutics

- Scripture interprets Scripture first.
- Immediate context and canonical warrant constrain model formation.
- Historical-grammatical analysis follows canonical constraints.
- Scientific and historical reconstructions are tested within, rather than over, the scriptural boundary.

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

DFM applies across cosmology, biology, geology, anthropology, and chronology.

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

CHFM applies across Earth history, paleontology, climatology, biogeography, archaeology, and chronology.

### Post-Flood History

A distinct post-Flood framework may be formalized later if needed for:

- post-Flood climatic adjustment;
- compressed ice-age models;
- biogeographic redistribution;
- Babel and human dispersal;
- normalization of geological and ecological systems.

## 3. World Domains

World Domains are subject-matter areas. They are not explanatory frameworks. Foundations constrain every domain, while one or more Historical Frameworks may apply to each domain.

### Cosmology and Physical Order

Scope includes:

- Day Four cosmology;
- starlight and observational reach;
- redshift and expansion;
- low initial entropy;
- early galaxy maturity;
- Hubble tension;
- dark matter / dark energy model questions;
- physical-law regularity and initial conditions.

Primary framework interfaces: DFM; potentially comparative DTE models.

### Earth History and Geology

Scope includes:

- tectonics;
- sedimentation;
- stratigraphy;
- fossilization;
- geochemistry;
- hydrothermal alteration;
- radiometric systems;
- catastrophic restructuring;
- post-Flood normalization.

Primary framework interfaces: DFM and CHFM.

### Biology and Life Systems

Scope includes:

- created kinds;
- biological information;
- systems biology;
- genomic function;
- adaptation and variation;
- abiogenesis critiques;
- biological maturity and initialization.

Primary framework interface: DFM.

### Anthropology

Scope includes:

- imago Dei;
- Adam and Eve;
- human nature and personhood;
- consciousness;
- language;
- symbolism;
- engineering and architecture;
- Neanderthal and Denisovan classification;
- human/non-human boundary questions.

Primary framework interfaces: DFM and PFH.

### Archaeology and Chronology

Scope includes:

- human antiquity;
- archaeological context;
- tools, structures, symbolic artifacts, and settlement traces;
- human mortality chronology;
- radiocarbon and other dating systems;
- chronological contamination;
- distinction between retrodictive age and actual elapsed history.

Primary framework interfaces: DFM, PFH, CHFM, and post-Fall mortality chronology requirements.

### Covenant and Redemptive History

Scope includes:

- Fall and covenantal curse;
- Noahic, Abrahamic, Mosaic, Davidic, and New Covenant structures;
- Israel;
- Christ;
- Church;
- kingdom;
- resurrection;
- consummation.

This domain anchors BWM in the full biblical narrative rather than reducing BWM to an origins model.

### Eschatology

May remain a subdomain of covenant/redemptive history or become a peer world domain if its content volume and architectural needs justify separation.

## 4. Integration

Integration evaluates whether foundations, historical frameworks, and world-domain models cohere without hiding tensions.

Primary integration artifacts include:

- framework-domain matrix;
- chronology model;
- evidence-ledger model;
- Bayesian/model-comparison ledgers;
- interface definitions;
- open-problems register;
- predictions and falsifiers;
- contradiction and dependency tracking.

Integration must distinguish:

- doctrinal or scriptural constraint;
- foundational framework;
- historical framework;
- domain model;
- hypothesis;
- empirical proposition;
- observation;
- unresolved tension.

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
8. Repository lifecycle structure shall remain independent from intellectual taxonomy.
9. Cross-cutting relationships shall be represented by interfaces and matrices rather than by forcing every relationship into directory nesting.
10. No file migration shall occur under this work package until inventory, migration manifest, link-impact analysis, and JD approval are complete.

## Proposed canonical target

After acceptance, this artifact should be promoted to:

`02-systems-baseline/2.2-architecture/bwm-component-architecture.md`

Human-Curated, AI-Enabled (HCAE)
