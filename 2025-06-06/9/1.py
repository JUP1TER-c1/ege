n_line = 0
max_sum = 0
for line in open('1.txt'):
    n_line += 1
    row = list(map(int, line.split()))
    if len(set(row)) != len(row) - 2: continue
    repeated = 0
    other = []
    for number in row:
        if row.count(number) == 3: repeated = number
        else: other.append(number)
    if sum(other)/len(other) > repeated: continue
    row = sorted(row)
    if row[-1] % row[0] == 0: continue
    if sum(row) > max_sum:
        print(n_line)
        max_sum = sum(row)
