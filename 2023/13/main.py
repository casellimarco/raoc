from aocd import data
import numpy as np

def solve(matrix, target):
    return reflection_location(matrix, target)*100 + reflection_location(matrix.T, target)

def reflection_location(matrix, target):
    for candidate in np.arange(1, len(matrix)):
        reflection = min(candidate, len(matrix) - candidate)
        if np.sum(~(matrix[candidate-reflection:candidate] == matrix[candidate:candidate+reflection][::-1]))==target:
            return candidate
    return 0

matrices = data.split("\n\n")
tot_1 = 0
tot_2 = 0
for m in matrices:
    matrix = np.array([list(map(int, row.replace(".", "0").replace("#", "1"))) for row in m.splitlines()])
    tot_1 += solve(matrix, 0)
    tot_2 += solve(matrix, 1)

print(1, tot_1)
print(2, tot_2)