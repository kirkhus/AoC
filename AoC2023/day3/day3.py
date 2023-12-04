import re
from functools import reduce

parts = {}
lines = [line.strip() for line in open("./input3.txt").readlines()]


def store_part(line, symbol_index, part):
    id_ = f"{lines.index(line)}-{symbol_index}"
    if id_ not in parts:
        parts[id_] = [part]
    else:
        parts[id_].append(part)  


def is_part(part, line, start, end):
    line = line.strip()
    slice =  line[start:end]
    for x in slice:
        if not re.search(r"\d|\.", x): # Check not a digit or "."
            store_part(line, start + slice.index(x), part)
            return True
    return False 

sum_part1 = 0
sum_part2 = 0


for i, line in enumerate(lines):
    matches = re.finditer(r"(\d+)", line) # find ALL matches

    for match in matches:
        found = False
        part = match.group(0)
        start = max(0, match.start(0) - 1)
        end = match.end(0) + 1

        if is_part(part, line, start, end): #same line
            found = True
        if i > 0 and not found: #previous line
            if is_part(part, lines[i - 1], start, end):
                found = True
        if i < (len(lines)-1) and not found: #next line
            if is_part(part, lines[i + 1], start, end):
                found = True

        if found:
            sum_part1 += int(part)
    

for keys in parts:
    if len(parts[keys]) > 1:
        product = reduce(lambda x, y: x*y, [int(x) for x in parts[keys]])
        sum_part2 += product
        

print("Part 1: ", sum_part1)
print("Part 2: ", sum_part2)