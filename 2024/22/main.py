from collections import Counter
from aocd import data
from tqdm import tqdm
import numpy as np

two_24 = 16777216
mod = two_24 - 1

def step(secret):
    value = secret << 6
    secret = (value ^ secret) & mod 
    value = secret >> 5
    secret = (value ^ secret) & mod
    value = secret << 11
    secret = (value ^ secret) & mod
    return secret

part1 = 0
values = []
for value in tqdm(data.splitlines()):
    value = int(value)
    values.append([value%10])
    for _ in range(2000):
        value = step(value)
        values[-1].append(value%10)
    part1 += value

print(1, part1)

values = np.array(values)
diffs = np.diff(values, axis=1)

def extract_sequences(diffs, values):
    seq_to_value = Counter()
    for i in range(4, diffs.shape[0]+1):
        key = tuple(diffs[i-4:i].tolist())
        if key not in seq_to_value:
            seq_to_value[key] = values[i]
    return seq_to_value

seqs = []   
for d, v in zip(diffs, values):
    seqs.append(extract_sequences(d, v))

part2 = 0
for k in tqdm(set.union(*[set(s.keys()) for s in seqs])):
    part2 = max(part2, sum(s[k] for s in seqs))
    
print(2, part2)

