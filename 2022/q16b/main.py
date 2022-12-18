import networkx as nx
import re
# import matplotlib.pyplot as plt
from functools import lru_cache

def simplify(G):
    simple_G = G.copy()
    for node, att in G.nodes(data=True):
        if node == "AA":
            continue
        if att["rate"] == 0:
            neighbors = list(simple_G[node])
            for i, n1 in enumerate(neighbors):
                weight = simple_G[n1][node]["weight"]
                for n2 in neighbors[i+1:]:
                    weight += simple_G[n2][node]["weight"]
                    if simple_G.has_edge(n1, n2):
                        old_weight = simple_G[n1][n2]["weight"]
                        weight = min(weight, old_weight)
                    simple_G.add_edge(n1, n2, weight=weight)
                simple_G.remove_edge(n1, node)
            simple_G.remove_node(node)
    return simple_G

def plot_graph(G):
    pos = nx.spring_layout(G)                                                    
    # node_labels = {k:f'{k}-{v["rate"]}' for k,v in G.nodes(data=True)}                                                        
    nx.draw(G, pos, labels=node_labels, with_labels=True)  
    nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
    plt.show()

@lru_cache(200)
def shortest_path(G, pos):
    return nx.shortest_path_length(G, pos, weight="weight")

def compute_value(G, path, turns_left, pos):
    values = {}
    if turns_left < 0:
        return values
    for node, length in shortest_path(G, pos).items():
        if node in path:
            continue
        value = G.nodes[node]["rate"] * (turns_left - length - 1)
        values[node] = (value, length+1)
    return values            

def get_next(G, path, t1, t2, p1, p2, score, path_history):
    new_scores_1 = compute_value(G, path, t1, p1)
    new_scores_2 = compute_value(G, path, t2, p2)
    paths = {path_history: score}
    visited = set()
    for node_1, values_1 in new_scores_1.items():
        new_t1 = t1 - values_1[1]
        visited.add((node_1, new_t1))
        for node_2, values_2 in new_scores_2.items():
            if node_1 == node_2 or (node_2, values_2) in visited:
                continue
            new_path = path
            new_score = score
            new_t2 = t2 - values_2[1]
            new_history = path_history
            if new_t1 >= 0:
                new_path += (node_1,)
                new_score += values_1[0]
                new_history += "1"+node_1
            if new_t2 >=0: 
                new_path += (node_2,)
                new_score += values_2[0]
                new_history += "2"+node_2
            if new_t2 >=0 or new_t1 >= 0:
                paths.update(get_next(G, new_path, new_t1, new_t2, node_1, node_2, new_score, new_history))
    
    return paths


G = nx.Graph()
with open("input.txt") as f:
    for line in f:
        valve_from = line.split(" ")[1]
        rate = int(line.split("rate=")[1].split(";")[0])
        valves_to = re.split("valves? ", line)[1].split(", ")
        G.add_node(valve_from, rate=rate)
        for to in valves_to:
            G.add_edge(valve_from, to.strip(), weight=1)

# plot_graph(G) 
simple_G = simplify(G)
# plot_graph(simple_G)

prova = get_next(simple_G, ("AA",), 26, 26, "AA", "AA", 0, "")
max_value = max(prova, key=prova.get)
print(max_value)
print(max(prova.values()))
# print(prova)