
instr = open('./2016/day12/input.txt', 'r').read().splitlines()
reg = {'a':0, 'b':0, 'c':1, 'd':0}
i = 0
while(i<len(instr)):
    l = instr[i].split()
    if l[0] == 'cpy':
        if l[1].isdigit():
            x = int(l[1])
        else:
            x = reg[l[1]]
        reg[l[2]] = x
    elif l[0] == 'inc':
        reg.update({l[1]:reg[l[1]]+1})
    elif l[0] == 'dec':
        reg.update({l[1]:reg[l[1]]-1})
    elif l[0] == 'jnz':
        if l[1].isdigit():
            x = int(l[1])
        else:
            x = reg[l[1]]
        if x != 0:
            i += int(l[2])
            continue
    i += 1
print(reg['a'])