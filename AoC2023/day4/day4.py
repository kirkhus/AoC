
import re

class Card:
    _id = 0
    _count = 0
    _winners = 0

    def __init__(self, line):
        self._id = line.split(":")[0]
        self._count = 1
        winner_numbers, your_numbers = re.split(r'\s*\|\s*', re.sub(r'^.*:\s*', '', line))
        winner_numbers = re.split("\s{1,2}", winner_numbers)
        your_numbers = re.split("\s{1,2}", your_numbers)
        self._winners = len(set(winner_numbers).intersection(your_numbers))

    def update_count(self, count):
        self._count = count

    def get_points(self):
        return self._count * self._winners
    
    def __repr__(self):
        return "Card: " + self._id + " " + str(self._count) + " " + str(self._winners)


# fucntion for adding up the series
def series(n):
    if (n == 0):
        return 0
    if n == 1:
        return 1
    else:
        return 2 * series(n - 1)

cards = []
lines = [line.strip() for line in open("./input4.txt").readlines()]

for line in lines:
    card = Card(line)
    cards.append(card)




part1_sum = 0
for card in cards:
    part1_sum += series(card.get_points())

print(part1_sum)


