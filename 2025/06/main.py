from aocd import data
import numpy as np

a = [d.split() for d in data.splitlines()]
m = [list(map(int,r)) for r in a[:-1]]
m = np.array(m)

s = np.cumsum(m, axis=0)[-1]
p = np.cumprod(m, axis=0)[-1]

mask = np.array(a[-1]) == "+"

print(s[mask].sum() + p[~mask].sum())

a = np.array([list(d) for d in data.splitlines()][:-1]).T
n = ["".join(list(d)).split() for d in a] + [[]]

part2 = 0
i = 0
c = []
for d in n:
    if not d:
        if mask[i]:
            part2+=np.sum(c)
        else:
            part2+=np.prod(c)
        i += 1
        c = []
    else:
        c.append(int(d[0]))

print(part2)

