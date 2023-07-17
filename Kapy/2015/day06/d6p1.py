
def getLights(pos1, pos2):
    lights = set()
    x1, x2, y1, y2 = pos1[0], pos2[0], pos1[1], pos2[1]
    for i in range(x2-x1+1):
        for j in range(y2-y1+1):
            lights.add((x1+i, y1+j))
    return lights

grid = [[False]*1000 for _ in range(1000)]

input = open('./2015/day06/input.txt', 'r').read().splitlines()
for l in input:
    instr = l.split(' ')
    if instr[0] == 'turn':
        instr.remove('turn')
    t1 = tuple([int(x) for x in instr[1].split(',')])
    t2 = tuple([int(x) for x in instr[3].split(',')])
    lights = getLights(t1,t2)
    for light in lights:
        if instr[0] == 'toggle':
            grid[light[0]][light[1]] = not(grid[light[0]][light[1]])
        elif instr[0] == 'on':
            grid[light[0]][light[1]] = True
        else: # off
            grid[light[0]][light[1]] = False

nbLightsOn = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y]:
            nbLightsOn += 1
print(nbLightsOn)