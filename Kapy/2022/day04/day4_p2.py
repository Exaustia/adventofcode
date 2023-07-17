
nb = 0
with open('./Kapy/day04/input.txt', 'r') as f:
    for line in f.readlines():
        pair = line.strip()
        elf1, elf2 = pair.split(',')

        setElf1 = set(range(int(elf1[:elf1.find('-')]),int(elf1[elf1.find('-')+1:])+1))
        setElf2 = set(range(int(elf2[:elf2.find('-')]),int(elf2[elf2.find('-')+1:])+1))

        if setElf1 & setElf2:
            nb += 1

print(nb)