
total = 0
input = open('./2015/day08/input.txt', 'r').read().splitlines()
for l in input:
    escape = 2
    i = 0
    while(i < len(l)):
        if l[i] == '\\':
            if l[i+1] == 'x':
                escape += 3
                i += 3
            else:
                escape += 1
                i += 1
        i += 1
    total += escape
print(total)