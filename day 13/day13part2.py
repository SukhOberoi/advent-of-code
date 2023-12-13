with open("day 13\\input.txt", "r") as file:
    data = file.read().split("\n\n")
    count = 0
    for pattern in data:
        pattern = pattern.split("\n")
        isSymmetrical = False
        lenpatt = len(pattern)
        for y in range(1, lenpatt):
            # print((list(reversed(pattern[:y])), pattern[y:(2*y)]) if 2*y < lenpatt else (list(reversed(pattern[y-(lenpatt-y):y])) , pattern[y:]))
            wrong = 0
            if 2*y<lenpatt:
                r = list(reversed(pattern[:y]))
                l = pattern[y:(2*y)]
            else:
                r = list(reversed(pattern[y-(lenpatt-y):y])) 
                l = pattern[y:]
            for i in range(len(r)):
                for j in range(len(r[i])):
                    if r[i][j] != l[i][j]:
                        wrong+=1
                    if wrong!=1 and wrong >0:
                        break
                if wrong !=1 and wrong >0:
                    break
            if wrong!=1:
                continue
            else:
                count += 100* y
                isSymmetrical=True
                break
        if isSymmetrical == False:
            lenx = len(pattern[0])
            for x in pattern:
                print(x)
            for x in range(1, lenx):
                wrong=0
                for y in range(len(pattern)):                
                    isSymmetrical = list(reversed(pattern[y][:x])) == list(pattern[y][x:(2*x)]) if 2*x < lenx else list(reversed(pattern[y][x-(lenx-x):x])) == list(pattern[y][x:])
                    if 2*x < lenx:
                        r=list(reversed(pattern[y][:x]))
                        l=list(pattern[y][x:(2*x)])
                    else:
                        r=list(reversed(pattern[y][x-(lenx-x):x]))
                        l= list(pattern[y][x:])
                    print(r,l)
                    for i in range(len(r)):
                        if r[i] != l[i]:
                            wrong+=1
                            print("wrong")
                        if wrong!=1 and wrong > 0:
                            break
                    if wrong!=1 and wrong >0:
                        break
                if wrong!=1:
                    continue
                else:
                    count+=x
                    break
    print(count)