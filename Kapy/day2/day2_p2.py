
with open('./day2/input.txt', 'r') as f:
    pointsTotal = 0
    for round in f.readlines():
        pointsRound = {
            "A X":3,
            "A Y":4,
            "A Z":8,
            "B X":1,
            "B Y":5,
            "B Z":9,
            "C X":2,
            "C Y":6,
            "C Z":7,
        }
        pointsTotal += pointsRound.get(round.strip())

print(pointsTotal)