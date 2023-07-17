
total = 0
input = open('./2015/day05/input.txt', 'r').read()
for w in input.split():
    hasDoublePair = False
    hasRepetition = False
    pairs = set()
    for i, x in enumerate(w):
        if i > 1:
            if w[i-2] == w[i]:
                hasRepetition = True
        if i > 0:
            pair = w[i-1]+w[i]
            if pair in pairs:
                if not (w[i-1] == w[i] and w[i-2] == w[i]):
                    hasDoublePair = True
            else:
                pairs.add(pair)

    if hasDoublePair and hasRepetition:
        total += 1

print(total)