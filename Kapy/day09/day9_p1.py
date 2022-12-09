
import numpy as np

res = set()

h = np.array([0, 0])
t = np.array([0, 0])

def follow(h, t):
    toGo = h - t
    toGoAbs = np.array(list(map(abs, toGo)))
    toGoSigns = np.array([0, 0])
    for i, x in enumerate(toGoAbs):
        if x != 0:
            toGoSigns[i] = int(toGo[i] / toGoAbs[i])

    if 2 in toGoAbs: 
        idxMax = np.where(toGoAbs == max(toGoAbs))[0][0] # look for the 2
        toGoAbs[idxMax] = toGoAbs[idxMax]-1
        toGo = toGoAbs * toGoSigns
        return t + toGo
    else:
        return t # don't move
 
with open('./Kapy/day09/input.txt', 'r') as f:
    for line in f.readlines():
        dir, nb = line.strip().split(' ')
        for _ in range(0, int(nb)):
            # move the Head
            if dir == 'R':
                h[0] = h[0] + 1
            elif dir == 'L':
                h[0] = h[0] - 1
            elif dir == 'U':
                h[1] = h[1] + 1
            elif dir == 'D':
                h[1] = h[1] - 1
            t = follow(h, t) # move the Tail
            
            res.add(str(t))

print(len(res))