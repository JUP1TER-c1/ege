file = open('107_9.csv')
c = 0
for row in file:
    row = row.replace('\n', '')
    cache = list(map(int, row.split(',')))

    cache.sort()
    sum_of_minimals = cache[0] + cache[1]
    if sum_of_minimals < cache[2] or sum_of_minimals < cache[3]:
        c += 1

print(c) #Ответ: 3094
