# WP-BWM-0022 — Retrodictive Age Terminology and Chronology Cleanup

Status: approved for execution

## Decision

BWM standardizes **retrodictive age** as the technical term for an age inferred by applying a chronological model backward from a measured present state. **Extrapolated age** is the preferred plain-language gloss where technical terminology would impede accessibility.

The phrase **apparent age** is deprecated for formal BWM chronology claims when it is being used to mean model-derived historical duration. It may remain where it is a quotation, a literature term, or where "apparent" modifies maturity rather than chronological age.

## Canonical vocabulary

- **Measured isotopic state**: present empirical measurements such as isotope ratios, mineral phases, concentrations, and correlations.
- **Retrodictive age** (`t_R`): a past time or elapsed duration inferred from present measurements under an explicitly identified chronometric model.
- **Actual elapsed age** (`t_H`): the historical elapsed duration since the event under examination.
- **Inherited/system-state age**: chronological information encoded in a system state that need not equal the elapsed duration of the specimen or event.
- **Initialization state** (`S_0`): the physically instantiated starting condition relevant to DFM reconstruction.

The governing distinction is:

`t_R != necessarily t_H`

A radiometric measurement establishes a present isotopic state. A radiometric age is a retrodictive quantity produced by an inference model. Equating that quantity with actual elapsed history requires the relevant initialization and system-history assumptions to be warranted.

## Canonical epistemic principle

**Age is not observed. State is observed. Age is inferred from state under a model of history.**

BWM therefore treats the phrase **apparent age** as epistemically underspecified when it is used without identifying the observer's inferential framework. The appropriate diagnostic question is:

> **Apparent to whom, under what model, given what assumptions, and under what historical interpretation?**

No specimen, astronomical object, isotope ratio, photon, stratum, crater, or other physical state bears an uninterpreted property called an "apparent age." What is empirically available is a present state or set of relationships. Chronological significance enters through an inferential chain.

The canonical chain is:

`observed state -> model + assumptions -> retrodictive calculation -> historical interpretation`

These stages shall remain analytically distinct. A measurement may be reliable, a calculation mathematically valid conditional on its model, and multiple independent calculations strongly consilient without logically entailing that the retrodicted duration equals actual elapsed historical duration.

This principle is model-neutral at the observational level. It does not license rejection of conventional chronology merely because chronology is inferred. Competing historical models inherit the burden of explaining the measured state, the success of the relevant models, and the observed consilience among independent lines of evidence.

## Methodological consequence

BWM shall preserve the chain:

`observation -> measurement -> model transformation -> retrodictive age -> historical interpretation`

The programme shall not describe a model-derived absolute age as though it were itself a direct observation.

This applies to radiometric dating, crater chronology, stratigraphic chronology, archaeological dating, and other backward reconstructions.

For crater studies specifically, observable morphology, superposition, cross-cutting relationships, crater density, and relative ordering shall be recorded separately from model-assigned absolute ages.

## DFM interface

DFM may investigate whether a common primordial retrodictive age reflects an initialization boundary rather than antecedent elapsed history. This does not license unconstrained initialization as a universal explanation. Isochrons, daughter-product distributions, short-lived radionuclide systems, reset ages, cosmic-ray exposure histories, and other structured evidence retain independent explanatory burdens.

## Consilience and initialization

BWM treats cross-domain consilience as an important property of the evidence, but not as a discriminator that by itself establishes elapsed chronology.

Under a continuous-history model, independent measurements should converge because they are traces of a common antecedent history. Under DFM, independent measurements should also converge because the created world is posited to have been instantiated as one coherent, functionally mature system. A physically integrated initialization state should not be expected to encode mutually contradictory system relationships.

Accordingly, the inference pattern is:

`observed state + model assumptions -> retrodictive/calculated age`

and the historical identity claim remains:

`calculated age != necessarily actual elapsed age`

Consilience therefore establishes a real explanatory constraint: any viable BWM/DFM account must explain why chronometric, cosmological, geological, and other relevant observations form coherent cross-checking relationships. It cannot dismiss those relationships as accidental or merely "apparent." However, convergence alone does not determine whether the reconstructed antecedent states were historically traversed or were physically instantiated at an initialization boundary.

### Genesis 1 expectation

Within BWM, functional maturity is grounded first in the Genesis 1 creation account. The text depicts created systems operating in their assigned functions within the creation sequence: vegetation productive, luminaries governing signs and seasons, living creatures reproducing, and humans functioning as mature agents. DFM therefore expects the initialized world to possess the coherent state information and inter-system relationships required for immediate function.

The computational analogy of **seed data** may be used as an explanatory aid: a virtual-world creator can initialize a coherent world with state information that, if later extrapolated backward under the world's ordinary update rules, implies antecedent states that were never actually instantiated. The analogy is illustrative rather than evidential and must not substitute for physical mechanism or empirical testing.

This yields a specific BWM burden: identify observations that discriminate between (a) a genuinely traversed deep history and (b) a coherently initialized mature state followed by ordinary history. Evidence that is expected under both models has low discriminatory force even when it has high internal consistency.

## Cleanup scope

1. Canonicalize the terminology in BWM chronology requirements and integration surfaces.
2. Update the DFM BWM interface.
3. Correct WP-BWM-0021 terminology where "apparent age" is being used for model-derived chronology.
4. Create a corresponding DFM work package and update active DFM draft language where appropriate.
5. Do not silently alter quotations or established literature terminology.

Human-Curated, AI-Enabled (HCAE)
