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
    for seed in seeds:
        soil=seed
        for ss in seedSoil:
            if seed in range(ss[1], ss[1]+ss[2]):
                soil= ss[0]+(seed-ss[1])
                break
        fertilizer=soil
        for sf in soilFertilizer:
            if soil in range(sf[1], sf[1]+sf[2]):
                fertilizer = sf[0] + (soil-sf[1])
                break
        water=fertilizer
        for fw in fertilizerWater:
            if fertilizer in range(fw[1], fw[1]+fw[2]):
                water = fw[0] + (fertilizer-fw[1])
                break
        light=water
        for wl in waterLight:
            if water in range(wl[1], wl[1]+wl[2]):
                light = wl[0] + (water-wl[1])
                break
        temp=light
        for lt in lightTemp:
            if light in range(lt[1], lt[1]+lt[2]):
                temp = lt[0] + (light-lt[1])
                break
        humid=temp
        for th in tempHumid:
            if temp in range(th[1], th[1]+th[2]):
                humid = th[0] + (temp-th[1])
                break
        loc=humid
        for hl in humidLoc:
            if humid in range(hl[1], hl[1]+hl[2]):
                loc = hl[0] + (humid-hl[1])
                break
        seedLoc.append(loc)
    print(min(seedLoc))
        