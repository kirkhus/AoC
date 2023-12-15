
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
    _source_start = 0
    _destination_start = 0
    _range = 0

    def __init__(self, name):
        self._name = name
        self._source_start = 0
        self._destination_start = 0
        self._range = 0


    def add_dest_source(self, dest, src, r):
        print("Adding for ", self._name)
        dest, src, r = [int(x) for x in [dest, src, r]]
        self._destination = dest
        self._source = src
        self._range = r

    def has_source(self, seed):
        return seed >= self._source and seed <= (self._source + self._range)
    
    def get_destination(self, seed):
        index = seed - self._source + 1
        return self._dest + index 

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



