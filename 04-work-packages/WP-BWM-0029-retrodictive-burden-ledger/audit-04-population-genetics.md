# Quantitative Audit 04 — Population Genetics, Waiting Time, Mutation Load, and Human Genetic Clocks

Status: primary-source provenance pass complete; canonical conclusions not authorized.

## 1. Directly measured mutation rate

Human germline de novo mutation is empirically measurable by sequencing pedigrees.

Kong et al. (2012) reported an SNV rate near 1.2e-8 per nucleotide per generation with a strong paternal-age effect. A 2025 four-generation, near-complete-genome pedigree study estimated an average of 74.5 de novo SNVs per transmission and 98–206 total DNMs per transmission when repeat-rich indels and structural variants are included.

**Disposition: RETAIN.**

The intake statement "60–100 mutations per person per generation" is directionally reasonable only when mutation class and assay coverage are specified. It is not itself a chronology.

## 2. Provenance of the submitted waiting-time numbers

The distinctive table values in the intake derive from:

Hössjer, O., Bechly, G., Gauger, A. & Sanford, J. (2015), *The waiting time problem in a model hominin population*, Theoretical Biology and Medical Modelling 12:18.

The paper simulates fixation of **prespecified nucleotide strings at specific locations** in a modeled hominin population and varies mutation rate, target-string length, fitness effect, and population size.

Important correction: the intake gives **3.95 x 10^9 years** as the extrapolated five-nucleotide result at the paper's stated biological mutation rate. Table 1 in the published paper gives **3.95 x 10^10 years**.

This is a source-transcription error and must not propagate.

## 3. What the waiting-time result does establish

Waiting time can become very long when all of the following are imposed:
- small effective population;
- long generation time;
- low site-specific mutation rate;
- a narrowly specified target;
- requirement for particular linked/co-dependent changes;
- specified intermediate fitness;
- requirement for establishment/fixation rather than mere first appearance.

This is a legitimate population-genetic constraint.

**Disposition: RETAIN/QUALIFY.**

The result is conditional, not a universal bound on evolutionary innovation.

## 4. Why target specification matters

A prespecified exact nucleotide string is a different stochastic problem from reaching any member of a large genotype set that realizes an adequate phenotype.

Required distinction:

```text
specified-sequence waiting time
!=
functional-target waiting time
```

Functional redundancy, standing variation, recombination, multiple mutational paths, target size, epistasis, and changing fitness landscapes can alter the waiting time substantially.

Conversely, a conventional response cannot simply invoke these mechanisms abstractly. For a claimed historical transition, their relevant target sizes, paths, fitnesses and population parameters should be constrained where possible.

## 5. Comparison with Durrett & Schmidt

Durrett & Schmidt (2008) analytically studied waiting for two specified mutations and applied the result to regulatory sequence evolution. They found a few million years could suffice in Drosophila under their modeled case, while a human-like effective population could require >100 million years for the particular two-step regulatory change.

Their model also shows why multiplying independent single-site waiting times naively is invalid: intermediate alleles can arise and persist before the second mutation occurs.

Therefore:

- "two mutations always take impossibly long" -> REJECT.
- "some specific multi-step changes can have long waiting times in small populations" -> RETAIN.
- "waiting-time claims require an explicit genotype-to-phenotype target and population model" -> CANONICAL METHODOLOGY CANDIDATE.

## 6. Haldane's dilemma

Haldane (1957) quantified the cost of gene substitution under particular assumptions and suggested an order-of-magnitude substitution pace for slowly reproducing organisms.

The intake treats this as a general proof that selection cannot support macroevolution.

**Disposition: REJECT AS STATED.**

The historical argument remains important, but substitution load depends on model structure, including selection regime, linkage, epistasis, soft versus hard selection, density regulation, initial allele frequency, standing variation, and whether substitutions proceed independently.

Research question retained:

> For a specified lineage and proposed transition, what rate of adaptive substitution is compatible with its demography, reproductive excess, linkage structure and fitness landscape?

## 7. Beneficial mutations lost by drift

A new beneficial allele can be lost stochastically while rare. Fixation probability depends on population model and selection coefficient. Therefore the qualitative claim is valid.

The intake's universal statement that "more than 99.9% of beneficial mutations" are lost is not portable without specifying s, dominance, effective population size and initial copy number.

**Disposition: QUALIFY.**

## 8. Deleterious mutation accumulation / "genetic entropy"

Direct observation supports a heterogeneous distribution of fitness effects, not a single category in which almost all mutations inexorably reduce population fitness.

Human nonsynonymous mutations span effectively neutral, weakly/moderately deleterious and strongly deleterious classes. Eyre-Walker et al. (2006) inferred a broad distribution; later work likewise models the DFE rather than treating all DNMs equivalently.

A claim of inevitable long-term genomic degeneration requires a population-level model including:
- DFE;
- dominance;
- epistasis;
- recombination;
- purifying selection;
- drift;
- mutation-selection balance;
- demography;
- fertility/reproductive excess;
- beneficial and compensatory mutations;
- environmental fitness landscape.

**Disposition of "mutation rate proves inevitable species degeneration": REJECT AS DEMONSTRATED.**

**Disposition of mutation load as a legitimate quantitative research question: RETAIN.**

## 9. Human genetic clocks

### mtDNA/Y coalescence
Coalescent dates are model-conditioned inferences depending on mutation rate, generation time, demography, population structure and lineage process.

They are therefore useful examples for WP-BWM-0022's retrodictive-age distinction.

The intake's assertion that paternal and maternal lineages converge within thousands of years is not supported by the conventional primary literature as stated.

**Disposition: REJECT AS STATED; retain model-dependence audit.**

### Heterozygosity
Low human heterozygosity can constrain effective population history but does not uniquely identify elapsed species age.

**Disposition: QUALIFY.**

### Population growth
Historical population growth is variable, density-dependent and punctuated by bottlenecks, expansions, mortality shocks and carrying-capacity changes.

**Disposition as age clock: REJECT.**

### Telomeres, somatic mutation, epigenetic drift
These are organismal/cellular processes and do not directly provide a species-age clock.

**Disposition as humanity/Earth clocks: REJECT.**

## 10. BWM/DFM research formulation

For a proposed evolutionary transition T:

```text
W(T) = f(
  Ne(t),
  generation_time,
  mutation spectrum,
  target size,
  standing variation,
  recombination,
  linkage,
  DFE,
  dominance,
  epistasis,
  intermediate fitness,
  environmental history,
  fixation/establishment criterion
)
```

The research burden is to determine whether plausible parameter ranges generate the transition within the historical interval assigned by the model.

This formulation is symmetrical. A conventional model may not invoke an unspecified "large target" or unknown adaptive path as a free rescue. A design/short-history model may not treat a prespecified exact sequence as the only possible functional target without evidence.

## 11. Corpus disposition

### Canonical BWM methodology candidates
- Separate measured mutation rates from historical coalescent/fixation inferences.
- Require explicit target definition in waiting-time arguments.
- Distinguish first appearance, establishment and fixation.
- Require parameter sensitivity rather than a single headline waiting time.
- Treat genetic dates as model-conditioned retrodictions.

### Biology / research programme
- Build case studies of proposed lineage transitions with biologically grounded target sizes and fitness landscapes.
- Reproduce Hössjer et al. and Durrett-Schmidt under matched assumptions.
- Determine where their results agree and where differing assumptions drive divergence.

### Rejected-argument register
- mutation count alone as a species-age clock;
- simple exponential human population growth as chronology;
- telomere shortening as humanity chronology;
- somatic mutation accumulation as humanity chronology;
- mtDNA/Y "thousands of years" assertion as presently stated;
- Haldane's cost as a general disproof of macroevolution;
- universal 99.9% beneficial-mutation-loss figure without parameters.

### Research quarantine
- "genetic entropy" until a reproducible population-genetic model is specified;
- exact waiting-time values copied from the intake without parameter provenance;
- any claimed maximum evolutionary rate derived from a single target-string simulation.

## Primary sources

- Haldane, J.B.S. (1957), *The Cost of Natural Selection*, Journal of Genetics 55, 511–524.
- Durrett, R. & Schmidt, D. (2008), *Waiting for Two Mutations: With Applications to Regulatory Sequence Evolution and the Limits of Darwinian Evolution*, Genetics 180, 1501–1509. DOI 10.1534/genetics.107.082610.
- Hössjer, O. et al. (2015), *The waiting time problem in a model hominin population*, Theoretical Biology and Medical Modelling 12:18.
- Kong, A. et al. (2012), *Rate of de novo mutations and the importance of father's age to disease risk*, Nature 488, 471–475.
- Eyre-Walker, A., Woolfit, M. & Phelps, T. (2006), *The Distribution of Fitness Effects of New Deleterious Amino Acid Mutations in Humans*, Genetics 173, 891–900.
- Sasani et al. (2025), *Human de novo mutation rates from a four-generation pedigree reference*, Nature 643, 427–436.

Confidence: HIGH on source provenance, the 3.95e10 correction, direct mutation-rate framing, and parameter dependence. MEDIUM on the ultimate evolutionary significance of waiting-time constraints because that requires transition-specific biological models.
