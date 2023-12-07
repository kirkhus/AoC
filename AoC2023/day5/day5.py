

keys = [
    "seeds:",
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]

values ={}


class Almanac:
    _name = ""
    _destination = ""
    _source = ""
    _range = []

def process_chuck(chunk):
    if not chunk:
        return
    
    values[chunk[0]] = []

    for value in chunk[1:]:
        



with open("./input55.txt") as fd:
    chunk = []
    for line in fd:
        line = line.strip()
        if ":" in line: # new chuck
            process_chuck(chunk)
            chunk = []
        if line: # remove empty lines
            chunk.append(line)


