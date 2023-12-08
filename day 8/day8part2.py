def create_dict():
    nodes = {}
    starts=[]
    for line in file.readlines():
        nodes[line[:3]] = [line[7:10], line[12:15]]
        if line[:3][-1] == "A":
            starts.append(line[:3])
    return starts, nodes

def check_all(count):
    for index, node in enumerate(current):
        if node[-1]=="Z":
            whenz.append(count)
            current.pop(index)
        
from math import lcm
from functools import reduce


with open("day 8\\input.txt", "r") as file:
    dirs = file.readline().rstrip("\n")
    file.readline()
    current, nodes = create_dict()
    count =0
    whenz= []
    while len(current):
        for dir in dirs:
            print(current)
            if dir == "L":
                for i in range(len(current)):
                    current[i] = nodes[current[i]][0]
            elif dir == "R":
                for i in range(len(current)):
                    current[i] = nodes[current[i]][1]
            count+=1
            check_all(count)
            if not len(current):
                break
    print(reduce(lcm, whenz)) 