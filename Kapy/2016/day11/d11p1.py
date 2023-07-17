from collections import deque as dq
import itertools as iter
import time
import re

def isValid(f):
    return f[1] == 0 or f[0]|f[1] == f[1]

def getCombi(room):
    m = [2 ** i for i in range(5) if room[0] & (1 << i)][::-1]
    g = [-(2 ** i) for i in range(5) if room[1] & (1 << i)][::-1]
    for x in m+g+list(iter.combinations(m+g,2)):
        m,g = 0,0
        if type(x) == tuple:
            for y in x:
                if y>0:
                    m += y
                else:
                    g += abs(y)
        else:
            if x>0:
                m = x
            else:
                g = abs(x)
        yield m,g

def removeTrucs(room, trucs):
    return room[0]-trucs[0], room[1]-trucs[1]

def addTrucs(room, trucs):
    return room[0]+trucs[0], room[1]+trucs[1]

def getNewFloors(floors,dir,room,next):
    newF = list(floors)
    elev = newF[0]
    newF[elev] = room
    newF[elev+dir] = next
    newF[0] = elev + dir
    return tuple(newF)

def d11(floors):
    nb = 0
    tested,toTest,toTest2 = dict(),dict(),dict()
    toTest[floors] = 0
    testOne = True
    while(True):
        nb += 1
        for floors in (toTest if testOne else toTest2): 
            elev = floors[0]
            room = floors[elev] # étage courant

            for combi in getCombi(room):
                newRoom = removeTrucs(room, combi) # on retire les éléments de l'étage
                if isValid(newRoom): 

                    if elev+1 <= 4: # si on peut monter
                        nextFloor = addTrucs(floors[elev+1],combi) # on monte
                        if isValid(nextFloor):
                            if nextFloor == (31,31) and elev+1 == 4: # finish
                                return len(tested), nb
                            newF = getNewFloors(floors,1,newRoom,nextFloor) # nouvelle photo
                            if newF not in tested: # si pas encore testée, on la rajoute
                                if testOne:
                                    toTest2[newF] = 0
                                else:
                                    toTest[newF] = 0

                    if elev-1 >= 1:
                        prevFloor = addTrucs(floors[elev-1],combi)
                        if isValid(prevFloor):
                            newF = getNewFloors(floors,-1,newRoom,prevFloor) 
                            if newF not in tested:
                                if testOne:
                                    toTest2[newF] = 0
                                else:
                                    toTest[newF] = 0

            tested[floors] = 0 # photo devient testée

        if testOne:
            toTest = dict() # on vide
        else:
            toTest2 = dict()
        testOne = not testOne
        
floors = (1, (0b00011, 0b00011), (0b01100, 0b11100), (0b10000, 0), (0, 0)) # pas de parse osef

start = time.time()
print(d11(floors))
print(int(time.time()-start))