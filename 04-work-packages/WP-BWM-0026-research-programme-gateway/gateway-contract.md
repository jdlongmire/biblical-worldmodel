# BWM Research Programme Gateway Contract

**Status:** Draft for WP-BWM-0026 Tranche B

## 1. Purpose

Define the minimum governed interface by which BWM consumes an externally authoritative research programme without duplicating or silently modifying its research.

## 2. Authority model

- **OWNS**: controls the proposition, evidence/proof, status, revision, and failure conditions.
- **CONSUMES**: imports a governed output without assuming ownership of its warrant.
- **INTEGRATES**: relates outputs across programmes/domains and records coherence, dependencies, and conflicts.
- **PUBLISHES**: renders governed integrated conclusions for readers without strengthening source claims.

## 3. Required interface fields

Each programme interface shall identify:

```yaml
programme:
  id:
  name:
  canonical_repository:
  programme_type:
  source_ref:
  source_commit:
  interface_status:

scope:
  jurisdiction:
  exclusions: []

exports:
  - id:
    statement:
    source:
    source_status:
    confidence:
    bwm_use:

dependencies:
  required: []
  conditional: []
  associated: []

open_items:
  unresolved: []
  tests_or_discriminators: []
  failure_conditions: []

integration:
  bwm_domains: []
  bwm_constraints: []
  conflicts: []
  last_reviewed:
```

The schema may be refined, but the semantic distinctions are required.

## 4. Pinning rule

BWM interfaces shall identify a source ref and commit or equivalent immutable version for the research state actually reviewed. A moving branch name alone is insufficient for an accepted integration baseline.

A later source commit does not silently alter BWM's accepted integration state. Refresh requires an interface review.

## 5. Claim-strength rule

BWM may summarize an imported proposition but shall not strengthen its modality, confidence, scope, or empirical status.

Examples:

- source says "candidate" -> BWM shall not say "established";
- source says "conditional on OPN-001" -> BWM shall preserve the condition;
- source says "unappraised" -> BWM shall not present the programme as empirically corroborated;
- source records an unresolved tension -> BWM shall not resolve it by synthesis language alone.

## 6. Conflict-return protocol

When BWM integration identifies conflict C between imported outputs:

1. record C in BWM integration;
2. identify the owning programme(s);
3. distinguish logical contradiction, empirical tension, terminology mismatch, boundary-condition mismatch, and unresolved dependency;
4. do not edit the imported proposition to manufacture coherence;
5. return the issue to the owning programme for disposition where source change is required;
6. consume the resulting governed state after review;
7. retain unresolved conflicts visibly when no disposition is available.

## 7. Relationship vocabulary

Interfaces shall distinguish at least:

- `depends_on`: downstream claim materially requires upstream claim;
- `conditional_on`: relationship applies only if named condition resolves;
- `situated_within`: programme/source declares an ontological or architectural containment relation;
- `formalizes`: one programme formalizes a constituent or proposition of another;
- `supports`: evidence/argument increases warrant without logical dependence;
- `constrains`: limits admissible downstream models;
- `associated_with`: explanatory relevance without dependency;
- `specializes`: narrower programme entails or adds commitments to a more general programme;
- `compares_with`: BWM comparison relationship only.

## 8. Internal architecture independence

The gateway contract standardizes the BWM-facing interface, not the internal directory structure or methodology of associated repositories.

TRT, LRT, SA, DFM, CHFM, FCD, CAC, and future programmes may retain different internal structures so long as source authority and exported state are governable.

## 9. Hypotheses and comparison families

BWM-owned hypotheses such as PFH do not require an external-programme interface while they remain BWM-owned. They still require explicit epistemic status and provenance.

Comparative families such as DTE and UTE are not registered as research programmes. They are governed through BWM comparison artifacts.

## 10. Verification criteria

An interface passes when:

- canonical source is unambiguous;
- reviewed version is immutable/pinned;
- exported propositions trace to source;
- confidence/status is preserved;
- dependencies are typed;
- unresolved items are visible;
- BWM use is stated;
- no duplicated research is presented as BWM-owned;
- public synthesis can trace back to the interface.

Human-Curated, AI-Enabled (HCAE)
