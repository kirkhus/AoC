import re

# Data class for Card that stores id, how many cards it has, and how many winners there are on this card    
class Card:
    def __init__(self, line):
        self._id = int(re.findall(r'^Card\s+(\d+)', line)[0]) # id that is the card number
        self._count = 1
        winner_numbers, your_numbers = re.split(r'\s*\|\s*', re.sub(r'^.*:\s*', '', line))
        self._winners = len(set(winner_numbers.split()).intersection(your_numbers.split()))

    def get_id(self):  
        return self._id

    def update_count(self, count):
        self._count = count

    def get_count(self):
        return self._count
    
    def get_winners(self):
        return self._winners

    def __str__(self):
        return f"Card: {self._id} {self._count} {self._winners}"


# Function for adding up the series
def series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return 2 * series(n - 1)

cards = {}
lines = [line.strip() for line in open("./input4.txt").readlines()]

for line in lines:
    card = Card(line)
    cards[card.get_id()] = card


# Loop through and create copies
for card in cards.values():
    if card.get_winners() > 0:
        for _ in range(card.get_count()):
            for x in range(1, card.get_winners() + 1):
                id_ = card.get_id() + x
                cards[id_].update_count(cards[id_].get_count() + 1)
                    
# Find answers
part1_sum, part2_sum = 0, 0

for card in cards.values():
    part1_sum += series(card.get_winners())
    part2_sum += card.get_count()

print("Part 1:", part1_sum)
print("Part 2:", part2_sum)

