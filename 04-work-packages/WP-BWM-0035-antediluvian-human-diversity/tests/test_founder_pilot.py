"""Run: python -m unittest discover -s tests -v (from this WP directory)."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / "src"))
from founder_pilot import independent_retention,found_family,family_retention_probability
import random

class FounderPilotTests(unittest.TestCase):
    def test_boundaries(self):
        self.assertEqual(independent_retention(0,16),0)
        self.assertEqual(independent_retention(1,16),0)
        self.assertAlmostEqual(independent_retention(0.5,16),1-2/65536)
    def test_family_structure(self):
        family=found_family(random.Random(17),0.5)
        self.assertEqual(len(family),8)
        self.assertTrue(all(len(g)==2 for g in family))
        self.assertTrue(all(g[0] in family[0] and g[1] in family[1]
                            for g in family[2:5]))
    def test_related_daughters_reduce_rare_retention(self):
        a=family_retention_probability(0.01,100000,0,123)
        b=family_retention_probability(0.01,100000,1,123)
        self.assertGreater(a,b)
    def test_invalid(self):
        with self.assertRaises(ValueError): independent_retention(-0.1,16)
        with self.assertRaises(ValueError): found_family(random.Random(),0.5,1.2)

if __name__=="__main__": unittest.main()
