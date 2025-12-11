from aocd import data
import networkx as nx

def n_paths(original_G, source, target):
    """ Adapted from nx.algorithms.simple_paths._all_simple_edge_paths """
    G = original_G.copy()
    for node in original_G.nodes:
        if not(nx.has_path(original_G, source, node) and nx.has_path(original_G, node, target)):
            G.remove_node(node)
    
    cutoff = len(G) - 1
    target = {target}
    # We simulate recursion with a stack, keeping the current path being explored
    # and the outgoing edge iterators at each point in the stack.
    # To avoid unnecessary checks, the loop is structured in a way such that a path
    # is considered for yielding only after a new node/edge is added.
    # We bootstrap the search by adding a dummy iterator to the stack that only yields
    # a dummy edge to source (so that the trivial path has a chance of being included).

    get_edges = (
        (lambda node: G.edges(node, keys=True))
        if G.is_multigraph()
        else (lambda node: G.edges(node))
    )
    tot = 0
    # The current_path is a dictionary that maps nodes in the path to the edge that was
    # used to enter that node (instead of a list of edges) because we want both a fast
    # membership test for nodes in the path and the preservation of insertion order.
    current_path = {None: None}
    stack = [iter([(None, source)])]

    while stack:
        # 1. Try to extend the current path.
        next_edge = next((e for e in stack[-1] if e[1] not in current_path), None)
        if next_edge is None:
            # All edges of the last node in the current path have been explored.
            stack.pop()
            current_path.popitem()
            continue
        _, next_node, *_ = next_edge

        # 2. Check if we've reached a target.
        if next_node in target:
            tot +=1

        # 3. Only expand the search through the next node if it makes sense.
        if len(current_path) - 1 < cutoff and (
            target - current_path.keys() - {next_node}
        ):
            current_path[next_node] = next_edge
            stack.append(iter(get_edges(next_node)))
    
    return tot

g = nx.DiGraph()

for d in data.splitlines():
    s, *es = d.split()
    g.add_edges_from([(s[:-1], e) for e in es])

print(len(list(nx.all_simple_paths(g, "you", "out"))))

assert not nx.has_path(g, "dac", "fft")
p1 = n_paths(g, "svr", "fft")
p2 = n_paths(g, "fft", "dac")
p3 = n_paths(g, "dac", "out")
print(p1*p2*p3)
