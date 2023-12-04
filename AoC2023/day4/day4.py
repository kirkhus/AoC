
import re

# fucntion for adding up the series
def series(n):
    if (n == 0):
        return 0
    if n == 1:
        return 1
    else:
        return 2 * series(n - 1)


lines = [line.strip() for line in open("./input4.txt").readlines()]

part1_sum = 0
for line in lines:
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Remove Card x: and split on |
    winner_numbers, your_numbers = re.split(r'\s*\|\s*', re.sub(r'^.*:\s*', '', line))
    winner_numbers = re.split("\s{1,2}", winner_numbers)
    your_numbers = re.split("\s{1,2}", your_numbers)

    your_winners = list(set(winner_numbers).intersection(your_numbers))

    part1_sum += series(len(your_winners))

print(part1_sum)


