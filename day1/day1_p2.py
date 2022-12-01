
listTop3 = []

with open('./day1/input.txt', 'r') as f:
    cal_elf = 0
    for calories in f.readlines():
        calories = calories.strip()
        if calories != '':
            cal_elf += int(calories)
        else: 
            if len(listTop3) < 3: # on met au moins les 3 premiers
                listTop3.append(cal_elf)
                if len(listTop3) == 3:
                    listTop3.sort()
            else: # quand il en a déjà 3
                for i in range(3):
                    if cal_elf > listTop3[i]: # on remplace le premier nombre du top 3 qui est plus petit
                        listTop3[i] = cal_elf
                        listTop3.sort() # on oublie pas de trier
                        break
            cal_elf = 0
    
print(sum(listTop3))