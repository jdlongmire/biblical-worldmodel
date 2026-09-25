# Modal Necessity Model

Status: Research draft
Work package: WP-BWM-0028
Date: 2026-09-25

## Purpose

Formalize the distinct modalities operating in the WP-BWM-0028 synthesis so that logical necessity, the certainty established by the Father's decree and ordination, and dispositional necessity under the curse are not conflated.

This model is deliberately modest. It formalizes distinctions needed by the theological argument without claiming a complete modal logic of divine action.

## 1. Primitive distinctions

Let:

- G = God.
- D(phi) = the Father decrees phi.
- O(phi) = the Father ordains phi within the decreed history.
- K(P) = person P exists under the fallen Adamic condition.
- Kn(P) = P bears the noetic effects of the curse.
- Ka(P) = P bears affective/dispositional disorder under the curse.
- V(P,a) = P voluntarily wills act a.
- R(P,a) = a is P's culpable rebellion.
- Q(P) = P is personally culpable.
- Gl(P) = P is glorified in perfected communion.

Modal notation:

- □L phi = phi is logically necessary.
- ◇L phi = phi is logically possible.
- □D phi = phi is certain given the Father's actual decree.
- □K phi = phi is dispositionally necessary given K and the relevant creaturely conditions.

## 2. Logical necessity

Logical necessity concerns what cannot be denied without contradiction.

### LN-1: Non-contradiction

□L not(phi and not-phi in the same respect).

God is inherently logical. This is not an external law constraining God.

### LN-2: Personal distinction

If P is a created person, then □L(P != G).

Creature and Creator cannot be numerically identical while remaining creature and Creator in the same respect.

### LN-3: Agency ownership

If P is personally culpable for voluntary rebellion a, then a must genuinely be attributable to P as moral agent.

Formally:

□L[Q(P,a) -> AgentOf(P,a)]

This does not yet specify a complete causal theory. It identifies an ownership condition for truthful moral predication.

### LN-4: Moral contradiction

It is incoherent to affirm simultaneously, in the same respect:

1. P is personally culpable because a is P's voluntary sinful act; and
2. a is not genuinely P's voluntary act.

Therefore genuine culpability cannot be purchased by denying genuine agency.

### LN-5: Evil is not required by agency as such

◇L(genuine created agency without actual sin).

The model has at least two theological limiting cases: pre-Fall moral agency and glorified moral agency. Therefore actual rebellion is not logically entailed merely by personhood or agency.

## 3. Decretive necessity

Decretive necessity concerns certainty relative to the Father's free, actual decree.

### DN-1: Decree entails certainty

D(phi) -> □D phi.

The Father's decree cannot fail.

### DN-2: Decretive does not imply logical necessity

□D phi does not entail □L phi.

The fact that God freely decrees a created history does not mean the history exists by metaphysical necessity.

### DN-3: Ordained means are included

Where the Father decrees an end and ordains means m to that end, the means belong to the certainty of the actual decreed history.

This prevents decree from being reduced to divine prediction of independently arising events.

### DN-4: Decretive certainty does not transfer moral intention

□D(event e) does not entail Identity[DivineIntention(e), CreaturelySinfulIntention(e)].

Genesis 50:20 and the crucifixion texts are canonical controls for this distinction.

### DN-5: Decretive certainty does not erase secondary/creaturely agency

If D(a occurs through P's willing), then the decreed certainty includes rather than negates the truth that P genuinely wills a.

The model therefore rejects:

□D a -> not AgentOf(P,a).

### DN-6: Fall

Within the actual decree:

□D(Adam's Fall).

This does not imply:

□L(Adam's Fall).

The Fall is certain because decreed and ordained, not because genuine moral agency logically requires rebellion.

## 4. Dispositional necessity

Dispositional necessity concerns what follows reliably/certainly from the actual fallen constitution and orientation of ordinary morally accountable human agents.

### KN-1: Structured condition

K(P) includes judicial, mortal, noetic, affective, relational, and creational dimensions.

### KN-2: Noetic condition is not culpability

Kn(P) != Q(P).

### KN-3: Affective disorder is not culpability

Ka(P) != Q(P).

### KN-4: Fallen orientation

For ordinary morally accountable descendants of Adam, K supplies a disordered noetic/affective orientation in which the self does not naturally remain ordered under supreme love for God.

### KN-5: Voluntary sin

The working hypothesis is:

K(P) and MoralAccountability(P) -> □K(exists a: V(P,a) and R(P,a)).

The person's sin is dispositionally necessary under K while genuinely voluntary because it proceeds through P's own willing.

### KN-6: Personal guilt follows actual culpable rebellion

R(P,a) -> Q(P,a).

K(P) alone does not, under H1, establish personal guilt for Adam's intention.

### KN-7: Recursive noetic hardening

Kn(P) + apprehended truth + culpable suppression may produce further noetic darkening. Thus some later impairment may be both consequence of K and judicial consequence of P's own rebellion.

## 5. The three modalities in Adam

For Adam before the Fall:

- genuine moral agency: actual;
- actual rebellion: logically possible, not logically necessary;
- Fall: decretively certain within D;
- sinful intention: genuinely Adam's;
- Adamic guilt: grounded in Adam's actual voluntary rebellion.

Therefore:

◇L(Fall) and not □L(Fall)
while
□D(Fall).

This is the cleanest case demonstrating why □L and □D must remain distinct.

## 6. The three modalities in fallen descendants

For ordinary morally accountable descendant P:

- P exists within the Adamic condition K by historical/corporate inheritance;
- Kn and Ka condition P's knowing, valuing, and desiring;
- actual personal rebellion is proposed as □K;
- P's actual act remains P's voluntary act;
- Q(P) attaches to P's culpable rebellion, not merely to Kn or Ka.

Thus:

K(P) -> □K(voluntary personal sin)

but:

K(P) -/-> Q(P) merely by inheritance, under H1.

The second relation remains subject to the Romans 5 open question concerning corporate condemnation and personal imputation.

## 7. Glorification as modal control

For glorified P:

Gl(P) -> perfected communion and absence of corruption.

The model proposes:

Gl(P) -> □K-like(impeccable righteous willing),

where the analogy means stable perfected disposition, not fallen K.

The key inference is conceptual:

genuine freedom does not require live metaphysical access to sinful alternatives.

If glorified persons remain genuine agents while perfectly loving God, contrary choice cannot be constitutive of agency.

The exact modal status of glorified impeccability is developed further in `glorified-agency-impeccability.md`. That model distinguishes conceptual knowledge of sin from deliberative and volitional availability and proposes that sanctification increasingly forms a positive desire for final freedom from sin.

## 8. Divine freedom as control

God cannot sin, lie, deny himself, or cease to be God. These impossibilities do not imply deficiency of divine freedom.

Therefore the equation:

freedom = ability to actualize evil

is false.

Creaturely freedom must be defined in a way that does not make God's perfect freedom defective.

## 9. Modal fallacies to prohibit

### MF-1: Decretive-to-logical fallacy

D(phi), therefore □L phi.

Invalid. What God freely decrees is certain without becoming metaphysically necessary in itself.

### MF-2: Certainty-to-coercion fallacy

□D(V(P,a)), therefore P is externally compelled against P's will.

Invalid unless an additional coercion premise is established.

### MF-3: Condition-to-guilt fallacy

Kn(P) or Ka(P), therefore Q(P).

Invalid under H1. Inherited noetic/affective condition and personal culpability are distinct predicates.

### MF-4: Agency-to-Fall fallacy

MoralAgent(P), therefore □L(P sins).

Invalid. Genuine agency does not logically entail actual rebellion.

### MF-5: Alternative-possibilities fallacy

not ◇(P sins), therefore P is not free.

Not established. Divine freedom and proposed glorified freedom are counter-controls.

### MF-6: Ordination-to-intention-identity fallacy

O(e), therefore God's moral intention in e = the creature's sinful intention in e.

Invalid. Canonical dual-intention texts directly resist the identity.

### MF-7: Corporate-to-personal equivocation

CorporateCondemnation(P in Adam), therefore PersonalCulpabilityForAdamAct(P).

This is precisely the open Romans 5 entailment and may not be assumed in either direction.

## 10. Integrated modal sequence

The current synthesis is:

God's inherently logical nature
-> logically coherent creaturely personhood and agency
-> Father's free decree and ordination of the actual history
-> decretively certain Adamic Fall through Adam's genuine willing
-> corporate Adamic judicial condition K
-> inherited noetic/affective/relational disorder
-> dispositionally necessary voluntary personal rebellion for morally accountable fallen agents [H1 working model]
-> individual culpability
-> righteous judgment
-> sovereign election and effectual redemption
-> Spirit-wrought renewal
-> glorified perfected communion
-> decreed consummation.

No arrow may silently change modal category.

## 11. Formal status ledger

| Proposition | Status |
|---|---|
| Contradictions are not actualizable | Logical commitment |
| Creature is genuinely distinct from God | Logical commitment |
| Personal culpability requires truthful agent attribution | Logical/moral commitment |
| Genuine agency logically requires actual sin | Rejected |
| Adam's Fall is logically necessary | Rejected |
| Adam's Fall is decretively certain | Affirmed within model |
| Divine ordination entails identity of sinful intention | Rejected |
| Fallen noetic corruption equals personal guilt | Rejected under H1 |
| Fallen affective corruption equals personal guilt | Rejected under H1 |
| Ordinary accountable fallen persons necessarily sin dispositionally | Working hypothesis |
| Corporate Adamic condemnation entails personal imputation of Adam's guilt | OPEN |
| Glorified agency is impeccable | Strong theological inference, further canonical test required |
| The decreed consummation can fail | Rejected |

## 12. Next tests

1. Test □K universal sin against Romans 1-3, Romans 7-8, Ephesians 2 and 4, and relevant counterexamples.
2. Test the ownership condition against the strongest Reformed compatibilist, libertarian, and hard-determinist formulations without defining the debate away.
3. Test glorified impeccability from Revelation 21-22, 1 John 3:2, and 1 Corinthians 15.
4. Carry these distinctions into the divine-authorship-of-sin analysis.
5. Preserve the noetic-effects / culpability distinction in every subsequent artifact.

Human-Curated, AI-Enabled (HCAE)
