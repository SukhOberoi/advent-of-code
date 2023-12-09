def find_diff_seq(seqs):
    new=[]
    for a, b in zip(seqs[-1], seqs[-1][1:]):
        new.append(b-a)
    seqs.append(new)
    return seqs

with open("day 9\\input.txt", "r") as file:
    data = file.readlines()
    sumval=0
    for line in data:
        line = [list(map(lambda x: int(x), line.rstrip("\n").split()))]
        while True:
            add=line[-1][0]
            if line[-1].count(add) == len(line[-1]):
                depth = len(line)-2
                while depth>=0:
                    line[depth].append(line[depth][-1]+add)
                    add = line[depth][-1]
                    depth-=1
                sumval+=line[0][-1]
                break
            else:
                line = find_diff_seq(line)
    print(sumval)