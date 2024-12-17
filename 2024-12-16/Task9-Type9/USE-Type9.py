count = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    row.sort()
    if not 6*row[0] < sum(row[1:]): continue
    if row[0]*row[-1] > row[1]*row[2]:
        count += 1

print(count)