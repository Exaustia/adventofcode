import math

# this code is only to check the differents stats and to know if I win or not
# few stats to check = I solved this by hand
# the print at the end doesn't even give me the gold I need to spend ...

myStats = [100,7,4]
bossStats = [103,9,2]
dmgDealth = myStats[1]-bossStats[2]
dmgDealth = 1 if dmgDealth < 1 else dmgDealth
dmgTaken = bossStats[1]-myStats[2]
dmgTaken = 1 if dmgTaken < 1 else dmgTaken
myTTK, bossTTK = (math.ceil(bossStats[0]/dmgDealth), math.ceil(myStats[0]/dmgTaken))
win = myTTK <= bossTTK

print(myTTK, bossTTK, win)