
import numpy as np

res = set()
rope = []
for _ in range(0,10):
    rope.append(np.array([0, 0]))

def follow(h, t):
    toGo = h - t
    toGoAbs = np.array(list(map(abs, toGo)))
    toGoSigns = np.array([0, 0])
    for i, x in enumerate(toGoAbs):
        if x != 0:
            toGoSigns[i] = int(toGo[i] / toGoAbs[i]) # [5, -7] --> [1, -1]

    if 2 in toGoAbs: 
        for idMax in np.where(toGoAbs == 2)[0]: # look for all 2s
            toGoAbs[idMax] = toGoAbs[idMax]-1
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
                rope[0][0] = rope[0][0] + 1
            elif dir == 'L':
                rope[0][0] = rope[0][0] - 1
            elif dir == 'U':
                rope[0][1] = rope[0][1] + 1
            elif dir == 'D':
                rope[0][1] = rope[0][1] - 1
            for i in range(1,10): # move each part of the body
                rope[i] = follow(rope[i-1], rope[i]) # the current part in the Tail, the previous one is the Head
            res.add(str(list(rope[9])))

print(len(res))