with open("day2\input.txt", "r") as file:
    data = file.readlines()
    totalPower=0
    for line in data:
        game= line.split(": ")
        rounds= game[1].split("; ")
        rounds[-1]= rounds[-1].rstrip("\n")
        print(rounds)
        red = 0
        green = 0
        blue = 0
        for round in rounds:
            colors = round.split(", ")
            for color in colors:
                x= color.split()
                match x[1]:
                    case 'red':
                        if red<int(x[0]):
                            red = int(x[0])
                    case 'green':
                        if green<int(x[0]):
                            green = int(x[0])
                    case 'blue':
                        if blue<int(x[0]):
                            blue = int(x[0])
        power= red* green * blue
        totalPower+=power
    print(totalPower)
                    

