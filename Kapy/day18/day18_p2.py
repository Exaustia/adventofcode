
def nextTo(c1, c2):
    if (c1[0], c1[1]) == (c2[0], c2[1]) and abs(c1[2]-c2[2]) == 1:
        return True
    if (c1[0], c1[2]) == (c2[0], c2[2]) and abs(c1[1]-c2[1]) == 1:
        return True
    if (c1[1], c1[2]) == (c2[1], c2[2]) and abs(c1[0]-c2[0]) == 1:
        return True
    return False

sum = 0
cubes = set()
for line in open('./Kapy/day18/input.txt', 'r').read().split('\n'):
    cube = tuple([int(x) for x in line.split(',')])
    sum += 6
    for c in cubes:
        if nextTo(c, cube):
            sum -= 2
    cubes.add(cube)

voidSets = [] 
for x in range(22):
    for y in range(22):
        for z in range(22):
            pixel = (x,y,z)
            if pixel not in cubes:
                added = -1
                toDel = []
                for idx, void in enumerate(voidSets):
                    for v in void:
                        if nextTo(v, pixel):
                            if added == -1: 
                                void.add(pixel)
                                added = idx
                            else: # if it was already added to a different void set, merge the 2 sets
                                voidSets[added].update(void)
                                toDel.append(idx)
                            break
                if len(toDel) > 0:
                    voidSets = [v for i, v in enumerate(voidSets) if i not in toDel]
                if added == -1:
                    voidSets.append({pixel})

voidSum = 0
for void in voidSets:
    if not(any(v[0] == 0 or v[1] == 0 or v[2] == 0 or v[0] == 21 or v[1] == 21 or v[2] == 21 for v in void)):
        voidSet = set()
        for v in void:
            voidSum += 6
            for x in voidSet:
                if nextTo(x, v):
                    voidSum -= 2
            voidSet.add(v)

print(sum-voidSum)