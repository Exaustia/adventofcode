
def addTuples(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

dirs = {
    '>':(1,0),
    '<':(-1,0),
    '^':(0,1),
    'v':(0,-1)
}

pos1, pos2 = (0,0), (0,0)
houses = {(0,0)}
input = open('./2015/day03/input.txt', 'r').read()
for i, d in enumerate(input):
    if i%2 == 0:
        pos1 = addTuples(pos1, dirs[d])
        pos = pos1
    else:
        pos2= addTuples(pos2, dirs[d])
        pos = pos2
    houses.add(pos)

print(len(houses))