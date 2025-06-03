cnt = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) != len(row) - 2: continue
    rep_numbers = [number for number in row if row.count(number) == 3]
    if sum(rep_numbers)**2 > (sum(row) - sum(rep_numbers))**2:
        cnt += 1
        print(row, rep_numbers)
print(cnt)