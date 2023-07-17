
total = 0
for line in open('./2016/day04/input.txt', 'r').read().splitlines():
    x = line.index('[')
    name = line[:x].split('-')
    name, id = name[:-1], int(name[-1])
    for word in name:
        newWord = ''
        for letter in word:
            newWord += chr((ord(letter)-ord('a')+id)%26 + ord('a'))
        if newWord == 'northpole':
            print(id)