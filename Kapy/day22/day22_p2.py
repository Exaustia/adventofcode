
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
    parsedPath.append(int(nb))
    return parsedPath

dicoSides = { # dico test
    'A1': {'taq':True, 'link':'A2', 'rota':'D', 'start':(8,0)},
    'A2': {'taq':True, 'link':'A1', 'rota':'D', 'start':(0,4)},
    'B1': {'taq':False, 'link':'B2', 'rota':'L', 'start':(8,0)},
    'B2': {'taq':False, 'link':'B1', 'rota':'R', 'start':(4,4)},
    'C1': {'taq':True, 'link':'C2', 'rota':'D', 'start':(11,0)},
    'C2': {'taq':True, 'link':'C1', 'rota':'D', 'start':(15,8)},
    'D1': {'taq':True, 'link':'D2', 'rota':'R', 'start':(11,4)},
    'D2': {'taq':True, 'link':'D1', 'rota':'L', 'start':(12,8)},
    'E1': {'taq':True, 'link':'E2', 'rota':'R', 'start':(8,8)},
    'E2': {'taq':True, 'link':'E1', 'rota':'L', 'start':(8,7)},
    'F1': {'taq':True, 'link':'F2', 'rota':'D', 'start':(0,7)},
    'F2': {'taq':True, 'link':'F1', 'rota':'D', 'start':(8,11)},
    'G1': {'taq':True, 'link':'G2', 'rota':'L', 'start':(12,11)},
    'G2': {'taq':True, 'link':'G1', 'rota':'R', 'start':(0,4)}
}

dicoSides = {
    'B2': {'taq':False, 'link':'B1', 'rota':'R', 'start':(0,100)},
    'E2': {'taq':False, 'link':'E1', 'rota':'O', 'start':(0,199)}, # O = pas de rota
    'A1': {'taq':False, 'link':'A2', 'rota':'R', 'start':(50,149)},
    'D1': {'taq':False, 'link':'D2', 'rota':'R', 'start':(50,0)},
    'E1': {'taq':False, 'link':'E2', 'rota':'O', 'start':(100,0)},
    'G1': {'taq':False, 'link':'G2', 'rota':'R', 'start':(100,49)},
    'B1': {'taq':False, 'link':'B2', 'rota':'L', 'start':(50,50)},
    'G2': {'taq':False, 'link':'G1', 'rota':'L', 'start':(99,50)},
    'C2': {'taq':False, 'link':'C1', 'rota':'D', 'start':(0,100)}, # D = demi tour
    'F2': {'taq':False, 'link':'F1', 'rota':'D', 'start':(99,100)},
    'D2': {'taq':False, 'link':'D1', 'rota':'L', 'start':(0,150)},
    'A2': {'taq':False, 'link':'A1', 'rota':'L', 'start':(49,150)},
    'C1': {'taq':False, 'link':'C2', 'rota':'D', 'start':(50,0)},
    'F1': {'taq':False, 'link':'F2', 'rota':'D', 'start':(149,0)}
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
                TaQ = dicoSides[nextID]['taq']
                if dicoSides[cellID]['rota'] == 'D':
                    nextPos = (nextPos[0], nextPos[1] + 49 - (y%50))
                else:
                    if TaQ:
                        nextPos = (nextPos[0] + 49 - (y%50), nextPos[1])
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
                TaQ = dicoSides[nextID]['taq']
                rota = dicoSides[cellID]['rota']
                if rota == 'O':
                    nextPos = (nextPos[0] + (x%50), nextPos[1])
                elif rota == 'D':
                    nextPos = (nextPos[0] + 49 - (x%50), nextPos[1])
                else:
                    if TaQ:
                        nextPos = (nextPos[0], nextPos[1] + 49 - (x%50))    
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
                TaQ = dicoSides[nextID]['taq']
                if dicoSides[cellID]['rota'] == 'D':
                    nextPos = (nextPos[0], nextPos[1] + 49 - (y%50))
                else:
                    if TaQ:
                        nextPos = (nextPos[0] + 49 - (y%50), nextPos[1])
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
                TaQ = dicoSides[nextID]['taq']
                rota = dicoSides[cellID]['rota']
                if rota == 'O':
                    nextPos = (nextPos[0] + (x%50), nextPos[1])
                elif rota == 'D':
                    nextPos = (nextPos[0] + 49 - (x%50), nextPos[1])
                else:
                    if TaQ:
                        nextPos = (nextPos[0], nextPos[1] + 49 - (x%50))
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

pos = (maze[0].index('.'), 0)
for move in path:
    if move == 'R':
        facing = (facing+1)%4
    elif move == 'L':
        facing = (facing-1)%4
    else:
        pos = moveBy(move)

print(1000*(pos[1]+1) + 4*(pos[0]+1) + facing)