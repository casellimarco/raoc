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
energized = {((0,0),0)}

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

def one_step(position, direction):
    # print(position, direction, m[position])
    position = move(position, direction)
    if not check(position):
        return
    if (position, direction) in energized:
        return
    energized.add((position, direction))
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
                    for d in [1, 3]: 
                        one_step(position, d)
                    return
        case "-":
            match direction:
                case 0 | 2:
                    pass # do nothing
                case _:
                    for d in [0, 2]: 
                        one_step(position, d)
                    return

    one_step(position, direction)

# first character is \, so it changes the direction
one_step((0,0), 1)
print(1, len(set(p[0] for p in energized)))
