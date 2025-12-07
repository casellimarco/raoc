from aocd import data
from collections import Counter

m = []
for r in data.splitlines():
    m.append(set())
    for i, c in enumerate(r):
        if c in "S^":
            m[-1].add(i)

part1=0
b = Counter(m[0])
for s in m[1:]:
    n = Counter()
    for q, c in b.items():
        if q in s:
            part1+=1
            n[q-1] += c
            n[q+1] += c
        else:
            n[q] += c
    b = n

print(part1)
print(b.total())

