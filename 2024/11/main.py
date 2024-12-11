from functools import lru_cache
from aocd import data

stones = list(map(int, data.split()))

@lru_cache(maxsize=None)
def convert(stone):
    if stone == 0:
        return 1,
    elif (digits:=len(str_stone:=str(stone))) % 2 == 0:
        half = digits // 2
        return int(str_stone[:half]), int(str_stone[half:])
    return stone * 2024,

@lru_cache(maxsize=None)
def process(stone, step):
    new_stones = convert(stone)
    if step == 1:
        return len(new_stones)
    return sum(process(stone, step-1) for stone in new_stones)

print(1, sum(process(stone, 25) for stone in stones))
print(2, sum(process(stone, 75) for stone in stones))

