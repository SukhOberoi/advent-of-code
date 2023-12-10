def find_S():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                return i,j



def look(dir):
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
        if look("S"):
            current[0]+=1
        elif look("N"):
            current[0]-=1
        elif look("W"):
            current[1]-=1
        elif look("E"):
            current[1]+=1
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
    for x in data:
        print(x)
    si, sj = find_S()
    count = 0
    current = [si, sj]
    print(current)
    prev = ""
    current = findadj(current)
    print(current)
    count+=1
    while(current!=[si,sj]):
        print(data[current[0]][current[1]])
        current = findadj(current)
        count+=1
    print(count//2)