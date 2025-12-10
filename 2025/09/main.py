from aocd import data
from shapely import Polygon, box

r = [list(map(int, p.split(","))) for p in data.splitlines()]
part1 = 0
part2 = 0
polygon = Polygon(r)
for i, c in enumerate(r):
    for d in r[i+1:]:
        c0,c1 = c
        d0,d1 = d
        area = (abs(c0-d0)+1)*(abs(c1-d1)+1)
        part1 = max(part1, area)
        b = box(min(c0, d0), min(c1,d1), max(c0,d0),max(c1,d1))
        if polygon.contains(b):
            part2 = max(part2, area)
print(part1)
print(part2)
