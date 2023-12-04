from collections import defaultdict

tot = 0
tickets = defaultdict(int)
with open("input.txt", "r") as f:
    for id, game in enumerate(f, start=1):
        tickets[id] += 1
        cards = game.split(": ")[1].split(" | ")
        cards = [list(map(int, c.split())) for c in cards]
        winning = len(set(cards[0]).intersection(set(cards[1])))
        if winning:
            tot += 2**(winning-1)
        for i in range(1, winning+1):
            tickets[id+i] += tickets[id]

print(1, tot)
print(2, sum(tickets.values()))