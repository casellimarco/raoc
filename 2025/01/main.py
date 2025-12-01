from aocd import data

part1=0
part2=0
part=2
loc=50
size=100
for rot in data.splitlines():
    update=int(rot[1:])*(1-2*(rot[0]=='L'))
    loc1=loc+update
    part2+=abs(loc1//size- loc//size)
    part2-=(loc1%size==0 and loc<loc1) or (loc%size==0 and loc1<loc)
    loc=loc1%size
    part1+=loc==0

print(part1)
print(part2 + part1)


