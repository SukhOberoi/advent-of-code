from functools import reduce

with open("day 3\\input.txt", "r") as file:
    data = file.readlines()
    data = list(map(lambda x: x.rstrip("\n"), data))
    linelen= len(data[0])
    nums={}
    for line in data:
        i=0
        while i < linelen:
            if line[i].isdigit():
                x=0
                while line[i:i+x+1].isnumeric() and i+x<linelen:
                    x+=1
                if not nums.get(data.index(line)):
                    nums[data.index(line)]=[]
                nums[data.index(line)].append([line[i:i+x], i, i+x])    #(lineNo, start index of num, end index of num)  = num(string)
                i=i+x+1
            else:
                i+=1
    specialchars=[]
    finalsum=0
    for line in data:
        for i in range(linelen):
            if line[i]=='*':
                gearcount=0
                gears=[]
                for num in nums[data.index(line)]:
                    if num[1]-1 == i or num[2] == i:
                        gearcount+=1
                        gears.append(int(num[0]))
                
                for num in nums[data.index(line)-1]:
                    if i in range(num[1]-1, num[2]+1):
                        gearcount+=1
                        gears.append(int(num[0]))
                
                for num in nums[data.index(line)+1]:
                    if i in range(num[1]-1, num[2]+1):
                        gearcount+=1
                        gears.append(int(num[0]))
                if gearcount==2:
                    finalsum+= int(reduce(lambda x, y: x*y, gears))
    print(finalsum)
                # specialchars.append((data.index(line),i))
    # finalSum=0
    # for (lineno, index) in specialchars:
    #     gearparts = []
    #     if nums.get(lineno):
    #         for num in nums.get(lineno): #same line
    #             numstoremove=[]
    #             if index == num[1]-1 or index == num[2]:
    #                 gearparts.append(int(num[0]))
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno).remove(num)
    #         if nums.get(lineno)== []:
    #                 nums.pop(lineno)
    #     if nums.get(lineno-1) and lineno!=0: #line before char
    #         for num in nums.get(lineno-1):
    #             numstoremove=[]
    #             if index in range(num[1]-1, num[2]+1):
    #                 gearparts.append(int(num[0]))
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno-1).remove(num)
    #         if nums.get(lineno-1)== []:
    #                 nums.pop(lineno-1)
    #     if nums.get(lineno+1):
    #         for num in nums.get(lineno+1): #line after char
    #             numstoremove=[]
    #             if index in range(num[1]-1, num[2]+1):
    #                 gearparts.append(int(num[0]))
    #                 numstoremove.append(num)
    #         for num in numstoremove:
    #             nums.get(lineno+1).remove(num)
    #         if nums.get(lineno+1)== []:
    #                 nums.pop(lineno+1)
    #     if len(gearparts) == 2:
    #         ratio = int(reduce(lambda x, y: x*y, gearparts))
    #         finalSum+=ratio
    # print(finalSum)