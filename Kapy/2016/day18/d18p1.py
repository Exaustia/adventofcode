import re

def getTile(x):
    return '^' if x in ['..^', '^..', '^^.', '.^^'] else '.'

row = open('./2016/day18/input.txt', 'r').read()
nbSafe = row.count('.')
for _ in range(40-1):
    matches = re.findall(r"(?=(.{3}))", '.' + row + '.')
    row = ''.join([getTile(m) for m in matches])
    nbSafe += row.count('.')
print(nbSafe)