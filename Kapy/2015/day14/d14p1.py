
deerStats = {}
for line in open('./2015/day14/input.txt', 'r').read().split('\n'):
    l = line.split()
    deerStats.update({l[0]:(l[3], l[6], l[13])})

time = 2503
distList = []
for deer in deerStats:
    stats = [int(x) for x in deerStats[deer]]
    dist = 0
    sec = 0
    restTime = 0
    flyTime = 0
    isResting = False
    while(sec < time):
        sec += 1
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
    distList.append(dist)
print(max(distList))