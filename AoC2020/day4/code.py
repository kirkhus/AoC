import re

f = open("input.txt")

passports = []
chunks = []
valid_passports  = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""


regex = {
    "byr" : lambda x: int(x) > 1919 and int(x) < 2003,
    "iyr" : lambda x: int(x) > 2009 and	int(x) < 2021,
    "eyr" : lambda x: int(x) > 2019 and int(x) < 2031,
    "hgt" : lambda x: True if (("cm" in x and int(x.replace("cm", "")) > 149 and int(x.replace("cm", "")) < 194) or ("in" in x and int(x.replace("in", "")) > 58 and int(x.replace("in", "")) < 77)) else False,
    "hcl" : lambda x: True if re.match("\#[0-9a-f]{6}", x) else False,
    "ecl" : lambda x: True if (len(x) == 3 and x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) else False,
    "pid" : lambda x: True if len(x) == 9 and re.match("[0-9]{9}", x) else False
    }


def validate_chunk(chunk):

    valid_fields = []
    values = chunk.replace("\n", " ").split(" ")
    for value in values:
        value = value.strip()
        if not value:
            continue
        key, v = value.split(":")
        if key in regex.keys():
            if regex.get(key)(v):
                valid_fields.append(key)
        
    if len(valid_fields) == 7:
        return True
    return False

i = 0
for line in f.readlines():
    if line.strip() != "":
        if i > len(chunks) -1:
            chunks.append("")
            
        chunks[i] += line
    else:
        i += 1



for c in chunks:
    if (validate_chunk(c)):
        valid_passports += 1



print("Valid: ", valid_passports)
