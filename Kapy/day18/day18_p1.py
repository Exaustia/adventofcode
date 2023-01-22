
cubes = set()
sum = 0

def nextTo(c1, c2):
    if (c1[0], c1[1]) == (c2[0], c2[1]) and abs(c1[2]-c2[2]) == 1:
        return True
    if (c1[0], c1[2]) == (c2[0], c2[2]) and abs(c1[1]-c2[1]) == 1:
        return True
    if (c1[1], c1[2]) == (c2[1], c2[2]) and abs(c1[0]-c2[0]) == 1:
        return True
    return False

for line in open('./Kapy/day18/input.txt', 'r').read().split('\n'):
    cube = tuple([int(x) for x in line.split(',')])
    sum += 6
    for c in cubes:
        if nextTo(c, cube):
            sum -= 2
    cubes.add(cube)

print(sum)