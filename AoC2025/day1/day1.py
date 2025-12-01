import math
lines = open("day1.txt").read().splitlines()



def rotate_dial(dial, direction, steps):
    if direction == "R":
        dial = (dial + steps) % 100
    else:
        dial = (dial - steps) % 100
    return dial




def part1():
    dial = 50
    count = 0
    for l in lines:
        direction, steps = l[0], int(l[1:])
        dial = rotate_dial(dial, direction, steps)
        if dial == 0:
            count += 1

    return count
def part2():
    dial = 50
    count = 0
    for l in lines:
        direction, steps = l[0], int(l[1:])
        for _ in range(steps):
            if direction == "R":
                dial = (dial + 1) % 100
            else:
                dial = (dial - 1) % 100
            if dial == 0:
                count += 1
    return count



print ("Part 1:", part1())
print ("Part 2:", part2())