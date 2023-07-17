
lights = [['.']*102 for _ in range(102)]
input = open('./2015/day18/input.txt', 'r').read().splitlines()
for j,line in enumerate(input):
    for i,l in enumerate(line):
        if l == '#':
            lights[j+1][i+1] = l

def nbNeighboursOn(x,y):
    nb = 0
    nb += lights[y][x-1] == '#'
    nb += lights[y][x+1] == '#'
    nb += lights[y-1][x-1] == '#'
    nb += lights[y-1][x+1] == '#'
    nb += lights[y-1][x] == '#'
    nb += lights[y+1][x-1] == '#'
    nb += lights[y+1][x+1] == '#'
    nb += lights[y+1][x] == '#'
    return nb

for _ in range(100):
    newLights = [l[:] for l in lights]
    for j,line in enumerate(lights[1:-1], start=1):
        for i,l in enumerate(line[1:-1], start=1):
            nb = nbNeighboursOn(i,j)
            if l == '#' and nb not in (2,3):
                newLights[j][i] = '.'
            if l == '.' and nb == 3:
                newLights[j][i] = '#'
    lights = [l[:] for l in newLights]
    lights[1][1] = '#'
    lights[1][-2] = '#'
    lights[-2][1] = '#'
    lights[-2][-2] = '#'

nb = 0    
for line in lights[1:-1]:
    nb += line.count('#')
print(nb)