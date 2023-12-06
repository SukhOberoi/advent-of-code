with open("day 5\\input.txt", "r") as file:
    data = file.read()
    data = data.split("\n\n")
    seeds = list(map(lambda x: int(x),data[0][7:].split()))
    seedLoc=[]
    seedSoil = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[1][data[1].find(":\n")+2:].rstrip("\n").split("\n")))]
    soilFertilizer = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[2][data[2].find(":\n")+2:].rstrip("\n").split("\n")))]
    fertilizerWater = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[3][data[3].find(":\n")+2:].rstrip("\n").split("\n")))]
    waterLight = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[4][data[4].find(":\n")+2:].rstrip("\n").split("\n")))]
    lightTemp = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[5][data[5].find(":\n")+2:].rstrip("\n").split("\n")))]
    tempHumid = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[6][data[6].find(":\n")+2:].rstrip("\n").split("\n")))]
    humidLoc = [list(map(int, i)) for i in list(map(lambda x: x.split(), data[7][data[7].find(":\n")+2:].rstrip("\n").split("\n")))]
    seeds = list(zip(seeds[::2], seeds[1::2]))
    seedRanges= []
    for (start, length) in seeds:
        seedRanges.append(range(start, start+length))
    loc=0
    found = False
    while True:
        humid = loc
        for lh in humidLoc:
            if loc in range(lh[0], lh[0] + lh[2]):
                humid = lh[1]+(loc-lh[0])
                break
        temp = humid
        for ht in tempHumid:
            if humid in range(ht[0], ht[0] + ht[2]):
                temp = ht[1]+(humid-ht[0])
                break
        light = temp
        for tl in lightTemp:
            if temp in range(tl[0], tl[0] + tl[2]):
                light = tl[1]+(temp-tl[0])
                break
        water = light
        for lw in waterLight:
            if light in range(lw[0], lw[0] + lw[2]):
                water = lw[1]+(light-lw[0])
                break
        fertilizer = water
        for wf in fertilizerWater:
            if water in range(wf[0], wf[0] + wf[2]):
                fertilizer = wf[1]+(water-wf[0])
                break
        soil = fertilizer
        for fs in soilFertilizer:
            if fertilizer in range(fs[0], fs[0] + fs[2]):
                soil = fs[1]+(fertilizer-fs[0])
                break
        seed = soil
        for ss in seedSoil:
            if soil in range(ss[0], ss[0] + ss[2]):
                seed = ss[1]+(soil-ss[0])
                break
        for seedrange in seedRanges:
            if seed in seedrange and found:
                print(loc)
                exit()
            if seed in seedrange and not found:
                loc-=10000
                found = True
        if found:
            loc+=1
        else:
            loc+=10000
    
    
    