from aocd import data
import numpy as np

a = [d.split() for d in data.splitlines()]
m = [list(map(int,r)) for r in a[:-1]]
m = np.array(m)

s = np.cumsum(m, axis=0)[-1]
p = np.cumprod(m, axis=0)[-1]

mask = np.array(a[-1]) == "+"

print(s[mask].sum() + p[~mask].sum())


