def findarr(row, blocks):
    row = list(row)
    print(row)
    try:
        pos = row.index("?")
        count=0
        row[pos]="."
        print(row)
        count+= findarr(row, blocks)
        row[pos]="#"
        print(row)
        count+= findarr(row,blocks)
        return count
    except ValueError:
        return checkblocks(row, blocks)

def checkblocks(row, blocks):
    testblock=[]
    count=0
    for char in row:
        if char == "#":
            count+=1
        elif count != 0:
            testblock.append(count)
            count=0
    if count:
        testblock.append(count)
    if testblock==blocks:
        return 1
    else:
        return 0

with open("day 12\\input.txt", "r") as file:
    data = file.readlines()
    totalarrangements=0
    for x in data:
        row, blocks=x.rstrip("\n").split(" ")
        blocks = list(map(lambda x: int(x), blocks.split(",")))
        print(list(row))
        totalarrangements+= findarr(row,blocks)
    print(totalarrangements)
    # print(findarr(".#.###.#.######", [1,3,1,6]))