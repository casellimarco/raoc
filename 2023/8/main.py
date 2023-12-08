from aocd import data
from math import lcm

dir_to_int = {"L": 0, "R": 1}
mapping = {}
lines = data.splitlines()
instructions = list(map(lambda x: dir_to_int[x], lines[0]))
for line in lines[2:]:
    in_, out = line.split(" = ")
    mapping[in_] = out[1:-1].split(", ")
    
def n_steps(pos, end_condition):
    c = 0
    while not end_condition(pos):
        pos = mapping[pos][instructions[c%len(instructions)]]
        c += 1
    return c

is_ZZZ = lambda x: x == "ZZZ"
print(1, n_steps("AAA", is_ZZZ))

ends_in_Z = lambda x: x[-1] == "Z"
print(2, lcm(*(n_steps(k, ends_in_Z) for k in mapping if k[-1] == "A")))
