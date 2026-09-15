# Figures

**Program:** David Williams Book Assistance  
**Canonical figure format:** source/design files plus publication-ready rendered derivatives  
**Initial scope:** Chapter 1, `The Timing Problem`

## Purpose

This folder manages figures that add explanatory or evidentiary value to the manuscript. Figures are part of the argument. They should clarify temporal relationships, distinguish observations from interpretations, expose competing mechanisms, or summarize verified quantitative evidence. Decorative graphics are out of scope.

## Figure architecture for Chapter 1

| ID | Working title | Type | Purpose | Priority | Evidence status |
|---|---|---|---|---|---|
| FIG-1.1 | A Petroleum System Is a History | Conceptual time-evolution schematic | Establish the governing idea that source, pathway, reservoir, seal, and trap evolve through time rather than existing as a static cross-section. | HIGH | Conceptual; grounded in Chapter 1 framework |
| FIG-1.2 | The Petroleum-System Timing Chain | Process/timeline diagram | Show Generation -> Expulsion -> Migration -> Trap Availability -> Preservation, including overlap, recurrence, leakage, recharge, and remigration. | MEDIUM | Conceptual |
| FIG-1.3 | The Rock We Measure Is the End Product | Burial/diagenetic evolution schematic | Show deposition -> early burial -> compaction/diagenesis -> generation/expulsion interval -> present rock, with qualitative changes in porosity, permeability, water content, effective stress, fractures, and hydrocarbon saturation. | HIGH | Conceptual; quantitative axes prohibited unless sourced |
| FIG-1.4 | The Barnett: Petroleum That Stayed and Petroleum That Escaped | Data-informed source/retention/expulsion diagram | Show Barnett as source and unconventional reservoir while Barnett-derived petroleum occurs outside the source interval. Include Jarvie et al. modeled generation/expulsion result with explicit model attribution. | HIGH | Requires evidence-ledger gate; ~60% expulsion currently HIGH confidence |
| FIG-1.5 | Same Basin, Different Timing | Three-panel paleostructural sequence | Visualize the trap-timing hypothesis: Trap A exists during principal migration and fills; future Trap B is absent/open; Trap B forms later and is barren in the present geometry. | HIGHEST | Hypothesis schematic, not field evidence |
| FIG-1.6 | Multiple Pathways Through Tight Rock | Competing-mechanisms schematic | Fairly represent early connected pores, compaction-related fluid movement, generation-induced microfracturing, natural fractures/faults, bedding-plane pathways, carrier beds, and episodic expulsion. | MEDIUM-HIGH | Conceptual; prevents question-begging |
| FIG-1.7 | Diagenesis as a Geological Clock | Comparative petrographic/sequence schematic | Contrast charge-before-cementation with charge-after-cementation and show how relative timing might be inferred from preserved rock relationships. | HIGH | Conceptual until individual field cases are verified |
| FIG-1.8 | How the Timing Hypothesis Will Be Tested | Convergence/evidence architecture | Connect source correlation, maturity, burial history, paleostructure, diagenesis, fluid inclusions, pathways, productive/barren traps, and competing mechanisms into a convergence test. | MEDIUM-HIGH | Methods figure |

## Signature figure

`FIG-1.5 Same Basin, Different Timing` is the candidate signature figure for Chapter 1 and potentially for the book's overall thesis.

Proposed three-panel sequence:

1. **Early state:** source system developing; Trap A already exists; future Trap B location has not yet become an effective closure.
2. **Principal migration state:** petroleum migrates through the active carrier/pathway system and accumulates in Trap A while passing the future location of Trap B.
3. **Present state:** both structures now appear geometrically favorable. Trap A is charged. Trap B is barren because it became effective after the principal charge interval, absent later charge or remigration.

The caption must state that this is a hypothesis schematic. It does not establish that every barren trap formed too late.

## Visual semantics

Use a consistent visual grammar throughout the book:

- **Observed/present state:** solid boundary or solid symbol.
- **Reconstructed historical state:** visually differentiated historical/reconstructed treatment.
- **Demonstrated migration relationship:** solid directional arrow when supported by source correlation or equivalent evidence.
- **Hypothesized migration pathway:** dashed directional arrow.
- **Temporal constraint:** timeline/clock marker.
- **Unresolved relationship:** explicit question marker or `unresolved` label.
- **Verified quantitative result:** number accompanied by source/caption attribution.
- **Model output:** explicitly labeled `modeled`, including assumptions/context where material.

Do not use visual certainty stronger than the underlying evidence.

## Evidence and citation rules

1. Every data-derived figure must trace its numbers and factual relationships to `../research/evidence-ledger.md`.
2. Primary sources are preferred for figure data.
3. Secondary-source data must be identified as secondary or `as cited in` when appropriate.
4. Hypothesis schematics must be labeled as hypothesis/conceptual figures.
5. Do not convert uncertain claims into visually authoritative graphics.
6. The Adkins `~200 salt domes / ~2,000 ft overburden` claim is **not approved for figure use** until the primary source is recovered and verified.
7. Large resource estimates such as Monterey OOIP must distinguish oil in place, technically recoverable resource, reserves, and production.
8. Figure captions are part of the evidence apparatus and must preserve material qualifications.

## Chapter 1 production order

Initial production should proceed in this order:

1. `FIG-1.5` Same Basin, Different Timing
2. `FIG-1.1` A Petroleum System Is a History
3. `FIG-1.4` The Barnett: Petroleum That Stayed and Petroleum That Escaped
4. `FIG-1.3` The Rock We Measure Is the End Product
5. `FIG-1.7` Diagenesis as a Geological Clock
6. `FIG-1.6` Multiple Pathways Through Tight Rock
7. `FIG-1.8` How the Timing Hypothesis Will Be Tested
8. `FIG-1.2` The Petroleum-System Timing Chain

This order prioritizes figures with the greatest argumentative value and establishes the visual language before lower-priority diagrams are produced.

## Proposed folder structure

As figure work begins, use one subfolder per figure:

```text
figures/
  README.md
  chapter-01/
    FIG-1.1-petroleum-system-history/
    FIG-1.2-timing-chain/
    FIG-1.3-rock-end-product/
    FIG-1.4-barnett-stayed-escaped/
    FIG-1.5-same-basin-different-timing/
    FIG-1.6-multiple-pathways/
    FIG-1.7-diagenesis-clock/
    FIG-1.8-hypothesis-test/
```

Each figure folder should eventually contain:

- `README.md` with purpose, claim boundary, evidence dependencies, caption draft, and review status;
- editable/source artifact where applicable;
- publication-ready rendered derivative(s);
- source/citation notes for data-derived figures.

## Review gate

A figure is manuscript-ready only when:

- its purpose is clear without decorative dependence;
- visual semantics match this README;
- evidentiary certainty is no stronger than the source material;
- quantitative content is verified through the evidence ledger;
- caption states necessary qualifications;
- David Williams has authority to accept, revise, or reject the geological interpretation represented.
