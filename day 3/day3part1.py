with open("day 3\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x.rstrip("\n"), data))
    linelen= len(data[0])
    specialchars=[]
    for line in data:
        for i in range(linelen):
            if line[i]!='.' and not line[i].isdigit():
                specialchars.append((data.index(line),i))
    # nums={}
    finalsum=0
    for line in data:
        i=0
        while i < linelen:
            if line[i].isdigit():
                x=0
                while line[i:i+x+1].isnumeric() and i+x<linelen:
                    x+=1
                # if not nums.get(data.index(line)):
                #     nums[data.index(line)]=[]
                if (data.index(line), i-1) in specialchars or (data.index(line), i+x) in specialchars:
                    finalsum+=int(line[i:i+x])
                    print("added", line[i:i+x])
                else:
                    for z in range(i-1, i+x+1):
                        if (data.index(line)+1, z) in specialchars or (data.index(line)-1, z) in specialchars:
                            finalsum+= int(line[i:i+x])
                            print("added", line[i:i+x])
                # nums[data.index(line)].append([line[i:i+x], i, i+x])    #(lineNo, start index of num, end index of num)  = num(string)
                i=i+x+1
            else:
                i+=1
    print(finalsum)

    
    # finalSum=0
    # for (lineno, index) in specialchars:
    #     if nums.get(lineno):
    #         for num in nums.get(lineno): #same line
    #             numstoremove=[]
    #             if index == num[1]-1 or index == num[2]:
    #                 finalSum+=int(num[0])
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno).remove(num)
    #         if nums.get(lineno)== []:
    #                 nums.pop(lineno)
    #     if nums.get(lineno-1) and lineno!=0: #line before char
    #         for num in nums.get(lineno-1):
    #             numstoremove=[]
    #             if index in range(num[1]-1, num[2]+1):
    #                 finalSum+=int(num[0])
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno-1).remove(num)
    #         if nums.get(lineno-1)== []:
    #                 nums.pop(lineno-1)
    #     if nums.get(lineno+1):
    #         for num in nums.get(lineno+1): #line after char
    #             numstoremove=[]
    #             if index in range(num[1]-1, num[2]+1):
    #                 finalSum+=int(num[0])
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno+1).remove(num)
    #         if nums.get(lineno+1)== []:
    #                 nums.pop(lineno+1)
    # print(finalSum)