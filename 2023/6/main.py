from aocd import data
import numpy as np

time_str, distance_str = data.split("\n")
time = list(map(int, time_str.split()[1:]))
distance = list(map(int, distance_str.split()[1:]))


# w * (t - w) > d
# -w**2 + t*w - d > 0
# delta = t**2 - 4*d

tot = 1
for t, d in zip(time, distance):
    delta = np.sqrt(t**2 - 4*(d+1))
    min_w = np.ceil((-t -delta)/2)  
    max_w = np.floor((-t +delta)/2)
    tot *= int(max_w - min_w + 1)
print(1, tot)

t = int("".join(map(str, time)))
d = int("".join(map(str, distance)))
delta = np.sqrt(t**2 - 4*(d+1))
min_w = np.ceil((-t -delta)/2)  
max_w = np.floor((-t +delta)/2)
print(2, int(max_w - min_w + 1))