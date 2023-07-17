import itertools as iter

for combi in iter.permutations('abcdefgh', 8):
    pwd = list(combi)
    for line in open('./2016/day21/input.txt', 'r').readlines():
        op = line.split()

        if (op[0],op[1]) == ('swap','position'):
            x,y = int(op[2]), int(op[5])
            pwd[x], pwd[y] = pwd[y], pwd[x]

        elif (op[0],op[1]) == ('swap','letter'):
            x,y = op[2], op[5]
            pwd = [x if l == y else y if l == x else l for l in pwd]

        elif op[0] == 'rotate':
            if op[1] == 'left':
                idx = int(op[2])
            elif op[1] == 'right':
                idx = -int(op[2])
            else:
                idx = pwd.index(op[6])
                idx = -(idx + 1 + (1 if idx >= 4 else 0)) % len(pwd)
            pwd = pwd[idx:] + pwd[:idx]

        elif op[0] == 'reverse':
            x,y = int(op[2]), int(op[4])
            pwd = pwd[:x] + pwd[x:y+1][::-1] + pwd[y+1:]

        elif op[0] == 'move':
            x,y = int(op[2]), int(op[5])
            letter = pwd[x]
            pwd.remove(letter)
            pwd.insert(y,letter)

    if ''.join(pwd) == 'fbgdceah':
        print(''.join(combi))
        break