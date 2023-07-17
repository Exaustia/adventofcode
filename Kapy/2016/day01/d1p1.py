
input = open('./2016/day01/input.txt', 'r').read()
look = 0 # 0, 1, 2, 3 for North, East, South, West
pos = [0,0]
for t in input.split():
    t = t[:-1] if ',' in t else t # remove the ,
    if t[0] == 'R':
        look = (look+1)%4
    else:
        look = (look-1)%4
    steps = int(t[1:])
    if look == 0:
        pos[1] += steps
    elif look == 1:
        pos[0] += steps
    elif look == 2:
        pos[1] -= steps
    elif look == 3:
        pos[0] -= steps
print(sum([abs(x) for x in pos]))