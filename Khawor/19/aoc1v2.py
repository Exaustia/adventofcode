import re
import copy
f = open("input.txt","r")
lines = f.readlines()


class factory():
    
    def __init__(self,nbOreRobot,nbClayRobot,nbObsiRobot,nbGeodeRobot,nbOre,nbClay,nbObsi,nbGeode,parentFact,currentMinute):
        self.nbOreRobot = nbOreRobot
        self.nbClayRobot = nbClayRobot
        self.nbObsiRobot = nbObsiRobot
        self.nbGeodeRobot = nbGeodeRobot
        self.nbOre = nbOre
        self.nbClay = nbClay
        self.nbObsi = nbObsi
        self.nbGeode = nbGeode
        self.parentFact = parentFact
        self.currentMinute = currentMinute
        
    def farm(self):
        self.nbOre += self.nbOreRobot
        self.nbClay += self.nbClayRobot
        self.nbObsi += self.nbObsiRobot
        self.nbGeode += self.nbGeodeRobot

    def __str__(self):
        return f"""{self.parentFact}
        {self.currentMinute} - ({self.nbOre},{self.nbClay},{self.nbObsi},{self.nbGeode}
        robot Ore = {self.nbOreRobot}
        robot Clay = {self.nbClayRobot}
        robot Obsi = {self.nbObsiRobot}
        robot Geode = {self.nbGeodeRobot})"""
    
    def __eq__(self, other):
        robots = self.nbOreRobot == other.nbOreRobot and self.nbClayRobot == other.nbClayRobot and self.nbObsiRobot == other.nbObsiRobot and self.nbGeodeRobot == other.nbGeodeRobot
        ressources = self.nbOre == other.nbOre and self.nbClay == other.nbClay and self.nbObsi == other.nbObsi and self.nbGeode == other.nbGeode
        return robots and ressources
    
    def addRobot(self, ore, clay, obsi, geode):
        self.nbOreRobot += ore
        self.nbClayRobot += clay
        self.nbObsiRobot += obsi
        self.nbGeodeRobot += geode

total = 0
for line in lines:
    s = line
    print(line)
    test = re.findall('Blueprint (.*): Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian.', line)
    numBlueprint = int(test[0][0])
    oreRobotcost = int(test[0][1])
    clayRobotCost = int(test[0][2])
    obsidianRobotCostore =int(test[0][3])
    obsidianRobotCostClay = int(test[0][4])
    geodeRobotCostOre = int(test[0][5])
    geodeRobotCostObsi = int(test[0][6])
    factories = []
    robotObsiConstructed = False
    firstTimeObsi = 0
    robotGeodeConstructed = 0
    firstTimeGeode = 0
    possibilities = [factory(1,0,0,0,0,0,0,0,None,0)]
    factories.append(possibilities)
    max = 0
    maxFact = None
    explored = False
    i = 1
    cptBoucle = 0
    bestLvlGeode = 30
    while explored == False:
        goingUp = False
        cptBoucle += 1
        if cptBoucle%100000 == 0:
            chaineFact = f"{cptBoucle}"
            
            for facto in factories:
                chaineFact += f"- {len(facto)}"
            print(chaineFact)
        # print(i)
        if len(factories[len(factories)-1])>0:
            currentFact = factories[len(factories)-1].pop()
        else:
            goingUp = True
            if len(factories) == 1 and len(factories[len(factories)-1]) == 0:
                explored = True
            factories.pop()
            i-=1
            



        if not(goingUp):
            possibilities = []
            if i == 25:
                newFact = copy.copy(currentFact)
                newFact.parentFact=currentFact
                newFact.currentMinute = i
                if ( newFact.nbGeode > max):
                    max = newFact.nbGeode
                    maxFact = newFact
                    print(max)
            elif bestLvlGeode < i and currentFact.nbGeodeRobot == 0:
                possibilities = []
            elif i == 24: #dernière minute, on fait juste rien
                newFact = copy.copy(currentFact)
                newFact.farm()
                newFact.parentFact=currentFact
                newFact.currentMinute = i
                possibilities.append(newFact)
                modif=True
            else:
                for k in range(0,5):
                    newFact = copy.copy(currentFact)
                    modif = False
                    oreplus = 0
                    clayplus = 0
                    obsiplus = 0
                    geodeplus = 0
                    newMaxGeode = False
                    match k:
                        case 0: #do nothing
                            modif = True  
                        case 1: #ore robot
                            if newFact.nbOre >= oreRobotcost:
                                oreplus += 1
                                newFact.nbOre -= oreRobotcost
                                modif = True
                        case 2: #clay robot
                            if newFact.nbOre >= clayRobotCost:
                                clayplus += 1
                                newFact.nbOre -= clayRobotCost
                                modif = True
                        case 3: #obsi robot
                            if newFact.nbOre >= obsidianRobotCostore and newFact.nbClay >= obsidianRobotCostClay:
                                obsiplus += 1
                                newFact.nbOre -= obsidianRobotCostore
                                newFact.nbClay -= obsidianRobotCostClay
                                robotObsiConstructed = True
                                firstTimeObsi += 1
                                modif = True
                        case 4: #geode robot
                            if newFact.nbOre >= geodeRobotCostOre and newFact.nbObsi >= geodeRobotCostObsi:
                                geodeplus += 1
                                newFact.nbOre -= geodeRobotCostOre
                                newFact.nbObsi -= geodeRobotCostObsi
                                firstTimeGeode += 1
                                if bestLvlGeode > i: 
                                    bestLvlGeode = i
                                # robotGeodeConstructed = True
                                modif = True
                    if modif and i < 25:
                        newFact.farm()
                        newFact.addRobot(oreplus,clayplus,obsiplus,geodeplus)
                        newFact.parentFact=currentFact
                        newFact.currentMinute = i
                        possibilities.append(newFact)

            if len(possibilities)>0:
                factories.append(possibilities)
                i+=1



    # for i in range(1,25):
    #     possibilities = []
    #     for currentFact in factories[i-1]:
    #         for k in range(0,5):
    #             newFact = copy.copy(currentFact)
    #             modif = False
    #             oreplus = 0
    #             clayplus = 0
    #             obsiplus = 0
    #             geodeplus = 0
    #             newMaxGeode = False
    #             match k:
    #                 case 0: #do nothing
    #                     modif = True  
    #                 case 1: #ore robot
    #                     if newFact.nbOre >= oreRobotcost:
    #                         oreplus += 1
    #                         newFact.nbOre -= oreRobotcost
    #                         modif = True
    #                 case 2: #clay robot
    #                     if newFact.nbOre >= clayRobotCost:
    #                         clayplus += 1
    #                         newFact.nbOre -= clayRobotCost
    #                         modif = True
    #                 case 3: #obsi robot
    #                     if newFact.nbOre >= obsidianRobotCostore and newFact.nbClay >= obsidianRobotCostClay:
    #                         obsiplus += 1
    #                         newFact.nbOre -= obsidianRobotCostore
    #                         newFact.nbClay -= obsidianRobotCostClay
    #                         robotObsiConstructed = True
    #                         firstTimeObsi += 1
    #                         modif = True
    #                 case 4: #geode robot
    #                     if newFact.nbOre >= geodeRobotCostOre and newFact.nbObsi >= geodeRobotCostObsi:
    #                         geodeplus += 1
    #                         newFact.nbOre -= geodeRobotCostOre
    #                         newFact.nbObsi -= geodeRobotCostObsi
    #                         firstTimeGeode += 1
    #                         # robotGeodeConstructed = True
    #                         modif = True
    #             if modif:
    #                 newFact.farm()
    #                 newFact.addRobot(oreplus,clayplus,obsiplus,geodeplus)
    #                 if robotGeodeConstructed < newFact.nbGeodeRobot:
    #                     robotGeodeConstructed = newFact.nbGeodeRobot
    #                     newMaxGeode = True
                    
    #                 # print(f"{i} - {newFact}")
    #                 add = True
    #                 # for possib in possibilities:
    #                 #     if newFact == possib:
    #                 #         # print('test')
    #                 #         add = False
    #                 #         break
    #                 # if robotObsiConstructed and newFact.nbObsiRobot == 0:
    #                 #     add = False
    #                 if robotGeodeConstructed > newFact.nbGeodeRobot:
    #                     add = False
                    
    #                 # if firstTimeObsi == 1:
    #                 #     firstTimeObsi += 1
    #                 #     possibilities = []
    #                 if newMaxGeode:
    #                     possibilities = []
    #                     print("Max Geode")
    #                 if add:
    #                     newFact.parentFact=currentFact
    #                     newFact.currentMinute = i
    #                     possibilities.append(newFact)
    #     print(len(factories))
    #     print(len(possibilities))
    #     factories.append(possibilities)
    
    
    print(maxFact)
    total += max * numBlueprint
    # print(factories)
    # print(max)

print(total)