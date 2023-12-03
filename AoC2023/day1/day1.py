import re

word_to_number = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def first_last(regex, line):
    numbers = re.findall(regex, line)
    first_number = word_to_number.get(numbers[0], numbers[0])
    last_number = word_to_number.get(numbers[-1], numbers[-1])
    return first_number, last_number

sum_digit = 0
sum_words = 0

lines = open("./input.txt").readlines()

for line in lines:

    first, last = first_last(r"\d", line)
    sum_digit += int(f"{first}{last}")

    first, last = first_last(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', line)
    sum_words += int(f"{first}{last}")

print("Part 1: ", sum_digit)
print("Part 2: ", sum_words)

