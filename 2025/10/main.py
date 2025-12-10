from aocd import data
import numpy as np
from itertools import combinations, product
from sympy import Matrix, linsolve, symbols, Integer
from tqdm import tqdm


def parse(l):
    lights, r = l[1:].split("] ")
    lights = np.array(list(lights)) == "#"
    wires, j = r[:-1].split(" {")
    wires = list(map(eval, wires.split()))
    wires = [list(wire) if type(wire) == tuple else [wire] for wire in wires]
    j = eval("["+j+"]")
    return lights, wires, j


def create_matrix(ligths, wires):
    w = np.array([np.zeros_like(lights)]*len(wires))
    for i, wire in enumerate(wires):
        w[i][wire] = True
    return w

def solve1(lights, wires):
    w = create_matrix(lights, wires)
    n = range(len(wires)) 
    for bits in n:
        for c in combinations(n, bits):
            if np.all(np.logical_xor.reduce(w[list(c)], axis=0) == lights):
                return bits

def solve2(lights, wires, j):
    w = create_matrix(lights, wires)
    m = Matrix(w.astype(int))
    b = Matrix(j)
    s = symbols(f'x0:{len(wires)}', integer=True, nonnegative=True)
    a = linsolve((m.T,b), s)
    b = min(sum(i) for i in a)
    min_value = np.inf
    syms = a.free_symbols
    if not syms:
        return b
    indices = [int(str(x)[1:]) for x in syms]
    j = np.array(j)
    ranges = [range(min(j[wires[i]])+1) for i in indices]
    for values in product(*ranges):
        r = dict(zip(syms, values))
        candidate_min = b.xreplace(r)
        if candidate_min < 0 or candidate_min > min_value or not candidate_min.is_integer:
            continue
        presses = np.array([i for i in a.xreplace(r)][0])
        if np.all(presses >=0) and all(p.is_integer for p in presses):
            min_value = candidate_min
    return min_value
        

    
part1=0
part2=0
for d in tqdm(data.splitlines()):
    lights, wires, j = parse(d)
    part1+=solve1(lights, wires)
    part2+=solve2(lights, wires, j)

print(part1)
print(part2)
    

