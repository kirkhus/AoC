sum_part1 = 0
sum_part2 = 0

for line in open("day2.txt").readlines():
    l, w, h = map(int, line.split("x"))
    sum_part1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    sum_part2 += 2*min(l+w, w+h, h+l) + l*w*h




print("Part 1: ", sum_part1)
print("Part 2: ", sum_part2)