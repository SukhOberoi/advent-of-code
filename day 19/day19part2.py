def sort(current, x,m,a,s):
    if current == "R":
        return 0
    elif current == "A":
        return len(x)*len(m)*len(a)*len(s)
    total = 0
    for rule in workflow[current]:
        if ":" in rule:
            colonind = rule.find(":")
            if rule [1] == ">":
                match rule[0]:
                    case 'x':
                        total += sort(rule[colonind+1:], range(int(rule[2:colonind])+1, x[-1]+1), m, a, s)
                        x=range(x[0],int(rule[2:colonind])+1)
                    case 'm':
                        total += sort(rule[colonind+1:], x, range(int(rule[2:colonind])+1, m[-1]+1), a, s)
                        m=range(m[0],int(rule[2:colonind])+1)
                    case 'a':
                        total += sort(rule[colonind+1:], x, m, range(int(rule[2:colonind])+1, a[-1]+1), s)
                        a=range(a[0],int(rule[2:colonind])+1)
                    case 's':
                        total += sort(rule[colonind+1:], x, m, a, range(int(rule[2:colonind])+1, s[-1]+1))
                        s=range(s[0],int(rule[2:colonind])+1)
            
            elif rule[1] == "<":
                match rule[0]:
                    case 'x':
                        total+= sort(rule[colonind+1:], range(x[0], int(rule[2:colonind])), m, a, s)
                        x=range(int(rule[2:colonind]), x[-1]+1)
                    case 'm':
                        total+=sort(rule[colonind+1:], x, range(m[0], int(rule[2:colonind])), a, s)
                        m=range(int(rule[2:colonind]), m[-1]+1)
                    case 'a':
                        total+=sort(rule[colonind+1:], x, m, range(a[0], int(rule[2:colonind])), s)
                        a=range(int(rule[2:colonind]), a[-1]+1)
                    case 's':
                        total+=sort(rule[colonind+1:], x, m, a, range(s[0], int(rule[2:colonind])))
                        s=range(int(rule[2:colonind]), s[-1]+1)
        else:
            total += sort(rule, x, m, a, s)
    return total

with open("day 19\\input.txt", "r") as file:
    workflows, parts = file.read().split("\n\n")
    w = workflows.split()
    parts = parts.split()
    workflow = {}
    for work in w:
        ind = work.find("{")
        workflow[work[:ind]] = work[ind+1:-1].split(",")
    total = 0
    total = sort("in", range(1,4001),range(1,4001),range(1,4001),range(1,4001))
    print(total)
