from collections import Counter, defaultdict
from math import prod
import matplotlib.pyplot as plt
import numpy as np

from tqdm import tqdm
from aocd import data

x_max = 101
y_max = 103

class Robot:
    def __init__(self, input_str: str):
        x_y, v_x_y = input_str[2:].split(" v=")
        self.x, self.y = map(int, x_y.split(","))
        self.v_x, self.v_y = map(int, v_x_y.split(","))
    
    def move(self, steps: int):
        self.x += self.v_x * steps
        self.y += self.v_y * steps
        self.x %= x_max
        self.y %= y_max
    
    def quad(self):
        if self.x == x_max // 2 or self.y == y_max // 2:
            return None
        return self.x < x_max//2, self.y < y_max // 2


robots = [Robot(line) for line in data.splitlines()]

quadrants = Counter()

steps = 100
for robot in robots:
    robot.move(steps)
    quad = robot.quad()
    if quad:
        quadrants[quad] += 1

print(1, prod(quadrants.values()))


# Part 2
robots = [Robot(line) for line in data.splitlines()]

def check(robots):
    maybe_tree = Counter()
    for robot in robots:
        maybe_tree[robot.y]+=1
    return maybe_tree.most_common(1)[0][1] > 30

for steps in tqdm(range(1, x_max*y_max)):
    for robot in robots:
        robot.move(1)
    if check(robots):
        matrix = np.zeros((y_max, x_max), dtype=bool)
        for robot in robots:
            matrix[robot.y, robot.x] = True
        plt.imshow(matrix)
        plt.title(f"Steps: {steps}")
        plt.show()

        