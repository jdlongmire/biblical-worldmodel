"""Synthetic multi-generation founder model. Not a historical inference."""
import random
from linked_pedigree import family, gamete

def metrics(pop):
    if not pop: raise ValueError("empty population")
    loci=len(pop[0][0]); copies=2*len(pop)
    counts=[sum(h[i] for person in pop for h in person) for i in range(loci)]
    return {"individuals":len(pop),"loci":loci,
            "segregating_sites":sum(0<k<copies for k in counts),
            "mean_expected_heterozygosity":sum(2*(k/copies)*(1-k/copies) for k in counts)/loci}

def next_generation(pop,rng,target,recombination=0.01,mutation=0.,pairs=None):
    if target<2: raise ValueError("target must be >=2")
    if pairs is None:
        pairs=[(i,j) for i in range(len(pop)) for j in range(i+1,len(pop))]
    if not pairs: raise ValueError("no permitted pairs")
    return [(gamete(pop[i],rng,recombination,mutation),
             gamete(pop[j],rng,recombination,mutation))
            for i,j in (rng.choice(pairs) for _ in range(target))]

def simulate(generations=8,seed=20261010,loci=500,frequency=0.05,
             recombination=0.01,mutation_schedule=None,size_schedule=None,
             daughter_sharing=0.):
    if generations<0: raise ValueError("negative generations")
    if mutation_schedule is None: mutation_schedule=[0.]*generations
    if size_schedule is None: size_schedule=[min(8*2**(g+1),256) for g in range(generations)]
    if len(mutation_schedule)!=generations or len(size_schedule)!=generations:
        raise ValueError("schedule length mismatch")
    pop=family(random.Random(seed),loci,frequency,recombination,0,daughter_sharing)
    rng=random.Random(seed+1)
    history=[{"generation":0,**metrics(pop)}]
    for g in range(generations):
        # The first generation is restricted to the three son/daughter-in-law couples.
        pairs=[(2,5),(3,6),(4,7)] if g==0 else None
        pop=next_generation(pop,rng,size_schedule[g],recombination,
                            mutation_schedule[g],pairs)
        history.append({"generation":g+1,**metrics(pop)})
    return history
