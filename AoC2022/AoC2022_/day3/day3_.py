
def find_duplicate(first, second):
    for c in first:
        if c in second:
            return c

def find_badge(group):
    for x in group[0]:
        if x in group[1] and x in group[2]:
            return x

def get_priority(duplicate):
    if duplicate.islower():
        return ord(duplicate) - 96

    return ord(duplicate) - 38

total_priority = 0
badge_priority = 0
group = []

for i, line in enumerate(open("input").readlines()):
    line = line.strip()
    first = line[0:len(line)//2]
    second = line[len(line)//2:]

    duplicate = find_duplicate(first, second)
    total_priority += get_priority(duplicate)

    group.append(line)
    if not (i+1)%3:
        badge = find_badge(group)
        badge_priority += get_priority(badge)
        group = []

    
print("Total part 1: ", total_priority)
print("Total part 2: ", badge_priority)
    
    
