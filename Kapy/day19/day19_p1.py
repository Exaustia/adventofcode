
for blueprintID, line in enumerate(open('./Kapy/day19/inputTest.txt', 'r').read().split('\n')):
    lineElements = line.split(" ")

    costs = [
        (0, int(lineElements[6])),
        (0, int(lineElements[12])), 
        ((0, 1), (int(lineElements[18]), int(lineElements[21]))), 
        ((0, 2), (int(lineElements[27]), int(lineElements[30])))
        ]
    ressources, robots = [0, 0, 0, 0], [1, 0, 0, 0]
    prio = [(1,3), (2,1), (1,4), (2,2)] # (robotNumber, howMany) # generate many versions of this and try them all
    idxPrio = 0

    for min in range(24):
        for i in range(len(robots)):
            ressources[i] += robots[i]

        if idxPrio < 4:
            pId = prio[idxPrio][0]
            pNb = prio[idxPrio][1]
        else:
            pId = 3
            pNb = 10

        if robots[pId] < pNb: # try to buy one
            if pId in (0, 1):
                if ressources[costs[pId][0]] >= costs[pId][1]:
                    ressources[costs[pId][0]] -= costs[pId][1]
                    robots[pId] += 1 # add 1 min timer before adding the new robot
            else: 
                if ressources[costs[pId][0][0]] >= costs[pId][1][0] and ressources[costs[pId][0][1]] >= costs[pId][1][1]:
                    ressources[costs[pId][0][0]] -= costs[pId][1][0]
                    ressources[costs[pId][0][1]] -= costs[pId][1][1]
                    robots[pId] += 1 # add 1 min timer before adding the new robot
            if idxPrio < 4:
                if prio[idxPrio][1] == robots[pId]: # we have enough, take the next prio
                    idxPrio += 1
        print(ressources)
        print(robots)
        print('\r\n')



