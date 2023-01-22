
goal = 2000000
posNoBeacons, posBeaconsSensors = set(), set()

with open('./Kapy/day15/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        Sx, Sy, Bx, By = int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])
        if Sy == goal:
            posBeaconsSensors.add(Sx)
        if By == goal:
            posBeaconsSensors.add(Bx)
        distSB = abs(Sx-Bx)+abs(Sy-By)
        overshoot = distSB - abs(Sy - goal)
        if overshoot >= 0:
            goalFrom, goalTo = (Sx - overshoot), (Sx + overshoot)
            for i in range(goalFrom, goalTo+1):
                posNoBeacons.add(i)

print(len(posNoBeacons-posBeaconsSensors))