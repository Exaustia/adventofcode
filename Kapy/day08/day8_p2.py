
forestRows, forestColumns = [], []

def getScore(x, y):
    height = forestRows[y][x]
    a = b = c = d = 0

    if x == 0 or y == 0 or x == len(forestColumns)-1 or y == len(forestRows)-1:
        return 0
    
    higher = [idx for idx,tree in enumerate(forestRows[y][0:x]) if tree >= height]
    if len(higher) > 0:
        a = x - higher[-1]
    else:
        a = len(forestRows[y][0:x])

    higher = [idx for idx,tree in enumerate(forestRows[y][x+1:]) if tree >= height]
    if len(higher) > 0:
        b = higher[0] + 1
    else:
        b = len(forestRows[y][x+1:])

    higher = [idx for idx,tree in enumerate(forestColumns[x][0:y]) if tree >= height]
    if len(higher) > 0:
        c = y - higher[-1]
    else:
        c = len(forestColumns[x][0:y])

    higher = [idx for idx,tree in enumerate(forestColumns[x][y+1:]) if tree >= height]
    if len(higher) > 0:
        d = higher[0] + 1
    else:
        d = len(forestColumns[x][y+1:])
    
    return a*b*c*d

with open('./Kapy/day08/input.txt', 'r') as f:
    for line in f.readlines():
        forestRows.append(list(map(int, line.strip())))
        for index, elem in enumerate(line.strip()):
            if len(forestColumns) == index:
                forestColumns.append([])
            forestColumns[index].append(int(elem))

maxScore = 0
for y, row in enumerate(forestRows):
    for x, _ in enumerate(row):
        score = getScore(x, y)
        if score > maxScore:
            maxScore = score
print(maxScore)