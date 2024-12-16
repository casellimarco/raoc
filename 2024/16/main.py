from aocd import data
import networkx as nx
import numpy as np


input = np.array([list(row) for row in data.split()])
map = input != "#"

directions = {
    "E": (0, 1),
    "N": (-1, 0),
    "W": (0, -1),
    "S": (1, 0),
}
directions = {k: np.array(v) for k, v in directions.items()}
turns = {
    "E": ["N", "S"],
    "N": ["W", "E"],
    "W": ["S", "N"],
    "S": ["E", "W"],
}

G = nx.Graph()
for a in np.argwhere(map): 
    for k, dir in directions.items():
        b = a + dir
        if np.any(b < 0) or np.any(b >= input.shape):
            continue
        if map[tuple(b)]:
            G.add_edge((k,tuple(a)), (k,tuple(b)), weight=1)
        for turn in turns[k]:
            G.add_edge((k,tuple(a)), (turn,tuple(a)), weight=1000)

start = ("E", tuple(np.argwhere(input == "S")[0]))
end_tile = tuple(np.argwhere(input == "E")[0])
end = ("0", end_tile)
for dir in directions.keys():
    G.add_edge((dir, end_tile), end, weight=0)

from_start = nx.shortest_path_length(G, source=start, weight="weight")
length = from_start[end]
print(1, length)

to_end = nx.shortest_path_length(G, target=end, weight="weight")

all_tiles = set()
for tile, distance in from_start.items():
    if distance + to_end[tile] == length:
        all_tiles.add(tile[1])
        
print(2, len(all_tiles))
