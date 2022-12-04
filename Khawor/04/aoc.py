import csv


with open('input.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    tot = 0
    for row in reader:
        range1 = row[0].split('-')
        range2 = row[1].split('-')
        if (int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])) or (int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1])):
            print(str(range1)+" - "+str(range2))
            tot+=1
    
    print(str(tot))