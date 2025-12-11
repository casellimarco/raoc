from aocd import data
import networkx as nx

g = nx.DiGraph()

for d in data.splitlines():
    s, *es = d.split()
    g.add_edges_from([(s[:-1], e) for e in es])

print(len(list(nx.all_simple_paths(g, "you", "out"))))

ps = nx.all_simple_paths(g, "svr", "dac")
s2d = 0
s2f2d = 0
for p in ps:
    if "out" in p:
        continue
    s2d += 1
    if "fft" in p:
        s2f2d += 1

print(s2d, s2f2d)
