import csv


with open('D:\\PYTHONTEST\\AdventofCode\\aoc1input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    top3 = 0
    top3 = []
    current = 0
    for row in reader:
        # print(row)
        if len(row) == 0 :
            print(str(current))
            top3.append(current)
            current = 0
        else:
            current = current + int(row[0])
            
        
    top3.sort(reverse=True)
    max = top3[0] + top3[1] + top3[2]
        
    
    print(str(max))

