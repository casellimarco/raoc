from aocd import data
from collections import Counter

cards_value = {c: i for i, c in enumerate("23456789TJQKA")}

class Hand:
    def __init__(self, input_string):
        self.cards, self.value = input_string.split()
        self.value = int(self.value)
        self.counts = list(Counter(self.cards).values())
        self.cards_value = sum(cards_value[c]*(4-i)**13 for i,c in enumerate(self.cards))


    def __gt__(self, other):
        if self.counts == other.counts:
            return self.cards_value > other.cards_value
        else:
            return self.counts > other.counts

data = data.splitlines()
games = [Hand(d) for d in data]
games.sort()

print(sum(i*g.value for i, g in enumerate(games, start=1)))