
def find_duplicate(first, second):
    for c in first:
        if c in second:
            return c

def get_priority(duplicate):
    if duplicate.islower():
        return ord(duplicate) - 96

    return ord(duplicate) - 38

total_priority = 0
        
for line in open("input").readlines():
    line = line.strip()
    first = line[0:len(line)//2]
    second = line[len(line)//2:]

    duplicate = find_duplicate(first, second)

    total_priority += get_priority(duplicate)
    
print("Total: ", total_priority)
    
    
