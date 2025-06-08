cnt = 0
for line in open('2.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) == len(row): continue
    row = sorted(row)
    if row.count(row[-1]) > 1: continue
    repeated = 0
    for number in row:
        if row.count(number) > 1: repeated += number
    if repeated < row[-1]:
        cnt += 1
print(cnt)