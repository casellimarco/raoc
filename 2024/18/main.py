from aocd import data
import networkx as nx
import numpy as np


input = np.array([list(map(int,row.split(","))) for row in data.splitlines()])

directions = [
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 0),
]
directions = [np.array(v) for v in directions]

def create_graph_at_t(t):
    G = nx.Graph()
    map = np.ones((71,71), dtype=bool)

    for input_value in input[:t]:
        map[tuple(input_value)] = False

    for a in np.argwhere(map): 
        for dir in directions:
            b = a + dir
            if np.any(b < 0) or np.any(b >= map.shape):
                continue
            if map[tuple(b)]:
                G.add_edge(tuple(a), tuple(b))
    return G

G = create_graph_at_t(1024)
start = (0,0)
end = (70,70)
length = nx.shortest_path_length(G, start, end)
print(1, length)


def find_first_zero(func, min, max):
    while max != min + 1:
        mid = (min + max) // 2
        if func(mid) == 0:
            max = mid
        else:
            min = mid
    return max

def check(t):
    G = create_graph_at_t(t)
    return nx.has_path(G, start, end)

t = find_first_zero(check, 0, len(input)+1)

print(2, ",".join(map(str,input[t-1])))