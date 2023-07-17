
crates = []

with open('./Kapy/day05/crates.txt', 'r') as f:
    for line in f.readlines():
        crates.append(line.strip())

with open('./Kapy/day05/input.txt', 'r') as f:
    for line in f.readlines():
        move = list(map(int, line.strip().split(' ')))
        toMove = crates[move[1]-1][:move[0]] # no reverse
        crates[move[1]-1] = crates[move[1]-1][move[0]:] # remove
        crates[move[2]-1] = toMove + crates[move[2]-1] # add

result = ''
for crate in crates:
    result += crate[0]

print(result)