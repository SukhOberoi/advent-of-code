with open("day 13\\input.txt", "r") as file:
    data = file.read().split("\n\n")
    count = 0
    for pattern in data:
        pattern = pattern.split("\n")
        isSymmetrical = False
        lenpatt = len(pattern)
        for y in range(1, lenpatt):
            isSymmetrical=  list(reversed(pattern[:y]))==pattern[y:(2*y)] if 2*y < lenpatt else list(reversed(pattern[y-(lenpatt-y):y])) == pattern[y:]
            if isSymmetrical : 
                count += 100* y
                break
        if isSymmetrical == False:
            lenx = len(pattern[0])
            for x in range(1, lenx):
                for y in range(len(pattern)):                
                    isSymmetrical = list(reversed(pattern[y][:x])) == list(pattern[y][x:(2*x)]) if 2*x < lenx else list(reversed(pattern[y][x-(lenx-x):x])) == list(pattern[y][x:])
                    if isSymmetrical == False:
                        break
                if isSymmetrical:
                    count+= x
    print(count)