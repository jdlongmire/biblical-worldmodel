"""Synthetic founder-pedigree pilot. Not a reconstruction of historical genomes."""
from __future__ import annotations
import random

def independent_retention(p: float, copies: int) -> float:
    if not 0 <= p <= 1 or copies < 1:
        raise ValueError("p in [0,1], copies >= 1 required")
    return 1.0 - p**copies - (1.0-p)**copies

def draw_genotype(rng: random.Random, p: float) -> tuple[int, int]:
    return (int(rng.random() < p), int(rng.random() < p))

def found_family(rng: random.Random, p: float, wife_relatedness: float = 0.0):
    """Eight diploid people: Noah, wife, three sons, three daughters-in-law.

    Sons inherit one randomly chosen copy from each parent at each *independent*
    locus. wife_relatedness is a synthetic probability that a daughter-in-law's
    allele copies are sampled from the existing parental alleles, not a kinship
    coefficient. No recombination or linkage is modeled.
    """
    if not 0 <= p <= 1 or not 0 <= wife_relatedness <= 1:
        raise ValueError("parameters must be in [0,1]")
    noah, wife = draw_genotype(rng,p), draw_genotype(rng,p)
    sons = [(rng.choice(noah),rng.choice(wife)) for _ in range(3)]
    source = noah + wife
    daughters = [tuple(rng.choice(source) if rng.random() < wife_relatedness
                       else int(rng.random() < p) for _ in range(2))
                 for _ in range(3)]
    return [noah,wife,*sons,*daughters]

def family_retention_probability(p: float, trials: int = 20000,
                                 wife_relatedness: float = 0.0,
                                 seed: int = 20261010) -> float:
    if trials < 1:
        raise ValueError("trials must be positive")
    rng = random.Random(seed)
    retained = 0
    for _ in range(trials):
        copies = [allele for person in found_family(rng,p,wife_relatedness)
                  for allele in person]
        retained += (0 in copies and 1 in copies)
    return retained / trials

def founder_sweep(frequencies=(0.001,0.01,0.05,0.5),
                  relatedness=(0.0,0.5,1.0), trials=20000):
    return [{"p":p,"wife_relatedness":r,
             "retention":family_retention_probability(p,trials,r),
             "independent_16":independent_retention(p,16)}
            for p in frequencies for r in relatedness]
