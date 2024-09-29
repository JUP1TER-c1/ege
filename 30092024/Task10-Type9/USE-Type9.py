count = 0
for line in open('09 (2).csv'):
    row = list(map(int, line.split()))
    if not row: continue
    if len(set(row)) != len(row): continue
    minmax_avg = (min(row) + max(row))/2
    oth_avg = (sum(row) - (min(row) + max(row)))/4
    if oth_avg < minmax_avg:
        count+=1

print(count) #6840