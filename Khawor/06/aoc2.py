f = open("input.txt","r")
lines = f.readlines()

ans = ""
for line in lines:
    ans = line[:14]
    line = line[14:]
    # print(line)
    for carac in line:
        ans+=carac
        fourcarac = ans[len(ans)-14:]
        notmarked=False
        for x in fourcarac:
            if fourcarac.count(x)>=2:
                notmarked=True
        
        if not(notmarked):
            print(str(len(ans)))
            break
        

        
        