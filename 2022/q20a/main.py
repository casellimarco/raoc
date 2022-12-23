from bidict import bidict

with open("input.txt", "r") as f:
    input = list(map(int, f))

# input = [1, 2, -3, 3, -2, 0, 4]
m = len(input)
scaling = 811589153
input = [i*scaling for i in input]

perm = bidict({k:k for k in range(m)})

def pr():
    out = [None]*m
    for pos, val in enumerate(input):
        out[perm[pos]] = val
    print(out)

loops = 10
def move(value, pos):
    old = perm.pop(pos)
    # new = (old + (value%(m-1))) % m
    new = (old + value) % (m-1)
    if old < new:
        for i in range(old+1, new+1):
            perm[perm.inverse[i]] -= 1
    else:
        for i in range(old-1, new-1, -1):
            perm[perm.inverse[i]] += 1
    perm[pos] = new



#pr()
for l in range(loops):
    print(l)
    for pos, value in enumerate(input):
        move(value, pos)
    #pr()

index = input.index(0)
print(sum(input[perm.inverse[(perm[index]+shift)%m]] for shift in [1000,2000,3000]))