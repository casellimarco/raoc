from aocd import data
import numpy as np

parts = [0, 0]

elements = data.split("\n\n")
for element in elements:
    lines = element.split("\n")
    buttons = [[int(h.split("+")[1]) for h in l.split(", ")] for l in lines[:2]]
    prize = np.array([int(l.split("=")[1]) for l in lines[2].split(", ")])
    matrix = np.matrix(buttons).T
    inv = np.linalg.inv(matrix)
    for i, p in enumerate([prize, prize + 10000000000000]):
        tentative = inv@p
        if i == 0 and np.any(tentative > 100):
            continue
        if not np.allclose(np.round(tentative), tentative, rtol=1e-13):
            continue
        value = (tentative@[3,1]).item()
        parts[i] += int(np.round(value))

print(1, parts[0])
print(2, parts[1])
