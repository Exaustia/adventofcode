
lettres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elfGroup = []
priority = 0

with open('./Kapy/day3/input.txt', 'r') as f:
    for line in f.readlines():
        elfGroup.append(line.strip())
        if len(elfGroup) == 3: 
            for x in elfGroup[0]:
                if x in elfGroup[1] and x in elfGroup[2]:
                    priority += lettres.find(x)+1
                    elfGroup = []
                    break

print(priority)

