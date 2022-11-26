import numpy as np
import networkx as nx

with open('input.txt') as f:
    inp = np.array([[int(l) for l in line.strip()] for line in f])

shape = (inp.shape[0]*5, inp.shape[1]*5)
G = nx.grid_2d_graph(*shape, create_using=nx.DiGraph())

def map_to_grid(i, j):
    q_x, r_x = divmod(i, inp.shape[0])
    q_y, r_y = divmod(j, inp.shape[1])
    return (inp[r_x,r_y] + q_x + q_y - 1)%9 + 1

for u, v in G.edges():
    G[u][v]['weight'] = map_to_grid(*v)

print(nx.shortest_path_length(G, (0,0), (shape[0]-1, shape[1]-1), weight='weight'))