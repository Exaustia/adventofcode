
instr = open('./2016/day23/input.txt', 'r').readlines()
reg = {'a':12, 'b':0, 'c':0, 'd':0}
i = 0
while(i<len(instr)):
    if i == 4: # nothing to see there
        reg.update({'a':reg['a'] + (reg['b']*reg['d'])})
        reg.update({'c':0})
        reg.update({'d':0})
        i = 10
        continue

    l = instr[i].split()
    
    if l[0] == 'tgl':
        if l[1].isdigit():
            x = int(l[1])
        else:
            x = reg[l[1]]
        if i+x < 0 or i+x >= len(instr):
            i += 1
            continue
        old = instr[i+x].split()
        if len(old) == 2:
            if old[0] == 'inc':
                old[0] = 'dec'
            else:
                old[0] = 'inc'
        else:
            if old[0] == 'jnz':
                old[0] = 'cpy'
            else:
                old[0] = 'jnz'
        instr[i+x] = ' '.join(old)

    elif l[0] == 'cpy':
        if l[1].lstrip('-').isdigit():
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
            if l[2].lstrip('-').isdigit():
                y = int(l[2])
            else:
                y = reg[l[2]]
            i += y
            continue
    i += 1
print(reg['a'])