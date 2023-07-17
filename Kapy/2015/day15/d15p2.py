
properties = {}
input = open('./2015/day15/input.txt', 'r').read()
for line in input.split('\n'):
    l = line.split()
    properties.update({l[0][:-1]:{'capa':int(l[2][:-1]), 
                           'dura':int(l[4][:-1]), 
                           'flav':int(l[6][:-1]),
                           'text':int(l[8][:-1]),
                           'cal':int(l[10])}})
ingredients = properties.keys()
props = list(properties[list(ingredients)[0]].keys())
props.remove('cal')
maxPts = 0
for i in range(100):
    for j in range(100 - i):
        for k in range(100 - i - j):
            l = 100 - i - j - k
            factors = [i,j,k,l]
            cal = 0
            for n, ingr in enumerate(ingredients):
                cal += factors[n]*properties[ingr]['cal']
            if cal == 500:
                pts = 1
                for p in props:
                    temp = 0
                    for n, ingr in enumerate(ingredients):
                        temp += factors[n]*properties[ingr][p]
                    if temp <= 0:
                        break
                    pts *= temp
                if pts > maxPts:
                    maxPts = pts
print(maxPts)