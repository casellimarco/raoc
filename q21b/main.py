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

rolls = {3:1,
         4:3,
         5:6,
         6:7,
         7:6,
         8:3,
         9:1}


scores = [0, 0]

player = 0
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=None)
def one_turn(positions, scores, player):
    wins = np.array([0,0])
    for roll, n_r in rolls.items():
        copy_positions = list(positions)
        copy_scores = list(scores)
        copy_positions[player] = mod(positions[player] + roll, 10)
        copy_scores[player] += copy_positions[player]
        if copy_scores[player] > 20:
            wins[player] += n_r
        else:
            wins += n_r*one_turn(tuple(copy_positions), tuple(copy_scores), 1 - player)
    return wins

wins = one_turn(tuple(positions), tuple(scores), player)

print(max(wins))