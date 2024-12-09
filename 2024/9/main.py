from aocd import data

input = [int(ch) for ch in data]

expanded = []
nones = []

for i, number in enumerate(input):
    if i%2 == 0:
        expanded.extend([i//2] * number)
    else:
        nones.extend(list(range(len(expanded), len(expanded) + number)))
        expanded.extend([None] * number)


first_none = nones.pop(0)

for i in range(len(expanded))[::-1]:
    if i < first_none:
        break
    if expanded[i] is None:
        continue
    value = expanded[i]
    expanded[i] = None
    expanded[first_none] = value
    first_none = nones.pop(0)


part1 = 0
for i, value in enumerate(expanded):
    if value is None:
        break
    part1 += value*i
        

print(1, part1)


# part 2
files = []
nones = []

position = 0

from dataclasses import dataclass

@dataclass
class Chunk:
    id: int | None
    position: int
    size: int
    
for i, size in enumerate(input):
    if i%2 == 0:
        files.append(Chunk(i//2, position, size))
    else:
        nones.append(Chunk(None, position, size))
    position += size

final_allocation = []

for file in files[::-1]:
    for i, none in enumerate(nones):
        if none.position > file.position:
            final_allocation.append(file)
            break
        if none.size < file.size:
            continue
        file.position = none.position
        none.position += file.size
        none.size -= file.size
        nones[i] = none
        final_allocation.append(file)
        break
        
part2 = 0
for file in final_allocation:
    part2 += sum(p*file.id for p in range(file.position, file.size + file.position))

print(2, part2)