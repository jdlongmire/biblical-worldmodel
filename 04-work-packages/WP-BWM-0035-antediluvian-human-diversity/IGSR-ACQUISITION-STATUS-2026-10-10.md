# IGSR data acquisition gate: 2026-10-10

## Verified publicly documented metadata

The official IGSR 1000 Genomes 30x GRCh38 collection confirms 3,202 samples, including related samples, phased variant calls, and pedigree metadata:
https://www.internationalgenome.org/data-portal/data-collection/1000genomes_30x

The chromosome 22 phased VCF filename and corresponding tabix index appear in public directory listings and independent genomics tutorials:
https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20220422_3202_phased_SNV_INDEL_SV/1kGP_high_coverage_Illumina.chr22.filtered.SNV_INDEL_SV_phased_panel.vcf.gz

## Acquisition result

An HTTPS request for the chromosome 22 VCF tabix index from the execution container failed with a connection error. Thus file accessibility, content, SHA-256, variant counts and empirical allele frequencies are **not verified**. Do not present the public directory's approximate 425 MB file size as a measured local file size.

## QC improvement

The exploratory `src/vcf_audit.py` now explicitly excludes non-PASS VCF records, with a regression test. This is necessary but not sufficient: it still lacks sample-subset selection, callable masks, region extraction, population stratification, phase/LD statistics, and genotype-likelihood handling.

## Next gate

Acquire a verified region-level BGZF VCF through an environment with access to IGSR, freeze the exact region and unrelated-sample manifest, run the tests and checksum verifier from a clean checkout, then perform a matched simulation comparison. **No empirical-fit claim is authorized before this gate.**
