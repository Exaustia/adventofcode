
forestRows, forestColumns = [], []

def isVisible(x, y):
    global forestColumns, forestRows
    if x == 0 or y == 0 or x == len(forestColumns)-1 or y == len(forestRows)-1:
        return True
    height = forestRows[y][x]
    if max(forestRows[y][0:x]) < height or max(forestRows[y][x+1:]) < height:
        return True
    if max(forestColumns[x][0:y]) < height or max(forestColumns[x][y+1:]) < height:
        return True
    return False

with open('./Kapy/day08/input.txt', 'r') as f:
    for line in f.readlines():
        forestRows.append(list(map(int, line.strip())))
        for index, elem in enumerate(line.strip()):
            if len(forestColumns) == index:
                forestColumns.append([])
            forestColumns[index].append(int(elem))

nbVisible = 0
for y, row in enumerate(forestRows):
    for x, _ in enumerate(row):
        nbVisible += int(isVisible(x, y))
print(nbVisible)