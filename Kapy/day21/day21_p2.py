
monkeys = {}
for line in open('./Kapy/day21/input.txt', 'r').read().split('\n'):
    monkey = line.split(' ')
    if len(monkey) == 2:
        monkeys[monkey[0][:-1]] = int(monkey[1])
    else:
        monkeys[monkey[0][:-1]] = (monkey[1], monkey[2], monkey[3])

def getNumber(id):
    if isinstance(monkeys[id], int):
        return(monkeys[id])
    else:
        if monkeys[id][1] == '+':
            return getNumber(monkeys[id][0]) + getNumber(monkeys[id][2])
        if monkeys[id][1] == '-':
            return getNumber(monkeys[id][0]) - getNumber(monkeys[id][2])
        if monkeys[id][1] == '*':
            return getNumber(monkeys[id][0]) * getNumber(monkeys[id][2])
        if monkeys[id][1] == '/':
            return int(getNumber(monkeys[id][0]) / getNumber(monkeys[id][2]))

enfant = 'humn'
operations = []
while(enfant != 'root'):
    for m in monkeys:
        if isinstance(monkeys[m], tuple):
            if monkeys[m][0] == enfant:
                operations.insert(0,(monkeys[m][1], getNumber(monkeys[m][2])))
            if monkeys[m][2] == enfant:
                operations.insert(0,(getNumber(monkeys[m][0]), monkeys[m][1]))
            if monkeys[m][0] == enfant or monkeys[m][2] == enfant:
                enfant = m
                break

goal = operations[0][0] if isinstance(operations[0][0], int) else operations[0][1]
for sign, nb in operations[1:]:
    inverse = False
    if isinstance(sign, int):
        sign, nb = nb, sign
        inverse = True
    if sign == '+':
        goal = goal - nb
    if sign == '-':
        if inverse:
            goal = nb - goal
        else:
            goal = goal + nb
    if sign == '*':
        goal = int(goal / nb)
    if sign == '/':
        if inverse:
            goal = int(nb / goal)
        else:
            goal = goal * nb

print(goal)
