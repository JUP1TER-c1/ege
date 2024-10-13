count = 0
for line in open('09.txt'):
    M = sorted([int(x) for x in line.split()])
    if len(set(M)) == 5:
        copied = sum(M) - sum(set(M))
        if copied < (sum(M) - copied*2) / 4:
            count += 1
print(count)