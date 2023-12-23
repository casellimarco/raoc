data="""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
# from aocd import data

import networkx as nx
import numpy as np


lines = data.splitlines()

m = np.array([[c for c in d] for d in data.splitlines()])


def check(position, m):
    i, j = position
    return 0 <= i < m.shape[0] and 0 <= j < m.shape[1] and m[position] != "#"

def get_neighbours(position, m):
    y, x = position
    n = {"E":(y, x+1), "S":(y+1, x), "W":(y, x-1), "N":(y-1, x)}
    return {d:pos for d, pos in n.items() if check(pos, m)}

direction = {">": "E", "v": "S", "<": "W", "^": "N"}

def get_G(m):
    G = nx.DiGraph()
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            match c:
                case "#":
                    continue
                case ".":
                    # From a point, you can go to any of the 4 directions
                    G.add_edges_from([((i,j), n) for n in get_neighbours((i,j), m).values()])
                case _: # Arrow
                    # From a arrow, you can only go to the direction of the arrow
                    G.add_edge((i,j),get_neighbours((i,j), m)[direction[c]])
    start = (0, np.argwhere(m[0] == ".")[0][0])
    return G, start

G, start = get_G(m)

from tqdm import tqdm

def get_longest_path_length(G, source, targets):
    longest_path_length = 0
    for i, target in tqdm(enumerate(targets)):
        for path in nx.all_simple_paths(G, source=source, target=target):
            longest_path_length = max(len(path), longest_path_length)
        if i % 100 == 0:
            print(i, longest_path_length)
    return longest_path_length

targets = [tuple(t) for t  in np.argwhere(m != "#")]
sp = nx.shortest_path_length(G, start)
targets = list(sp.keys())
print(get_longest_path_length(G, start, targets))

targets = [e for e in G.nodes if len(G[e]) == 1]
for e in G.edges:
    G[e]
    if e[0] == (1, 4):
        print(e)
        break

print(get_longest_path_length(G, start, targets) - 1)
