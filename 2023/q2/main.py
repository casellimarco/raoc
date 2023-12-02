from collections import Counter
from functools import reduce
from operator import mul, or_

thres = Counter({"red":12, "green":13, "blue":14})

tot_1 = 0
tot_2 = 0
with open("input.txt", "r") as f:
    for game in f:
        game_id, draws = game.strip().split(": ")
        game_id = int(game_id.split(" ")[1])
        draws = [[c.split(" ") for c in d.split(", ")] for d in draws.split("; ")]
        draws = [Counter({c[1]:int(c[0]) for c in d}) for d in draws]
        tot_1 += all(d<=thres for d in draws) * game_id
        tot_2 += reduce(mul, reduce(or_, draws).values())
        

print(1, tot_1)
print(2, tot_2)
