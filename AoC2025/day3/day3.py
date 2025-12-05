banks = open("day3.txt").read().split("\n")

def find_highest(numbers):
    highest = 0
    for x in numbers:
        if int(x) > highest:
            highest = int(x)
    return str(highest)

def largest_joltage_12(digits):

    keep = 12
    n = len(digits)
    remove = n - keep
    stack = []

    for ch in digits:
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    if remove > 0:
        stack = stack[:-remove]

    result_digits = "".join(stack[:keep])
    return int(result_digits)

def part1():
    sum_joltage = 0 
    for bank in banks:
        tens = find_highest(bank[:-1])

        index = bank.index(tens)
        right = bank[index + 1:]
        ones = find_highest(right)
        sum_joltage += int(tens + ones)        


    return sum_joltage

def part2():
    sum_joltage = 0
    for bank in banks:
        sum_joltage += largest_joltage_12(bank)

    return sum_joltage

print("Part 1:", part1())
print("Part 2:", part2())

