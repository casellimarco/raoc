from aocd import data
from functools import cmp_to_key

less_than = set()
sequences = []

for line in data.splitlines():
    if "|" in line:
        a, b = map(int, line.split("|"))
        less_than.add((a,b))
    if "," in line:
        sequences.append(list(map(int, line.split(","))))

def compare(a,b):
    """Return -1 if a < b, 0 if a == b, 1 if a > b"""
    if a == b:
        return 0
    greater_than = not (a,b) in less_than
    return 2*greater_than - 1

key = cmp_to_key(compare)

part1 = 0
part2 = 0

for sequence in sequences:
    sorted_sequence = sorted(sequence, key=key)
    if sorted_sequence == sequence:
        part1 += sequence[len(sequence)//2]
    else:
        part2 += sorted_sequence[len(sequence)//2]

print(1, part1)
print(2, part2)
