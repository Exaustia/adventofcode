import hashlib
import numpy as np

def sort2lists(l1,l2): # sort 2 lists by the length of the elements of the 1st list, reversed
    lenList = [-len(x) for x in l1]
    sortedIndex = np.argsort(lenList)
    newL1, newL2 = ['']*len(l1), ['']*len(l2)
    for i in range(len(l1)):
        newL1[i] = l1[sortedIndex[i]]
        newL2[i] = l2[sortedIndex[i]]
    return newL1, newL2

solutions = []
pathList = ['']
posList = [np.array([0,0])]
passcode = open('./2016/day17/input.txt', 'r').read()
while(len(posList)>0):
    pathList, posList = sort2lists(pathList, posList)
    path, pos = pathList.pop(), posList.pop()
    hash = hashlib.md5((passcode+path).encode('utf-8')).hexdigest()[:4]
    open = []
    for i,x in enumerate(hash):
        if x in ['b','c','d','e','f']:
            if i == 0:
                open.append(('U',(0,-1)))
            elif i == 1:
                open.append(('D',(0,1)))
            elif i == 2:
                open.append(('L',(-1,0)))
            elif i == 3:
                open.append(('R',(1,0)))
    for o in open:
        if ((pos+o[1]) == np.array([3,3])).all():
            solutions.append(path+o[0])
            continue
        else:
            if ((pos+o[1]) >= (0,0)).all() and  ((pos+o[1]) <= (3,3)).all():
                pathList.append(path+o[0])
                posList.append(pos+o[1])
print(len(solutions[-1]))