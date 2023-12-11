with open("day 11\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: list(x.rstrip("\n")), data))
    #expansion of universe
    blank = [[], []]
    for index, row in enumerate(data):
        if '#' not in row:
            blank[0].append(index)
    for x in range(len(data[0])):
        col=[]
        for y in range(len(data)):
            col.append(data[y][x])
        if '#' not in col:
            blank[1].append(x)
    # count =0
    # for x in blank[0]:
    #     data.insert(x+count, ['.']*len(data[0]))
    #     count+=1
    # count = 0
    # for x in blank[1]:
    #     for y in range(len(data)):
    #         data[y].insert(x+count, '.')
    #     count+=1
    galaxies = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]=="#":
                offsety= len(list(filter(lambda z: z<y, blank[0])))
                offsetx= len(list(filter(lambda z: z<x, blank[1])))
                galaxies.append([y+ (999999*offsety),x+ (999999*offsetx)])
    
    from itertools import combinations
    totaldistances = 0
    for combo in combinations(galaxies, 2):
        totaldistances+= abs(combo[0][0]- combo[1][0]) + abs(combo[0][1]- combo[1][1])
    print(totaldistances)