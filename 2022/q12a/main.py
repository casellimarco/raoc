import numpy as np

river = []
with open("2022/q12a/input.txt") as f:
    for l in f:
        river.append(list(map(ord, l.strip())))

a = np.array(river) 
start = np.where(a == ord("S"))
end = np.where(a == ord("E"))
a[start] = ord("a")
a[end] = ord("z")
a -= ord("a")
import networkx as nx
G = nx.DiGraph()

def get_nn(index):
    nn = []
    for d in [[0,1], [1,0], [0,-1],[-1,0]]:
        nn_index = (index[0]+d[0], index[1]+d[1])
        if not(0 <= nn_index[0] < a.shape[0] and 0 <= nn_index[1] < a.shape[1]):
            continue
        
        if a[index] + 1 >= a[nn_index]:
            nn.append((index, nn_index))
    return nn

for index in np.ndindex(a.shape):
    G.add_node(index, signal=a[index]) 
    nn = get_nn(index)
    if nn:
        G.add_edges_from(nn)

start = (start[0][0], start[1][0])
end = (end[0][0], end[1][0])
print(nx.shortest_path_length(G, source=start, target=end))
nx.shortest_path(G, source=start, target=end)


def knbrs(G, start):
    nbrs = set([start])
    k = 0
    while  0 not in set(a[e] for e in nbrs): 
        nbrs = set((nbr for n in nbrs for nbr in G[n]))
        k += 1
    return k

print(knbrs(G.reverse(), end))