# Dataset access verification and first empirical gate (2026-10-10)

## Source verification

- IGSR's official 30x GRCh38 collection documents 3,202 genomes, 602 trios, phased calls, and pedigree metadata: https://www.internationalgenome.org/data-portal/data-collection/1000genomes_30x
- Byrska-Bishop et al. (2022), *Cell*, DOI 10.1016/j.cell.2022.08.004, provides the peer-reviewed cohort description.
- The phased chromosome 22 candidate filename is independently used in published software documentation: `1kGP_high_coverage_Illumina.chr22.filtered.SNV_INDEL_SV_phased_panel.vcf.gz`, under the IGSR `20220422_3202_phased_SNV_INDEL_SV` directory. This corroborates its intended path but **does not verify its current HTTP availability, checksum or content**.
- A direct HTTPS HEAD attempt from the execution container failed with a connection error. No dataset was downloaded.

## Next executable gate

1. Obtain the source VCF and tabix index from IGSR or a documented mirror. Record URL, byte size, SHA-256 and timestamp.
2. Extract a fixed chromosome 22 interval with bcftools/tabix, recording exact coordinates and command versions. Avoid processing the entire VCF with the demonstration Python parser.
3. Select unrelated samples using the published pedigree metadata and freeze the sample manifest.
4. Apply callable-region mask, PASS and biallelic-SNP filters, missingness thresholds, and population strata.
5. Compare observed allele-count spectrum and heterozygosity to matched simulated sampling, with chromosome regions held out before parameter fitting.
6. Record failures and exclude all empirical-fit claims until data and scripts have been executed.

**Blocking dependency:** accessible verified genomic bytes. Synthetic numerical outputs cannot substitute for empirical observation.
