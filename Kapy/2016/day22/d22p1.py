import itertools as iter

dir = dict()
for line in open('./2016/day22/input2.txt', 'r').readlines():
    info = line.split()
    pos = tuple([x[1:] for x in info[0].split('-')[1:]])
    dir[pos] = {'used':int(info[2][:-1]), 'avail':int(info[3][:-1])}

n = 0
for p in iter.permutations(dir.keys(),2):
    used = dir[p[0]]['used']
    avail = dir[p[1]]['avail']
    if used > 0 and avail >= used:
        n += 1
print(n)