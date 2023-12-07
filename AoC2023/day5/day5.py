
_SEEDS = "seeds:"

keys = [
    _SEEDS,
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
    _destination = ""
    _source = ""
    _range = ""

    def __init__(self, name, destination, source, range):
        self._name = name
        self._destination = destination
        self._source = source
        self._range = range

    def __repr__(self):
        return f"{self._name} {self._destination} {self._source} {self._range}"


def process_chuck(chunk):
    if not chunk:
        return
    
    values[chunk[0]] = []

    if _SEEDS in chunk[0]: # special case
        seeds = chunk[0].split(" ")[1:]
        return
    

    print(chunk)
    key = chunk[0]
    values[key] = []
    for value in chunk[1:]:
        destination, source, range = value.split(" ")
        almanac = Almanac(key, destination, source, range)
        values[key].append(almanac)

    print(values)
    

        



with open("./input55.txt") as fd:
    chunk = []
    for line in fd:
        line = line.strip()
        if ":" in line: # new chuck
            process_chuck(chunk)
            chunk = []
        if line: # remove empty lines
            chunk.append(line)


