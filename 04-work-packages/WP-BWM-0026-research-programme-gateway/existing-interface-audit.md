# Existing BWM Interface Audit

**Status:** WP-BWM-0026 Tranche B audit  
**Date:** 2026-09-24

## Summary

BWM's accepted architecture already requires pinned interfaces to externally authoritative programmes, but the canonical architecture surfaces audited here do not yet instantiate a normalized programme-interface artifact for TRT, LRT, DFM, or CHFM.

The architecture contains the policy. The gateway contract supplies the missing repeatable implementation pattern.

## Existing policy

### Foundations

`foundations/README.md` states that BWM owns interfaces to externally authoritative foundational programmes such as TRT and LRT and that source programmes are consumed through pinned BWM interface artifacts rather than copied wholesale.

### Historical Frameworks

`historical-frameworks/README.md` states that framework folders should carry BWM interface artifacts, adopted propositions, jurisdiction, unresolved tensions, and provenance, while detailed external programmes remain authoritative in their own repositories.

### Integration

`integration/README.md` correctly states that Integration records coherence, conflict, constraints, evidence, open problems, predictions, and dependency tracking without replacing source frameworks or domains.

## Gap

The intended interface pattern is described but not normalized as a reusable contract with required fields, pinning semantics, claim-strength preservation, and conflict-return behavior.

The gateway contract drafted in WP-BWM-0026 closes that implementation gap.

## Current classification debt

The accepted framework-domain matrix currently labels:

- TRT as Foundation;
- LRT as Foundation;
- Semantic Actualism as Foundation;
- DFM as Historical Framework;
- PFH as Historical Framework;
- CHFM as Historical Framework.

These labels mix **BWM use category** with **source construct type**.

A research programme can feed a BWM Foundation or Historical Framework without ceasing to be an externally authoritative research programme.

The revised architecture should therefore carry two dimensions:

```text
SOURCE TYPE
research programme / BWM hypothesis / comparison family / BWM construct

BWM ROLE
foundation / historical interval or boundary / world domain /
integration / comparison / publication
```

This avoids forcing source programmes into BWM taxonomy as though BWM owned them.

## Interface implementation recommendation

Create a canonical BWM interface registry under:

`02-systems-baseline/2.2-architecture/interfaces/`

with:

```text
interfaces/
├── README.md
├── registry.yaml
├── trt.yaml
├── lrt.yaml
├── semantic-actualism.yaml
├── dfm.yaml
├── chfm.yaml
├── fcd.yaml
└── cac.yaml
```

The YAML artifacts should implement the gateway contract. Human-readable architecture pages should reference the registry rather than duplicating programme status.

## Pinning

Each accepted interface records the exact reviewed source commit. Refresh is explicit. BWM main shall not automatically track a source programme's moving branch.

## Conclusion

The existing BWM architecture anticipated gateway behavior correctly. WP-BWM-0026 should refine and mechanize it rather than replace it.

Human-Curated, AI-Enabled (HCAE)
