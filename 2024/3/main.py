from aocd import data
import re

regex = r"mul\(?(\d+),?(\d+)\)"
matches = re.findall(regex, data)

part1 = 0

for a, b in matches:
    part1 += int(a) * int(b)

print(1, part1)


regex = r"(mul\((?P<a>\d+),(?P<b>\d+)\))|(?P<do>do\(\))|(?P<undo>don't\(\))"
matches = re.findall(regex, data)

part2 = 0   

count = True
for match in matches:
    _, a, b, do, undo = match
    if do:  
        count = True
    elif undo:
        count = False
    else:
        if count:
            part2 += int(a) * int(b)

print(2, part2)