
vowels = 'aeiou'
bad = ['ab', 'cd', 'pq', 'xy']

total = 0
input = open('./2015/day05/input.txt', 'r').read()
for w in input.split():
    isGood = True
    vowelCount = 0
    hasDouble = False
    for i, x in enumerate(w):
        if i > 0:
            if w[i-1]+w[i] in bad:
                isGood = False
                break
            if w[i-1] == w[i]:
                hasDouble = True
        if x in vowels:
            vowelCount += 1
    
    if vowelCount >= 3 and hasDouble and isGood:
        total += 1

print(total)