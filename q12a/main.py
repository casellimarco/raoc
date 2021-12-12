from collections import defaultdict
from copy import copy

graph = defaultdict(list)
with open('input.txt', 'r') as f:
    data = [line.strip().split("-") for line in f.readlines()]

for d in data:
    graph[d[0]].append(d[1])
    graph[d[1]].append(d[0])

def append_node(path, node):
    new_path = copy(path)
    new_path.append(node)
    if node == "end":
        return [new_path]
    elif node.isupper() or not node in path:
        paths = []
        for next_node in graph[node]:
            paths.extend(append_node(new_path, next_node))
        return paths
    else:
        return []
        


def get_all_graphs():
    paths = []
    for node in graph["start"]:
        paths.extend([path for path in append_node(["start"], node) if path])
    return paths

print(len(get_all_graphs()))