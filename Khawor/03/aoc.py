f = open("E:\\AOC\\03\\input.txt","r")
lines = f.readlines()
       
def trouveSame(part1,part2):
    # pasTrouved = True
    # i = 0
    for x in part1:
        if x in part2:
            return x
    # while pasTrouved:
    #     if part1[i] in part2:
    #         pasTrouved = False
    #         return part1[i]
    #     i += 1

print("----- start-----\n-----------")
  
tot = 0
calc = 0
for line in lines:
    
    line = line.strip()
    half = int(len(line)/2)
    part1 = line[:half]
    part2 = line[half:]
    same = trouveSame(part1,part2)
    # same = 'z'
    codeCarac = ord(same)
    
    if codeCarac < 97:
        calc = codeCarac - 64 + 26
    else:
        calc = codeCarac - 96
    tot += calc
    
    print(part1 +" - "+part2+" = "+same+" - "+ str(calc))
   
print(str(tot))   

        
 
