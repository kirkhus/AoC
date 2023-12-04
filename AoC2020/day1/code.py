import sys
f = open("input.txt", "r")

lines = [int(i) for i in f.read().splitlines()]


for i,x in enumerate(lines):
    for j in range(len(lines)):
        for k in range(len(lines)):
            if (2020 - x - lines[j]) in lines:
                print("Match: ", x, lines[j], (2020 - x - lines[j]))
                sys.exit(0)
                
            #if (x + lines[j] + lines[k]) == 2020:
            #print("Found match: ", x, lines[j], lines[k])
        
            
            
            

    

               
    
