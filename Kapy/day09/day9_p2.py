
import numpy as np

rope = []
for _ in range(0,10):
    rope.append(np.array([0, 0]))
res = set()

def follow(h, t):
    toGo = h - t
    toGoAbs = np.array(list(map(abs, toGo)))
    toGoSigns = np.array([0, 0])
    for i, x in enumerate(toGo):
        if x == 0:
            toGoSigns[i] = 0
        else:
            toGoSigns[i] = int(toGo[i] / toGoAbs[i])

    if [pos for pos in toGoAbs if pos > 1]:
        idsMax = np.where(toGoAbs == max(toGoAbs))[0]
        for idMax in idsMax:
            toGoAbs[idMax] = toGoAbs[idMax]-1
        toGo = toGoAbs * toGoSigns
        return t + toGo
    else:
        return t # don't move

with open('./Kapy/day09/input.txt', 'r') as f:
    for line in f.readlines():
        dir, nb = line.strip().split(' ')
        for _ in range(0, nb):
            h = rope[0]
            if dir == 'R':
                h[0] = h[0] + 1
            elif dir == 'L':
                h[0] = h[0] - 1
            elif dir == 'U':
                h[1] = h[1] + 1
            elif dir == 'D':
                h[1] = h[1] - 1
            for i in range(0,9):
                rope[i] = follow(rope[i], rope[i+1])
            res.add(str(list(rope[9])))

print(len(res))