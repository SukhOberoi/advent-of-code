def mirr(new_coords, dirn):
    next_tile = data[new_coords[0]][new_coords[1]]
    match next_tile:
        case '.':
            calcEnergized(new_coords, dirn)
        case '/':
            if dirn == "E":
                calcEnergized(new_coords, "N")
            elif dirn == "S":
                calcEnergized(new_coords, "W")
            elif dirn == "W":
                calcEnergized(new_coords, "S")
            elif dirn == "N":
                calcEnergized(new_coords, "E")
        case '|':
            if dirn in ["W", "E"]:
                calcEnergized(new_coords, "N")
                calcEnergized(new_coords, "S")
            elif dirn in ["S", "N"]:
                calcEnergized(new_coords, dirn)
        case '-':
            if dirn in ["S", "N"]:
                calcEnergized(new_coords, "E")
                calcEnergized(new_coords, "W")
            elif dirn in ["E", "W"]:
                calcEnergized(new_coords, dirn)
        case "\\": # \
            if dirn == "E":
                calcEnergized(new_coords, "S")
            elif dirn == "N":
                calcEnergized(new_coords, "W")
            elif dirn == "W":
                calcEnergized(new_coords, "N")
            elif dirn == "S":
                calcEnergized(new_coords, "E")

def calcEnergized(coords:tuple, dirn):
    if not loop.get((coords, dirn)):
        if coords not in energized:
            energized.append(coords)
            loop[(coords, dirn)]="visited"
    else:
        return
    match dirn:
        case "N":
            if coords[0]-1>=0:
                new_coords = coords[0]-1, coords[1]
            else:
                return
        case "E":
            if coords[1]+1<len(data[0]):
                new_coords = coords[0], coords[1]+1
            else:
                return
        case "S":
            if coords[0]+1<len(data):
                new_coords = coords[0]+1, coords[1]
            else:
                return
        case "W":
            if coords[1]-1>=0:
                new_coords = coords[0], coords[1]-1
            else:
                return
    mirr(new_coords, dirn)

import sys
sys.setrecursionlimit(500000)

with open("day 16\\input.txt", "r") as file:
    data = list(map(lambda x: x.rstrip("\n"), file.readlines()))
    for x in data:
        print(x)
    enerconfigs=[]
    for i in range(len(data)):
        energized = []
        loop={}
        energized.append((i,0))
        mirr((i,0), "E")
        print("Hello")
        enerconfigs.append(len(energized))
        energized = []
        energized.append((i,len(data[0])-1))
        mirr((i,len(data[0])-1), "W")
        enerconfigs.append(len(energized))
    for i in range(len(data[0])):
        energized = []
        loop={}
        energized.append((0,i))
        mirr((0,i), "S")
        print("Sukh")
        enerconfigs.append(len(energized))
        energized = []
        energized.append((len(data)-1, i))
        mirr((len(data)-1, i), "N")
        enerconfigs.append(len(energized))
        
    print(max(enerconfigs))