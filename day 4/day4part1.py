with open("day 4\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x[10:].rstrip("\n"), data))
    wingot = list(map(lambda x: x.split(" | "), data))
    totalpoints=0
    for line in wingot:
        points=0
        wins = line[0].split()
        scratch = line[1].split()
        for num in scratch:
            if num in wins:
                if points==0:
                    points=1
                else:
                    points*=2
        totalpoints+=points
print(totalpoints)