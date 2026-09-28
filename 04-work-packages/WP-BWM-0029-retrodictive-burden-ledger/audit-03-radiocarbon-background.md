# Quantitative Audit 03 — Residual Radiocarbon in Conventionally Ancient Materials

Status: initial measurement-system framing.

## Observation class

AMS systems can report finite apparent radiocarbon signals in nominally old/background carbon materials.

This fact alone does not identify the origin of the measured C-14.

## Measurement model

For low-level samples, represent the measured signal as:

```text
C14_measured =
  C14_sample
+ C14_pretreatment
+ C14_combustion
+ C14_graphitization
+ C14_storage_handling
+ C14_instrument
+ C14_environmental_contamination
+ other in-situ production
```

Vogel, Nelson & Southon explicitly studied contributions from combustion, graphitization, storage, handling and accelerator background. Meijer and colleagues report that modern-carbon contamination of very old AMS targets is a material problem because ambient modern C-14 levels greatly exceed those of very old samples. Lowe reports finite C-14 ages in coal background materials and considers pre-laboratory contamination, including biological contamination.

## Disposition

- **Residual measured signal:** RETAIN as an observation class.
- **"C-14 in coal/diamond/fossil therefore young":** UNRESOLVED and REFER to WP-BWM-0021.
- **Use as a clock without blank/background characterization:** REJECT.

## Promotion requirements

A candidate anomalous sample must report:
- provenance and geological context;
- sample mass;
- chemical pretreatment;
- laboratory;
- fraction modern/pMC and uncertainty;
- process blank measured in the same batch;
- carrier and graphitization chemistry;
- machine background;
- storage/handling controls;
- contamination correction;
- possible in-situ nuclear production;
- replicate measurements;
- independent laboratory replication where feasible.

The discriminating quantity is not merely a non-zero machine result. It is a reproducible excess above the full demonstrated process/background distribution.

## Corpus recommendation

Detailed C-14 work remains under WP-BWM-0021. WP-0029 supplies the general measurement-system rule:

> Near a method's detection floor, the instrument-plus-preparation system becomes part of the historical model and must be explicitly characterized before residual signal is interpreted historically.

Confidence: HIGH.
