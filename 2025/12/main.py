from aocd import data

def parse(d):
    a, b = d.split(": ")
    a1,a2 = list(map(int, a.split("x")))
    b = list(map(int, b.split()))
    return a1,a2,b

part1=0
for d in data.splitlines():
    if not "x" in d:
        continue
    a,b,c = parse(d)
    if sum(c)*9 <= a*b:
        part1+=1

print(part1)
        
