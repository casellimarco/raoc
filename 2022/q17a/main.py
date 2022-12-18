from dataclasses import dataclass
from typing import List
import numpy as np
from copy import deepcopy

@dataclass
class Shape:
    # coordinates are y, x [YES SWAPPED]
    coordinates: np.ndarray #relative location in a rectangle with shape = (4,4)
    pivot = np.ndarray = np.array([[0],[0]])#shape = (2,1)
    limit_l: int = 0
    limit_r: int = 6
    limit_d: int = 0
    # most likely overkill:
    # coord_d: tuple
    # coord_r: tuple
    # coord_l: tuple

    def now(self):
        return self.location(self.pivot)

    def location(self, pos):
        return self.coordinates + pos

    def allow_position(self, pos, rocks):
        current_pos = self.location(pos) 
        if (  any(current_pos[1] < self.limit_l)
           or any(current_pos[1] > self.limit_r)
           or any(current_pos[0] < self.limit_d) ):
            return False
        return not any(rocks[tuple(current_pos)])

    # Movements: 
    # try to move pivot
    # check if violates boundary conditions
    #   check if overlays with rocks
    #       update pivot

    def starting_point(self, rocks):
        for height, row in enumerate(rocks):
            if not any(row):
                break
        self.pivot = np.array([[height+3],[2]])
    
    def move(self,rocks, direction):
        new_pos = self.pivot + direction
        if self.allow_position(new_pos, rocks):
            self.pivot = new_pos 
            return True
        return False

    def add(self, rocks):
        rocks[tuple(self.now())] = True
    
    def move_l(self, rocks):
        direction = np.array([[0],[-1]])
        self.move(rocks, direction)

    
    def move_r(self, rocks):
        direction = np.array([[0],[1]])
        self.move(rocks, direction)

    def move_d(self, rocks)-> bool:
        direction = np.array([[-1],[0]])
        if not self.move(rocks, direction):
            self.add(rocks)
            return False
        else:
            return True

    def print(self):
        sprite = np.empty((10,7), dtype=str)
        sprite.fill(" ")
        sprite[tuple(self.now())] = "█"
        print(sprite[::-1])

print("long")
long = Shape(
    np.array([[0,1,2,3],
              [0,0,0,0]])
)
long.print()

print("large")
large = Shape(
    np.array([[0,0,0,0],
              [0,1,2,3]])
)
large.print()

print("corner")
corner = Shape(
    np.array([[0,0,0,1,2],
              [0,1,2,2,2]])
)
corner.print()
        
print("square")
square = Shape(
    np.array([[0,0,1,1],
              [0,1,0,1]])
)
square.print()
        
print("plus")
plus = Shape(
    np.array([[1,1,1,0,2],
              [0,1,2,1,1]])
)
plus.print()
        

# Transpose arrays to have the "right" orientation or swap the axis (e.g, y,x)

rocks = np.zeros((int(1e5),7), dtype=bool)
rocks[0] = True

plus.starting_point(rocks)
plus.move_l(rocks)
plus.print()


with open("input.txt", "r") as f:
    input = f.read().strip()
# input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

@dataclass
class Game:
    rocks: np.array
    input: str
    turns: int = 2022
    symbols = [large, plus, corner, long, square]
    turn = 0
    step = 0
    current_shape = None

    def play(self):
        while self.turn < self.turns:
            self.do_turn()

    def do_turn(self):
        self.current_shape = deepcopy(self.symbols[self.turn%5])
        self.current_shape.starting_point(self.rocks)
        while self.do_step():
            continue
        self.turn +=1
    
    def do_step(self):
        self.step %= len(input)
        if input[self.step] == ">":
            self.current_shape.move_r(rocks)
        else:
            self.current_shape.move_l(rocks)
        self.step += 1
        return self.current_shape.move_d(rocks)
    
    def get_high(self):
        for height, row in enumerate(rocks):
            if not any(row):
                break
        return height
    
    def print(self):
        map = {True:"█", False:" ",}
        converted = np.vectorize(map.get)(self.rocks)
        print(converted[:20][::-1])
            

game = Game(rocks, input, turns=2022)
game.play() 
print(game.get_high()-1)