
boss = dict()
spells = dict()
input = open('./2015/day22/input.txt', 'r').read().splitlines()
for i, line in enumerate(input):
    if i < 5:
        if i == 0:
            spellName = 'MM'
        elif i == 1:
            spellName = 'D'
        elif i == 2:
            spellName = 'S'
        elif i == 3:
            spellName = 'P'
        elif i == 4:
            spellName = 'R'
        manaCost = int(line.split()[-2])
        spells.update({spellName:manaCost})
    elif i == 6:
        boss.update({'PV':int(line.split()[-1])})
    elif i == 7:
        boss.update({'DMG':int(line.split()[-1])})

print(spells)
print(boss)
