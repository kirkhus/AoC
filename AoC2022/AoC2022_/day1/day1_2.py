
list_ = []
calories = 0

for x in open("input.txt").readlines():
    if x.strip():
        calories += int(x)
    else:
        list_.append(calories)
        calories = 0

sorted_ = sorted(list_)
print("Top: ", sorted_[-1:])
print("Top 3: ", sum(sorted(list_)[-3:]))

