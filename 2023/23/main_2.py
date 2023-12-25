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
from aocd import data

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
                case _:
                    G.add_edges_from([((i,j), n) for n in get_neighbours((i,j), m).values()])
    start = (0, np.argwhere(m[0] == ".")[0][0])
    return G, start

G, start = get_G(m)

from tqdm import tqdm

def get_longest_path_length(G, source, targets):
    longest_path_length = 0
    for target in tqdm(targets):
        for path in nx.all_simple_paths(G, source=source, target=target):
            len_path = 0
            for e in [e for e in zip(path, path[1:])]:
                len_path += G.edges[e]["length"]
            longest_path_length = max(len_path, longest_path_length)
    return longest_path_length

def walk_until(n, p, d=1):
    nn = G[n]
    if len(nn) != 2:
        return n, d
    not_p = [_ for _ in nn if _ != p][0]
    return walk_until(not_p, n, d+1)
       
G_small = nx.Graph()

proper_nodes = [e for e in G.nodes if len(G[e]) != 2]

for node in proper_nodes:
    for n in G[node]:
        next_node, d = walk_until(n, node)
        G_small.add_edge(node, next_node, length=d)

targets = [n for n in G_small.nodes if len(G_small[n]) == 1]
print(get_longest_path_length(G_small, start, targets))
