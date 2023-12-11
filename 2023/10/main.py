from aocd import data
import networkx as nx

lines = data.splitlines()
G = nx.DiGraph()

def add_edges(from_node, c):
    from_node = (i, j)
    to_nodes = []
    N, S, E, W = (i-1, j), (i+1, j), (i, j+1), (i, j-1)
    match c:
        case "|":
            to_nodes.extend([N, S])
        case "-":
            to_nodes.extend([E, W])
        case "L":
            to_nodes.extend([N, E])
        case "J":
            to_nodes.extend([N, W])
        case "7":
            to_nodes.extend([S, W])
        case "F":
            to_nodes.extend([S, E])
    G.add_edges_from([(from_node, to_node) for to_node in to_nodes])

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        add_edges((i, j), c)
        if c == "S":
            start = (i, j)

h = nx.Graph()
for edge in G.edges(): 
    if edge[-1] == start or edge[::-1] in G.edges(): #check if reverse edge exist in graph
        h.add_edge(edge[0],edge[1])

def compute_1(cycle, start):
    length = nx.single_source_shortest_path_length(cycle,start)
    return  max(length.values())

for component in nx.connected_components(h):
    if start in component:
        cycle = h.subgraph(component).copy()
        print(1, compute_1(cycle, start))
        break


import numpy as np
enlarged = np.zeros((len(lines)*3, len(lines[0])*3))
full = np.ones((len(lines)*3, len(lines[0])*3)).astype(bool)

def convert(c):
    output = np.zeros((3, 3))
    output[1, 1] = 1
    match c:
        case "|":
            output[0, 1] = 1
            output[2, 1] = 1
        case "-":
            output[1, 0] = 1
            output[1, 2] = 1
        case "L"|"S": # Start S is a L
            output[0, 1] = 1
            output[1, 2] = 1
        case "J":
            output[0, 1] = 1
            output[1, 0] = 1
        case "7":
            output[1, 0] = 1
            output[2, 1] = 1
        case "F":
            output[1, 2] = 1
            output[2, 1] = 1
    return output
        

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if (i, j) in cycle:
            enlarged[3*i:3*(i+1), 3*j:3*(j+1)] = convert(c)
            full[3*i:3*(i+1), 3*j:3*(j+1)] = np.zeros((3, 3)).astype(bool)

string = " ■"
open("enlarged.txt", "w").write("\n".join(["".join([string[int(x)] for x in line]) for line in enlarged]) + "\n")

#visual inspection
inside = (99,32)

from skimage.segmentation import flood

flooded = flood(enlarged, inside)

really_inside = np.logical_and(flooded, full)
print(2, int(really_inside.sum()/9))