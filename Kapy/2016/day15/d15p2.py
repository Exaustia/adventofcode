import re

nbPos = []
start = []
for i,l in enumerate(open('./2016/day15/input.txt', 'r').readlines()):
    s = re.search(r'(\d+) p.+n (\d+)', l)
    nbPos.append(int(s.groups()[0]))
    start.append(int(s.groups()[1]))
nbPos.append(11)
start.append(0)

time = -1
while(True):
    time += 1
    nope = False
    for i in range(len(start)):
        if (start[i]+time+1+i) % nbPos[i] != 0:
            nope = True
            break
    if not nope:
        break
print(time)