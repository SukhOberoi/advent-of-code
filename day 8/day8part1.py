def create_dict():
    nodes = {}
    for line in file.readlines():
        nodes[line[:3]] = [line[7:10], line[12:15]]
    return "AAA", nodes


with open("day 8\\input.txt", "r") as file:
    dirs = file.readline().rstrip("\n")
    file.readline()
    current, nodes = create_dict()
    count =0
    while current != "ZZZ":
        for dir in dirs:
            if dir == "L":
                current = nodes[current][0]
            elif dir == "R":
                current = nodes[current][1]
            count+=1
            if current == "ZZZ":
                break
    print(count)