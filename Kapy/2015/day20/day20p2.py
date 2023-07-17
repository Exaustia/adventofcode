
goal = int(open('./2015/day20/input.txt', 'r').read())
maxGifts = set()

def getDivisors(n):
    divs = {1,n}
    added = False
    maxDiv = n/2
    i = 0
    while i+1 <= maxDiv:
        i += 1
        if i not in maxGifts:
            if n%i == 0:
                divs.add(i)
                if i > 1 and not added:
                    added = True                      
            elif not added:
                maxDiv = n/(i+1)
    return divs

i = 0
while True:
    i += 1
    if sum(getDivisors(i))*11 >= goal:
        print(i)
        break
    elif i%50 == 0:
        maxGifts.add(int(i/50))    