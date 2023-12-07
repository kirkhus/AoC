
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
values ={}


class Almanac:
    _name = ""
    _destination = []
    _source = []

    def __init__(self, name):
        self._name = name
        self._destination = []
        self._source = []


    def add_dest_source(self, dest, src, length):
        dest, src, length = [int(x) for x in [dest, src, length]]
        self._destination.extend(list(range(dest, dest+length)))
        self._source.extend(list(range(src, src + length)))

    def __repr__(self):
        return f"{self._name} {self._destination} {self._source}"


def process_chuck(chunk):
    if not chunk:
        return
    
    if _SEEDS in chunk[0]: # special case
        seeds = chunk[0].split(" ")[1:]
        values[_SEEDS] = seeds
        return
    
    values[chunk[0]] = []
    key = chunk[0]
    almanac = Almanac(key)
    for value in chunk[1:]:
        destination, source, range = value.split(" ")
        almanac.add_dest_source(destination, source, range)
    
    
    values[key] = almanac

with open("./input55.txt") as fd:
    chunk = []
    for line in fd:
        line = line.strip()
        if ":" in line: # new chuck
            process_chuck(chunk)
            chunk = []
        if line: # remove empty lines
            chunk.append(line)

    
    process_chuck(chunk)



for seed in values[_SEEDS]:
    position = int(seed)
    for key in keys:
        almanac = values[key]
        if position in almanac._source:
            position = almanac._source[almanac._source.index(position)]

    print(seed, position)
    