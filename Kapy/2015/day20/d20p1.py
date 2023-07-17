
goal = int(open('./2015/day20/input.txt', 'r').read())/10

def getDivisors(n):
    divs = {1,n}
    added = False
    maxDiv = n/2
    i = 1
    while i <= maxDiv:
        i += 1
        if n%i == 0:
            divs.add(i)
            added = True
        elif not added:
            maxDiv = n/(i+1)
    return divs

i = 786000
while True:
    i += 1
    if sum(getDivisors(i)) >= goal:
        print(i)
        break