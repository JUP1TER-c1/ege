data = list(map(float, open('18.txt').read().split()))

max_sum = 0
cache = 0
flag = False
for i in range(len(data) - 1):
    if cache < 0:
        cache = 0
        flag = False
    if abs(data[i] - data[i + 1]) <= 8:
        flag = True
        cache += data[i]
    else:
        if flag:
            cache += data[i]
            flag = False
            max_sum = max(max_sum, cache)
            cache = 0



print(max_sum)