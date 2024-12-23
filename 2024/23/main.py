from aocd import data
import networkx as nx

G = nx.Graph()
for line in data.splitlines():
    a, b = line.split("-")
    G.add_edge(a, b)

part1 = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique) < 3:
        continue
    if len(clique) == 4:
        break
    part1 += any(node.startswith("t") for node in clique)
print(1, part1)

max_clique, _ = nx.max_weight_clique(G, weight=None)
max_clique.sort()
print(2, ",".join(max_clique))
