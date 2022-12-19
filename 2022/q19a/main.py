from dataclasses import dataclass, field
from typing import List
import numpy as np
import re
from enum import Enum

@dataclass
class Robot:
    cost: List[int]
    produce: List[int]
    
    def __post_init__(self):
        self.cost = np.array(self.cost)
        self.produce = np.array(self.produce)
    
    def can_be_bought(self, materials):
        return all(self.cost <= materials) and (not all(self.cost < materials))



@dataclass
class Blueprint:
    index: int
    ore_robot: int
    clay_robot: int
    obsidian_robot_ore: int
    obsidian_robot_clay: int
    geode_robot_ore: int
    geode_robot_obsidian: int
    materials: np.array = field(default_factory= lambda: np.array([0,0,0,0]))
    num_robots: list = field(default_factory= lambda: [1,0,0,0])
    
    def __post_init__(self):
        self.robots = [
            Robot([self.ore_robot,0,0,0],[1,0,0,0]),
            Robot([self.clay_robot,0,0,0],[0,1,0,0]),
            Robot([self.obsidian_robot_ore,self.obsidian_robot_clay,0,0],[0,0,1,0]),
            Robot([self.geode_robot_ore,0,self.geode_robot_obsidian,0],[0,0,0,1]),
        ]
    
    def produce(self):
        for num_robot, robot in zip(self.num_robots, self.robots):
            self.materials += num_robot*robot.produce

    def can_be_bought(self):
        return [i for i,r in enumerate(self.robots) if r.can_be_bought(self.materials)]
    
    def buy(self, index):
        self.materials -= self.robots[index].cost
        self.num_robots[index] += 1


blue = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

with open("input2.txt", "r") as f:
    blueprints = []
    for line in f:
        p = re.match(blue, line)
        blueprints.append(Blueprint(*list(map(int, p.groups()))))

from copy import deepcopy

steps = 24

def play(b, steps_left):
    b = deepcopy(b)
    
    for i in range(steps_left):
        possible_next = b.can_be_bought()
        b.produce()
        if possible_next and  possible_next[-1] in [2,3]:
            b.buy(possible_next[-1])
        elif possible_next: # i.e [0,1], [1], [0]
            subcases = []
            for index in possible_next:
                b_copy = deepcopy(b)
                b_copy.buy(index)
                subcases.append(b_copy)
            # case where you don't buy
            b_copy = deepcopy(b)
            subcases.append(b_copy)
            plays = [play(new_b, steps_left - i -1) for new_b in subcases]
            if plays:
                plays.sort(key=lambda p: p.materials[3], reverse=True)
                return plays[0]
    return b
            
            

# sum(play(deepcopy(b), steps).materials[3]*b.index for b in blueprints)
#print([play(deepcopy(b), steps).materials[3] for b in blueprints])



b = blueprints[0]
play(deepcopy(b), steps)
