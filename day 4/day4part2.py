from functools import reduce
with open("day 4\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x[10:].rstrip("\n"), data))
    wingot = list(map(lambda x: x.split(" | "), data))
    cards = [1]*len(wingot)
    for lineno, line in enumerate(wingot):
        points=0
        wins = line[0].split()
        scratch = line[1].split()
        for num in scratch:
            if num in wins:
                points+=1
                if lineno+points < len(wingot):
                    cards[lineno+points]+=cards[lineno]
    print(int(reduce(lambda x, y: x+y, cards)))