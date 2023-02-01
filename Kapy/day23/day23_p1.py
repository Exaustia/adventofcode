
import numpy as np

around = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
def someoneAround(elf):
    for pos in around:
        if exist(elves, elf + pos):
            return True
    return False

def exist(arr, value):
    for x in arr:
        if not(False in (x == value)):
            return True
    return False

elves = []
for y, line in enumerate(open('./Kapy/day23/inputTest.txt', 'r').read().split('\n')):
    for x, elem in enumerate(line):
        if elem == '#':
            elves.append((x,y))
elves = np.array(elves)

prios = [(0, -1), (1, -1), (-1, -1), # N NE NW
         (0, 1), (1, 1), (-1, 1), # S SE SW
         (-1, 0), (-1, -1), (-1, 1), # W NW SW
         (1, 0), (1, -1), (1, 1)] # E NE SE

while True:
    propos = []
    for elf in elves:
        moved = False
        if someoneAround(elf):
            for dir in prios:
                if not exist(elves, elf + dir):
                    propos.append(elf + dir)
                    moved = True
                    break
        if not moved:
            propos.append(elf)
    
    if set([tuple(x) for x in elves]) == set([tuple(x) for x in propos]): # no one moved
        break
    else:
        prios = prios[3:] + prios[:3]

print(elves)