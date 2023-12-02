with open("day 1\input1.txt", "r") as file:
    data = file.readlines()
    totalValue= 0
    digs= ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for line in data:
        digindexes= list(map(lambda x: line.find(x) if line.find(x)!= -1 else 999, digs))
        # print(digindexes)
        # print(str(digindexes.index(min(digindexes))+1))

        digindexeslast= list(map(lambda x: line.rfind(x), digs))
        # print(digindexeslast)
        # print(str(digindexeslast.index(max(digindexeslast))+1))


        l = list(line)
        nums={}
        for i in range(len(l)):
            if l[i].isdigit():
                nums[i]=l[i]
        # print(nums)


        if min(digindexes)<min(nums):
            first = str(digindexes.index(min(digindexes))+1)
        else:
            first = nums[min(nums)]
        
        if max(digindexeslast)>max(nums):
            last = str(digindexeslast.index(max(digindexeslast))+1)
        else:
            last = nums[max(nums)]

        final = int(first+last)
        # print(final)
        totalValue+=final
    print(totalValue)