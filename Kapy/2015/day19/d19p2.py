
rules = {}
input = open('./2015/day19/input.txt', 'r').read().splitlines()
for i, line in enumerate(input):
    if i == 44:
        medString = line
    elif i < 43:
        line = line.split()
        if line[0] not in rules.keys():
            rules.update({line[0]:[line[2]]})
        else:
            l = rules[line[0]]
            l.append(line[2])
            rules.update({line[0]:l})

def ungroupMol(string):
    skip = False
    medicine = []
    for i in range(len(string)):
        if skip:
            skip = False
            continue
        if i+1 < len(string):
            if string[i+1].isupper() or string[i+1] == 'e':
                medicine.append(string[i])
            else:
                medicine.append(string[i]+string[i+1])
                skip = True
        else:
            medicine.append(string[i])
    return medicine

#medString = 'HOHOHO'
medicine = ungroupMol(medString)
molSet = set('e')
steps = 0
toValid = 1
while True:
    steps += 1
    newMol = set()
    for mol in molSet:
        molList = list(mol)
        for i,atom in enumerate(molList):
            if atom in rules.keys():
                for rempl in rules[atom]:
                    newMol.add(tuple(molList[0:i] + ungroupMol(rempl) + molList[i+1:]))
    molSet = set()
    for mol in newMol:
        if list(mol)[:toValid] == medicine[:toValid]:
            molSet.add(mol)
    if len(molSet) == 0:
        molSet = newMol.copy()
    else:
        toValid += 1
        
    if tuple(medicine) in molSet:
        break
    if toValid > len(medicine):
        print('cassé')
        break

print(steps)