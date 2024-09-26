count = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) != 5: continue
    conditionCheck = True
    repAvg = 0
    for number in row:
        if row.count(number) > 2:
            conditionCheck = False
            break
        if row.count(number) == 2: repAvg += number

    if conditionCheck:
        othAvg = (sum(row) - repAvg)/3
        repAvg = repAvg/4
        if othAvg > repAvg:
            count+=1

print(count) #96
