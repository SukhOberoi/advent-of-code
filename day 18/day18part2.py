def findedges():
    currx, curry = 0,0
    maxx, maxy=0,0
    minx, miny=0,0
    for move in data:
        match move[0]:
            case "R":
                currx += int(move[1])
                maxx= max(maxx, currx)
            case "L":
                currx -= int(move[1])
                minx= min(minx, currx)
            case "U":
                curry -= int(move[1])
                miny = min(miny, curry)
            case "D":
                curry += int(move[1])
                maxy = max(maxy, curry)
    return minx, miny, maxx, maxy


def makePath():
    global distance
    
    curry = abs(miny) if miny !=0 else 0
    currx = abs(minx) if minx !=0 else 0
    points.append((currx, curry))
    distance=1
    for line, move in enumerate(data):
        match move[0]:
            case "R":
                currx+=int(move[1])
            case "L":
                currx-=int(move[1])
            case "U":
                curry-=int(move[1])
            case "D":
                curry+=int(move[1])
        points.append((currx, curry))
        distance += int(move[1])
    
    
def area_by_shoelace(x, y):
	return abs(sum(x[i-1]*y[i]-x[i]*y[i-1] for i in range(len(x)))) / 2.


import sys
sys.setrecursionlimit(100000)
with open("day 18\\input.txt", "r") as file:
    data = list(map(lambda x: x.rstrip("\n").split(), file.readlines()))
    for index, instruction in enumerate(data):
        data[index][1] = int(instruction[2][2:-2], 16)
        print(instruction[2])
        print(instruction[2][-2])
        match instruction[2][-2]:
            case "0":
                data[index][0]= "R"
            case "1":
                data[index][0]= "D"
            case "2":
                data[index][0]= "L"
            case "3":
                data[index][0]= "U"
    
    
    for x in data:
        print(x)
    minx, miny, maxx, maxy = findedges()
    print(minx, miny, maxx, maxy)
    distance =0
    points=[]
    makePath()
    print(points)
    x, y = zip(*points)
    print(area_by_shoelace(x,y)+ (distance//2) +1)
    