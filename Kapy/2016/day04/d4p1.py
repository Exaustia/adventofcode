
total = 0
for line in open('./2016/day04/input.txt', 'r').read().splitlines():
    x = line.index('[')
    name = line[:x].split('-')
    name, id = ''.join(name[:-1]), int(name[-1])
    cs = line[x+1:-1]
    letters = set(name)
    dico = {}
    for x in letters:
        if x not in dico:
            dico.update({x:name.count(x)})
    ok = True
    for x in cs:
        if x not in dico:
            ok = False
            break
    if ok:
        if dico[cs[0]] >= dico[cs[1]] and dico[cs[1]] >= dico[cs[2]] and dico[cs[2]] >= dico[cs[3]] and dico[cs[3]] >= dico[cs[4]]:
            for d in dico:
                if d not in cs and dico[d] > dico[cs[4]]:
                    ok = False
                    break
        else:
            ok = False
    if ok:
        total += id
print(total)