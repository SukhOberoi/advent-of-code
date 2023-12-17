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

import sys
sys.setrecursionlimit(500000)

with open("day 16\\input.txt", "r") as file:
    data = list(map(lambda x: x.rstrip("\n"), file.readlines()))
    for x in data:
        print(x)
    energized = []
    loop={}
    calcEnergized((0,0), "S")
    print(loop)
    print(len(energized))