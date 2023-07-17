import itertools as iter

dir = dict()
for line in open('./2016/day22/test.txt', 'r').readlines():
    info = line.split()
    pos = tuple([int(x[1:]) for x in info[0].split('-')[1:]])
    dir[pos] = {'used':int(info[2][:-1]), 'avail':int(info[3][:-1])}

def getAround(pos):
    p1 = (pos[0], pos[1]+1)
    p2 = (pos[0], pos[1]-1)
    p3 = (pos[0]+1, pos[1])
    p4 = (pos[0]-1, pos[1])
    return [x for x in [p1, p2, p3, p4] if x[0]>=0 and x[1]>=0 and x[0]<=2 and x[1]<=2] #and x[0]<=36 and x[1]<=27]

def getDispo(posList):
    for p in iter.permutations(posList,2):
        used = dir[p[0]]['used']
        avail = dir[p[1]]['avail']
        if used > 0 and avail >= used:
            yield p

for pos in dir:
    for d in getDispo(getAround(pos)+[pos]):
        print(d)