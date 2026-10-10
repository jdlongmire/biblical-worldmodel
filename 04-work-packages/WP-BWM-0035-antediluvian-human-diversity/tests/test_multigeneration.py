import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from multigeneration import simulate
class TestMulti(unittest.TestCase):
    def test_schedule(self):
        self.assertEqual([r["individuals"] for r in simulate(3,size_schedule=[12,24,48])],[8,12,24,48])
    def test_determinism(self):
        self.assertEqual(simulate(3),simulate(3))
    def test_no_mutation_no_initial_diversity(self):
        self.assertTrue(all(r["segregating_sites"]==0 for r in simulate(3,frequency=0)))
    def test_mutation(self):
        self.assertGreater(simulate(1,frequency=0,mutation_schedule=[0.5])[-1]["segregating_sites"],0)
    def test_empty(self):
        self.assertEqual(len(simulate(0)),1)
    def test_invalid(self):
        with self.assertRaises(ValueError):simulate(2,mutation_schedule=[0])
