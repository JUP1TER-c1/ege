count = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) == len(row): continue
    if row.count(max(row)) > 1: continue
    if sum([number for number in row if row.count(number) > 1]) < max(row):
        count+=1

print(count)
