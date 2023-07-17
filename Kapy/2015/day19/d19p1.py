
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

medicine = ungroupMol(medString)
newMol = set()
for mol in rules:
    indexes = [i for i in range(len(medicine)) if medicine[i] == mol]
    for r in rules[mol]:
        for i in indexes:
            newMol.add(tuple(medicine[0:i] + ungroupMol(r) + medicine[i+1:]))

print(len(newMol))