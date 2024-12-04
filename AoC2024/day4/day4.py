
def check(lines, l, i):
    print(line[l][i:i+4])




with open("day44.txt") as file:
    lines = [line.strip() for line in file]

sum_part1 = 0
for l in range(len(lines)):
    line = lines[l]
    for i in range(len(line)):
        c = line[i]
        if c == "X":



            if all(elem in line[i:i+4] for elem in ["X", "M", "A", "S"]):
                sum_part1 += 1
                break
            elif all(elem in line[i-4:i] for elem in ["X", "M", "A", "S"]):
                sum_part1 += 1            
                break
            elif l >= 3 and all(lines[l-j][i] == elem for j, elem in enumerate(["X", "M", "A", "S"])):                
                sum_part1 += 1
            elif l <= len(lines) - 4 and all(lines[l+j][i] == elem for j, elem in enumerate(["X", "M", "A", "S"])):
                sum_part1 += 1


print(sum_part1)    








