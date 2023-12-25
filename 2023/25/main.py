from aocd import data
import networkx as nx
from tqdm import tqdm

G = nx.Graph()
for line in data.splitlines():
    parent, children = line.split(":")
    children = children.split()
    G.add_edges_from([(parent, child) for child in children])

target_edges = []
N = G.copy()
for edge in tqdm(G.edges):
    N.remove_edge(*edge)
    if nx.edge_connectivity(N, *edge) == 2:
        target_edges.append(edge)
    N.add_edge(*edge)

N = G.copy()
N.remove_edges_from(target_edges)

a, b = nx.connected_components(N)
print(1, len(a)*len(b))