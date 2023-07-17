import itertools as iter
import math

weights = [int(i) for i in open('./2015/day24/input.txt', 'r').read().splitlines()]
goal = int(sum(weights)/3)
qe = []

for i in range(5,10):
    if len(qe) == 0:
        for c in iter.combinations(weights, i):
            if sum(c) == goal:
                qe.append(math.prod(list(c)))
    else:
        break

print(min(qe))