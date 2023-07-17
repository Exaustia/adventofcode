
pos = 0
floor = 0
for c in open('./2015/day01/input.txt', 'r').read():
    pos += 1
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break
print(pos)