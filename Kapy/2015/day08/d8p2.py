
escape = 0
input = open('./2015/day08/input.txt', 'r').read().splitlines()
for l in input:
    escape += l.count('"') + l.count('\\') + 2
print(escape)