from dataclasses import dataclass, field
from typing import List
import numpy as np
import re

@dataclass
class Robot:
    cost: List[int]
    produce: List[int]
    
    def __post_init__(self):
        self.cost = np.array(self.cost)
        self.produce = np.array(self.produce)
    
    def can_be_bought(self, materials):
        return all(self.cost <= materials)

    def __hash__(self):
        return hash(tuple(v) for v in self.__dict__.values())
        



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
    skip_robots: set = field(default_factory=set)
    
    def get_robots(self):
        return (
            Robot([self.ore_robot,0,0,0],[1,0,0,0]),
            Robot([self.clay_robot,0,0,0],[0,1,0,0]),
            Robot([self.obsidian_robot_ore,self.obsidian_robot_clay,0,0],[0,0,1,0]),
            Robot([self.geode_robot_ore,0,self.geode_robot_obsidian,0],[0,0,0,1]),
        )

    @property
    def max_robots(self):
        return (
            max(self.ore_robot, self.clay_robot, self.obsidian_robot_ore, self.geode_robot_ore),
            self.obsidian_robot_clay,
            self.geode_robot_obsidian,
        )

    def produce(self, robots):
        for num_robot, robot in zip(self.num_robots, robots):
            self.materials += num_robot*robot.produce

    def can_be_bought(self, robots):
        return [i for i,r in enumerate(robots) if r.can_be_bought(self.materials) and not i in self.skip_robots]
    
    def buy(self, index, robots):
        self.materials -= robots[index].cost
        self.num_robots[index] += 1
        self.skip_robots = set()

    def __hash__(self):
        return hash(tuple(v) for v in self.__dict__.values())


blue = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

with open("input.txt", "r") as f:
    blueprints = []
    for line in f:
        p = re.match(blue, line)
        blueprints.append(Blueprint(*list(map(int, p.groups()))))

from copy import deepcopy


def play(b, steps_left, robots):
    for i in range(steps_left):
        possible_next = b.can_be_bought(robots)
        b.produce(robots)
        if possible_next and possible_next[-1] == 3:
            b.buy(possible_next[-1], robots)
        elif len(possible_next):
            # case where you don't buy
            subcases = [] 
            for index in possible_next:
                if b.num_robots[index] < b.max_robots[index]:
                    b_copy = deepcopy(b)
                    b_copy.buy(index, robots)
                    subcases.append(b_copy)
            b.skip_robots = b.skip_robots.union(set(possible_next))
            subcases.append(b)
            plays = [play(new_b, steps_left - i -1, robots) for new_b in subcases]
            if len(plays):
                plays.sort(key=lambda p: p.materials[3], reverse=True)
                return plays[0]
    return b
            
            

# sum(play(deepcopy(b), steps).materials[3]*b.index for b in blueprints)
#print([play(deepcopy(b), steps).materials[3] for b in blueprints])



steps = 24
total = 0
for b in blueprints:
    result = play(deepcopy(b), steps, b.get_robots())
    total += result.materials[-1]*b.index
    print("Index", b.index, "tot", total)

print("Part 1:", total)

steps = 32
total = 1
for b in blueprints[:3]:
    result = play(b, steps, b.get_robots())
    total *= result.materials[-1]
    print(b.index)
    print(total)

print("Part 2:", total)