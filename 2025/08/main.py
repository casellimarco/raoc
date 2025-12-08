from aocd import data
import numpy as np
import networkx as nx


a = np.array([list(map(int,d.split(','))) for d in data.splitlines()])

d = []
for i, p in enumerate(a):
    for j, q in enumerate(a):
        if j <= i:
            continue
        d.append((np.linalg.norm(p-q), i, j))

d.sort(key= lambda x: x[0])

g = nx.Graph()

for _, i, j in d[:1000]:
    g.add_edge(i,j)

s = [len(c) for c in nx.connected_components(g)]
s.sort(reverse=True)

print(np.prod(s[:3]))

e = 1000
while len(g) != len(a) or nx.number_connected_components(g) != 1:
    _, i, j = d[e]
    g.add_edge(i,j)
    e+=1

print(a[i][0]*a[j][0])
