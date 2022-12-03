
lettres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = 0

with open('./Kapy/day3/input.txt', 'r') as f:
    for line in f.readlines():
        backpack = line.strip()
        milieu = int(len(backpack)/2)
        part1 = backpack[:milieu]
        part2 = backpack[milieu:]
        for x in part1:
            if x in part2:
                priority += lettres.find(x)+1
                break

print(priority)
