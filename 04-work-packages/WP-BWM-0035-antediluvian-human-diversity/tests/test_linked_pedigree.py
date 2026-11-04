import sys, random, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from linked_pedigree import gamete, family, sweep

class TestLinked(unittest.TestCase):
    def test_no_recombination(self):
        pair = ((0,0,0,0), (1,1,1,1))
        for seed in range(20):
            self.assertIn(gamete(pair, random.Random(seed), 0, 0), pair)
    def test_always_recombines(self):
        g = gamete(((0,0,0,0),(1,1,1,1)),random.Random(2),1,0)
        self.assertEqual(g,(g[0],1-g[0],g[0],1-g[0]))
    def test_mutation(self):
        self.assertEqual(gamete(((0,0,0),(0,0,0)),random.Random(1),0,1),(1,1,1))
    def test_pedigree(self):
        people=family(random.Random(11),loci=50,crossover_rate=0,mutation_rate=0)
        self.assertEqual(len(people),8)
        self.assertTrue(all(len(h)==50 for person in people for h in person))
        for son in people[2:5]:
            self.assertIn(son[0],people[0])
            self.assertIn(son[1],people[1])
    def test_reproducibility(self):
        self.assertEqual(family(random.Random(10)),family(random.Random(10)))
    def test_sweep(self):
        self.assertEqual(len(sweep(loci=20,crossover_rates=(0,1))),8)
    def test_validation(self):
        with self.assertRaises(ValueError):
            gamete(((0,),(1,)),random.Random(),-0.1)
        with self.assertRaises(ValueError):
            family(random.Random(),daughter_sharing=1.2)
