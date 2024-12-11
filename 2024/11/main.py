from aocd import data

stones = list(map(int, data.split()))

def process(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            half = len(stone) // 2
            new_stones.append(int(stone[:half]))
            new_stones.append(int(stone[half:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

from tqdm import tqdm

for _ in tqdm(range(25)):
    stones = process(stones)

print(1, len(stones))



