
import numpy as np

def exist(value):
    return len(elvesSet.intersection(set([tuple(x) for x in value]))) > 0

def getDoublons(l):
    Ds = [] # doublons
    noDs = list(set(l))
    for x in noDs:
        if l.count(x) > 1:
            Ds.append(x)
    return Ds

elves = []
for y, line in enumerate(open('./Kapy/day23/inputTest.txt', 'r').read().split('\n')):
    for x, elem in enumerate(line):
        if elem == '#':
            elves.append((x,y))
elves = np.array(elves)

prios = [((0, -1), (1, -1), (-1, -1)), # N NE NW
         ((0, 1), (1, 1), (-1, 1)), # S SE SW
         ((-1, 0), (-1, -1), (-1, 1)), # W NW SW
         ((1, 0), (1, -1), (1, 1))] # E NE SE

around = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

n = 1
while True:
    propos = []
    elvesSet = set([tuple(x) for x in elves])
    for elf in elves:
        moved = False
        if exist(elf + around):
            for dir in prios:
                if not exist(elf + dir):
                    propos.append(elf + dir[0])
                    moved = True
                    break
        if not moved:
            propos.append(elf)
    
    propos = [tuple(x) for x in propos]
    if elvesSet == set(propos): # no one moved
        break
    else:
        staticElves = getDoublons(propos)
        for i, p in enumerate(propos):
            if p not in staticElves:
                elves[i] = propos[i]
        prios.append(prios.pop(0))
    n += 1

print(n)