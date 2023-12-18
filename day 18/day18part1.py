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
    curry = abs(miny) if miny !=0 else 0
    currx = abs(minx) if minx !=0 else 0
    lagoon[curry][currx]= "#"
    for line, move in enumerate(data):
        # print(curry, currx, line+1)
        match move[0]:
            case "R":
                for i in range(int(move[1])):
                    currx+=1
                    lagoon[curry][currx]= "#"
            case "L":
                for i in range(int(move[1])):
                    currx-=1
                    lagoon[curry][currx]= "#"
            case "U":
                for i in range(int(move[1])):
                    curry-=1
                    lagoon[curry][currx]= "#"
            case "D":
                for i in range(int(move[1])):
                    curry+=1
                    lagoon[curry][currx]= "#"


def flood_recursive(matrix):
    width = len(matrix)
    height = len(matrix[0])
    def fill(x,y,start_color,color_to_update):
        #if the square is not the same color as the starting point
        if matrix[x][y] != start_color:
            return
        #if the square is not the new color
        elif matrix[x][y] == color_to_update:
            return
        else:
            #update the color of the current square to the replacement color
            matrix[x][y] = color_to_update
            neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    fill(n[0],n[1],start_color,color_to_update)
    #pick a random starting point
    start_x = 0
    start_y = 0
    start_color = matrix[start_x][start_y]
    fill(start_x,start_y,start_color," ")
    return matrix

def pad():
    row_len = len(lagoon)
    col_len = len(lagoon[0])

    newlagoon = list()
    for n in range(row_len+2):
        if n == 0 or n == row_len + 1:
            newlagoon.append(["*"] * (col_len + 2)) 
        else:
            newlagoon.append(["*"] + lagoon[n - 1] + ["*"]) 
    return newlagoon

import sys
sys.setrecursionlimit(100000)
with open("day 18\\input.txt", "r") as file:
    data = list(map(lambda x: x.rstrip("\n").split(), file.readlines()))
    minx, miny, maxx, maxy = findedges()
    print(minx, miny, maxx, maxy)
    lagoon = [list("*"*(abs(minx)+maxx+1)) for _ in range(abs(miny)+maxy+1)]
    makePath()
    # fillPath()
    lagoon = pad()
    lagoon = flood_recursive(lagoon)


    for x in lagoon:
        print("".join(x))
    count = 0
    for x in lagoon:
        for z in x:
            if z != " ":
                count+=1
    print(count)