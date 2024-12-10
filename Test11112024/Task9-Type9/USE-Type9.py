count = 0
with open('09.txt') as file:
    for line in file:
        row = list(map(int, line.split()))
        row = sorted(row)
        if row[0]*row[1] + row[0]*row[2] < row[1]*row[2]:
            count += 1

print(count)