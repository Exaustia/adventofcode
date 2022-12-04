
tab_calories = []

with open('./day1/input.txt', 'r') as f:
    cal_elf = 0
    for calories in f.readlines():
        calories = calories.strip()
        if calories != '':
            cal_elf += int(calories)
        else:
            tab_calories.append(cal_elf)
            cal_elf = 0

print(max(tab_calories))