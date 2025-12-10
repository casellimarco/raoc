from aocd import data
import numpy as np
from itertools import combinations

def parse(l):
    lights, r = l[1:].split("] ")
    lights = np.array(list(lights)) == "#"
    wires, j = r[:-1].split(" {")
    wires = list(map(eval, wires.split()))
    j = eval("["+j+"]")
    return lights, wires, j

def solve1(lights, wires):
    w = np.array([np.zeros_like(lights)]*len(wires))
    for i, wire in enumerate(wires):
        v = list(wire) if type(wire) == tuple else [wire]
        w[i][v] = True

    n = range(len(wires)) 

    for bits in n:
        for c in combinations(n, bits):
            if np.all(np.logical_xor.reduce(w[list(c)], axis=0) == lights):
                return bits

    
part1=0
for d in data.splitlines():
    lights, wires, j = parse(d)
    part1+=solve1(lights, wires)

print(part1)
    

