from aocd import data
from collections import Counter

cards = "23456789TJQKA" 
cards_value = {c: i for i, c in enumerate(cards)}
joker_cards_value = cards_value.copy()
joker_cards_value["J"] = -1

class Hand:
    def __init__(self, input_string, with_jokers=False):
        self.cards, self.value = input_string.split()
        self.value = int(self.value)
        counter = Counter(self.cards)
        if with_jokers and self.cards != "JJJJJ":
            jokers = counter.pop("J", 0)
            counter[counter.most_common()[0][0]] += jokers 
        self.counts = sorted(counter.values(), reverse=True)
        values = joker_cards_value if with_jokers else cards_value
        self.cards_value = [values[c] for c in self.cards]

    def __gt__(self, other):
        if self.counts == other.counts:
            return self.cards_value > other.cards_value
        return self.counts > other.counts

for J in [0, 1]:
    games = sorted([Hand(d, J) for d in data.splitlines()])
    print(J+1, sum(i*g.value for i, g in enumerate(games, start=1)))
