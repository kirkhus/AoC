
max_calories = 0
calories = 0

for x in open("input.txt").readlines():

    if x.strip():
        calories += int(x)
    else:
        if calories > max_calories:
            max_calories = calories
            print("New max: ", calories)
        calories = 0


