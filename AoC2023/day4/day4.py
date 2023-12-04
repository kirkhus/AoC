
import re

class Card:
    _id = 0
    _count = 0
    _winners = 0

    def __init__(self, line):
        # Card   1:  4 16 87 61 11 37 43 25 49 17 | 54 36 14 55 83 58 43 15 87 17 97 11 62 75 37  4 49 80 42 61 20 79 25 24 16
        self._id = int(re.findall(r'^Card\s+(\d+)', line)[0])
        
        self._count = 1
        winner_numbers, your_numbers = re.split(r'\s*\|\s*', re.sub(r'^.*:\s*', '', line))
        winner_numbers = re.split("\s{1,2}", winner_numbers)
        your_numbers = re.split("\s{1,2}", your_numbers)
        self._winners = len(set(winner_numbers).intersection(your_numbers))

    def get_id(self):  
        return self._id

    def update_count(self, count):
        self._count = count

    def get_count(self):
        return self._count
    
    def get_points(self):
        return self._count * self._winners
    
    def __str__(self):
        return f"Card: {self._id} {self._count} {self._winners}"


# fucntion for adding up the series
def series(n):
    if (n == 0):
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


part1_sum = 0
for card in cards.values() :
    part1_sum += series(card.get_points())

for card in cards.values():
    print(card)
    if card.get_points() > 0:
        for x in range(1, card.get_points() + 1):
            id = card.get_id()
            if id in cards:
                cards[id].update_count(cards[id].get_count() + 1)
                print("Added to card")
            

part2_sum = 0
for card in cards.values() :
    part2_sum += series(card.get_points())        

print(part1_sum)
print(part2_sum)

