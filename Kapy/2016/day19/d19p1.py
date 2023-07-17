
nb = int(open('./2016/day19/input.txt', 'r').read())
elves = [i+1 for i in range(nb)]
while(len(elves)>1):
    elves = [e for i,e in enumerate(elves) if i%2 == 0 and not (i == 0 and len(elves)%2 == 1)]
    # not (i == 0 and len(elves)%2 == 1) is here to remove the 1st element when len(elves) is odd
print(elves[0])

# print(int('0b' + bin(nb)[3:] + '1', 2)) # one liner ???