

data="""3-5
10-14
16-20
12-18
21-24
29-32
23-30
19-22


1
5
8
11
17
32"""
from aocd import data

fresh = set()
ids = []

for d in data.splitlines():
    if not d:
        continue
    if "-" in d:
        fresh.add(tuple(map(int, d.split("-"))))
    else:
        ids.append(int(d))


part1=0
for i in ids:
    for f in fresh:
        if f[0] <= i <= f[1]:
            part1+=1
            break

print(part1)


def union_pairs(fresh):
    new = set()
    checked = set()
    for i, f in enumerate(fresh):
        for j, g in enumerate(fresh):
            if i in checked:
                break
            if j <= i or j in checked:
                continue
            if f[0] <= g[0] <= f[1] or f[0] <= g[1] <= f[1]:
                new.add((min(f[0],g[0]), max(f[1],g[1])))
                checked.add(i)
                checked.add(j)
                break
        if not i in checked:
            new.add(f)
            checked.add(i)

    return new                           

old = set()

while old != fresh:
    old = fresh.copy()
    fresh = union_pairs(fresh)


part2 = 0
for f in fresh:
    part2+=f[1] - f[0] + 1

print(part2)
