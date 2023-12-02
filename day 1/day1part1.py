with open("day 1\input1.txt", "r") as file:
    data = file.readlines()
    totalValue= 0
    for line in data:
        l = list(line)
        print(l)
        nums = list(filter(lambda x: x.isnumeric(), l))
        print(nums)
        calibrationValue = int(nums[0]+nums[-1])
        print(calibrationValue)
        totalValue+=calibrationValue
    print(totalValue)