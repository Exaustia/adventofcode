
realOne = {}
for line in open('./2015/day16/MFCSAM.txt', 'r').read().split('\n'):
    l = line.split()
    realOne.update({l[0][:-1] : int(l[1])})

input = open('./2015/day16/input.txt', 'r').read().split('\n')
for i, line in enumerate(input):
    l = line.split()
    SueN = {l[2][:-1]:int(l[3][:-1]),
            l[4][:-1]:int(l[5][:-1]),
            l[6][:-1]:int(l[7])}
    ok = True
    for x in SueN.keys():
        if SueN[x] != realOne[x]:
            ok = False
            break
    if ok:
        break
print(i+1)