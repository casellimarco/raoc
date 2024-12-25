from aocd import data
import numpy as np

locks = []
keys = []
for m in data.split("\n\n"):
    matrix = np.array([list(l) for l in m.splitlines()]) == "#"
    if matrix[0].mean() == 1:
        locks.append(matrix.sum(axis=0))
    else:
        keys.append(matrix.sum(axis=0))

max_value = matrix.shape[0]

part1 = 0
for lock in locks:
    for key in keys:
        if np.all(lock + key <= max_value):
            part1 += 1

print(1, part1)