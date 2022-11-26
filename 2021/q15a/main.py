import numpy as np
import networkx as nx

with open('input.txt') as f:
    inp = np.array([[int(l) for l in line.strip()] for line in f])

G = nx.grid_2d_graph(*inp.shape, create_using=nx.DiGraph())

for u, v in G.edges():
    G[u][v]['weight'] = inp[v]

print(nx.shortest_path_length(G, (0,0), (inp.shape[0]-1, inp.shape[1]-1), weight='weight'))