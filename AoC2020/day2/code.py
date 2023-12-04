import sys
f = open("input.txt", "r")

lines = f.read().splitlines()
valid_number = 0

for line in lines:
    
    rule, password = line.split(": ")
    numbers, character = rule.split(" ")
    min, max = numbers.split("-")
    count = password.count(character)
    
    if count < int(min):
        continue
    if count <= int(max):
        valid_number += 1
        
print("Valid: ", valid_number)
            
            

    

               
    
