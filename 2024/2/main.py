from aocd import data
import numpy as np


increasing = {1, 2, 3}
decreasing = {-1, -2, -3}

part1 = 0
part2 = 0


def counter_part2(report):
    for possible_steps in [increasing, decreasing]:
        for i in range(len(report)):
            if set(np.diff(report[:i]+report[i+1:])).issubset(possible_steps):
                return True
    return False

for line in data.splitlines():
    report = list(map(int, line.split()))
    increments = set(np.diff(report))
    is_part_1 = increments.issubset(increasing) or increments.issubset(decreasing)
    part1 += is_part_1
    part2 += counter_part2(report)

print(1, part1)
print(2, part2)