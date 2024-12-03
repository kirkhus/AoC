input = open("day1.txt", "r").read()

up = input.count("(")
down = input.count(")")


sum  = up - down

print("Part 1: ", sum)


pos = 0 

for i in range(len(input)):
    if input[i] == "(":
        pos += 1
    else:
        pos -= 1
    if pos == -1:
        print("Part 2: ", i+1)
        break


