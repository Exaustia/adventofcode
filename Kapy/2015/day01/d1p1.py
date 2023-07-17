
floor = 0
for c in open('./2015/day01/input.txt', 'r').read():
    if c == '(':
        floor += 1
    else:
        floor -= 1
print(floor)