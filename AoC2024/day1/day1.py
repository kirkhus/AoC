
list1 = []
list2 = []

lines = open("./day1.txt").read().splitlines()
for line in lines:
    chunk = [int(x) for x in line.strip().split('   ')]    
    list1.append(chunk[0])
    list2.append(chunk[1])

list1.sort()
list2.sort()

sum_part1 = 0
sum_part2 = 0
for i in range(len(list1)):
    x = list1[i]
    y = list2[i]   
    count = list2.count(x) 

    sum_part1 += abs(x-y)
    sum_part2 += x * count

print("Part 1:", sum_part1)
print("Part 2:", sum_part2)




