import re

def is_divisible_by_2(n):
    return n % 2 == 0

def split_in_half(s):
    mid = len(s) // 2
    return s[:mid], s[mid:]

def is_invalid1(id):
    id = str(id)
    if not is_divisible_by_2(len(id)):
        return False
    
    first_half, second_half = split_in_half(id)
    if not first_half == second_half:
        return False
    
    return True


def is_invalid2(id):
    id = str(id)
    m = re.fullmatch(r"(\d+)\1+", id)
    if not m:
        return False
    if m.group(0) == id:
        return True

    return False

def part1():
    sum_invalid = 0
    for l in products:
        first, last = l.split("-")
        ids = make_complete_liste(first, last)

        for id in ids:
            if is_invalid1(id):
                sum_invalid += id
    return sum_invalid

def part2():
    sum_invalid = 0
    for l in products:
        first, last = l.split("-")
        ids = make_complete_liste(first, last)

        for id in ids:
            if is_invalid2(id):
                print("Invalid ID:", id)
                sum_invalid += id
    return sum_invalid

def make_complete_liste(first, last):
    return list(range(int(first), int(last)+1))
        
products = open("day2.txt").read().split(",")

print("Part 1:", part1())
print("Part 2:", part2())
