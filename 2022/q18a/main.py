from dataclasses import dataclass
from typing import List
import numpy as np

cubes = set()
max_x = 0
max_y = 0
max_z = 0
with open("input.txt", "r") as f:
    for line in f:
        cube = tuple(map(int, line.strip().split(',')))
        cubes.add(cube)
        max_x = max(cube[0], max_x)
        max_y = max(cube[1], max_y)
        max_z = max(cube[2], max_z)

# Avoid edges
labels = np.zeros((max_x+3, max_y+3, max_z+3))
sides = 0
for c in cubes:
    # Shift by 1 to not have anything touching edges
    labels[(c[0]+1, c[1]+1, c[2]+1)] = 1
    for d in [
        [0,0,1],
        [0,0,-1],
        [0,1,0],
        [0,-1,0],
        [1,0,0],
        [-1,0,0],
        ]:
        next_cube = (c[0]+d[0], c[1]+d[1], c[2]+d[2])
        sides += next_cube not in cubes

print(sides)

import cc3d
connectivity = 6 
labels_out = cc3d.connected_components(1-labels, connectivity=connectivity)

filled_cubes = set()

for cube, label in np.ndenumerate(labels_out):
    if label != 1:
        filled_cubes.add(cube)

filled_sides = 0
for c in filled_cubes:
    for d in [
        [0,0,1],
        [0,0,-1],
        [0,1,0],
        [0,-1,0],
        [1,0,0],
        [-1,0,0],
        ]:
        next_cube = (c[0]+d[0], c[1]+d[1], c[2]+d[2])
        filled_sides += next_cube not in filled_cubes

print(filled_sides)
