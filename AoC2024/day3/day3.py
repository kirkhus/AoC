import re

lines = open("day3.txt").readlines()

sum_part1 = 0
for line in lines:
    matches = re.findall((r"mul\((\d+),(\d+)\)"), line)
    for match in matches:
        sum_part1 += int(match[0]) * int(match[1])



sum_part2 = 0
do = True
for line in lines:
    matches = re.findall((r"(do\(\)|don\'t\(\))+|mul\((\d+),(\d+)\)"), line)
    for match in matches:
        if "do()" in match:
            do = True
            continue
        if "don't()" in match:
            do = False
            continue

        if do:
            sum_part2 += int(match[1]) * int(match[2])

print("Part 1:", sum_part1)
print("Part 2:", sum_part2)