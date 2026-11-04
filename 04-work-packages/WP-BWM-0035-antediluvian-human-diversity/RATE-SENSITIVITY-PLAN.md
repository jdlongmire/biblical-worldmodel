# Linked-segment and rate-sensitivity validation plan

Status: preregistered extension; implementation pending.

1. Validate the single-locus founder pilot with independent unit tests and clean notebook execution.
2. Extend the model to synthetic linked markers with a crossover probability per adjacent marker, a controlled seed, and explicit pedigree inheritance.
3. Sweep bounded recombination and mutation scenarios without treating any historical rate as established.
4. Compare founder pedigree results against an independent-copy null and report loss of rare variants.
5. Add multi-generation expansion, phased segments and held-out empirical statistics only after validation.
6. Preserve negative findings, uncertainty and explicit separation of synthetic demonstration from historical evidence.

Acceptance: reproducible environment, tests, notebook execution, provenance, and review before merge.
