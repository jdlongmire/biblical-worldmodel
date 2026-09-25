# Systematic Theology Architecture Candidate

Status: Candidate architecture
Work package: WP-BWM-0029
Date: 2026-09-25

## Architectural decision candidate

Revise the BWM intellectual architecture from four categories:

Foundations | Historical Frameworks | World Domains | Integration

to five:

**Foundations | Systematic Theology | Historical Frameworks | World Domains | Integration**

The repository lifecycle structure `00`-`06` remains unchanged. This is an intellectual taxonomy change, not a repository operating-model change.

## Jurisdiction

### Foundations

Owns the epistemic, hermeneutical, ontological, and methodological constraints under which BWM reasons.

### Systematic Theology

Owns canonical doctrinal synthesis: what Scripture teaches coherently about God, creation, covenant, humanity, moral order, sin, redemption, restoration, judgment, and consummation.

### Historical Frameworks

Owns intervals, transitions, and boundary events in created history.

### World Domains

Owns subject-matter models of created reality.

### Integration

Owns cross-category consistency, dependency, tension, evidence/model ledgers, and explicit reconciliation.

## Governing Systematic Theology motif

**Covenant is structural. Communion is teleological.**

Covenant describes the divinely established relational order, authority, obligations, promises, offices, and means.

Communion describes the relational end: rightly ordered fellowship with God, neighbor, self, and creation under God's lordship.

Neither concept supersedes Scripture. Both are theological syntheses governed by canonical warrant.

## Primary trajectory

Triune Purpose
-> Creation and Covenant Communion
-> Creaturely Agency and Stewardship
-> Rupture of Communion
-> Judgment and Curse
-> Covenant Redemption
-> Spirit-wrought Restoration
-> Glorification
-> Consummated Covenant Communion
-> Glory of God.

## Modules

### ST-1 God and Triune Purpose

Owns Theology Proper, divine nature/attributes, holiness, inherent logicality, sovereignty, decree/ordination, providence, Trinity, inseparable operation, and personal missions.

### ST-2 Creation and Covenant Communion

Owns doctrine of creation, Creator-creature distinction, imago Dei, personhood, natural self-love, ordered love, moral agency, delegated authority, stewardship, original communion, and covenant order.

### ST-3 Rupture, Sin, and Curse

Owns temptation/sin distinction, autonomous self-interest, first sin, Fall doctrine, privation/disorder account, curse, Adamic corporate condition, noetic/affective corruption, personal culpability, and the Adamic representation/imputation question.

### ST-4 Providence and Moral Agency

Owns cross-cutting doctrine of comprehensive decree/ordination, modality, derivative agency, intention, causation, responsibility, judgment, divine-authorship-of-sin analysis, and theodicy interfaces.

### ST-5 Covenant Redemption

Owns election, giving to the Son, incarnation, Christ's obedience, atonement, justification, reconciliation, adoption, union with Christ, effectual redemption, and covenant fulfillment.

### ST-6 Spirit-wrought Restoration

Owns Spirit of Truth, conviction, regeneration, faith/repentance, indwelling, sanctification, noetic renewal, reordered love, preservation, sealing, assurance/inheritance, and restoration of communion.

### ST-7 Church, Bride, and Covenant People

Owns Church, Bride, communion of saints, covenant community, worship, mission, Israel/Church relation, and kingdom/community doctrine.

### ST-8 Judgment and Consummated Communion

Owns resurrection, final judgment, differentiated culpability, glorification, freely embraced impeccability, New Creation, removal of curse, perfected ordered love, eternal communion, and consummation.

## Cross-reference loci

Conventional doctrinal loci remain discoverable as tags/views rather than exclusive containers:

Theology Proper; Trinitarian Theology; Christology; Pneumatology; Doctrine of Creation; Theological Anthropology; Hamartiology; Providence; Moral Theology; Soteriology; Ecclesiology; Eschatology; Covenant Theology.

This avoids artificially confining Christology and Pneumatology to single modules.

## Ownership rule

An artifact's primary owner is determined by the question it answers:

- "What is true doctrinally?" -> Systematic Theology.
- "What happened and when?" -> Historical Framework.
- "How does this created domain behave or appear?" -> World Domain.
- "How do these claims cohere across boundaries?" -> Integration.
- "By what authority/method are these claims known and interpreted?" -> Foundations.

Cross-references do not duplicate source authority.

## Doctrine/history rule

A doctrine and its historical manifestation may have separate artifacts.

Example:

Systematic Theology / ST-3 owns the doctrine of Fall, sin, curse, and culpability.

PFH owns the human-creation-to-Fall interval and Fall boundary as historical framework.

Likewise ST-5 owns covenant-redemption doctrine while Covenant/Redemptive History traces promise, covenant administration, Israel, Christ, Church, kingdom, and consummation through canonical history.

## Theology/domain rule

Theological Anthropology and empirical Anthropology are distinct.

Systematic Theology owns:
imago Dei; personhood; moral agency; ordered love; corruption; accountability; redemption; glorification.

Anthropology World Domain owns:
human biology; populations; cognition as empirical study; language; culture; Neanderthal/Denisovan classification; demographic and archaeological interfaces.

Neither silently absorbs the other's jurisdiction.

## Constraint and feedback rule

Systematic Theology supplies doctrinal constraints to Historical Frameworks and World Domains.

Historical/domain work can expose tension with a doctrinal synthesis. Such tension is routed through Integration and can trigger re-exegesis or revision.

Therefore "constraint" does not mean immunity from falsification. It means doctrinal change occurs explicitly at the doctrinal layer through the governing epistemic/hermeneutical process rather than being silently overwritten by a domain model.

## Promotion rule

Research remains in work packages until accepted.

When accepted:
1. promote a canonical derivative to its owning ST module;
2. retain the originating WP as provenance;
3. preserve confidence/status and unresolved alternatives;
4. create cross-domain interface references rather than copies;
5. update dependency maps.

Open hypotheses are never promoted merely because neighboring material is accepted.

## Initial source mapping

### WP-BWM-0020

Candidate promotion targets:
- ST-2: ordered love, natural self-love, communion, stewardship;
- ST-3: autonomy/rebellion/curse;
- ST-5: redemptive trajectory;
- ST-8: consummated communion;
- Moral Theology cross-reference.

### WP-BWM-0028

Candidate promotion targets after pressure testing:
- ST-1: decree/ordination, Trinitarian mission;
- ST-2: image-bearing agency, self-love, communion;
- ST-3: temptation, Fall, curse, noetic effects, culpability;
- ST-4: modal necessity, agency, divine-authorship analysis;
- ST-5: election/effectual redemption;
- ST-6: Spirit application, sanctification, sealing;
- ST-8: judgment, glorification, impeccability.

H1 on Adamic personal guilt remains open and excluded from automatic promotion.

## Architectural effect on current Covenant and Redemptive History domain

Retain the domain, but narrow its primary jurisdiction to canonical-historical tracing:

Fall consequences -> covenant administrations -> promise/Seed -> Israel -> Christ -> Church -> kingdom -> resurrection/consummation.

Move or reference doctrinal definitions to/from Systematic Theology rather than maintaining competing doctrinal sources.

## Proposed canonical location

If accepted, create:

`02-systems-baseline/2.2-architecture/systematic-theology/`

with:
- `README.md`
- `st-1-god-triune-purpose/`
- `st-2-creation-covenant-communion/`
- `st-3-rupture-sin-curse/`
- `st-4-providence-moral-agency/`
- `st-5-covenant-redemption/`
- `st-6-spirit-restoration/`
- `st-7-church-covenant-people/`
- `st-8-judgment-consummated-communion/`
- `cross-reference-loci.md`
- `interfaces.md`

Directory creation should occur only after architecture acceptance.

## Decision status

CANDIDATE. Requires comparison with WP-BWM-0013 and explicit Principal Operator acceptance before canonical implementation.

Human-Curated, AI-Enabled (HCAE)
