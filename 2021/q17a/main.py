f = open("input.txt").readlines()[0]
x, y = f.strip().split("target area: x=")[1].split(", y=")
x_min, x_max = [int(i) for i in x.split("..")]
y_min, y_max = [int(i) for i in y.split("..")]


def in_target(x, y):
    return x_min<= x <= x_max and y_min<= y <= y_max

def over(x,y):
    return x>x_max or y< y_min

def shot(v0,v1):
    x=v0
    y=v1
    while not (in_target(x,y) or over(x,y)): 
        v0 = max(0, v0-1)
        v1 -=1
        x += v0
        y += v1 
    if in_target(x, y):
        return 1
    else:
        return 0
    
tot = 0
for x in range(0,x_max+1):
    for y in range(y_min, -y_min+1):
        tot += shot(x,y)

print(-y_min*(-y_min-1)//2)
print(tot)