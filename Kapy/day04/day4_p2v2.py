
nb = 0
with open('./Kapy/day04/input.txt', 'r') as f:
    for line in f.readlines():
        pair = line.strip()

        a, b = pair.split(',')
        
        a = list(map(int, a.split('-')))
        b = list(map(int, b.split('-')))
        
        a[1] = a[1]+1 # ['2', '4'] --> ['2', '5']
        b[1] = b[1]+1

        setA = set(range(*map(int, a))) # histoire d'utiliser map et *
        setB = set(range(*map(int, b)))

        if (setA & setB):
            nb += 1

print(nb)
