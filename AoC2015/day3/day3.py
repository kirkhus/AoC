

input = open("day3.txt", "r").read()


def part1():       
    x = 0
    y = 0
    houses = set()
    houses.add((x, y))
    for i in range(len(input)):
        if input[i] == "^":
            y += 1
        elif input[i] == "v":
            y -= 1
        elif input[i] == ">":
            x += 1
        elif input[i] == "<":
            x -= 1
        houses.add((x, y))
    print("Part 1: ", len(houses))

def part2():
    x = 0
    y = 0
    x2 = 0
    y2 = 0
    houses = set()
    houses.add((x, y))
    for i in range(len(input)):
        if i % 2 == 0:
            if input[i] == "^":
                y += 1
            elif input[i] == "v":
                y -= 1
            elif input[i] == ">":
                x += 1
            elif input[i] == "<":
                x -= 1
            houses.add((x, y))
        else:
            if input[i] == "^":
                y2 += 1
            elif input[i] == "v":
                y2 -= 1
            elif input[i] == ">":
                x2 += 1
            elif input[i] == "<":
                x2 -= 1
            houses.add((x2, y2))
    print("Part 2: ", len(houses))

part1()
part2()