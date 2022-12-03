f = open("E:\\AOC\\03\\input.txt","r")
lines = f.readlines()

i = 0
numLines = len(lines)
tot = 0
for i in range(0,numLines-1, 3):
    group1 = lines[i].strip()
    group2 = lines[i+1].strip()
    group3 = lines[i+2].strip()
    
    for x in group1:
        if x in group2:
            if x in group3:
                same = x
                break
    
    codeCarac = ord(same)
    
    if codeCarac < 97:
        calc = codeCarac - 64 + 26
    else:
        calc = codeCarac - 96
    tot += calc
print(str(tot))