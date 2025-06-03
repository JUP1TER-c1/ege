count = 0
for line in open('09.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) > 4: continue
    repeated = []
    other = []
    flag = False
    for i in row:
        if row.count(i) >= 3:
            flag = True
        if row.count(i) > 1:
            repeated.append(i)
        else:
            other.append(i)

    if len(other) == 0: continue
    if flag and sum(repeated)/len(repeated) > sum(other)/len(other):
        count += 1

print(count)
