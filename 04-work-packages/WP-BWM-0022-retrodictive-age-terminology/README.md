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

## Methodological consequence

BWM shall preserve the chain:

`observation -> measurement -> model transformation -> retrodictive age -> historical interpretation`

The programme shall not describe a model-derived absolute age as though it were itself a direct observation.

This applies to radiometric dating, crater chronology, stratigraphic chronology, archaeological dating, and other backward reconstructions.

For crater studies specifically, observable morphology, superposition, cross-cutting relationships, crater density, and relative ordering shall be recorded separately from model-assigned absolute ages.

## DFM interface

DFM may investigate whether a common primordial retrodictive age reflects an initialization boundary rather than antecedent elapsed history. This does not license unconstrained initialization as a universal explanation. Isochrons, daughter-product distributions, short-lived radionuclide systems, reset ages, cosmic-ray exposure histories, and other structured evidence retain independent explanatory burdens.

## Cleanup scope

1. Canonicalize the terminology in BWM chronology requirements and integration surfaces.
2. Update the DFM BWM interface.
3. Correct WP-BWM-0021 terminology where "apparent age" is being used for model-derived chronology.
4. Create a corresponding DFM work package and update active DFM draft language where appropriate.
5. Do not silently alter quotations or established literature terminology.

Human-Curated, AI-Enabled (HCAE)
