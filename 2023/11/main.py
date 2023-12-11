from aocd import data
from functools import partial
import numpy as np

data = data.replace(".", "0").replace("#", "1")

space = np.array([list(map(int, row)) for row in data.splitlines()])

empty_cols = np.where(np.sum(space, axis=0)==0)[0]
empty_rows = np.where(np.sum(space, axis=1)==0)[0]

galaxies = np.array(np.where(space)).T

def expand_space(galaxy, expansion=2):
    r, c = galaxy
    return (r + (expansion-1)*(empty_rows < r).sum(), c + (expansion-1)*(empty_cols < c).sum())

def distance(galaxy_1, galaxy_2):
    return np.abs(galaxy_1 - galaxy_2).sum()

for part, expansion in enumerate([2, 1000000]):
    expanded_galaxies = np.apply_along_axis(partial(expand_space, expansion=expansion), 1, galaxies)
    tot = 0
    for i, g1 in enumerate(expanded_galaxies):
        for g2 in expanded_galaxies[i+1:]:
            tot += distance(g1, g2)
    print(part+1, tot)