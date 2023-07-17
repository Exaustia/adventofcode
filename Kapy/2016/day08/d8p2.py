
sl = 50 # screen length
sh = 6 # screen height
screen = [[' ']*sl for _ in range(sh)]

for instr in open('./2016/day08/input.txt', 'r').read().splitlines():
    instr = instr.split()
    if instr[0] == 'rect':
        a,b = instr[1].split('x')
        for i in range(int(a)):
            for j in range(int(b)):
                screen[j][i] = '#'
    elif instr[0] + instr[1] == 'rotate'+'row':
        row = int(instr[2].split('=')[1])
        shift = int(instr[4])%sl
        screen[row] = screen[row][-shift:] + screen[row][:-shift]
    else: # instr[0] + instr[1] == 'rotate'+'column':
        column = int(instr[2].split('=')[1])
        shift = int(instr[4])%sh
        sc = [row[column] for row in screen] # screen column
        sc = sc[-shift:] + sc[:-shift]
        for i,pixel in enumerate(sc):
            screen[i][column] = pixel

for row in screen:
    print(''.join(row))