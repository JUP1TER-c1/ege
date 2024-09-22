count = 0
for line in open('09-_1_.txt'):
    row = [int(number) for number in line.split()]
    if not row: continue
    if len(row) != len(set(row)): continue
    avg_minmax = (min(row) + max(row))/2
    avg = (sum(row) - min(row) - max(row)) / 4
    if avg_minmax > avg:
        count += 1

print(count)
#Ответ: 6840