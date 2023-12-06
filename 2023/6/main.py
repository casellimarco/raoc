from aocd import data
import numpy as np

time_str, distance_str = data.split("\n")
time = list(map(int, time_str.split()[1:]))
distance = list(map(int, distance_str.split()[1:]))

# w * (t - w) > d
# -w**2 + t*w - d > 0
# delta = t**2 - 4*d
def num_solutions(t, d):
    delta = np.sqrt(t**2 - 4*(d+1))
    min_w = np.ceil((-t -delta)/2)  
    max_w = np.floor((-t +delta)/2)
    return int(max_w - min_w + 1)

print(1, np.prod([num_solutions(t,d) for t,d in zip(time, distance)]))

t = int("".join(map(str, time)))
d = int("".join(map(str, distance)))
print(2, num_solutions(t,d))