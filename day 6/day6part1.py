with open("day 6\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x.split(), data))
    time = [int(x) for x in data[0][1:]]
    distance = [int(x) for x in data[1][1:]]
    sets= list(zip(time,distance))
    print(sets)
    marginError=1
    for (time, distanceToBeat) in sets:
        waysToWin=0
        distance=0
        for timeHeld in range(time):
            speed=timeHeld
            timeLeft= time-timeHeld
            distance= timeLeft*speed
            if distance>distanceToBeat:
                waysToWin+=1
        marginError*=waysToWin
    print(marginError)