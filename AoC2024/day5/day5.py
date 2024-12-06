
def sum_middle_elements(list_): 
    sum = 0
    for l in list_:
        mid_index = len(l) // 2
        sum += l[mid_index]
    return sum


def is_present(rule, print_):
    return rule[0] in print_ and rule[1] in print_

def is_valid_rule(rule, print_):
    if rule[0] not in print_ or rule[1] not in print_:
        return False
    if print_.index(rule[0]) > print_.index(rule[1]):
        return False
    return True


def is_valid_print_part1(print_, rules):
    
    for rule in rules:
        if not is_present(rule, print_):
            continue
        
        if not is_valid_rule(rule, print_):
            return False

    return True
    

with open("day55.txt") as file:
    lines = [line.strip() for line in file]

rules = []
prints = []

for line in lines:
    if "|" in line:
        rules.append([int(x) for x in line.split("|")])
    elif "," in line:
        prints.append([int(x) for x in line.split(",")])

valid_prints = []
invalid_prints = []
for print_ in prints:
    if is_valid_print_part1(print_, rules):
        valid_prints.append(print_)
    else:
        invalid_prints.append(print_)



sum_part1 = sum_middle_elements(valid_prints)
fixed_list = []
for print_ in invalid_prints:
    print("Fixing print:", print_)  

    for rule in rules:
        if is_present(rule, print_):
            if not is_valid_rule(rule, print_):
                print("Rule:", rule, print_)
                print_.remove(rule[0])
                print_.insert(print_.index(rule[1])+1, rule[0])

    print("Fixed print:", print_)
    fixed_list.append(print_)

                
print("Part 1:", sum_part1)
print("Part 2:", sum_middle_elements(fixed_list))