
with open('./day2/input.txt', 'r') as f:
    pointsTotal = 0
    pointsRound = {
        "A X":4,
        "A Y":8,
        "A Z":3,
        "B X":1,
        "B Y":5,
        "B Z":9,
        "C X":7,
        "C Y":2,
        "C Z":6,
    }
    for round in f.readlines():
        pointsTotal += pointsRound.get(round.strip())

print(pointsTotal)