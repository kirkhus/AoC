
def check_diagonal_part1(matrix, i, j):
    count = 0
    try:
        if matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
            count += 1
    except:
        pass
    try:
        if j - 3 >= 0 and matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S":
            count += 1
    except:
        pass

    try:
        if i - 3 >= 0 and matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S":
            count += 1
    except:
        pass    

    try:
        if i - 3 >= 0 and j - 3 >= 0 and matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S":
            count += 1
    except:
        pass

    return count



def is_xmas(matrix, i, j):
    """
    Valid XMAS pattern:
    
    Above - Below
        M M - S S
        S S - M M 
        M S - S M 
        S M - M S
        
    """
    try:
        if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "S":
            return True
        
        if matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "M":
            return True
        
        if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "S":
            return True
        
        if matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "M":
            return True
    except:
        pass
        
    return False


with open("day4.txt") as file:
    lines = [line.strip() for line in file]

lines_transposed = ["".join(x) for x in list(zip(*lines))]

sum_part1 = 0
for line in lines + lines_transposed:
    sum_part1 += line.count("XMAS")
    sum_part1 += line.count("SAMX")

for i in range(len(lines)):
    for j in range(len(lines[i])):
        c = lines[i][j] 
        if c == "X":
            sum_part1 += check_diagonal_part1(lines, i, j)
            

sum_part2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        c = lines[i][j] 
        if c == "A":
            if is_xmas(lines, i, j):    
                sum_part2 += 1
    


print("Part 1: ", sum_part1)
print("Part 2: ", sum_part2)







