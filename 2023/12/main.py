from aocd import data

def get_groups(springs):
    groups = []
    running = False
    for spring in springs:
        if spring == "#":
            if running:
                groups[-1] += 1
            else:
                running = True
                groups.append(1)
        else:
            running = False
    return tuple(groups)

from functools import cache

@cache
def compute(springs, groups):
    ques = [i for i, ltr in enumerate(springs) if ltr == "?"]
    if len(ques) == 0:
        return int(get_groups(springs) == groups)
    if len(ques) > 1:
        q1 = ques[0]
        q2 = len(springs) - ques[-1] - 1
        if q2 > q1: # Better starts from end
            ques = [len(springs) -1 -q for q in ques[::-1]]
            springs = springs[::-1]
            groups = groups[::-1]
    q = ques[0]
    end_fixed_block = max(0,springs[:q].rfind("."))
    fixed_groups = get_groups(springs[:end_fixed_block])
    if fixed_groups != groups[:len(fixed_groups)]:
        return 0
    groups = groups[len(fixed_groups):]
    subcases = 0
    for c in ".#":
        s = springs[:q] + c + springs[q+1:]
        subcases += compute(s[end_fixed_block:], tuple(groups))
    return subcases
    

tot_1 = 0
tot_2 = 0 
from tqdm import tqdm 
for line in tqdm(data.splitlines()):
    springs, groups = line.split(" ")
    groups = list(map(int, groups.split(",")))
    tot_1 += compute(springs, tuple(groups))
    springs = (springs + "?")*4 + springs
    groups = groups*5
    tot_2 += compute(springs, tuple(groups))

print(1, tot_1)
print(2, tot_2)    
