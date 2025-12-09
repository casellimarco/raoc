from aocd import data
import numpy as np
from itertools import batched

r = [list(map(int, p.split(","))) for p in data.splitlines()]
r = np.array(r)
a = []
for i, c in enumerate(r):
    for d in r[i+1:]:
        a.append(np.prod(np.abs(c -d)+1))

print(np.max(a))

m = np.zeros(np.max(r, axis=0)+1, dtype=np.bool)
for i, (c0, c1) in enumerate(r):
    d0, d1 = r[i-1]
    m[min(c0, d0):max(c0,d0)+1,min(c1,d1):max(c1,d1)+1]==True

for i, l in enumerate(m):
    print(i, len(m))
    for c, d in batched(np.argwhere(m), n=2):
        if d == c+1:
            continue
        f[l][c:d+1] = True

a = []
for i, (c0, c1) in enumerate(r):
    for (d0, d1) in r[i+1:]:
        if np.all(f[min(c0, d0):max(c0,d0)+1,min(c1,d1):max(c1,d1)+1]):
            a.append(np.prod(np.abs(c -d)+1))

print(np.max(a))





