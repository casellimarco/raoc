import os
from csv import reader
import numpy as np
import networkx as nx

def get_dir():
    return os.path.dirname(os.path.realpath(__file__))

def read(filename, dir_path):
    with open(os.path.join(dir_path, f'{filename}.txt'), 'r') as file:
        return [row[0] for row in reader(file)]

def to_numpy_array(ls):
    return np.array([[int(x) for x in line] for line in ls])

def generate_vertices(n):
    vertices = []
    for i in range(n):
        for j in range(n):
            vertices.append((i,j))
    return vertices

def generate_edges(n, vertices):
    edges = []
    for i,j in vertices:
        if i<n-1:
            edges.append([(i,j),(i+1,j)])
        if i>0:
            edges.append([(i,j),(i-1,j)])
        if j<n-1:
            edges.append([(i,j),(i,j+1)])
        if j>0:
            edges.append([(i,j),(i,j-1)])
    return edges

def add_weights(edges, node_weights):
    for e in edges:
        # e[1] is the target vertex (i,j) of the edge that starts in e[0]
        # and the cost of going from e[0] to e[1] is the weight of (i,j)
        i = e[1][0]
        j = e[1][1]
        e.append(node_weights[i][j])
    return edges

def generate_weighted_edges(n, node_weights):
    vertices = generate_vertices(n)
    edges = generate_edges(n, vertices)
    return add_weights(edges, node_weights)

def interesting_bits(length, path, node_weights, n):
    node_weights_used = []
    visual_path = np.array([['.']*n]*n)
    for v in path:
        node_weights_used.append(node_weights[v[0]][v[1]])
        visual_path[v[0]][v[1]] = 'X'
    print(node_weights_used)
    print(visual_path)

def problem1(node_weights, n):
    edge_list = generate_weighted_edges(n, node_weights)
    G = nx.DiGraph()
    G.add_weighted_edges_from(edge_list)
    length, path = nx.bidirectional_dijkstra(G, (0,0), (n-1,n-1))
    interesting_bits(length, path, node_weights, n)
    return length

dir_path = get_dir()
for input_file in ['input2']:
    node_weights_ls = read(input_file, dir_path)

    node_weights = to_numpy_array(node_weights_ls)
    n = node_weights.shape[0] # it's a square, so both dimensions are the same
    result = problem1(node_weights, n)