f = open("input.txt","r")
lines = f.readlines()


tot = len(lines) * 2 + ((len(lines[0].strip())-2)*2)
# print(tot)x
print(str(range(1, len(lines)-1)))
for i in range(1, len(lines)-1):
    
    lines[i] = lines[i].strip()
    # print(lines[i])
    for j in range(1, len(lines[i])-1):
        currentTree = lines[i][j]
        #on test a gauche
        gauche = True
        for k in range(j-1, -1, -1):
            if currentTree <= lines[i][k]:
                gauche = False
                # print(str(currentTree) +" - "+ str(lines[i][k]))
                break
        
        #on test a droite
        droite = True
        for k in range(j+1, len(lines[i])):
            if currentTree <= lines[i][k]:
                droite = False
                break
        #on test vers le haut
        haut = True
        for k in range(i-1, -1, -1):
            if currentTree <= lines[k][j]:
                haut = False
                break
        #on test vers le bas
        bas = True
        for k in range(i+1, len(lines)):
            # if i == 3 and j == 2:
            #     print(str(k)+" - "+str(j))
            if currentTree <= lines[k][j]:
                bas = False
                break
        
        if gauche or droite or bas or haut:
            tot += 1
            print(str(i)+" - "+str(j)+" - "+str(currentTree))

print(tot)