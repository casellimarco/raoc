
data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


from aocd import data
from math import ceil

part1=0

sum_n = lambda n: (n*(n+1))//2

for interval in data.split(","):
    a,b = interval.split("-")
    for d in range(len(a),len(b)+1):
        if d%2 == 1:
            continue
        factor = 10**(d//2) + 1
        upper = factor - 2
        lower = 10**(d-1)//factor
        if d == len(b):
            upper = int(b) // factor 
        if d == len(a):
            lower = ceil((int(a))/factor) - 1

        part1+=factor*(sum_n(upper) - sum_n(lower))

print(part1)

