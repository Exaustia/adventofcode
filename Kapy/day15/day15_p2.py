
#posNoBeacons = set((x,y) for x in range(4000001) for y in range(4000001)) #4000001

with open('./Kapy/day15/input.txt', 'r') as f:
    for line in f.readlines():
        print('coucou')
        line = line.strip().split(' ')
        Sx, Sy, Bx, By = int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])
        distSB = abs(Sx-Bx)+abs(Sy-By)
        for i in range(distSB+1):
            j = distSB - i
            nb = set((x,Sy+j) for x in range(Sx-i, Sx+i+1))
            if j != 0:
                nb2 = set((x,Sy-j) for x in range(Sx-i, Sx+i+1))
                nb = nb.union(nb2)
            posNoBeacons = posNoBeacons.difference(nb)

print(posNoBeacons)