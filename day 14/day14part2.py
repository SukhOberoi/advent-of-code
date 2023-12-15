
def cycle(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "O":
                ya = y
                if y != 0:
                    data[ya][x]="."
                    while ya-1 >= 0 and data[ya-1][x] not in ["O", "#"]:
                        ya-=1
                    data[ya][x]="O"
    for x in data:
        print(x)   
    print("----------------")
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] == "O":
                xa = x
                if x != 0:
                    data[y][xa]="."
                    while xa-1 >= 0 and data[y][xa-1] not in ["O", "#"]:
                        xa-=1
                    data[y][xa]="O"
    for x in data:
        print(x)   
    print("----------------")
    for y in range(len(data)-1,-1,-1):
        for x in range(len(data[0])):
            if data[y][x] == "O":
                ya = y
                if y != len(data)-1:
                    data[ya][x]="."
                    while ya+1 < len(data) and data[ya+1][x] not in ["O", "#"]:
                        ya+=1
                    data[ya][x]="O"
    for x in data:
        print(x)   
    print("----------------")
    for x in range(len(data[0])-1,-1,-1):
        for y in range(len(data)):
            if data[y][x] == "O":
                xa = x
                if x != len(data[0])-1:
                    data[y][xa]="."
                    while xa+1 < len(data[0]) and data[y][xa+1] not in ["O", "#"]:
                        xa+=1
                    data[y][xa]="O"
    for x in data:
        print(x)
    print("----------------") 
    return calcW(data)


def calcW(data):
    height = len(data)
    weight=0
    for y, row in enumerate(data):
        if "O" in row:
            weight+=(height- y)*row.count("O")
    return weight

with open("day 14\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: list(x.rstrip("\n")), data))
    weight= 0
    
    for x in data:
        print(x)
    print("------------")
    for i in range(1000):
        weight=cycle(data)
    print(weight)
            