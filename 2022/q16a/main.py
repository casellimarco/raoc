import networkx as nx
import re
import matplotlib.pyplot as plt

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
    node_labels = {k:f'{k}-{v["rate"]}' for k,v in G.nodes(data=True)}                                                        
    nx.draw(G, pos, labels=node_labels, with_labels=True)  
    nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
    plt.show()


def compute_value(G, path, turns_left):
    values = {}
    for node, length in nx.shortest_path_length(G, path[-1], weight="weight").items():
        if node in path:
            continue
        value = G.nodes[node]["rate"] * (turns_left - length - 1)
        values[node] = (value, length+1)
    return values            

def get_next(G, path, turns_left, score):
    new_scores = compute_value(G, path, turns_left)
    paths = {path: score}
    for node, values in new_scores.items():
        new_t = turns_left - values[1]
        if new_t >= 0:
            new_path = path + (node,)
            new_score = score + values[0]
            paths.update(get_next(G, new_path, new_t, new_score))
    
    return paths


G = nx.Graph()
with open("input.txt") as f:
    for line in f:
        valve_from = line.split(" ")[1]
        rate = int(line.split("rate=")[1].split(";")[0])
        valves_to = re.split(f"valves? ", line)[1].split(", ")
        G.add_node(valve_from, rate=rate)
        for to in valves_to:
            G.add_edge(valve_from, to.strip(), weight=1)

# plot_graph(G) 
simple_G = simplify(G)
# plot_graph(simple_G)
prova = get_next(simple_G, ("AA",), 30, 0)
print(max(prova.values()))

# part 2
prova = get_next(simple_G, ("AA",), 26, 0)
prova = [(set(k[1:]),v) for k,v in prova.items()]
prova.sort(key= lambda x: x[1], reverse=True)

max_value = 0
for i, (p1, s1) in enumerate(prova):
    if max_value > s1*2:
        break
    for p2, s2 in prova[i+1:]:
        value = s1+s2
        if max_value < value:
            if p1.isdisjoint(p2):
                max_value = value

print(max_value)

