f = open("input.txt","r")
lines = f.readlines()


# tot = len(lines) * 2 + ((len(lines[0].strip())-2)*2)
# print(tot)x
print(str(range(1, len(lines)-1)))
scenicScoreMax=0
for i in range(1, len(lines)-1):
    
    lines[i] = lines[i].strip()
    # print(lines[i])
    for j in range(1, len(lines[i])-1):
        currentTree = lines[i][j]
        scenicScore = 0
        scenicScoreGauche = 0
        scenicScoreDroite = 0
        scenicScoreHaut = 0
        scenicScoreBas = 0
        #on test a gauche
        for k in range(j-1, -1, -1):
            scenicScoreGauche+=1
            if currentTree <= lines[i][k]:
                # print(str(currentTree) +" - "+ str(lines[i][k]))
                break
        
        #on test a droite
        droite = True
        for k in range(j+1, len(lines[i])):
            scenicScoreDroite+=1
            if currentTree <= lines[i][k]:
                break
        #on test vers le haut
        haut = True
        for k in range(i-1, -1, -1):
            scenicScoreHaut+=1
            if currentTree <= lines[k][j]:
                break
        #on test vers le bas
        bas = True
        for k in range(i+1, len(lines)):
            scenicScoreBas+=1
            # if i == 3 and j == 2:
            #     print(str(k)+" - "+str(j))
            if currentTree <= lines[k][j]:
                break
        
        scenicScore = scenicScoreGauche * scenicScoreBas * scenicScoreDroite * scenicScoreHaut
        if scenicScore > scenicScoreMax:
            scenicScoreMax = scenicScore
           

print(scenicScoreMax)