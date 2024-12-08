from aocd import data
import numpy as np
from itertools import combinations

def get_antinodes(input, frequency):
    antinodes = set()
    for a in np.argwhere(input == frequency):
        for b in np.argwhere(input == frequency):
            if np.all(a == b):
                continue
            antinode = 2*b - a
            if (antinode >= 0).all() and (antinode < input.shape).all():
                antinodes.add(tuple(antinode))
        
    return antinodes

def get_antinodes_part_2(input, frequency):
    antinodes = set()
    for a, b in combinations(np.argwhere(input == frequency), 2):
        step = b - a
        max_number_antinodes = int(max(input.shape)/max(step)) + 1
        for i in np.arange(-max_number_antinodes, max_number_antinodes):
            antinode = b + i*step
            if (antinode >= 0).all() and (antinode < input.shape).all():
                antinodes.add(tuple(antinode))
        
    return antinodes

input = np.array([[ch for ch in row] for row in data.splitlines()])

frequencies = np.unique(input).tolist()
frequencies.remove(".")

antinodes = set()
antinodes2 = set()
for frequency in frequencies:
    antinodes |= get_antinodes(input, frequency)
    antinodes2 |= get_antinodes_part_2(input, frequency)

print(1, len(antinodes))
print(2, len(antinodes2))