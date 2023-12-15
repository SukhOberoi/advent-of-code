def hashalgo(string):
    val = 0
    for char in string:
        val+=ord(char)
        val*=17
        val%=256
    return val

def minus(label):
    box = hashalgo(label)
    if boxes[box]!="":
        for index, lens in enumerate(boxes[box]):
            if lens[:len(lens)-1] == label:
                boxes[box].pop(index)
                if boxes[box] == []:
                    boxes[box]=""
                return

def equal(label, focal):
    box = hashalgo(label)
    if boxes[box]== "":
        boxes[box]= [label+focal]
    else:
        for index, lens in enumerate(boxes[box]):
            if lens[:len(lens)-1] == label:
                boxes[box][index] = label+focal
                return
        boxes[box].append(label+focal)

def count(boxes):
    focuspower=0
    for boxno, box in enumerate(boxes):
        if box != "":
            for lensno, lens in enumerate(box):
                focuspower+= (boxno+1)*(lensno+1)*int(lens[-1])
    return focuspower

with open("day 15\\input.txt", "r") as file:
    data = file.read().rstrip("\n").split(",")
    finalsum=0
    boxes = [""]*256
    for instruction in data:
        if instruction[-1]=="-":
            minus(instruction[0:len(instruction)-1])
        else:
            eqind = instruction.index("=")
            equal(instruction[0:eqind], instruction[eqind+1:])
    print(count(boxes))