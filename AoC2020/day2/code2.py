import sys
f = open("input.txt", "r")

lines = f.read().splitlines()
valid_number = 0

for line in lines:
    
    rule, password = line.split(": ")
    numbers, character = rule.split(" ")
    first, second = [int(x) for x in numbers.split("-")]

    count = 0
    if password[first-1] == character:
        count += 1
    if password[second-1] == character:
        count += 1

    if count == 1:
        valid_number += 1
        
print("Valid: ", valid_number)
            
            

    

               
    
