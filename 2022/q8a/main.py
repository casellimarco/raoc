import numpy as np

jungle = []
with open("2022/q8a/input.txt") as f:
# with open("input.txt") as f:
    for l in f:
        jungle.append(list(map(int, l.strip())))

jungle = np.array(jungle)
jungle_pad = np.pad(jungle,1,"constant", constant_values=-1)
hor_pad = jungle_pad[1:-1,:]
ver_pad = jungle_pad[:,1:-1]

left = np.maximum.accumulate(hor_pad,axis=1)
right = np.maximum.accumulate(hor_pad[:,::-1],axis=1)
up = np.maximum.accumulate(ver_pad)
down = np.maximum.accumulate(ver_pad[::-1])

left_filtered = np.less(left[:,:-1],left[:,1:])[:,:-1]
right_filtered = np.less(right[:,:-1],right[:,1:])[:,::-1][:,1:]
up_filtered = np.less(up[:-1],up[1:])[:-1]
down_filtered = np.less(down[:-1],down[1:])[::-1][1:]

print((left_filtered | right_filtered | up_filtered | down_filtered).sum())
external = left_filtered | right_filtered | up_filtered | down_filtered

def distance(value, row):
    if len(row) == 0:
        return 0
    else:
        above = np.where(row >= value)[0]
        if len(above) == 0:
            return len(row)
        else:
            return above[0]+1

def prod(i, j):
    entry = jungle[i,j]
    r = distance(entry, jungle[i, j+1:])
    l = distance(entry, jungle[i,:j][::-1])
    d = distance(entry, jungle[i+1:,j])
    u = distance(entry,jungle[:i,j][::-1]) 
    return d*u*r*l

distances = np.zeros_like(jungle)
a,b = distances.shape
for i in range(a):
    for j in range(b):
        distances[i,j] = prod(i, j)

print(np.max(distances))