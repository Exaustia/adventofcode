
reg = {'a' : 0, 'b' : 0}
instr = open('./2015/day23/input.txt', 'r').read().splitlines()

i = 0
while i >= 0 and i < len(instr):
    line = instr[i].split()
    if line[0] == 'hlf':
        r = line[1]
        reg.update({r:int(reg[r]/2)})
    elif line[0] == 'tpl':
        r = line[1]
        reg.update({r:reg[r]*3})
    elif line[0] == 'inc':
        r = line[1]
        reg.update({r:reg[r]+1})
    elif line[0] == 'jmp':
        i += int(line[1])
        continue
    elif line[0] == 'jie':
        r = line[1][0]
        if reg[r]%2 == 0:
            i += int(line[2])
            continue
    elif line[0] == 'jio':
        r = line[1][0]
        if reg[r] == 1:
            i += int(line[2])
            continue
    i += 1

print(reg['b'])