import itertools as iter

containers = [int(x) for x in open('./2015/day17/input.txt', 'r').read().split()]
containers.sort()
goal = 150

nb = 0
for i in range(len(containers)):
    for c in iter.combinations(containers, i+1):
        if sum(c) == goal:
            nb += 1
    if nb > 0:
        break
print(nb)