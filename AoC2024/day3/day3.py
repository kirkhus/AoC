import re 

def split_line(line):   
    return re.match('(\d+)-(\d+) (\w): (\w+)', line).groups()

def is_valid_password_part1(input):
    min_, max_, char, password = split_line(input)
    min_ = int(min_)
    max_ = int(max_)
    count = password.count(char)
    return count >= min_ and count <= max_

def is_valid_password_part2(input):  
    first, second, char, password = split_line(input)
    first = int(first) - 1
    second = int(second) - 1
    return (password[first] == char) ^ (password[second] == char)


lines  = open('day3.txt').readlines()

sum_part1 = 0
sum_part2 = 0
for line in lines:
    if is_valid_password_part1(line.strip()):
        sum_part1 += 1
    if is_valid_password_part2(line.strip()):
        sum_part2 += 1

print("Part 1:", sum_part1)
print("Part 2:", sum_part2)