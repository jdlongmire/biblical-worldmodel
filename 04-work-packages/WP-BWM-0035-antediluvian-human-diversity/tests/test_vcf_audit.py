import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from vcf_audit import summarize_vcf

class TestVCFAudit(unittest.TestCase):
    def test_biallelic(self):
        lines=["##fileformat=VCFv4.2\n",
               "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\ta\tb\n",
               "1\t10\t.\tA\tG\t.\tPASS\t.\tGT\t0/1\t1|1\n"]
        x=summarize_vcf(lines)
        self.assertEqual(x["sites"],1)
        self.assertEqual(x["allele_count_spectrum"]["(3, 4)"],1)
        self.assertEqual(x["observed_heterozygosity"],0.5)
    def test_missing_and_multiallelic(self):
        lines=["1\t10\t.\tA\tG,T\t.\tPASS\t.\tGT\t0/1\n",
               "1\t11\t.\tA\tG\t.\tPASS\t.\tGT\t./.\n"]
        x=summarize_vcf(lines)
        self.assertEqual(x["sites"],0)
        self.assertEqual(x["skipped"]["non_biallelic_snp"],1)
        self.assertEqual(x["skipped"]["no_called_diploid_genotypes"],1)
    def test_filter_exclusion(self):
        line="1\\t12\\t.\\tA\\tG\\t.\\tLowQual\\t.\\tGT\\t0/1\\n"
        x=summarize_vcf([line])
        self.assertEqual(x["sites"],0)
        self.assertEqual(x["skipped"]["not_pass"],1)
    def test_no_samples(self):
        self.assertEqual(summarize_vcf([])["observed_heterozygosity"],None)
