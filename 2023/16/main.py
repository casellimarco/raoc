data=r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
from aocd import data
import sys
sys.setrecursionlimit(100000)

def move(position, direction):
    y, x = position
    match direction:
        case 0:
            return (y, x+1)
        case 1:
            return (y+1, x)
        case 2:
            return (y, x-1)
        case 3:
            return (y-1, x)

import numpy as np
m = np.array([[c for c in d] for d in data.splitlines()])

def check(position):
    return 0 <= position[0] < m.shape[0] and 0 <= position[1] < m.shape[1]

def new_direction(position, direction):
    match m[position]:
        case ".":
            pass # do nothing
        case "/":
            match direction:
                case 0:
                    direction = 3
                case 1:
                    direction = 2
                case 2:
                    direction = 1
                case 3:
                    direction = 0
        case "\\":
            match direction:
                case 0:
                    direction = 1
                case 1:
                    direction = 0
                case 2:
                    direction = 3
                case 3:
                    direction = 2
        case "|":
            match direction:
                case 1 | 3:
                    pass # do nothing
                case _:
                    return [1, 3]
        case "-":
            match direction:
                case 0 | 2:
                    pass # do nothing
                case 1 | 3:
                    return [0, 2]
    return [direction]

def one_step(position, direction, energized):
    # print(position, direction, m[position])
    position = move(position, direction)
    if not check(position):
        return
    if (position, direction) in energized:
        return
    energized.add((position, direction))
    for d in new_direction(position, direction):
        one_step(position, d, energized)

def solve(position, direction):
    energized = {(position,direction)}
    for d in new_direction(position, direction):
        one_step(position, d, energized)
    return len(set(p[0] for p in energized))


position = (0,0)
direction = 0
print(1, solve(position, direction))


# part 2

energies = []
for i in range(m.shape[0]):
    energies.append(solve((i,0), 0))
    energies.append(solve((i,m.shape[1]-1), 2))
for i in range(m.shape[1]):
    energies.append(solve((0,i), 1))
    energies.append(solve((m.shape[0]-1,i), 3))

print(2, max(energies))