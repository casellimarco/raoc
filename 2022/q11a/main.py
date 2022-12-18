from dataclasses import dataclass
from pydantic import validate_arguments
from math import prod
from typing import List, Callable

@validate_arguments
@dataclass
class Monkey:
    id: int
    items: List[int]
    operation: Callable
    check: int
    if_true: int
    if_false: int
    counter: int = 0

    def throw(self, relief=None):
        item = self.items.pop(0)
        self.counter += 1
        if relief:
            worry = self.operation(item)%relief
        else:
            worry = int(self.operation(item)/3)
        if worry % self.check == 0:
            return worry, self.if_true
        else:
            return worry, self.if_false

@dataclass
class Game:
    monkeys: List["Monkey"]
    rounds: int
    relief: int=None

    def turn(self, monkey):
        while monkey.items:
            item, receiving_monkey = monkey.throw(self.relief)
            self.monkeys[receiving_monkey].items.append(item)
    
    def round(self):
        for monkey in self.monkeys:
            self.turn(monkey)
    
    def play(self):
        for _ in range(self.rounds):
            self.round()


def parse_monkey(monkey_string: str) -> Monkey:
    lines = monkey_string.splitlines()
    return Monkey(
        id = lines[0][-2],
        items = lines[1].split(": ")[1].split(","),
        operation = lambda old: eval(lines[2].split("= ")[1]),
        check = lines[3].split("by ")[1],
        if_true = lines[4][-1],
        if_false = lines[5][-1],
        )


with open("2022/q11a/input.txt") as f:
    monkeys = list(map(parse_monkey, f.read().split("\n\n")))

part = "b"

if part == "a":
    game = Game(monkeys, 20)
elif part == "b":
    relief = prod(m.check for m in monkeys)
    game = Game(monkeys, 10000, relief)

game.play()
print(prod(sorted(m.counter for m in game.monkeys)[-2:]))
