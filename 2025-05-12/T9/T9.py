cnt = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) != len(row): continue
    row = sorted(row)
    maxmax = sum(row.pop(-1) for i in range(2))
    if maxmax <= sum(row):
        cnt += 1

print(cnt)