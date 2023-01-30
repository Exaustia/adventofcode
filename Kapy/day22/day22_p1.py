
def parsePath(path):
    parsedPath = []
    nb = ''
    for x in path:
        if x == 'R' or x == 'L':
            parsedPath.append(int(nb))
            parsedPath.append(x)
            nb = ''
        else:
            nb += x
    return parsedPath

def getRightBorder(line):
    line = line[::-1]
    return len(line) - line.index(line.replace(' ', '')) - 1
    
def getLeftBorder(line):
    return line.index(line.replace(' ', ''))

def moveBy(nb):
    x, y = pos
    for _ in range(nb):
        b = True
        if facing == 0: # LEFT
            if x < getRightBorder(maze[y]):
                if maze[y][x+1] != "#":
                    x += 1
                    b = False
            else:
                idx = getLeftBorder(maze[y])
                if maze[y][idx] != '#':
                    x = idx
                    b = False
        elif facing == 1: # DOWN
            if y < getRightBorder(mazeRotated[x]):
                if mazeRotated[x][y+1] != "#":
                    y += 1
                    b = False
            else:
                idx = getLeftBorder(mazeRotated[x])
                if mazeRotated[x][idx] != '#':
                    y = idx
                    b = False
        elif facing == 2: # RIGHT
            if x > getLeftBorder(maze[y]):
                if maze[y][x-1] != "#":
                    x -= 1
                    b = False
            else:
                idx = getRightBorder(maze[y])
                if maze[y][idx] != '#':
                    x = idx
                    b = False
        else: # facing == 3 # UP
            if y > getLeftBorder(mazeRotated[x]):
                if mazeRotated[x][y-1] != "#":
                    y -= 1
                    b = False
            else:
                idx = getRightBorder(mazeRotated[x])
                if mazeRotated[x][idx] != '#':
                    y = idx
                    b = False
        if b:
            break
    return x, y

lenMax = 0
facing = 0
maze = open('./Kapy/day22/input.txt', 'r').read().split('\n')
path = parsePath(maze[-1])
maze = maze[:-2]
lenMax = max([len(x) for x in maze])

for i, line in enumerate(maze):
    if len(line) < lenMax:
        maze[i] += (lenMax-len(line))*' '

mazeRotated = []
for y, line in enumerate(maze):
    for x, pixel in enumerate(line):
        if len(mazeRotated) == x:
            mazeRotated.append('')
        mazeRotated[x] += pixel

#for line in mazeRotated:
#    print(line)

pos = (maze[0].index('.'), 0)
for move in path:
    if move == 'R':
        facing = (facing+1)%4
    elif move == 'L':
        facing = (facing-1)%4
    else:
        pos = moveBy(move)

print(1000*(pos[1]+1) + 4*(pos[0]+1) + facing)