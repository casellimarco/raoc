import numpy as np
from collections import Counter
from bidict import bidict   

scanners = []

with open("input.txt") as f:
    for line in f:
        if line.startswith("--"):
            new_scanner = []
        elif line == "\n":
            scanners.append(np.array(new_scanner, dtype=int))
        else:
            new_scanner.append(line.strip().split(","))

scanners.append(np.array(new_scanner, dtype=int))

distances = []
distances_counters = []
for s in scanners:
    L1 = np.sum(np.abs(s[:, np.newaxis, :] - s), axis=2)
    d = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            d[i,j] = L1[i, j]
    distances.append(d)
    distances_counters.append(Counter(d.values()))

maybe_connections = {}
for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        intersection = distances_counters[i] & distances_counters[j]
        tot = sum(intersection.values())
        if tot>=66:
            maybe_connections[i,j] = intersection
connection = {}
for pair, intersection in maybe_connections.items():
    connection[pair] = {}
    for i in pair:
        connection[pair][i] = bidict()
        edges = Counter()
        for edge, distance in distances[i].items():
            if distance in intersection:
                edges[edge[0]] += 1
                edges[edge[1]] += 1
        complete = [v for v, c in edges.most_common(12) if c >= 11]
        if len(complete) < 12:
            connection.pop[pair]
            continue
        complete.sort()
        for index, e1 in enumerate(complete):
            distance_from_e1 = []
            for e2 in complete[:index]:
                distance_from_e1.append(distances[i][e2,e1])
            for e2 in complete[index+1:]:
                distance_from_e1.append(distances[i][e1,e2])
            distance_from_e1.sort()
            connection[pair][i][e1] = tuple(distance_from_e1)

mapping = {}
for pair, d in connection.items():
    mapping[pair] = {}
    for e0, d0 in d[pair[0]].items():
        mapping[pair][e0] = d[pair[1]].inverse[d0]

vectors = {}
for pair, map in mapping.items():
    first = []
    second = []
    for f,t in map.items():
        first.append(scanners[pair[0]][f])
        second.append(scanners[pair[1]][t])
    vectors[pair] = np.array(first), np.array(second)

unique_entries = {tuple(e) for e in scanners[0]}
betas = {}
for pair, matrices in vectors.items(): 
    X, Y = matrices
    X_p = np.hstack((np.ones((len(X),1)),X))
    beta = np.round(np.linalg.inv(X_p.T@X_p)@X_p.T@Y).astype(int)
    betas[pair] = beta 
    X, Y = Y, X
    X_p = np.hstack((np.ones((len(X),1)),X))
    beta = np.round(np.linalg.inv(X_p.T@X_p)@X_p.T@Y).astype(int)
    betas[pair[1], pair[0]] = beta 


import networkx as nx
G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_edges_from(vectors.keys())  # add edges from iterable container
for end in range(1,len(scanners)):
    path = nx.shortest_path(G, end, 0)
    points = scanners[end]
    for i, f in enumerate(path):
        if i + 1 < len(path):
            points = np.hstack((np.ones((len(points),1)),points))
            t = path[i+1]
            points = points@betas[f,t]
    unique_entries = unique_entries.union({tuple(e) for e in points})

print(len(unique_entries))

scanners_coords = [[0,0,0]]
for end in range(1,len(scanners)):
    path = nx.shortest_path(G, end, 0)
    points = np.array([[0,0,0]])
    for i, f in enumerate(path):
        if i + 1 < len(path):
            points = np.hstack((np.ones((len(points),1)),points))
            t = path[i+1]
            points = points@betas[f,t]
    scanners_coords.append(points.tolist()[0])

s = np.array(scanners_coords)
L1 = int(np.max(np.sum(np.abs(s[:, np.newaxis, :] - s), axis=2)))
print(L1)