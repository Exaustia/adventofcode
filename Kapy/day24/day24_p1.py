
def getDir(pixel):
    if pixel == '>':
        return (1,0)
    elif pixel == '<':
        return (-1,0)
    elif pixel == 'v':
        return (0,1)
    else: # pixel == '^':
        return (0,-1)

def flatten(l):
    return [item for sublist in l for item in sublist]

def addT(t1, t2): # add two Tuples together
    return t1[0] + t2[0], t1[1] + t2[1]

def moveBliz(b, d):
    nextPos = addT(b,d)
    if nextPos in walls:
        if d == (1,0): # '>'
            nextPos = 1, b[1]
        elif d == (-1,0): # '<'
            nextPos = len(line)-2, b[1]
        elif d == (0,1): # 'v'
            nextPos = b[0], 1
        else: # d == (0,-1): # '^'
            nextPos = b[0], len(file)-2
    return nextPos

def validMoves(pos):
    valid = {addT(pos, (0,1)), addT(pos, (1, 0)), addT(pos, (0,-1)), addT(pos, (-1, 0))}
    valid = valid.difference(set(walls))
    valid = valid.difference(set(bliz['pos']))
    return valid if valid != set() else {pos}

walls = [(1, 0), (1, -1)] # adding a wall on and above the start
bliz = {'pos':[], 'dir':[]}
file = open('./Kapy/day24/input.txt', 'r').read().split('\n')
for y, line in enumerate(file):
    for x, pixel in enumerate(line):
        if pixel == '#':
            walls.append((x,y))
        elif pixel != '.':
            bliz['pos'].append((x,y))
            bliz['dir'].append(getDir(pixel))
goal = line.index('.'), len(file)-1

nbBliz = len(bliz['pos'])
meList = [(1,0)]
min = 0
while True:
    bliz['pos'] = [moveBliz(bliz['pos'][i], bliz['dir'][i]) for i in range(nbBliz)]
    meList = list(set(flatten([validMoves(me) for me in meList])))
    min += 1
    if goal in meList:
        break

print(min)