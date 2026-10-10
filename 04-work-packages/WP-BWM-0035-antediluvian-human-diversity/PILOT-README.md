# Founder genomics executable pilot

This is the first executable component of WP-BWM-0035, following SOP-RSCH-001. It uses **Python standard library only**; no external data or packages are needed.

Run from this directory:

```sh
python -m unittest discover -s tests -v
python -c "import sys; sys.path.insert(0, 'src'); from founder_pilot import founder_sweep; print(founder_sweep())"
```

Open `notebooks/02-founder-reconstruction.ipynb` in Jupyter, and run from this directory or `notebooks/`. The notebook has no stored outputs, so users can reproduce its calculations. Python 3.10+ recommended.

**Model contract:** This is a synthetic single-locus allele-retention study. Sons inherit Noah/wife alleles; daughters-in-law have a configurable synthetic probability of sharing founder parental alleles. This parameter is **not** a genetic relatedness coefficient. It does not represent genome-wide founder reconstruction, post-Flood population genetics, linked haplotypes, or observed genomic evidence. Historical claims are not warranted by this pilot.

**Acceptance for this pilot:** executable notebook, tested founder inheritance, independent-copy reference formula, controlled seed, parameter sweep and explicit limitations. No claim of empirical validation. Research programme acceptance criteria remain open.

## Linked-marker extension

- `src/linked_pedigree.py`: synthetic haplotype inheritance, recombination and mutation switches, and scenario sweep.
- `tests/test_linked_pedigree.py`: seven boundary, inheritance and determinism checks.
- `RATE-SENSITIVITY-PLAN.md`: preregistered extension criteria.

A matching local implementation passed seven tests on 2026-10-10. The committed module was not imported into that local run; direct clean-checkout execution and Jupyter execution are still required. The linked-marker notebook has not been committed. These synthetic parameters are not historical estimates.

## Empirical calibration gate

- [Pre-registered empirical calibration protocol](EMPIRICAL-CALIBRATION-PROTOCOL.md) lists accession verification, data quality, holdouts, model discriminators and stop conditions.
- `src/vcf_audit.py` and `tests/test_vcf_audit.py` add a minimal, transparent diploid biallelic VCF allele-count audit. This is a demonstration parser, not a substitute for established genomics QC pipelines. It does not process ancient-DNA genotype likelihoods, callable masks, phasing uncertainty, multi-allelic records or compressed VCFs.

**No human genome datasets have been fetched, and no empirical genomic fit has been run.** The new code and tests have been committed but not executed from a clean checkout. The draft PR remains unmerged pending verification.
