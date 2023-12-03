import re

# 12 red cubes, 13 green cubes, and 14 blue cubes

# Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green
# Game 2: 6 blue, 3 green; 4 red, 1 green, 7 blue; 2 green

lines = open("./input2.txt").readlines()

part1 = 0
part2 = 0

def is_valid_part1(set_):
    red = sum([int(x) for x in re.findall(r"(\d+) red", set_)])
    green = sum([int(x) for x in re.findall(r"(\d+) green", set_)])
    blue = sum([int(x) for x in re.findall(r"(\d+) blue", set_)])
 
    return red <= 12 and green <= 13 and blue <= 14

def find_max(line, regex):
    return max([int(x) for x in re.findall(regex, line)])

for line in lines:
    game = re.search(r"Game (\d+):", line).group(1)
    sets = line.split(";")

    if all([is_valid_part1(set_) for set_ in sets]):
        part1 += int(game)

    max_red, max_green, max_blue = [find_max(line, x) for x in [r"(\d+) red", r"(\d+) green", r"(\d+) blue"]]
    
    part2 += max_blue * max_green * max_red

print("Part 1: ", part1)
print("Part 2: ", part2)

