def moveN(x,y, data):
    global weight
    global height
    if y != 0:
        data[y][x]="."
        while y-1 >= 0 and data[y-1][x] not in ["O", "#"]:
            y-=1
        data[y][x]="O"
    weight += height-y
    return data


with open("day 14\\sample.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: list(x.rstrip("\n")), data))
    weight= 0
    height = len(data)
    for x in data:
        print(x)
    print("------------")
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "O":
                data = moveN(x,y, data)
    for x in data:
        print(x)
    print(weight)
            