
input_ = open("input").read()

shortest_marker = 0
shortest_message = 0

marker = 4
message = 14

found_marker = False
found_message = False

for i, c in enumerate(input_):
    if not found_marker:
        slice_marker = set(input_[i-1:i+marker-1])
        if len(slice_marker) == marker:
            shortest_marker = i+marker-1
            found_marker = True
            
    if not found_message:
        slice_message =  set(input_[i-1:i + message -1])
        if len(slice_message) == message:
            shortest_message = i+message-1
            found_messsage = True

print("Part 1:", shortest_marker)
print("Part 2:", shortest_message)



