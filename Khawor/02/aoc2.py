import csv


with open('D:\\PYTHONTEST\\AdventofCode\\aoc2input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    player1 = 0
    me = 0
    score = 0
    currentScore = 0
    for row in reader:
        if row[0] == 'A':
            player1 = 0
        elif row[0] == 'B':
            player1 = 1
        else:
            player1 = 2

        if row[1] == 'X':
            me = 0
        elif row[1] == 'Y':
            me = 1
        else:
            me = 2

        if (me-1)%3 == player1:
            currentScore = 6 + me + 1 
        elif me == player1:
            currentScore = 3 + me + 1
        else:
            currentScore =me +1
            
        score +=  currentScore
        print(str(player1)+' '+str(me)+ ' - '+str(currentScore))

    print(str(score))