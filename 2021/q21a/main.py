first, second = open("input.txt").readlines()

first_position = int(first.strip().split(": ")[1])   
second_position = int(second.strip().split(": ")[1])

positions = [first_position, second_position]

def mod(x, y):
    maybe_mod = x % y
    if maybe_mod == 0:
        return y
    else:
        return maybe_mod

def die():
    d = 1
    while True:
        result = 0
        for i in range(3):
            result += d
            d = mod(d+1, 100)
        yield result

roll = die()

scores = [0, 0]

player = 0
rolls = 0
while all([s<1000 for s in scores]):
    positions[player] = mod(positions[player] + next(roll), 10)
    scores[player] += positions[player]
    player = 1 - player
    rolls += 3

print(scores[player]*rolls)



