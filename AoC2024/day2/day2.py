

def is_increasing(line):
    for i in range(1, len(line)):
        if line[i] <= line[i-1]:
            return False
    return True

def is_decreasing(line):
    for i in range(1, len(line)):
        if line[i] >= line[i-1] :
            return False
    return True

def is_max_3(line):
    for i in range(1, len(line)):
        if abs(line[i] - line[i-1]) > 3:
            return False
    return True

def is_valid(line):
    return (is_increasing(line) or is_decreasing(line)) and is_max_3(line)

sum_part1 = 0 
sum_part2 = 0
for line in open("day2.txt").readlines():
    line =  [int(x) for x in line.strip().split(' ')]
    if is_valid(line):
        sum_part1 += 1
    else:
        for i in range(len(line)):
            line_copy = line.copy()
            removed_element = line_copy.pop(i)
            if is_valid(line_copy):
                sum_part2 += 1
                break

print("Part 1:", sum_part1)
print("Part 2:", sum_part1 + sum_part2)



