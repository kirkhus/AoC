
import re

# fucntion for adding up the series
def series(n):
    if (n == 0):
        return 0
    if n == 1:
        return 1
    else:
        return 2 * series(n - 1)


class Card:
    id_ = 0
    count_ = 0
    winner_numbers = []
    your_numbers = []

    def __init__(self, id_, count_, winner_numbers, your_numbers):
        self.id_ = id_
        self.count_ = count_
        self.winner_numbers = winner_numbers
        self.your_numbers = your_numbers




lines = [line.strip() for line in open("./input44.txt").readlines()]
cards = {}

for line in lines:
    key = line.split(":")[0]    
    values = line.split(":")[1].split("|")  
    cards[




part1_sum = 0
for i, line in enumerate(lines):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    
    winner_numbers, your_numbers = re.split(r'\s*\|\s*', re.sub(r'^.*:\s*', '', line))
    winner_numbers = re.split("\s{1,2}", winner_numbers)
    your_numbers = re.split("\s{1,2}", your_numbers)

    your_winners = list(set(winner_numbers).intersection(your_numbers))
    part1_sum += series(len(your_winners))

    for x in range(len(your_winners)):
        lines.insert(i+x, lines[i+x])





print(len(extra_cards))
print(part1_sum)


