f = open("input.txt","r")
lines = f.readlines()

piles=[]
i = 0
firstLine=True

for line in lines:
    if len(line)>1:        
        if (line[0] == '[' or line[1] == ' ') and line[1] != '1':
            for i in range(9):
                if firstLine:
                    piles.append([])
                elem = line[:4]
                line = line[4:]
                if '   ' not in elem:
                    piles[i].append(elem.strip())
        elif line[0] == 'm':
            nbMove = int(line[line.find('e')+1:line.find('f')-1])
            pileStart = int(line[line.find('f')+4:line.find('t')-1])
            pileEnd = int(line[len(line)-2:])
            print(str(nbMove) + "-"+str(pileStart)+"-"+str(pileEnd))
            
        

            pileMove = []
            for i in range(nbMove):
                pileMove.append(piles[pileStart-1].pop(0))
                
            for i in range(nbMove):
                piles[pileEnd-1].insert(0,pileMove.pop(len(pileMove)-1))

    firstLine=False

for pile in piles:
    print(str(pile[0]))

   


    
