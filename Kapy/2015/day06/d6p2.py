
grid = [[0]*1000 for _ in range(1000)]
input = open('./2015/day06/input.txt', 'r').read().splitlines()
for l in input:
    instr = l.split(' ')
    if instr[0] == 'turn':
        instr.remove('turn')
    t1 = tuple([int(x) for x in instr[1].split(',')])
    t2 = tuple([int(x) for x in instr[3].split(',')])
    for x in range(t2[0]-t1[0]+1):
        for y in range(t2[1]-t1[1]+1):
            if instr[0] == 'toggle':
                grid[t1[0]+x][t1[1]+y] += 2
            elif instr[0] == 'on':
                grid[t1[0]+x][t1[1]+y] += 1
            else: # off
                if grid[t1[0]+x][t1[1]+y] >0:
                    grid[t1[0]+x][t1[1]+y] -= 1
total = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        total += grid[x][y]
print(total)