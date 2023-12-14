data="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
from aocd import data

import numpy as np

m = np.array([list(row) for row in data.splitlines()])

from functools import cache

to_tuple = lambda m: tuple(map(tuple, m))

@cache
def move_north(m):
    m = np.array(m)
    # already in the correct order
    rounded = np.where(m == "O")
    for old_loc in zip(*rounded):
        next_loc = list(old_loc)
        next_loc[0] -= 1
        while next_loc[0] >= 0 and m[tuple(next_loc)] == ".":
            next_loc[0] -= 1
        next_loc[0] += 1
        m[old_loc] = "."
        m[tuple(next_loc)] = "O"
    return m

def score(m):
    rounded_x = np.where(m == "O")[0]
    return len(m)*len(rounded_x) - np.sum(rounded_x)
    
m_1 = move_north(to_tuple(m))
print(1, score(m_1))

from tqdm import tqdm
scores = []
# for c in tqdm(range(1000000000)):
for c in tqdm(range(10000)):
    for t in range(4):
        m = move_north(to_tuple(m))
        # print(t)
        # print(np.rot90(m, t))
        m = np.rot90(m, -1) 
    scores.append(score(m))

import matplotlib.pyplot as plt
plt.plot(scores[-100:])
plt.show()

#it's really periodic with period 10 after the first bit! 
#Just pick a big enough entry == 10**9 mod(10) (-1 because of 0-indexing)
print(2, scores[999])
