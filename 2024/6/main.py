from aocd import data
import numpy as np
from dataclasses import dataclass

input = np.array([list(row) for row in data.splitlines()])

location = np.concatenate(np.where(input == "^"))
area = input == "#"

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
directions = list(map(np.array, directions))

@dataclass
class Game:
    area: np.ndarray
    location: tuple
    direction: int
    
    def __post_init__(self):
        self.visited = np.zeros_like(self.area)
        self.visited[tuple(self.location)] = 1
        self.last_turns = []
        self.has_a_loop = False

    def move(self):
        maybe_location = self.location + directions[self.direction]
        if maybe_location[0] < 0 or maybe_location[0] >= self.area.shape[0] or maybe_location[1] < 0 or maybe_location[1] >= self.area.shape[1]:
            return False
        if self.area[tuple(maybe_location)]:
            if tuple(self.location) in self.last_turns[-4::-4]:
                self.has_a_loop = True
                return False
            self.direction = (self.direction + 1) % 4
            self.last_turns.append(tuple(self.location))
        else:
            self.location = maybe_location
            self.visited[tuple(self.location)] = 1
        return True
    

game = Game(area, location, 0)
while game.move():
    pass

print(1, game.visited.sum())

# Part 2

# Skip starting location
game.visited[tuple(location)] = False
# All others visited locations are the only possible candidates for the additional wall

part2 = 0

from tqdm import tqdm

for candidate in tqdm(np.argwhere(game.visited)):
    candidate_area = area.copy()
    candidate_area[tuple(candidate)] = True
    game = Game(candidate_area, location, 0)
    while game.move():
        pass
    part2 += game.has_a_loop


print(2, part2)