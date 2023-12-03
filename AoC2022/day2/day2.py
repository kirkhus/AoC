
HANDS = {
    "A" : "ROCK",
    "B" : "PAPER",
    "C" : "SCISSORS",
    "X" : "ROCK",
    "Y" : "PAPER",
    "Z" : "SCISSORS"
}

RULES = {
    "ROCK" : "SCISSORS",
    "PAPER" : "ROCK",
    "SCISSORS" : "PAPER"
}

SCORE = {
    
    "ROCK" : 1, 
    "PAPER" : 2, 
    "SCISSORS" : 3
} 


def rockpapersissor(elf, you):

    score = SCORE[HANDS[you]]

    # draw
    if HANDS[elf] == HANDS[you]:
        return score + 3

    # elf wins
    if RULES[HANDS[elf]] == HANDS[you]:
        return score

    # you win
    return score + 6

sum_ = 0

for line in open("input").readlines():
    elf, you = map(lambda x: x.strip(), line.split(" "))
    sum_ += rockpapersissor(elf, you)

print("Total score: ", sum_)
