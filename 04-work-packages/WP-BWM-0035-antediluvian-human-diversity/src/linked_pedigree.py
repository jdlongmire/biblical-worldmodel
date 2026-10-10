"""Synthetic linked-marker pedigree; not a historical reconstruction."""
import random

def gamete(pair, rng, crossover_rate=0.01, mutation_rate=0.0):
    if not (0 <= crossover_rate <= 1 and 0 <= mutation_rate <= 1):
        raise ValueError("rates outside [0,1]")
    a, b = pair
    if not a or len(a) != len(b):
        raise ValueError("unequal or empty haplotypes")
    side = rng.randrange(2)
    out = []
    for i in range(len(a)):
        if i and rng.random() < crossover_rate:
            side = 1 - side
        value = (a if side == 0 else b)[i]
        if rng.random() < mutation_rate:
            value = 1 - value
        out.append(value)
    return tuple(out)

def genotype(rng, loci, frequency):
    if loci < 1 or not 0 <= frequency <= 1:
        raise ValueError("invalid genotype parameters")
    return tuple(tuple(int(rng.random() < frequency) for _ in range(loci))
                 for _ in range(2))

def family(rng, loci=100, frequency=0.01, crossover_rate=0.01,
           mutation_rate=0.0, daughter_sharing=0.0):
    """Daughter sharing is a synthetic whole-haplotype copy switch, not kinship."""
    if not 0 <= daughter_sharing <= 1:
        raise ValueError("invalid sharing")
    noah = genotype(rng, loci, frequency)
    wife = genotype(rng, loci, frequency)
    sons = [(gamete(noah, rng, crossover_rate, mutation_rate),
             gamete(wife, rng, crossover_rate, mutation_rate))
            for _ in range(3)]
    pool = noah + wife
    daughters = []
    for _ in range(3):
        h = []
        for _ in range(2):
            h.append(rng.choice(pool) if rng.random() < daughter_sharing
                     else tuple(int(rng.random() < frequency)
                                for _ in range(loci)))
        daughters.append(tuple(h))
    return [noah, wife, *sons, *daughters]

def polymorphic_loci(people):
    length = len(people[0][0])
    return sum(len({h[i] for person in people for h in person}) == 2
               for i in range(length))

def sweep(seed=20261010, loci=1000, frequency=0.01,
          crossover_rates=(0.0, 0.001, 0.01, 0.1),
          mutation_rates=(0.0, 0.001), daughter_sharing=(0.0, 1.0)):
    result = []
    for share in daughter_sharing:
        for recomb in crossover_rates:
            for mutation in mutation_rates:
                people = family(random.Random(seed), loci, frequency,
                                recomb, mutation, share)
                result.append({"daughter_sharing": share,
                               "crossover_rate": recomb,
                               "mutation_rate": mutation,
                               "polymorphic_loci": polymorphic_loci(people),
                               "loci": loci})
    return result
