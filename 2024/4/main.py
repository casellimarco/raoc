from aocd import data
import numpy as np


input = np.array([[ch for ch in row] for row in data.splitlines()])

inc = np.arange(4)
dec = np.arange(0, -4, -1)
null = np.zeros(4)

directions = [
    (inc, null), # Down
    (inc, inc), # Down Right
    (null, inc), # Right
    (dec, inc), # Up Right
    (dec, null), # Up
    (dec, dec), # Up Left
    (null, dec), # Left
    (inc, dec) # Down Left
]

match = np.array(["X", "M", "A", "S"]) 


def get_index(start, dir):
    index = start+dir
    if np.any(index < 0):
        raise IndexError
    return index.astype(int).tolist() 


part1 = 0
for starting in np.argwhere(input == "X"):
    for direction in directions:
        try:
            value = input[get_index(starting[0], direction[0]), get_index(starting[1], direction[1])]
        except IndexError:
            continue
        part1 += np.all(value == match)
        
print(1, part1)

# Part 2

direction = np.array([-1, 1, 0, -1, 1]), np.array([-1, -1, 0, 1, 1])

matches = [
    np.array(["M", "M", "A", "S", "S"]),
    np.array(["S", "S", "A", "M", "M"]),
    np.array(["M", "S", "A", "M", "S"]),
    np.array(["S", "M", "A", "S", "M"]),
] 

part2 = 0
for starting in np.argwhere(input == "A"):
    try:
        value = input[get_index(starting[0], direction[0]), get_index(starting[1], direction[1])]
    except IndexError:
        continue
    part2 += any([np.all(value == match) for match in matches])
        
print(2, part2)