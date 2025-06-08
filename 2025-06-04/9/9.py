cnt = 0
for line in open('9.txt'):
    row = sorted(list(map(int, line.split())))
    if row[-1] >= sum(row) - row[-1]: continue
    if len(set(row)) == len(row) - 1:
        cnt += 1

print(cnt)
