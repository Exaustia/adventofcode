
deerStats = {}
for line in open('./2015/day14/input.txt', 'r').read().split('\n'):
    l = line.split()
    deerStats.update({l[0]:{'stats':(int(l[3]), int(l[6]), int(l[13])), # speed, flyTimeMax, restTimeMax
                            'rest':(False,0), # isResting + restTime
                            'fly':0, # flyTime
                            'dist':0, # distance
                            'points':0}}) 
time = 2503
sec = 0
while(sec < time):
    sec += 1
    maxDist = 0
    deersAhead = []
    for deer in deerStats:
        stats = deerStats[deer]['stats']
        isResting = deerStats[deer]['rest'][0]
        restTime = deerStats[deer]['rest'][1]
        dist = deerStats[deer]['dist']
        flyTime = deerStats[deer]['fly']
        points = deerStats[deer]['points']
        if isResting:
            restTime += 1
            if restTime == stats[2]:
                isResting = False
                restTime = 0
        else:
            dist += stats[0]
            flyTime += 1
            if flyTime == stats[1]:
                isResting = True
                flyTime = 0
        deerStats.update({deer:{'stats':stats, 
                                'rest':(isResting,restTime), 
                                'fly':flyTime, 
                                'dist':dist, 
                                'points':points}})
        if dist > maxDist:
            maxDist = dist
    for deer in deerStats:
        if deerStats[deer]['dist'] == maxDist:
            deerStats[deer].update({'points':deerStats[deer]['points']+1})

points = []
for deer in deerStats:
    points.append(deerStats[deer]['points'])
print(max(points))
