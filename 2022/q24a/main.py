import numpy as np
import networkx as nx

input = []
with open("input.txt", "r") as f:
    for line in f:
        input.append([c for c in line.strip()]) 

input = np.array(input)

trimmed_input = input[1:-1,1:-1]
right = trimmed_input == ">"
left = trimmed_input == "<"
up = trimmed_input == "^"
down = trimmed_input == "v"

free = ~(right | left | up | down)

special =(-1,0)
special_end = (free.shape[0], free.shape[1]-1)
specials = {special, special_end}
heads = {special}

def get_neighbors(pos, free):
    neighbors = {pos,
                 (pos[0]+1, pos[1]),
                 (pos[0]-1, pos[1]),
                 (pos[0], pos[1]+1),
                 (pos[0], pos[1]-1),
                 }
    for n in neighbors.copy():
        if n in specials:
            continue
        if 0<=n[0]<free.shape[0] and 0<=n[1]<free.shape[1]:
            if free[n]:
                continue
        neighbors.remove(n)
    return neighbors

def update(left, right, up, down):
    left = np.roll(left,-1,axis=1)
    right = np.roll(right,1,axis=1)
    up = np.roll(up,-1,axis=0)
    down = np.roll(down,1,axis=0)
    free = ~(right | left | up | down)
    return left, right, up, down, free

turns = 0
for i, target in enumerate([special_end, special, special_end]):
    while True:
        left, right, up, down, free = update(left, right, up, down)
        new_heads = set()
        for pos in heads:
            new_heads.update(get_neighbors(pos, free))
        heads = new_heads
        turns += 1
        if target in heads:
            if i == 0:
                print(turns) # part A
            heads = {target}
            break

print(turns)