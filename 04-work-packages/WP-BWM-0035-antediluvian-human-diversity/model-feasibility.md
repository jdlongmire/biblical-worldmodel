# Founder bottleneck: analytical feasibility baseline v0.1

**Status:** Mathematical boundary model only. No empirical genomic fitting has been performed.

## Scope and assumptions

For an autosomal locus, each diploid founder carries at most two allele copies. Eight people yield at most 16 sampled copies; these are not 16 unrelated chromosomes because the passengers include close relatives. If only Noah, his wife, and three unrelated daughters-in-law are genetically independent at a locus, there are at most ten independent parental copies; the three sons inherit from Noah and his wife. The actual maximum of independent copies depends on wives' kinship and on the genetic relationships of all founders. Do not treat this simplification as an estimate of observed ancient diversity.

**Hard limit:** A founding population of eight diploid humans can transmit no more than 16 distinct ancestral alleles at any single autosomal locus *at the instant of the bottleneck*, absent new mutation, duplication, gene conversion, or other post-bottleneck variation. It can transmit fewer. This locus-specific statement does not cap the number of variants across the genome at 16.

## Transparent neutral sampling approximation

For a pre-bottleneck biallelic locus at frequency `p`, if `k` independent gene copies are sampled randomly, the probability that both alleles are retained is:

`P(retain both) = 1 - p^k - (1-p)^k`.

For `p=0.5` and `k=16`: `P=0.999969482421875`. For `p=0.01` and `k=16`: `P≈0.1485`. For `p=0.01` and `k=10`: `P≈0.0956`.

These are **illustrative conditional probabilities**, not model predictions for Noah's family. Relatedness, selection, population structure and nonrandom mate choice violate independent sampling. Rare ancestral variants are disproportionately lost under random sampling; deliberately specified founder genotypes could preserve a different set, but must be justified and cannot be selected post hoc to fit each observation.

## Three clocks

- `t_variant`: first appearance of a particular mutation.
- `t_divergence`: population separation (potentially followed by gene flow).
- `t_specimen`: death and deposition of a fossil individual.

These must not be equated. Ancient coalescent times may precede population splits.

## Forward-model specification

Inputs: biblical chronology scenario; Fall-to-Flood years; age-specific fertility; founder kinship graph; founder phased haplotypes; effective population size by generation; mutation/recombination map; migration/admixture; survival/selection; sampling design.

Outputs: site-frequency spectrum, heterozygosity, linkage disequilibrium, archaic haplotype lengths, D-statistics/f4, lineage sharing, runs of homozygosity, spatial differentiation and uncertainty intervals.

Compare simulated distributions against primary-data summaries using held-out metrics. No manual allele placement after observing the target statistic. Use sensitivity analyses and preregister bounds.

## Falsification and identifiability

- An observed genetic configuration impossible under the specified founder genotypes and allowed mutation/recombination mechanisms falsifies that parameterization.
- A model requiring arbitrary initialized genotypes at each challenged locus is non-predictive and fails explanatory-evasion criteria.
- Even a feasible simulated match is not proof of historical placement; alternative demographic histories may be observationally equivalent.
- The hypothesis that *all* archaic lineages ended at the Flood must distinguish extinction of recognizable populations from persistence of their alleles in descendants.

## First quantitative experiment

1. Establish a reproducible neutral Wright–Fisher simulation and a pedigree-aware alternative.
2. Sweep `k ∈ {8,10,12,16}`, `p ∈ {0.001,0.01,0.05,0.5}`, multiple generations and mutation rates.
3. Validate against the closed-form retention formula at generation zero.
4. Add linked genomic segments, recombination and admixed ancestry tracts.
5. Compare pre-registered statistics with the published ancient genomes, and retain negative results.

The present document establishes formulas and a research protocol. No inference of feasibility for a global Flood bottleneck is warranted yet.
