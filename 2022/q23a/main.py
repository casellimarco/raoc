import numpy as np
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Elf:
    x: int
    y: int
    old_x: int = None
    old_y: int = None

    def neighbors(self, dir):
        if dir == "N":
            return {(self.x-1, self.y-1), (self.x-1, self.y), (self.x-1, self.y+1)}, (self.x-1, self.y)
        if dir == "S":
            return {(self.x+1, self.y-1), (self.x+1, self.y), (self.x+1, self.y+1)}, (self.x+1, self.y)
        if dir == "E":
            return {(self.x+1, self.y+1), (self.x, self.y+1), (self.x-1, self.y+1)}, (self.x, self.y+1)
        if dir == "W":
            return {(self.x+1, self.y-1), (self.x, self.y-1), (self.x-1, self.y-1)}, (self.x, self.y-1)
        if dir == "A":
            return {
                (self.x+1, self.y-1), (self.x, self.y-1), (self.x-1, self.y-1),
                (self.x+1, self.y),                       (self.x-1, self.y),
                (self.x+1, self.y+1), (self.x, self.y+1), (self.x-1, self.y+1)
                }, (self.x, self.y)

    def move(self, elfs, turn):
        n, next_pos = self.neighbors("A")
        if not n.intersection(elfs.keys()):
            return next_pos, True
        dirs = "NSWE"
        for i in range(4):
            dir = dirs[(i+turn)%4]
            n, next_pos = self.neighbors(dir)
            if not n.intersection(elfs.keys()):
                self.old_x, self.old_y = self.x, self.y
                self.x, self.y = next_pos
                return next_pos, False
        return (self.x, self.y), True
        
    def go_back(self):
        self.x, self.y = self.old_x, self.old_y
        return self.x, self.y
    

        


input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append([c for c in line.strip()])
 
input = np.array(input)
coords = np.where(input == "#")

elfs = defaultdict(list)
for x,y in zip(*coords):
    elf = Elf(x,y)
    elfs[(x,y)].append(elf)

def pr(elfs):
    locs = np.array([[k[0], k[1]] for k in elfs.keys()])
    locs -= np.min(locs, axis=0)
    rows, cols = np.max(locs, axis=0)
    new_locs = set((r[0],r[1]) for r in locs)
    for row in range(rows+1):
        line = ""
        for col in range(cols+1):
            if (row, col) in new_locs:
                line+="#"
            else:
                line +="."
        print(line)

move = True
turn = 0
while move:
    #pr(elfs)
    new_elfs = defaultdict(list)
    are_stuck = True
    for elf in elfs.values():
        elf = elf[0]
        new_pos, stuck = elf.move(elfs, turn)
        are_stuck &= stuck
        new_elfs[new_pos].append(elf)
    elfs = new_elfs.copy()
    for pos, group in new_elfs.items():
        if len(group) > 1:
            elfs.pop(pos)
            for elf in group:
                old_pos = elf.go_back()
                elfs[old_pos].append(elf)
    turn+=1
    if turn == 10:          
        locs = np.array([[k[0], k[1]] for k in elfs.keys()])
        area = np.prod(np.max(locs, axis=0) - np.min(locs, axis=0) + np.array([1,1]))
        print(area - len(elfs))
    move = not are_stuck

print(turn)
#pr(elfs)


