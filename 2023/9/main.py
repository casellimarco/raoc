from aocd import data
import numpy as np

def process(array):
    derivatives = [array]
    for n in range(len(array) -1):
        derivatives.append(np.diff(derivatives[-1]))
        if np.abs(derivatives[-1]).sum() == 0:
            break
    first_part = sum(d[-1] for d in derivatives)
    second_part = sum(d[0]*(-1)**i for i, d in enumerate(derivatives))
    return first_part, second_part

tot = np.array([0, 0])
for line in data.splitlines():
    array = np.array(list(map(int, line.split())))
    tot += process(array)
    
print(1, tot[0])
print(2, tot[1])