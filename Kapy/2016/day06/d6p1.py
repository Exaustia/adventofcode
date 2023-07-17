
input = open('./2016/day06/input.txt', 'r').read().splitlines()
nbCol = len(input[0])
dico = {}
for i in range(nbCol):
    dico.update({i:{}})

for line in input:
    for i, l in enumerate(line):
        n = 0
        if l in dico[i]:
            n = dico[i][l]
        dico[i].update({l:n+1})

message = ''
for i in range(nbCol):
    maxi = 0
    for l in dico[i]:
        if dico[i][l] > maxi:
            maxi = dico[i][l]
            char = l
    message += char

print(message)