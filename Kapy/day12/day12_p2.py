
grid = []
with open('./Kapy/day12/input.txt', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == 'S':
            grid[r][c] = 'a'

def getSurroundings(pos):
    surroundings = []
    if pos[1] > 0:
        surroundings.append((pos[0], pos[1]-1))
    if pos[1] < len(grid)-1:
        surroundings.append((pos[0], pos[1]+1))
    if pos[0] > 0:
        surroundings.append((pos[0]-1, pos[1]))
    if pos[0] < len(grid[0])-1:
        surroundings.append((pos[0]+1, pos[1]))
    return surroundings

paths = []
for y in range(0, len(grid)):
        
    height = 'a'
    goal = 'b'
    path = [(0,y)]
    seekers = []
    foundE = False
    while not(foundE): 
        currentPos = path[-1]
        seekers = [path[-1:]]
        checkLower = 0
        toCheck = [goal, height]
        if goal == 'E':
            toCheck.append('z')
        foundNextLetter = False
        while not(foundNextLetter):
            if len(seekers) == 0:
                seekers = [path[-1:]]
                checkLower += 1
            newSeekers = []
            for seeker in seekers:
                for surroundPos in getSurroundings(seeker[-1]):
                    letter = grid[surroundPos[1]][surroundPos[0]]
                    if checkLower > len(toCheck)-2:
                        toCheck.append(chr(ord(toCheck[-1])-1))
                    if letter in toCheck:
                        seekerTemp = seeker.copy()
                        seekerTemp.append(surroundPos)
                        if letter == goal:
                            path += seekerTemp[1:] # this is the chosen one !
                            foundNextLetter = True
                            foundE = letter == 'E'
                            break
                        s = set()
                        s.update(path)
                        for seek in newSeekers:
                            s.update(seek)
                        for seek in seekers:
                            s.update(seek)
                        if surroundPos not in s:
                            newSeekers.append(seekerTemp)
                        
                if foundNextLetter or foundE:
                    break
            seekers = newSeekers.copy()
            
        height = chr(ord(height) + 1) # next char
        goal = 'E' if height == 'y' else chr(ord(height) + 1)
    
    lenPath = len(path[1:])
    print(lenPath)
    paths.append(lenPath)


print('\n\n'+str(min(paths)))
