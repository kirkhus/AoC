import re

f = open("input.txt")

"""
For example, consider just the first seven characters of "FBFBBFFRLR":

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
"""

line = "FBFBBFFRLR"


if line[0] == "F":
    
    

#for lin in f.readlines():

