
_SEEDS = "seeds:"

keys = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]


seeds = []
values = {}


class Almanac:
    _name = ""
    _destination = []
    _source = []

    def __init__(self, name):
        self._name = name
        self._destination = []
        self._source = []


    def add_dest_source(self, dest, src, length):
        print("Adding for ", self._name)
        dest, src, length = [int(x) for x in [dest, src, length]]
        self._destination.extend(range(dest, dest+length))
        self._source.extend(range(src, src + length))

    def __repr__(self):
        return f"{self._name} {self._destination} {self._source}"


def process_chuck(chunk):
    if not chunk:
        return
    
    if _SEEDS in chunk[0]: # special case
        seeds = [int(x) for x in chunk[0].split(" ")[1:]]
        values[_SEEDS] = seeds
        return
    
    values[chunk[0]] = []
    key = chunk[0]
    almanac = Almanac(key)
    for value in chunk[1:]:
        destination, source, range = value.split(" ")
        almanac.add_dest_source(destination, source, range)
    
    
    values[key] = almanac

# read input
with open("./input5.txt") as fd:
    chunk = []
    for line in fd:
        line = line.strip()
        if ":" in line: # new chuck
            process_chuck(chunk)
            chunk = []
        if line: # remove empty lines
            chunk.append(line)

    
    process_chuck(chunk)
# map seeds to final location
locations = []
for seed in values[_SEEDS]:
    original = seed
    for key in keys:
        almanac = values[key]
        if seed in  almanac._source:
            pos = almanac._source.index(seed)
            seed = almanac._destination[pos]    
    locations.append(seed)
     

print("Part 1: ", min(locations))



