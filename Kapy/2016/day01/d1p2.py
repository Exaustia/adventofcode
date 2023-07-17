
input = open('./2016/day01/input.txt', 'r').read()
look = 0 # 0, 1, 2, 3 for North, East, South, West
stop = False
visited = set()
pos = (0,0)
for t in input.split():
    t = t[:-1] if ',' in t else t # remove the ','
    if t[0] == 'R':
        look = (look+1)%4
    else:
        look = (look-1)%4
    for _ in range(int(t[1:])):
        if look == 0:
            pos = (pos[0], pos[1]+1)
        elif look == 1:
            pos = (pos[0]+1, pos[1])
        elif look == 2:
            pos = (pos[0], pos[1]-1)
        elif look == 3:
            pos = (pos[0]-1, pos[1])
        if pos in visited:
            stop = True
            break
        visited.add(pos)
    if stop:
        break
print(sum([abs(x) for x in pos]))