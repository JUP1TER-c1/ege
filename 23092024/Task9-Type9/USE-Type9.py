count = 0
for line in open('09.txt'):
    row = [int(number) for number in line.split()]
    if not row: continue
    if row.count(max(row)) > 1: continue
    if len(row) <= len(set(row)): continue
    avg = ((sum(row) - max(row))/(len(row)-1))*3
    if max(row) > avg:
        count += 1

print(count)
#Ответ: 95