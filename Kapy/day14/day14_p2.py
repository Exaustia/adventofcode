
import numpy as np
import re

grid = [([' ']*200) for _ in range(700)]
yMax = 0
nb = 0

with open('./Kapy/day14/inputP2.txt', 'r') as f:
    for line in f.readlines():
        for i, point in enumerate(line.strip().split(' -> ')):
            x, y = map(int, point.split(','))
            if y > yMax:
                yMax = y # useful to know when sand comes to rest
            if i == 0:
                prevX, prevY = x, y
                grid[x][y] = '#'
            else:
                distX, distY = abs(x - prevX), abs(y - prevY)
                if distX > 0: # horizontal line
                    dirX = int((x - prevX)/distX)
                    for j in range(1, distX+1):
                        grid[prevX+(j*dirX)][y] = '#'
                else: # vertical line
                    dirY = int((y - prevY)/distY)
                    for j in range(1, distY+1):
                        grid[x][prevY+(j*dirY)] = '#'
                prevX, prevY = x, y

def whereToDrop(fromX, fromY):
    isObstacle = re.search('[.#]', ''.join(grid[fromX][fromY:]))
    if isObstacle:
        return fromX, fromY + isObstacle.start() - 1
    else:
        return fromX, yMax + 1        

while(True):
    posX, posY = whereToDrop(500,0)
    rest = False
    while(not rest):
        if grid[posX-1][posY+1] == ' ': # if no obstacle at [-1, 1] relative to pos (a drop to the left)
            posX, posY = whereToDrop(posX-1, posY+1)
        elif grid[posX+1][posY+1] == ' ': # if no obstacle at [1, 1] relative to pos (a drop to the right)
            posX, posY = whereToDrop(posX+1, posY+1)
        else:
            grid[posX][posY] = '.'
            nb += 1
            rest = True
        if posY == 0:
            exit(0)