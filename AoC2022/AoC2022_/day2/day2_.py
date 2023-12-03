
HANDS_ELF = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS"
}

HANDS_YOU = {
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

RULES = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

SCORE = {
    "ROCK": 1, 
    "PAPER": 2, 
    "SCISSORS": 3
} 

LOSE = "X"
DRAW = "Y"
WIN = "Z"


def get_score(elf, result):
    if result == LOSE:
        return SCORE[RULES[HANDS_ELF[elf]]]

    if result == DRAW:
        return SCORE[HANDS_ELF[elf]] + 3

    for key, value in RULES.items():
        if HANDS_ELF[elf] == value:
            return SCORE[key] + 6


def rockpapersissor1(elf, you):

    score = SCORE[HANDS_YOU[you]]

    # draw
    if HANDS_ELF[elf] == HANDS_YOU[you]:
        return score + 3

    # elf wins
    if RULES[HANDS_ELF[elf]] == HANDS_YOU[you]:
        return score

    # you win
    return score + 6
        
        
def rockpapersissor2(elf, result):
    return get_score(elf, result)
    

sum1 = 0
sum2 = 0
for line in open("input").readlines():
    elf, you = map(lambda x: x.strip(), line.split(" "))
    sum1 += rockpapersissor1(elf, you)
    sum2 += rockpapersissor2(elf, you)

print("Total score part 1: ", sum1)
print("Total score part 2: ", sum2)
