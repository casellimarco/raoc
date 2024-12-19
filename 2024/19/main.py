from tqdm import tqdm
from functools import lru_cache
from aocd import data

store, designs = data.split("\n\n")
store = store.split(", ")

@lru_cache(maxsize=None)
def count(design):
    tot = 0
    for s in store:
        if design == s:
            tot += 1
        elif design.startswith(s):
            tot += count(design[len(s):])
    return tot

part1 = 0
part2 = 0
for design in tqdm(designs.splitlines()):
    counts = count(design)
    part1 += bool(counts)
    part2 += counts

print(1, part1)
print(2, part2)
