from aocd import data
from math import ceil


def prime_factors(num):
  factors = []
  factor = 2
  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return list(set(factors))


def get_value(d, p, a, b):
    factor = sum([10**(d//p*i) for i in range(p)])
    upper = 10**d//factor
    lower = 10**(d-1)//factor
    if d == len(b):
        upper = int(b) // factor 
    if d == len(a):
        lower = ceil((int(a))/factor) - 1

    return factor*(sum_n(upper) - sum_n(lower))


def sum_n(n): 
    return (n*(n+1))//2


part1=0
part2=0
for interval in data.split(","):
    a,b = interval.split("-")
    for d in range(len(a),len(b)+1):
        primes = prime_factors(d)
        for i, p in enumerate(primes):
            value = get_value(d, p, a, b);
            part2+=value
            if p == 2:
                part1+=value
            for q in primes[i+1:]:
                part2-= get_value(d, p*q, a, b)


print(part1)
print(part2)

