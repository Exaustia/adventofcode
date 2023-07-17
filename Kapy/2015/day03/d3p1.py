
def addTuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

dirs = {
    '>':(1,0),
    '<':(-1,0),
    '^':(0,1),
    'v':(0,-1)
}

pos = (0,0)
posList = {(0,0)}
input = open('./2015/day03/input.txt', 'r').read()
for d in input:
    pos = addTuples(pos, dirs[d])
    posList.add(pos)

print(len(posList))