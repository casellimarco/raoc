from aocd import data
import networkx as nx
import numpy as np

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
directions = [np.array(d) for d in directions]

input = np.array([[int(ch) for ch in line] for line in data.splitlines()])

def knbrs(G, start, k):
    nbrs = set([start])
    for l in range(k):
        nbrs = set((nbr for n in nbrs for nbr in G[n]))
    return nbrs

G = nx.DiGraph()

for a in np.ndindex(input.shape):
    for dir in directions:
        b = a + dir
        if np.any(b < 0) or np.any(b >= input.shape):
            continue
        b = tuple(b)
        if input[b] - input[a] != 1:
            continue
        G.add_edge(a, b)

part1 = 0
part2 = 0
for a in np.argwhere(input == 0):
    nines = knbrs(G, tuple(a), 9)
    part1 += len(nines)
    part2 += sum((len(list(nx.all_simple_paths(G, tuple(a), b))) for b in nines))

print(1, part1)
print(2, part2)