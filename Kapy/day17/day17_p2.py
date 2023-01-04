
import numpy as np

rocks = [
        np.array([(3,0), (4,0), (5,0), (6,0)]),
        np.array([(4,0), (4,1), (3,1), (5,1), (4,2)]),
        np.array([(3,0), (4,0), (5,0), (5,1), (5,2)]),
        np.array([(3,0), (3,1), (3,2), (3,3)]),
        np.array([(3,0), (3,1), (4,0), (4,1)])
    ]
heights = [1, 3, 3, 4, 2]
obstacles = {(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)} # bottom floor

jets = open('./Kapy/day17/input.txt', 'r').read()
iRock = 0
iJet = 0
highest = 0
jump = False
nbRocks = 0
maxRocks = 1000000000000
while(nbRocks < maxRocks):
    rock = rocks[iRock] + (0, highest + 4) # spawn a rock
    rockMaxHeight = highest + 3 + heights[iRock]

    while(True):
        if jets[iJet] == '>':
            if not(set([tuple(r) for r in rock+(1,0)]).intersection(obstacles)) and not(any(r[0] == 8 for r in rock+(1,0))): # if we can go right
                rock += (1,0)
        else:
            if not(set([tuple(r) for r in rock-(1,0)]).intersection(obstacles)) and not(any(r[0] == 0 for r in rock-(1,0))): # if we can go left
                rock -= (1,0)

        iJet = (iJet+1)%len(jets)
        if iJet == 0:
            nbJumps = int((maxRocks-nbRocks)/1735)
            maxRocks = (maxRocks-nbRocks)%1735
            nbRocks = 0
        
        if set([tuple(r) for r in rock-(0,1)]).intersection(obstacles): # if we find an obstacle when trying to go down
            obstacles.update(list(tuple(r) for r in rock))
            if rockMaxHeight > highest:
                highest = rockMaxHeight
            # draw()
            break # stop moving and take the next rock
        else:
            rock -= (0,1) # go down
            rockMaxHeight -= 1

    nbRocks += 1
    iRock = (iRock+1)%len(rocks)

print(highest + (nbJumps*2711))