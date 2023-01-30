
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

dicoSides = {
    'B2': {'sens':'v', 'link':'B1', 'rota':'R', 'start':(0,100)},
    'E2': {'sens':'v', 'link':'E1', 'rota':'O', 'start':(0,199)}, # O = pas de rota
    'A1': {'sens':'v', 'link':'A2', 'rota':'R', 'start':(50,149)},
    'D1': {'sens':'v', 'link':'D2', 'rota':'R', 'start':(50,0)},
    'E1': {'sens':'v', 'link':'E2', 'rota':'O', 'start':(100,0)},
    'G1': {'sens':'v', 'link':'G2', 'rota':'R', 'start':(100,49)},
    'B1': {'sens':'h', 'link':'B2', 'rota':'L', 'start':(50,50)},
    'G2': {'sens':'h', 'link':'G1', 'rota':'L', 'start':(99,50)},
    'C2': {'sens':'h', 'link':'C1', 'rota':'D', 'start':(0,100)}, # D = demi tour
    'F2': {'sens':'h', 'link':'F1', 'rota':'D', 'start':(99,100)},
    'D2': {'sens':'h', 'link':'D1', 'rota':'L', 'start':(0,150)},
    'A2': {'sens':'h', 'link':'A1', 'rota':'L', 'start':(49,150)},
    'C1': {'sens':'h', 'link':'C2', 'rota':'D', 'start':(50,0)},
    'F1': {'sens':'h', 'link':'F2', 'rota':'D', 'start':(149,0)}
}

def getRightBorder(line):
    line = line[::-1]
    return len(line) - line.index(line.replace(' ', '')) - 1
    
def getLeftBorder(line):
    return line.index(line.replace(' ', ''))

def moveBy(nb):
    global facing
    x, y = pos
    for _ in range(nb):
        b = True
        cubed = False
        if facing == 0: # RIGHT
            if x < getRightBorder(maze[y]):
                if maze[y][x+1] != "#":
                    x += 1
                    b = False
            else:
                cellID = mazeCube[y][x]
                if len(cellID) == 5:
                    cellID = cellID.split(',')[0]
                nextID = dicoSides[cellID]['link']
                nextPos = dicoSides[nextID]['start']
                if dicoSides[cellID]['rota'] == 'D':
                    nextPos = (nextPos[0], nextPos[1] + 49 - (y%50))
                else:
                    nextPos = (nextPos[0] + (y%50), nextPos[1])
                if maze[nextPos[1]][nextPos[0]] != '#':
                    x, y = nextPos
                    b = False
                    cubed = True
        elif facing == 1: # DOWN
            if y < getRightBorder(mazeRotated[x]):
                if mazeRotated[x][y+1] != "#":
                    y += 1
                    b = False
            else:
                cellID = mazeCube[y][x]
                if len(cellID) == 5:
                    cellID = cellID.split(',')[1]
                nextID = dicoSides[cellID]['link']
                nextPos = dicoSides[nextID]['start']
                if dicoSides[cellID]['rota'] == 'O':
                    nextPos = (nextPos[0] + (x%50), nextPos[1])
                else:
                    nextPos = (nextPos[0], nextPos[1] + (x%50))
                if maze[nextPos[1]][nextPos[0]] != '#':
                    x, y = nextPos
                    b = False
                    cubed = True
        elif facing == 2: # LEFT
            if x > getLeftBorder(maze[y]):
                if maze[y][x-1] != "#":
                    x -= 1
                    b = False
            else:
                cellID = mazeCube[y][x]
                if len(cellID) == 5:
                    cellID = cellID.split(',')[0]
                nextID = dicoSides[cellID]['link']
                nextPos = dicoSides[nextID]['start']
                if dicoSides[cellID]['rota'] == 'D':
                    nextPos = (nextPos[0], nextPos[1] + 49 - (y%50))
                else:
                    nextPos = (nextPos[0] + (y%50), nextPos[1])
                if maze[nextPos[1]][nextPos[0]] != '#':
                    x, y = nextPos
                    b = False
                    cubed = True
        else: # facing == 3 # UP
            if y > getLeftBorder(mazeRotated[x]):
                if mazeRotated[x][y-1] != "#":
                    y -= 1
                    b = False
            else:
                cellID = mazeCube[y][x]
                if len(cellID) == 5:
                    cellID = cellID.split(',')[1]
                nextID = dicoSides[cellID]['link']
                nextPos = dicoSides[nextID]['start']
                if dicoSides[cellID]['rota'] == 'O':
                    nextPos = (nextPos[0] + (x%50), nextPos[1])
                else:
                    nextPos = (nextPos[0], nextPos[1] + (x%50))
                if maze[nextPos[1]][nextPos[0]] != '#':
                    x, y = nextPos
                    b = False
                    cubed = True
        if b:
            break
        if cubed:
            rota = dicoSides[cellID]['rota']
            if rota == 'R':
                facing = (facing+1)%4
            elif rota == 'L':
                facing = (facing-1)%4
            elif rota == 'D':
                facing = (facing+2)%4
            # else rota == '0' # don't rotate
    return x, y

lenMax = 0
facing = 0
maze = open('./Kapy/day22/input.txt', 'r').read().split('\n')
path = parsePath(maze[-1])
maze = maze[:-2]
lenMax = max([len(x) for x in maze])

mazeCube = open('./Kapy/day22/inputCube.txt', 'r').read().split('\n')
mazeCube = [x.split('\t') for x in mazeCube]

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