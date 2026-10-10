"""Small VCF genotype-count audit; NOT an ancient-DNA inference pipeline.

Only diploid, unphased-or-phased, fully called biallelic SNP GT fields are
counted. Missing or malformed genotypes are excluded per site. No imputation.
Input VCF must be plaintext; stream and checksum provenance externally.
"""
from collections import Counter

def summarize_vcf(lines):
    sites = 0
    skipped = Counter()
    spectrum = Counter()
    heterozygotes = 0
    called_individuals = 0
    for line in lines:
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.rstrip("\n").split("\t")
        if len(fields) < 10:
            skipped["malformed"] += 1
            continue
        ref, alt = fields[3], fields[4]
        if len(ref) != 1 or len(alt) != 1 or ref not in "ACGT" or alt not in "ACGT":
            skipped["non_biallelic_snp"] += 1
            continue
        fmt = fields[8].split(":")
        if "GT" not in fmt:
            skipped["no_gt"] += 1
            continue
        index = fmt.index("GT")
        alleles = []
        n_het = 0
        for sample in fields[9:]:
            parts = sample.split(":")
            if index >= len(parts):
                continue
            gt = parts[index].replace("|", "/").split("/")
            if len(gt) != 2 or any(a not in ("0", "1") for a in gt):
                continue
            a, b = map(int, gt)
            alleles.extend((a, b))
            n_het += a != b
        if not alleles:
            skipped["no_called_diploid_genotypes"] += 1
            continue
        sites += 1
        called_individuals += len(alleles) // 2
        heterozygotes += n_het
        spectrum[(sum(alleles), len(alleles))] += 1
    return {"sites": sites, "skipped": dict(skipped),
            "allele_count_spectrum": {str(k): v for k, v in sorted(spectrum.items())},
            "called_genotypes": called_individuals,
            "observed_heterozygosity": (heterozygotes / called_individuals
                                       if called_individuals else None)}
