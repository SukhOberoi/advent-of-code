def sort(part):
    part = part.lstrip("{").rstrip("}").split(",")
    x = int(part[0][2:])
    m = int(part[1][2:])
    a = int(part[2][2:])
    s = int(part[3][2:])
    current = "in"
    status = "None"
    while status == "None":
        for rule in workflow[current]:
            if ":" in rule:
                match rule[0]:
                    case 'x':
                        operand = x
                    case 'm':
                        operand = m
                    case 'a':
                        operand = a
                    case 's':
                        operand = s
                if rule [1] == ">":
                    if operand > int(rule[2:rule.find(":")]):
                        current = rule[rule.find(":")+1:]
                        if current in ["R", "A"]:
                            status = current
                        break
                elif rule[1] == "<":
                    if operand < int(rule[2:rule.find(":")]):
                        current = rule[rule.find(":")+1:]
                        if current in ["R", "A"]:
                            status = current
                        break
            else:
                if rule == 'R':
                    status = "R"
                    break
                elif rule == 'A':
                    status = "A"
                    break
                else:
                    current = rule
    if status == "A":
        parttotal = x+m+a+s
    elif status == "R":
        parttotal = 0
    return parttotal

with open("day 19\\input.txt", "r") as file:
    workflows, parts = file.read().split("\n\n")
    w = workflows.split()
    parts = parts.split()
    workflow = {}
    for work in w:
        ind = work.find("{")
        workflow[work[:ind]] = work[ind+1:-1].split(",")
    print(workflow)
    total = 0
    for part in parts:
        total += sort(part)
    print(total)