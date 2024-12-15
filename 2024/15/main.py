from aocd import data
import numpy as np
from dataclasses import dataclass

matrix, instructions = data.split("\n\n")

matrix = np.array([list(row) for row in matrix.split("\n")])
instructions = instructions.replace("\n", "")

directions = {
    ">": (0, 1),
    "^": (-1, 0),
    "<": (0, -1),
    "v": (1, 0),
}
directions = {k: np.array(v) for k, v in directions.items()}
rotations = {
    ">": 0, "^": 3, "<": 2, "v": 1
}

@dataclass
class Game:
    walls: np.ndarray
    boxes: np.ndarray
    robot: np.ndarray
    instructions: str
    
    def excute(self):
        for instruction in self.instructions:
            self.move(instruction)

    def robot_location(self, robot_matrix):
        return np.argwhere(robot_matrix)[0]
    
    def move(self, instruction):
        current_robot_location = self.robot_location(self.robot)
        maybe_robot = current_robot_location + directions[instruction]
        if self.walls[tuple(maybe_robot)]:
            return
        rotated_robot = np.rot90(self.robot, rotations[instruction])
        rotated_walls = np.rot90(self.walls, rotations[instruction])
        rotated_boxes = np.rot90(self.boxes, rotations[instruction])
        rotated_robot_location = self.robot_location(rotated_robot)
        walls_line = rotated_walls[rotated_robot_location[0]][rotated_robot_location[1]+1:]
        first_wall = np.argwhere(walls_line)[0]
        boxes_line = rotated_boxes[rotated_robot_location[0]][rotated_robot_location[1]+1:rotated_robot_location[1]+1+first_wall[0]]
        first_empty_space = np.argwhere(~boxes_line)[:1]
        if len(first_empty_space):
            rotated_boxes[rotated_robot_location[0]][rotated_robot_location[1] + 1 + first_empty_space[0]] = True
            rotated_boxes[rotated_robot_location[0]][rotated_robot_location[1] + 1] = False
            self.boxes = np.rot90(rotated_boxes, -rotations[instruction])
            self.robot[tuple(current_robot_location)] = False
            self.robot[tuple(maybe_robot)] = True

    def score(self):
        return np.sum(np.argwhere(self.boxes)@(100,1))
    

game = Game(matrix == "#", matrix == "O", matrix == "@", instructions)
game.excute()
print(1, game.score())