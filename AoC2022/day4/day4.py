
COMPLETE_OVERLAPPING = 2
PARTIAL_OVERLAPPING = 1

def get_list(pair):
    from_, to = pair.split("-")
    return range(int(from_), int(to)+1)

def is_overlapping(range_, list_):
    start, end = map(lambda x: int(x), range_.split("-"))

    if start in list_ and end in list_:
        return COMPLETE_OVERLAPPING

    if start in list_ or end in list_:
        return PARTIAL_OVERLAPPING

count_complete_overlap = 0
count_partial_or_complete_overlap = 0

for line in open("input").readlines():

    pair1, pair2 = line.split(",")

    pair1_list = get_list(pair1)
    pair2_list = get_list(pair2)

    if is_overlapping(pair1, pair2_list) == COMPLETE_OVERLAPPING or is_overlapping(pair2, pair1_list) == COMPLETE_OVERLAPPING:
        count_complete_overlap += 1
        count_partial_or_complete_overlap += 1
    elif is_overlapping(pair1, pair2_list) == PARTIAL_OVERLAPPING or is_overlapping(pair2, pair1_list) == PARTIAL_OVERLAPPING:
        count_partial_or_complete_overlap += 1

print("Complete overlapping count: ", count_complete_overlap)
print("Partial or complete overlapping count: ", count_partial_or_complete_overlap)
    
    
