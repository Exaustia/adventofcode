import itertools as iter

containers = [int(x) for x in open('./2015/day17/input.txt', 'r').read().split()]
containers.sort()
goal = 150

somme = 0
for maxi, n in enumerate(containers):
    somme += n
    if somme > goal:
        break
nb = 0
for i in range(maxi):
    for c in iter.combinations(containers, i+1):
        if sum(c) == goal:
            nb += 1
print(nb)