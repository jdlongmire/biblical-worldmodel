# DFM vs UTE Evidence Dependency Graph

Status: Live Integration control artifact
Type: Dependency / anti-double-counting map

## Purpose

Prevent correlated premises, shared observations, and repeated explanatory burdens from being counted as independent evidence across the DFM-vs-UTE ledgers.

## Dependency classes

- **PARENT** — downstream items materially depend on the parent proposition.
- **CORRELATED** — items share substantial evidence or explanatory machinery and require discounted joint weight.
- **DERIVED** — item is a reformulation or consequence of another item and receives no independent evidential weight unless new evidence is added.
- **INTERFACE** — item crosses component/domain boundaries and must preserve source uncertainty.

## Current graph

```text
FND-001  Why anything exists
   └── interface only to worldview-level comparison

FND-002  Binding logic
   ├── FND-004 actualizable informational states
   └── all formal model comparison

FND-003  Stable lawfulness
   ├── COS-002 low-entropy / ordered initial condition [INTERFACE]
   └── operational science across all domains [shared, neutral]

FND-004  Information / actualization grounding
   ├── BIO-003 biological information [PARENT]
   └── BIO-004 abiogenesis state transition [PARENT]

FND-005  Initial/boundary-state justification
   ├── COS-001 early mature structure [PARENT]
   ├── COS-002 low-entropy condition [PARENT]
   ├── COS-004 distant starlight / mature observation [PARENT]
   ├── BIO-001 functional organization [INTERFACE]
   ├── BIO-004 abiogenesis boundary [PARENT]
   ├── ERH-001 concordant ages [INTERFACE]
   └── ERH-003 pristine old systems [PARENT]

FND-006  Auxiliary-rescue discipline
   ├── COS-005 dark-sector/model residual interpretation [PARENT]
   ├── ERH-003 pristine old systems [PARENT]
   └── ERH-005 slow-process geological models [PARENT]

BIO-001  Functional organization
   ├── BIO-002 function discovery [DERIVED/CORRELATED]
   └── BIO-003 information organization [CORRELATED]

ERH-001  Concordant ages
   └── ERH-003 pristine coherent old systems [CORRELATED unless closure/pristine evidence is independent]

ERH-002  Alteration-correlated discordance
   └── ERH-004 catastrophe-correlated disturbance [CORRELATED unless CHFM-specific pattern is independently demonstrated]

COS-001  Early mature structures
   └── COS-002 may be CORRELATED when both are explained by the same special initialized boundary state
```

## Counting rules

1. A child does not receive full independent evidential weight merely because it appears in another domain ledger.
2. A DERIVED item receives zero additional weight unless it introduces genuinely new evidence.
3. CORRELATED items require either explicit covariance/dependency treatment or conservative ordinal discounting.
4. Shared operational regularity is background evidence available to all models and is normally neutral.
5. Foundational burdens are not repeatedly added to every empirical domain score.
6. CHFM-specific disturbance evidence remains CHFM evidence unless a DFM claim independently predicts it.
7. A single observation may inform multiple claims, but the observation itself is counted once.

## Quantitative gate implication

No numerical Bayesian aggregation may proceed until each evidence item has:

- a dependency classification;
- identified shared observations;
- an independence or conditional-independence rationale;
- bounded likelihood ranges;
- a sensitivity test for correlated items.

Until then, subledger conclusions remain ordinal.

Human-Curated, AI-Enabled (HCAE)
