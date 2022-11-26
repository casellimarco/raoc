from collections import defaultdict
from copy import copy

graph = defaultdict(list)
with open('input.txt', 'r') as f:
    data = [line.strip().split("-") for line in f.readlines()]

for d in data:
    graph[d[0]].append(d[1])
    graph[d[1]].append(d[0])

def append_node(path, node, graph):
    new_path = copy(path)
    new_path.append(node)
    if node == "end":
        return [new_path]
    elif node.isupper() or not node in path:
        paths = []
        for next_node in graph[node]:
            paths.extend(append_node(new_path, next_node, graph))
        return paths
    else:
        return []
        


def get_all_graphs():
    paths = []
    for node in graph["start"]:
        paths.extend([path for path in append_node(["start"], node, graph) if path])
    len_paths = len(paths)
    for small, connections in graph.items():
        if not small.isupper() and not small in ["start", "end"]:
            modified_graph = copy(graph)
            new_small = "new"+small
            modified_graph[new_small] = connections
            for node, node_c in graph.items():
                if small in node_c:
                    modified_graph[node].append(new_small)
            for node in graph["start"]:
                new_paths = [path for path in append_node(["start"], node, modified_graph) if small in path and new_small in path]
                len_paths += len(new_paths) / 2
    return len_paths


p =get_all_graphs()
print(p)
