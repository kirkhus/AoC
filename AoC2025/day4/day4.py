grid = open("day4.txt").read().splitlines()

roll = "@"
empty = "."

def part1():
    num_accessable = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if is_accessable(x, y):
                num_accessable += 1
    return num_accessable

def part2():
    num_accessable = 0
    while True:
        removed = []

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if is_accessable(x, y):
                    num_accessable += 1
                    removed.append((x, y))

        for (x, y) in removed:
            grid[x] = grid[x][:y] + empty + grid[x][y+1:]

        if len(removed) == 0:
            break
    return num_accessable




def is_accessable(x, y):    
    c = grid[x][y]
    if c != roll:
          return False

    rolls = -1

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x + dx < 0 or x + dx >= len(grid):
                continue
            if y + dy < 0 or y + dy >= len(grid[x]):
                continue

            if grid[x + dx][y + dy] == roll:
                rolls += 1

    # accessable if less than 4 rolls around
    print(x, y, rolls)
    return rolls < 4


print("Part 1:", part1())
print("Part 2:", part2())