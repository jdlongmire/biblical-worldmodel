# WP-BWM-0029: Systematic Theology and Covenant-Communion Architecture

Status: Proposed / architecture concept captured
Date: 2026-09-25

## Purpose

Restructure the BWM intellectual architecture to introduce **Systematic Theology** as a first-class category between Foundations and the historical/domain modeling layers, with **covenant and communion** as the principal organizing motif.

This work package exists because WP-BWM-0020 and WP-BWM-0028 developed theological content whose proper ownership is broader than the current Covenant and Redemptive History World Domain.

This package defines architecture, ownership, interfaces, and migration. It does not itself settle open theological hypotheses in WP-BWM-0028.

## Architectural problem

The accepted BWM architecture currently has four conceptual categories:

1. Foundations
2. Historical Frameworks
3. World Domains
4. Integration

That structure works for epistemology, history, and subject-matter models, but it lacks an explicit home for systematic doctrinal synthesis.

Consequently, theology concerning decree, Trinity, personhood, moral agency, sin, curse, election, redemption, pneumatology, sanctification, judgment, and glorification is at risk of being placed inside historical or empirical domains that it actually constrains.

## Proposed five-category architecture

1. **Foundations**
2. **Systematic Theology**
3. **Historical Frameworks**
4. **World Domains**
5. **Integration**

Approximate dependency direction:

Foundations
-> Systematic Theology
-> Historical Frameworks <-> World Domains
-> Integration

Integration may expose tensions requiring reconsideration upstream. It does not silently rewrite doctrine or foundational commitments.

## Foundations

Foundations continue to own:

- ontology and metaphysics interfaces;
- TRT/LRT pinned interfaces;
- Semantic Actualism interface;
- epistemology;
- canonical authority;
- hermeneutics;
- distinctions among observation, inference, retrodiction, and history.

Foundations answer questions such as:

- What is the authority structure?
- What makes rational inquiry and interpretation possible?
- What ontological and epistemological commitments constrain BWM?
- How is Scripture interpreted relative to nature and model inference?

## Systematic Theology

Systematic Theology answers:

> What does Scripture teach coherently about God, creation, humanity, moral order, sin, redemption, and consummation?

Its primary organizing architecture is **covenant communion**, not merely a flat list of conventional doctrinal loci.

### Governing trajectory

**Triune Purpose**
-> **Creation and Covenant Communion**
-> **Creaturely Agency and Stewardship**
-> **Rupture of Communion**
-> **Judgment and Curse**
-> **Covenant Redemption**
-> **Spirit-wrought Restoration**
-> **Glorification**
-> **Consummated Covenant Communion**
-> **Glory of God**

### Architectural principle

**Covenant is structural. Communion is teleological.**

Covenant describes the divinely established relational order, authority, obligations, promises, offices, and means.

Communion describes the relational end: rightly ordered fellowship with God, neighbor, self, and creation under God's lordship.

## Systematic Theology modules

### ST-1: God and Triune Purpose

Scope:
- Theology Proper;
- divine nature and attributes;
- holiness;
- inherent logicality;
- sovereignty;
- decree and ordination;
- providence;
- Trinitarian unity and personal distinction;
- inseparable operation and personal missions.

### ST-2: Creation and Covenant Communion

Scope:
- doctrine of creation;
- Creator-creature distinction;
- imago Dei;
- personhood;
- natural self-love;
- ordered love;
- moral agency;
- delegated authority;
- stewardship;
- original communion;
- covenant structure.

### ST-3: Rupture, Sin, and Curse

Scope:
- temptation versus sin;
- autonomous self-interest;
- first sin;
- Fall;
- privation/disorder account of evil;
- curse;
- corporate Adamic condition;
- noetic effects;
- affective disorder;
- personal culpability;
- Adamic representation/imputation question.

### ST-4: Providence and Moral Agency

Scope:
- comprehensive decree and ordination;
- logical, decretive, and dispositional necessity;
- creaturely agency;
- intention;
- secondary/derivative causation;
- divine-authorship-of-sin objection;
- moral responsibility;
- judgment and differentiated culpability;
- problem of evil/theodicy interfaces.

This module is cross-cutting and may eventually be treated as an integration spine within Systematic Theology.

### ST-5: Covenant Redemption

Scope:
- election;
- Father's giving of a people to the Son;
- incarnation;
- obedience of Christ;
- atonement;
- effectual redemption;
- justification;
- reconciliation;
- adoption;
- union with Christ;
- covenant fulfillment.

### ST-6: Spirit-wrought Restoration

Scope:
- Spirit of Truth;
- conviction;
- regeneration;
- faith and repentance;
- indwelling;
- sanctification;
- noetic renewal;
- reordered love;
- preservation;
- sealing;
- assurance/inheritance;
- communion of the redeemed.

### ST-7: Church, Bride, and Covenant People

Scope:
- Church;
- Bride;
- communion of saints;
- covenant community;
- worship;
- mission;
- relation of Israel and Church;
- kingdom/community interfaces.

### ST-8: Judgment and Consummated Communion

Scope:
- resurrection;
- final judgment;
- degrees/differentiation of culpability;
- glorification;
- freely embraced impeccability;
- New Creation;
- removal of curse;
- perfected ordered love;
- eternal communion;
- consummation.

## Conventional doctrinal loci as cross-reference taxonomy

The classical categories remain useful but do not define the primary navigation.

Cross-reference tags may include:

- Theology Proper
- Trinitarian Theology
- Christology
- Pneumatology
- Doctrine of Creation
- Theological Anthropology
- Hamartiology
- Providence
- Moral Theology
- Soteriology
- Ecclesiology
- Eschatology
- Covenant Theology

This prevents Christology or Pneumatology from being artificially confined to one folder when the Son and Spirit act throughout creation and redemption.

## Key doctrinal trajectory

The emerging synthesis can be represented:

God creates persons for communion
-> communion is covenantally ordered
-> creatures exercise genuine derivative agency and stewardship
-> sin culpably rejects/disorders covenant communion
-> curse judicially follows rupture
-> fallen humanity exists under corporate, noetic, affective, relational, and mortal disorder
-> Father elects
-> Son effectually accomplishes redemption
-> Spirit effectually applies and perfects redemption
-> communion is restored
-> sanctification reorders loves
-> glorification perfects the redeemed agent
-> New Creation is consummated covenant communion.

## Definition candidates

### Sin

> Sin is culpable creaturely rebellion against God, expressed as the rejection and disordering of covenant communion through lawlessness, unbelief, and the elevation of autonomous self-interest over love for God and neighbor.

### Redemption

> Redemption is the Son's effectual accomplishment of the restoration of covenant communion for the people the Father gives him, applied and perfected by the Holy Spirit.

### Consummated communion

> Consummated communion is the perfected covenant state in which redeemed image-bearers freely and immutably love God, neighbor, self, and creation according to their proper order.

These remain candidates until the source work is accepted.

## Interfaces to Historical Frameworks

### DFM

Systematic Theology supplies:
- doctrine of creation;
- Creator-creature distinction;
- divine purpose;
- created goodness;
- human creatureliness where relevant.

DFM remains responsible for creation/initialization historical-model questions.

### PFH

Systematic Theology supplies:
- imago Dei;
- original communion;
- moral agency;
- stewardship;
- temptation/sin distinction;
- Fall and curse doctrine.

PFH remains responsible for admissible pre-Fall human history and the Fall boundary as historical framework.

### CHFM

Systematic Theology supplies:
- judgment;
- covenant;
- providence;
- human moral history constraints.

CHFM remains responsible for the physical Flood mechanism and terrestrial historical model.

### Post-Fall / Redemptive History

Systematic Theology supplies doctrinal definitions of covenant, sin, election, redemption, Church, judgment, and consummation.

Historical representation traces those doctrines through actual canonical history.

## Interfaces to World Domains

### Cosmology and Physical Order

Consumes doctrine of creation, providence, Creator-creature distinction, and relevant theological constraints.

### Earth History and Geology

Consumes doctrine of creation, curse/judgment where textually warranted, and providence without turning theological claims into geological mechanisms.

### Biology and Life Systems

Consumes doctrine of creation, creaturely kinds/life constraints where established, human uniqueness, and stewardship boundaries.

### Anthropology

Empirical/domain Anthropology owns human biology, populations, cognition, language, culture, Neanderthal/Denisovan classification, and related models.

Systematic Theology owns theological anthropology: imago Dei, personhood, moral agency, ordered love, corruption, accountability, redemption, and glorification.

### Archaeology and Chronology

Consumes theological/historical constraints without allowing dating models to silently redefine doctrine.

### Covenant and Redemptive History

The current World Domain requires reevaluation. Much of its doctrinal content should move conceptually to Systematic Theology, while the domain should retain the historical tracing of covenants, Israel, Christ, Church, kingdom, and consummation.

## Integration rules

1. Systematic Theology is constrained by Foundations and canonical hermeneutics.
2. Systematic Theology supplies doctrinal constraints to Historical Frameworks and World Domains.
3. Historical Frameworks and World Domains may expose tensions, anomalies, or apparent conflicts.
4. Such tensions route to Integration for explicit reconciliation or model revision.
5. Empirical/domain models do not silently rewrite doctrine.
6. Theological synthesis does not dictate physical mechanisms absent scriptural or evidential warrant.
7. Open theological hypotheses remain work-package material until accepted.
8. Conventional doctrinal loci are cross-reference classifications, not necessarily exclusive ownership containers.
9. Covenant and communion provide the primary relational architecture.
10. Canonical promotion must preserve provenance to the originating work package.

## Migration candidates

### WP-BWM-0020

Accepted material concerning ordered love, creaturely autonomy, law, judgment, redemptive trajectory, and consummated communion should map principally into:

- ST-2 Creation and Covenant Communion;
- ST-3 Rupture, Sin, and Curse;
- ST-5 Covenant Redemption;
- ST-8 Judgment and Consummated Communion;
- Moral Theology cross-reference.

### WP-BWM-0028

If accepted after pressure testing, material maps principally into:

- ST-1 God and Triune Purpose;
- ST-2 Creation and Covenant Communion;
- ST-3 Rupture, Sin, and Curse;
- ST-4 Providence and Moral Agency;
- ST-5 Covenant Redemption;
- ST-6 Spirit-wrought Restoration;
- ST-8 Judgment and Consummated Communion.

Open H1 material concerning Adamic guilt must not be promoted merely because the architecture exists.

## Planned artifacts

- [`systematic-theology-architecture.md`](systematic-theology-architecture.md): five-category canonical architecture candidate, ST jurisdiction, eight modules, ownership and promotion rules. Draft completed 2026-09-25.
- [`systematic-theology-interface-map.md`](systematic-theology-interface-map.md): directional interfaces to Foundations, Historical Frameworks, World Domains, and Integration. Draft completed 2026-09-25.
- [`migration-map.md`](migration-map.md): phased mapping of WP-BWM-0020, WP-BWM-0028, Covenant/Redemptive History, Anthropology, and related artifacts into the proposed architecture. Draft completed 2026-09-25.
- [`covenant-communion-taxonomy.md`](covenant-communion-taxonomy.md): governing definitions, module relationships, conventional-loci crosswalk, status vocabulary, and navigation rules. Draft completed 2026-09-25.
- [`architecture-impact-analysis.md`](architecture-impact-analysis.md): comparison against WP-BWM-0013, required changes, preserved structures, and restructure risks. Draft completed 2026-09-25.
- [`canonical-promotion-plan.md`](canonical-promotion-plan.md): gated implementation sequence, verification, rollback, and acceptance boundary. Draft completed 2026-09-25.

## Acceptance criteria

1. Systematic Theology has a clearly defined jurisdiction distinct from Foundations, Historical Frameworks, World Domains, and Integration.
2. Covenant and communion are defined as organizing concepts without displacing Scripture as epistemic authority.
3. Conventional theological loci remain discoverable through a cross-reference taxonomy.
4. Theological Anthropology and empirical/domain Anthropology have an explicit boundary.
5. Covenant doctrine and Covenant/Redemptive History have an explicit doctrine/history boundary.
6. WP-BWM-0020 and WP-BWM-0028 have migration maps preserving provenance.
7. Open hypotheses are not accidentally canonicalized.
8. Dependency and interface rules preserve genuine feedback and falsification.
9. The accepted component architecture can be updated without breaking the repository operating model.
10. Principal Operator approves the architecture before canonical promotion or content migration.

## Current disposition

Architecture concept captured for research and migration planning. No canonical restructure has yet been performed.

Human-Curated, AI-Enabled (HCAE)
