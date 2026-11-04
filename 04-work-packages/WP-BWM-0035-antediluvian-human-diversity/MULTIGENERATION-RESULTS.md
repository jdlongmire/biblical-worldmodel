# Synthetic multi-generation experiment (2026-10-10)

Status: synthetic experiment, not a fit to observed human genomes.

An independently executed local implementation passed nine tests. The GitHub-committed adaptation and notebooks have not yet been directly executed from a clean checkout.

Configuration: 500 synthetic markers, eight founders, eight generations, population cap 256, fixed seed 20261010, initial allele frequency 0.05, recombination probability 0.01 per marker boundary.

| Scenario | Founder segregating sites | Generation 8 segregating sites | Founder heterozygosity | Generation 8 heterozygosity |
|---|---:|---:|---:|---:|
| No mutation | 186 | 179 | 0.077781 | 0.075699 |
| Variable synthetic mutation (0.002 for 2 generations; 0.0001 for 6) | 186 | 260 | 0.077781 | 0.083751 |

These numerical results come from the independently executed local implementation, not direct execution of the committed code. Mutation probabilities are intentionally synthetic and not historical human estimates. No population structure, selection, calibrated genome map, ancient DNA, or held-out genomic evidence is modeled.

Next: clean-checkout execution of committed tests and notebooks, compare outputs, then empirically constrain model parameters and perform severe tests.
