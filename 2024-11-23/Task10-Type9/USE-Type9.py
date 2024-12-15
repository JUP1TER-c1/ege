count = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if not len(set(row)) == 4: continue
    rsum = 0
    for element in row:
        if row.count(element) == 3:
            rsum += element
    if rsum**2 > (sum(row) - rsum)**2:
        count += 1

print(count)