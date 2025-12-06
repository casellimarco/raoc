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

a = []
for s,e in fresh:
    a.extend([(s,0), (e,1)])

a.sort(key = lambda p: p[0] + 0.1*p[1])

o = 0
s = None
part2 = 0
for b,t in a:
    if t:
        o -= 1
        if o == 0:
            part2+= b - s + 1
    else:
        o += 1
        if o == 1:
            s = b

print(part2)

