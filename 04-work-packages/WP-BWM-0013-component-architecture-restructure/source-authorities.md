# BWM External Source Authorities

Status: Working source-of-truth registry under WP-BWM-0013
Authority: Approved implementation input for BWM interface construction

## TRT

Authoritative repository:

`jdlongmire/triadic-reality-theory`

Pinned provenance for current BWM restructure planning:

`491cb32ac3e937125a4844fb9417e1ea50a0e489`

The repository declares TRT v0.9 as the current coherent position-paper state and identifies TRT as the broader ontology within which LRT is situated.

BWM treatment:

- do not fork TRT prose or formalization;
- create `foundations/ontology/trt-interface.md`;
- record the pinned source commit used for each BWM interface revision;
- consume only propositions that have explicit BWM disposition.

## LRT

Authoritative source location:

`jdlongmire/triadic-reality-theory`

Primary formal sub-project:

`formalization/lrt/`

Pinned repository provenance for current BWM restructure planning:

`491cb32ac3e937125a4844fb9417e1ea50a0e489`

The TRT repository explicitly states the relationship:

`TRT -> LRT -> LRM -> predictions`

and identifies LRT as formalizing TRT's logical constituent.

BWM treatment:

- do not create an independent LRT source repository merely for BWM;
- create `foundations/ontology/lrt-interface.md`;
- point the interface to the TRT repository and exact LRT paths/version used;
- preserve the distinction between TRT-level ontology and LRT formal logical work.

## CHFM

Authoritative repository:

`jdlongmire/catastrophic-hydrotectonic-flood-model`

Pinned provenance for current BWM restructure planning:

`22dcdea8126861f3c9d7ecca89f71cf586287cd0`

The repository presents itself as the active Catastrophic Hydrotectonic Flood Model research programme, with a VWMM layout, current hard core, protective belt, discriminators, and position paper.

Legacy/predecessor repository observed:

`jdlongmire/global-flood-hydrotectonic-model`

The legacy repository remains useful for provenance and historical calculations but shall not be treated as the current BWM source of truth unless a specific artifact is intentionally cited from that lineage.

BWM treatment:

- create `historical-frameworks/chfm/bwm-interface.md`;
- reference the current CHFM repository as authoritative;
- pin source commits in BWM interface revisions;
- cite legacy material only with explicit predecessor/provenance labeling;
- do not duplicate the CHFM programme's calculations, datasets, notebooks, or detailed theory tree into BWM.

## Source-authority rule

BWM interface artifacts shall record:

1. authoritative repository;
2. pinned commit or tagged release;
3. authoritative source path(s);
4. BWM-adopted propositions;
5. propositions intentionally excluded or still unresolved;
6. source work package and Operator disposition;
7. update date and supersession lineage.

A moving `main` branch is not sufficient provenance for a canonical BWM interface. Canonical interfaces must pin an immutable commit or release.

Human-Curated, AI-Enabled (HCAE)
