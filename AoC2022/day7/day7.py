import re

from dataclasses import dataclass
from enum import Enum


CD = "$ cd"
LS = "$ ls"
DIR = "dir"

pointer = ""
tree = {}

class Type(Enum):
    FILE = 1
    DIR = 2
    


@dataclass
class Element:
    name: str
    type_: Type
    size: int
    sub_folder: list
    files: list


def is_command(line):
    return line.startswith("$")

def is_cd(line):
    return line.startswith(CD)

def is_ls(line):
    return startswith(LS)

def get_dir_name(line):
    print(line)
    match = re.match("(dir|\$ cd) ([a-z])+ (.*?)", line)
    if match:
        print("Match ", match.groups())
        return  match.group(2)
    return "Unknown"
    

current = None
for line in open("input2"):
    line = line.strip()
    if is_cd(line):
        name = get_dir_name(line)
        print(name)
        element = Element(name, Type.DIR, None, [], [])


        
    
    
    
