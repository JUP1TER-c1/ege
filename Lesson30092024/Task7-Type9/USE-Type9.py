count = 0
for line in open('USE-Type9'):
    row = list(map(int, line.split()))
    if len(set(row)) != len(row): continue
    minmax_avg = (min(row) + max(row)) / 2
    other_avg = (sum(row) - max(row) - min(row)) / 4
    if minmax_avg < other_avg:
        count += 1
print(count)