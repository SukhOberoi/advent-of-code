with open("day 2\input.txt", "r") as file:
    data = file.readlines()
    validGames = 0
    for line in data:
        game= line.split(": ")
        rounds= game[1].split("; ")
        game = int(game[0][5:])
        rounds[-1]= rounds[-1].rstrip("\n")
        # print(game)
        print(rounds)
        red = 12
        green = 13
        blue = 14
        valid = True
        for subset in rounds:
            cubes= subset.split(", ")
            for color in cubes:
                x = color.split(" ")
                match x[1]:
                    case 'red':
                        if int(x[0])>red:
                            valid=False
                            break
                    case 'green':
                        if int(x[0])>green:
                            valid=False
                            break
                    case 'blue':
                        if int(x[0])>blue:
                            valid=False
                            break
            if valid==False:
                break
        if valid:
            validGames+=game
    print(validGames)
                    

