from aocd import data
from collections import Counter

cards = "23456789TJQKA" 
cards_value = {c: i for i, c in enumerate(cards)}
joker_cards = "J23456789TQKA" 
joker_cards_value = {c: i for i, c in enumerate(joker_cards)}

class Hand:
    def __init__(self, input_string, with_jokers=False):
        self.cards, self.value = input_string.split()
        self.value = int(self.value)
        counter = Counter(self.cards)
        if with_jokers and self.cards != "JJJJJ":
            jokers = counter.pop("J", 0)
            counter[counter.most_common()[0][0]] += jokers 
        self.counts = list(counter.values())
        self.counts.sort(reverse=True)
        values = joker_cards_value if with_jokers else cards_value
        self.cards_value = sum(values[c]*len(cards)**(4-i) for i,c in enumerate(self.cards))

    def __gt__(self, other):
        if self.counts == other.counts:
            return self.cards_value > other.cards_value
        else:
            return self.counts > other.counts

for i in [0, 1]:
    games = sorted([Hand(d, i) for d in data.splitlines()])
    print(i+1, sum(i*g.value for i, g in enumerate(games, start=1)))
