def hashalgo(string):
    val = 0
    for char in string:
        val+=ord(char)
        val*=17
        val%=256
    return val


with open("day 15\\input.txt", "r") as file:
    data = file.read().rstrip("\n").split(",")
    finalsum=0
    for string in data:
        finalsum+=hashalgo(string)
    print(finalsum)
    