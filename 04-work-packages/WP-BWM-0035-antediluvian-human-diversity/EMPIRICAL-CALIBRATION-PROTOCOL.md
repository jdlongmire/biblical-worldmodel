# Empirical calibration gate: preregistration

**Status:** proposed protocol, no empirical fit performed. Synthetic toy data are not observations.

## Observational targets

1. Within-population site-frequency spectra and heterozygosity from quality-filtered, phased modern human whole genomes. Record callable sequence, sampling frame, ploidy, sequencing technology, genotype uncertainty and ascertainment.
2. Haplotype-length distributions and linkage disequilibrium as separate targets from allele-count statistics. Account for chromosome-specific recombination maps, phasing error and demography.
3. Neanderthal and Denisovan high-coverage ancient genomes: report sample provenance, contamination, postmortem damage, mapping bias and genotype uncertainty. Separate observed shared alleles from introgression-model interpretations.
4. Allele sharing, population structure and archaic ancestry statistics with explicit null models, confidence intervals and independently reproduced reference implementations.

## Candidate primary data sources for accession-level verification

- 1000 Genomes Project high-coverage phased genomes, IGSR (https://www.internationalgenome.org/). Select and freeze release, accession, population, assembly and callable mask before fitting.
- Human Genome Diversity Project, public release (https://www.internationalgenome.org/data-portal/data-collection/hgdp). Confirm data-use conditions and population consent constraints.
- Max Planck / Leipzig ancient genome data archive (https://www.eva.mpg.de/genetics/genome-projects/). Confirm exact specimen and download manifest before analysis.
- European Nucleotide Archive (https://www.ebi.ac.uk/ena/browser/home). Use accession-level source checksums, not inferred sample identities.

These are **discovery entrypoints**, not yet validated accession selections. Do not claim that any dataset was downloaded or analyzed.

## Holdout and anti-overfitting protocol

Pre-register reference panel, callable regions, filters, statistics and tolerances. Partition chromosomes or independent genomic regions into calibration and held-out validation sets. Fit bounded demographic and time-varying mutation/recombination models to calibration statistics only. Compare against constant-rate and conventional demographic baselines. Report failure cases, uncertainty, model complexity and identifiability; no parameter may be tuned against the held-out results after inspection.

## Required discriminators

- Genome-wide site-frequency spectrum and heterozygosity must both be reproduced, not just one statistic.
- Correlated linked variation must be reproduced, not only per-site allele retention.
- Rare allele and deep coalescence patterns must be confronted explicitly.
- Archaic-modern haplotype sharing and tract lengths must be explained by a coherent pedigree and population history, not a single matching percentage.
- All historical-rate changes require independent constraints and a testable mechanism. Extreme synthetic mutation settings are stress tests, not estimates.

## Stop conditions

A model that cannot fit held-out genomic features under biologically bounded parameters is rejected or revised with the revision logged. A model whose parameters are not identifiable cannot be described as historically confirmed. Dataset limitations or missing access are recorded as incomplete, not positive support.
