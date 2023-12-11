def find_S():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                return i,j



def look(dir, current):
    global prev
    if dir == "N":
        if current[0]-1>-1 and data[current[0]-1][current[1]] in ["|", "7", "F"]:
            prev = "S"
            # return current[0]-1, current[1]
            return 1
        return -1
    if dir == "S":
        if current[0]+1<len(data) and data[current[0]+1][current[1]] in ["|", "J", "L"]:
            prev = "N"
            # return current[0]+1, current[1]
            return 1
        return -1
    if dir == "W":
        if current[1]-1 > -1 and data[current[0]][current[1]-1] in ["-", "F", "L"]:
            prev = "E"
            # return current[0], current[1]-1
            return 1
        return -1
    if dir == "E":
        if current[1]+1 < len(data[current[0]]) and data[current[0]][current[1]+1] in ["-", "7", "J"]:
            prev = "W"
            # return current[0], current[1]+1
            return 1
        return -1



def findadj(current):
    global prev
    if data[current[0]][current[1]]=="S": #check all 4
        if look("S", current):
            current[0]+=1
            prev= "N"
        elif look("N", current):
            current[0]-=1
            prev = "S"
        elif look("W", current):
            current[1]-=1
            prev = "E"
        elif look("E", current):
            current[1]+=1
            prev = "W"
    elif data[current[0]][current[1]]=="|": #opp of prev
        if prev == "N":
            current[0]+=1
        else:
            current[0]-=1
    elif data[current[0]][current[1]]=="-": #opp of previous
        if prev == "W":
            current[1]+=1
        else:
            current[1]-=1
    elif data[current[0]][current[1]]=="F": #if prev south east, else south
        if prev == "S":
            current[1]+=1
            prev = "W"
        else:
            current[0]+=1
            prev = "N"
    elif data[current[0]][current[1]]=="J": #if prev west north, else west
        if prev == "W":
            current[0]-=1
            prev = "S"
        else:
            current[1]-=1
            prev = "E"
    elif data[current[0]][current[1]]=="L": #if prev north east, else north
        if prev == "N":
            current[1]+=1
            prev = "W"
        else:
            current[0]-=1
            prev = "S"
    elif data[current[0]][current[1]]=="7": # if prev west south, else west
        if prev == "W":
            current[0]+=1
            prev = "N"
        else:
            current[1]-=1
            prev = "E"
    return current

with open("day 10\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: list(x.rstrip("\n")), data))
    si, sj = find_S()
    path = []
    current = [si, sj]
    path.append(tuple(current))
    prev = ""
    # replace_s(si, sj)
    for x in data:
        print(x)
    current = findadj(current)
    count=0
    while(current!=[si,sj]):
        path.append(tuple(current))
        current = findadj(current)
    print(path)
    # data[si][sj]= "|"
    # for i in range(len(data)):
    #     flipswitch=False
    #     for j in range(len(data[0])):
    #         prevz=""
    #         if (i, j) in path and data[i][j] in ["F", "L"] and prevz=="":
    #             prevz=data[i][j]
            
    #         if (i, j) in path and data[i][j] == "7" and prevz == "F":
    #             prevz=""
    #         if (i, j) in path and data[i][j] == "J" and prevz == "L":
    #             prevz=""
            
    #         if (i, j) in path and data[i][j] == "7" and prevz == "L":
    #             flipswitch = not flipswitch
    #             prevz=""
                
    #         if (i, j) in path and data[i][j] == "J" and prevz == "F":
    #             flipswitch = not flipswitch
    #             prevs=""
    #         # print(prevz)
    #         if (i, j) in path and data[i][j] == "|":
    #             flipswitch= not flipswitch
    #             prevs=""
    #         if flipswitch and (i,j) not in path:
    #             count+=1
    #             print("counted", i,j)
    # print(count)
    import matplotlib.path

    poly = matplotlib.path.Path(path)
    num = sum(1 for y in range(1, len(data)) for x in range(1, len(data[0]) - 1)
          if (c := (y, x)) not in path and poly.contains_point(c))
    print(num)