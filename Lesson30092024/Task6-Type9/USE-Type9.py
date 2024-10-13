count = 0
for line in open('09.txt'):
    row = list(map(int, line.split()))
    row.sort()

    if row[0] + row[1] < row[3]:
        count += 1

print(count)