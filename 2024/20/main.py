from itertools import combinations
from aocd import data
import networkx as nx
import numpy as np
from tqdm import tqdm

input = np.array([list(row) for row in data.split()])
map = input != "#"

directions = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
]
directions = [np.array(v) for v in directions]

G = nx.Graph()
for a in np.argwhere(map): 
    for dir in directions:
        b = a + dir
        if np.any(b < 0) or np.any(b >= input.shape):
            continue
        if map[tuple(b)]:
            G.add_edge(tuple(a), tuple(b))

start = tuple(np.argwhere(input == "S")[0])
end = tuple(np.argwhere(input == "E")[0])

from_start = nx.shortest_path_length(G, source=start)
to_end = nx.shortest_path_length(G, target=end)

target_distance = from_start[end] - 100

walls = input == "#"
part1 = 0
for a in np.argwhere(walls):
    for cheat in combinations(directions, 2):
        b = tuple(a + cheat[0])
        c = tuple(a + cheat[1])
        for e1, e2 in [(b, c), (c, b)]:
            if e1 in from_start and e2 in to_end:
                distance = from_start[e1] + to_end[e2] + 2
                if distance <= target_distance:
                    part1+=1

print(1, part1)

part2 = 0
for a in tqdm(G.nodes):
    from_a = from_start[a]
    if from_a > target_distance:
        continue
    for b in G.nodes:
        distance_cheat = np.abs(a[0]-b[0]) + np.abs(a[1]-b[1])
        if distance_cheat > 20:
            continue
        distance = from_a + to_end[b] + distance_cheat
        if distance <= target_distance:
            part2+=1

print(2, part2)