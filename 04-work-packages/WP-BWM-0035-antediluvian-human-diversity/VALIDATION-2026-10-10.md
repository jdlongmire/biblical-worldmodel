# Validation record: 2026-10-10

**Scope:** Independent local reimplementation of three baseline checks, not direct execution of the repository test suite or Jupyter notebook.

- Single-locus independent retention boundary at p=0 and p=1: PASS.
- Analytical reference at p=0.5 and 16 independent copies: PASS.
- Synthetic pedigree has eight people and three sons inherit one allele from each parental genotype: PASS.
- Rare-allele retention is reduced in the extreme daughter-sharing scenario compared with independent daughter alleles (100,000 Monte Carlo trials, fixed seed): PASS.

Environment: Python standard library; standalone local check executed during review. All three checks passed in approximately one second. The standalone check reproduced the mathematical structure of the committed code but did not import repository modules directly. Therefore this is **not** evidence of successful clean-checkout notebook execution or full repository test coverage.

Remaining gates: execute committed unittest suite from clean checkout, execute both notebooks top-to-bottom, inspect deterministic outputs, add linked-marker inheritance and nonuniform-rate sensitivity, and then evaluate empirical datasets. Do not merge the draft PR until these gates are satisfied or explicitly waived by the principal.
