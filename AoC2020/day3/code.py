f = open("input.txt", "r")

lines = f.read().splitlines()
problem_set = ((1, 1), (3,1), (5, 1), (7, 1), (1, 2))


trees = []

for problem in problem_set:

    right = problem[0]
    down = problem[1]
    position = [0,0]
    tree_count = 0
    
    while position[1] < (len(lines)):
        x, y = position
        if lines[y][x%31] == "#":
            tree_count += 1
            
        position = [x + right, y + down]

    trees.append(tree_count)

x = 1

for y in trees:
    x = x * y


        
print("Answer: %s" % x)
    
            
            

    

               
    
