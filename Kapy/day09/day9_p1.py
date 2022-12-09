
import numpy as np

h = np.array([0, 0])
t = np.array([0, 0])
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
        idxMax = np.where(toGoAbs == max(toGoAbs))[0][0]
        toGoAbs[idxMax] = toGoAbs[idxMax]-1
        
        toGo = toGoAbs * toGoSigns
        return t + toGo
    else:
        return t # don't move
    
def move(h, t, dir, nb):
    for _ in range(0, nb):
       
        if dir == 'R':
            h[0] = h[0] + 1
        elif dir == 'L':
            h[0] = h[0] - 1
        elif dir == 'U':
            h[1] = h[1] + 1
        elif dir == 'D':
            h[1] = h[1] - 1
        t = follow(h, t)
        
        res.add(str(t))
    return h, t
 
with open('./Kapy/day09/input.txt', 'r') as f:
    for line in f.readlines():
        dir, nb = line.strip().split(' ')
        h, t = move(h, t, dir, int(nb))

print(len(res))