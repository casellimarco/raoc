data="""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
from aocd import data
import networkx as nx
import numpy as np


from collections import defaultdict
import heapq as heap


def is_too_straight(node, adjNode, parentsMap, straight_maximum, visited):
    maybe_line = [node, adjNode]
    previous_node = node
    for _ in range(straight_maximum-1):
        if previous_node not in parentsMap:
            return False
        previous_node = parentsMap[previous_node]
        maybe_line.append(previous_node)
    maybe_line_visited = set(n for n in maybe_line) & visited
    if len(maybe_line_visited) < straight_maximum:
        return False
    for i in range(2):
    	if len(set([n[i] for n in maybe_line])) == 1:
            return True
    return False


def get_cost_other_direction(parent, costs, step):
    steps = [step, (-step[0], -step[1])]
    return min([float("inf")]+[v for k, v in costs[parent].items() if not k[:2] in steps])


def line_length(node, next_node, parentsMap, straight_maximum, costs, G):
    step = next_node[0] - node[0], next_node[1] - node[1]
    lines = {}
    additional_cost = G[node][next_node]["weight"]
    lines[step + (1,)] = (get_cost_other_direction(node, costs, step) + additional_cost, node)
    maybe_parents = parentsMap.get(node, None)
    if maybe_parents:
        for i in range(1,straight_maximum):
            key = step + (i,) 
            next_key = step + (i+1,) 
            maybe_parent = maybe_parents.get(key, None)
            if maybe_parent:
                x, y = maybe_parent
                xs, ys = step
                additional_cost = 0
                for j in range(1, i+2):
                    additional_cost += G[x + (j-1)*xs, y+(j-1)*ys][x + j*xs, y+j*ys]["weight"]
                assert x + (j-1)*xs == node[0] and y+(j-1)*ys == node[1]
                assert x + j*xs == next_node[0] and y+j*ys == next_node[1]
                lines[next_key] = (get_cost_other_direction(maybe_parent, costs, step) + additional_cost, maybe_parent)
    return lines

def dijkstra_no_straight_2(G, startingNode, straight_maximum):
    from collections import Counter
    visited = Counter()
    parentsMap = defaultdict(dict)
    pq = []
    nodeCosts = defaultdict(lambda: defaultdict(lambda: float('inf')))
    nodeCosts[startingNode] = {
        (0,1,1): 0, (1,0,1): 0, (-1,0,1): 0, (0,-1,1): 0,
        (0,1,2): 0, (1,0,2): 0, (-1,0,2): 0, (0,-1,2): 0,
        (0,1,3): 0, (1,0,3): 0, (-1,0,3): 0, (0,-1,3): 0}
    heap.heappush(pq, (0, startingNode))

    while pq:
		# go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited[node] += 1

        for adjNode, weight in G[node].items():
            if visited[adjNode] > straight_maximum*4:
                continue
            lines = line_length(node, adjNode, parentsMap, straight_maximum, nodeCosts, G)
            for line_key, (value, parent) in lines.items():
                nodeCosts[adjNode][line_key]
                if nodeCosts[adjNode][line_key] > value:
                    parentsMap[adjNode][line_key] = parent 
                    nodeCosts[adjNode][line_key] = value
                    heap.heappush(pq, (value, adjNode))
        
    return parentsMap, nodeCosts
            

def dijkstra_no_straight(G, startingNode, straight_maximum):
    visited = set()
    parentsMap = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[startingNode] = 0
    heap.heappush(pq, (0, startingNode))

    while pq:
		# go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for adjNode, weight in G[node].items():
            if adjNode in visited:
                continue
            if is_too_straight(node, adjNode, parentsMap, straight_maximum, visited):
                continue
                
            newCost = nodeCosts[node] + weight["weight"]
            if nodeCosts[adjNode] > newCost:
                parentsMap[adjNode] = node
                nodeCosts[adjNode] = newCost
                heap.heappush(pq, (newCost, adjNode))
        
    return parentsMap, nodeCosts

assert is_too_straight((0,0), (0,1), {}, 1, set([(0,0)]))
assert is_too_straight((0,2), (0,3), {(0,2):(0,1), (0,1):(0,0)}, 3, set([(0,0), (0,1), (0,2)]))

lines = data.splitlines()
max_i = len(lines)
max_j = len(lines[0])
m = np.array([[int(c) for c in d] for d in data.splitlines()])


def check(position):
    i, j = position
    return 0 <= i < max_i and 0 <= j < max_j

def get_neighbours(position):
    y, x = position
    n = [(y, x+1), (y+1, x), (y, x-1), (y-1, x)]
    return [pos for pos in n if check(pos)]

G = nx.DiGraph()

for position in np.ndindex(m.shape):
    cost = m[position]
    neighbours = get_neighbours(position)
    for n in neighbours:
        G.add_edge(n, position, weight=cost)

parentsMap, nodeCosts = dijkstra_no_straight(G, (0, 0), 3)
end = (max_i-1, max_j-1)
print(nodeCosts[end])


# def get_path(node):
#     path = [node]
#     while path[-1] != (0,0):
#         path.append(parentsMap[path[-1]])
#     return path[::-1] 

# G[(0,0)].items()
# nodeCosts[(0,3)]
# nodeCosts[(1,0)]

# node = (0,3)
# assert get_path(node) == [(0,0), (1,0), (1,1), (1,2), (0,2), (0, 3)], get_path(node)
# assert nodeCosts[node] == 10, nodeCosts[node]

# node = (1,1)
# assert get_path(node) == [(0,0), (1,0), (1,1)], get_path(node)
# assert nodeCosts[node] == 5, nodeCosts[node]

parentsMap, nodeCosts = dijkstra_no_straight_2(G, (0, 0), 3)

def print_score(node):
    print(node)
    print(nodeCosts[node])
    print(get_cost_other_direction(node, nodeCosts, (100,100)))


def get_previous(node, parentsMap, nodeCosts, previous_best_step):
    best_score = get_cost_other_direction(node, nodeCosts, previous_best_step[:2])
    best_step = [k for k, v in nodeCosts[node].items() if v == best_score and k[:2] != previous_best_step[:2]][0]
    return parentsMap[node][best_step], best_step,
    
def get_path(node, parentsMap, nodeCosts):
    path = [node]
    previous_best_step = (100,100)
    score = 0
    while path[-1] != (0,0):
        new_node, previous_best_step = get_previous(path[-1], parentsMap, nodeCosts, previous_best_step)
        path.append(new_node)
    return path[::-1] 

end = (max_i-1, max_j-1)
print_score(end)
print(get_path(end, parentsMap, nodeCosts))
print_score((0,4))
print_score((4,0))
print_score((5,0))
print_score((6,0))