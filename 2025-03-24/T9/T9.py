data = open('9.txt').read()
data = data.replace('\t', ' ')
data = data.split('\n')
for i in range(len(data)):
    data[i] = list(map(int, data[i].split()))

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if len(set(data[i])) != len(data[i]): continue
        if data[i][j] >= sum(data[i]) / len(data[i]): continue
        column_count = 0
        for k in range(len(data)):
            if data[k][j] == data[i][j]:
                column_count += 1
        if column_count < 335: continue
        count += 1
print(count)