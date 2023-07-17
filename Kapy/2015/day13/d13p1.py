import itertools as iter

happyList = {}
for line in open('./2015/day13/input.txt', 'r').read().split('\n'):
    l = line.split(' ')
    p1 = l[0]
    mult = 1 if l[2] == 'gain' else -1
    nb = int(l[3])
    p2 = l[-1][:-1]
    if p1 not in happyList:
        happyList.update({p1:{}})
    happyList[p1].update({p2:mult*nb})

happies = []
for table in iter.permutations(happyList.keys()):
    happiness = 0
    for i, guest in enumerate(table):
        if i == 0:
            v1 = table[-1]
        else:
            v1 = table[i-1]
        if i == len(table)-1:
            v2 = table[0]
        else:
            v2 = table[i+1]
        happiness += happyList[guest][v1] + happyList[guest][v2]
    happies.append(happiness)

print(max(happies))