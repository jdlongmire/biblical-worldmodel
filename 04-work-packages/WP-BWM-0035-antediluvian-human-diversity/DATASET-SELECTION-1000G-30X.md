# Empirical dataset selection v0.1 (2026-10-10)

**Selected reference:** 1000 Genomes Project high-coverage 30x, GRCh38, 3,202 individuals and 602 trios. Primary study: Byrska-Bishop et al. (2022), Cell, DOI 10.1016/j.cell.2022.08.004; accession PRJEB55077.

**Source authority:** https://www.internationalgenome.org/data-portal/data-collection/1000genomes_30x

**Candidate phased chromosome 22 VCF:** https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20220422_3202_phased_SNV_INDEL_SV/1kGP_high_coverage_Illumina.chr22.filtered.SNV_INDEL_SV_phased_panel.vcf.gz

**Companion sample pedigree metadata:** https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/1kGP.3202_samples.pedigree_info.txt

**Verification status:** IGSR confirms this collection has phased calls and pedigree information. The exact candidate URLs above must be checked against the authoritative directory listing before download. Network access to the EBI file server was unavailable from the execution environment during this session. No dataset was downloaded or analyzed; checksums and file sizes remain unverified.

## Predeclared first pass

- Genome assembly GRCh38; chromosome 22 only; pilot region chosen *before* examining genotype outcomes.
- Use pedigree metadata to distinguish unrelated individuals from related samples; record population and sample exclusions.
- Use biallelic PASS SNPs, diploid fully called genotypes, and explicit callable masks; report missingness and exclusions.
- Calculate alternate-allele count distribution, allele-frequency spectrum, observed heterozygosity, and uncertainty with denominators.
- Preserve phase for subsequent haplotype and LD statistics; a simple VCF allele-count audit does not provide an LD analysis.
- Freeze accessions, region boundaries, masks, checksums, exact command line, and software versions before fitting.
- Do not compare a single 500-marker synthetic model to genome-wide observed counts without matched ascertainment and sample size.
- Hold out distinct regions for validation and separately evaluate the conventional demographic comparison.

## Stop conditions

No inference about the Flood, chronology, Neanderthals, or Denisovans from this modern-only pilot. No empirical-fit claim until real data have been downloaded, audited, and compared under preregistered procedures.
