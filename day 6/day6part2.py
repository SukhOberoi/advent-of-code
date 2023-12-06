with open("day 6\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x.split(), data))
    time = ""
    distanceToBeat = ""
    for x in data[0][1:]:
        time+=x
    for x in data[1][1:]:
        distanceToBeat+=x
    time = int(time)
    distanceToBeat = int(distanceToBeat)
    waysToWin=0
    distance=0
    for timeHeld in range(time):
        speed=timeHeld
        timeLeft= time-timeHeld
        distance= timeLeft*speed
        if distance>distanceToBeat:
            waysToWin+=1
    print(waysToWin)