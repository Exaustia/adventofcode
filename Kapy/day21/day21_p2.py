
monkeys = {}
for line in open('./Kapy/day21/inputTest.txt', 'r').read().split('\n'):
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
                number = getNumber(monkeys[m][2])
            if monkeys[m][2] == enfant:
                number = getNumber(monkeys[m][0])
            if monkeys[m][0] == enfant or monkeys[m][2] == enfant:
                enfant = m
                operations.insert(0,(number, monkeys[m][1]))
                break

print(operations)
