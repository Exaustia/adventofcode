
nb = 0
with open('./Kapy/day04/input.txt', 'r') as f:
    for line in f.readlines():
        pair = line.strip()
        elf1 = pair[:pair.find(',')]
        elf2 = pair[pair.find(',')+1:]

        rangeElf1 = range(int(elf1[:elf1.find('-')]),int(elf1[elf1.find('-')+1:])+1)
        rangeElf2 = range(int(elf2[:elf2.find('-')]),int(elf2[elf2.find('-')+1:])+1)

        if set(rangeElf1).intersection(set(rangeElf2)):
            nb += 1

print(nb)