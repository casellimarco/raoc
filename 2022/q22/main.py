import re
from dataclasses import dataclass
from typing import Tuple
import numpy as np

size = 50

@dataclass
class Cube:
    faces: np.array
    direction: int = 0
    instructions: str = None
    current_location: Tuple[int, int, int] = (0, 0, 0)
    three_d = False

    def map_2d(self, point):
        z, y, x = point
        if z == 0:
            if y == -1:
                new_z = 4
            elif y == size:
                new_z = 2
            else:
                new_z = 1
        if z == 1:
            if x in [-1, size]:
                new_z = 0
            else:
                new_z = 1
        if z == 2:
            if y == -1:
                new_z = 0
            elif y == size:
                new_z = 4
            else:
                new_z = 2
        if z == 3:
            if y in [-1, size]:
                new_z = 5
            else:
                new_z = 4
        if z == 4:
            if y == -1:
                new_z = 2
            elif y == size:
                new_z = 0
            else:
                new_z = 3
        if z == 5:
            if x in [-1, size]:
                new_z = 5
            else:
                new_z = 3
            
        return new_z, y%size, x%size
    
    def map_3d(self, point):
        z, y, x = point
        new_direction = self.direction
        new_y = y%size
        new_x = x%size
        if z == 0:
            if y == -1:
                new_z = 5
                new_direction = 0
                new_y = new_x
                new_x = 0
            elif y == size:
                new_z = 2
            elif x == -1:
                new_z = 3
                new_direction = 0
                new_x = 0
                new_y = size - new_y - 1
            elif x == size:
                new_z = 1
        if z == 1:
            if y == -1:
                new_z = 5
            elif y == size:
                new_z = 2
                new_direction = 2
                new_y = new_x
                new_x = size - 1
            elif x == -1:
                new_z = 0
            elif x == size:
                new_z = 4
                new_direction = 2
                new_x = size - 1 
                new_y = size - new_y - 1
        if z == 2:
            if y == -1:
                new_z = 0
            elif y == size:
                new_z = 4
            elif x == -1:
                new_z = 3
                new_direction = 1
                new_x = new_y
                new_y = 0
            elif x == size:
                new_z = 1
                new_direction = 3
                new_x = new_y
                new_y = size - 1
        if z == 3:
            if y == -1:
                new_z = 2
                new_direction = 0
                new_y = new_x
                new_x = 0
            elif y == size:
                new_z = 5
            elif x == -1:
                new_z = 0
                new_direction = 0
                new_x = 0
                new_y = size - new_y - 1
            elif x == size:
                new_z = 4
        if z == 4:
            if y == -1:
                new_z = 2
            elif y == size:
                new_z = 5
                new_direction = 2
                new_y = new_x
                new_x = size - 1
            elif x == -1:
                new_z = 3
            elif x == size:
                new_z = 1
                new_direction = 2
                new_x = size - 1
                new_y = size - new_y - 1
        if z == 5:
            if y == -1:
                new_z = 3
            elif y == size:
                new_z = 1
            elif x == -1:
                new_z = 0
                new_direction = 1
                new_x = new_y
                new_y = 0
            elif x == size:
                new_z = 4
                new_direction = 3
                new_x = new_y
                new_y = size - 1
            
        return new_z, new_y, new_x, new_direction
    
    def map(self, point):
        if self.three_d:
            return self.map_3d(point)
        return self.map_2d(point)

    def move(self):
        z, y, x = self.current_location
        if self.direction == 0:
            possible_next = (y, x+1)
        if self.direction == 1:
            possible_next = (y+1, x)
        if self.direction == 2:
            possible_next = (y, x-1)
        if self.direction == 3:
            possible_next = (y-1, x)
        possible_next = (z,) + possible_next
        if set(p for p in possible_next).intersection({-1, size}):
            possible_next = self.map(possible_next)
        if self.faces[possible_next[:3]] == 0:
            self.current_location = possible_next[:3]
            if len(possible_next) == 4:
                self.direction = possible_next[3]

    def run(self):
        # split instructions at every letter
        for ins in re.split('([L]|[R])', cube.instructions):
            if ins in ["L", "R"]:
                self.direction = (self.direction + (1 if ins == "R" else -1)) % 4
            else:
                for _ in range(int(ins)):
                    self.move()
        
        


cube = Cube(np.empty((6, size, size)))

conv = {".":0, "#":1}

with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        row = line.strip()
        if i < size:
            cube.faces[0][i] = np.array([conv[c] for c in row[:size]])
            cube.faces[1][i] = np.array([conv[c] for c in row[size:]])
        elif i < size*2:
            cube.faces[2][i%size] = np.array([conv[c] for c in row])
        elif i < size*3:
            cube.faces[3][i%size] = np.array([conv[c] for c in row[:size]])
            cube.faces[4][i%size] = np.array([conv[c] for c in row[size:]])
        elif i < size*4:
            cube.faces[5][i%size] = np.array([conv[c] for c in row])
        elif i == size*4+1:
            cube.instructions = line.strip()

from copy import deepcopy

cube3d = deepcopy(cube) 
cube.run()
face_map = {0: (0, size), 1: (0, size*2), 2: (size, size), 3: (size*2, 0), 4: (size*2, size*2), 5: (size*3, 0)}
face_location = face_map[cube.current_location[0]]
score = (cube.current_location[1]+1+face_location[0])*1000 + (cube.current_location[2]+face_location[1]+1)*4 + cube.direction 
print(1, score)

cube3d.three_d = True
cube3d.run()
face_location = face_map[cube3d.current_location[0]]
score = (cube3d.current_location[1]+1+face_location[0])*1000 + (cube3d.current_location[2]+face_location[1]+1)*4 + cube3d.direction 
print(2, score)
