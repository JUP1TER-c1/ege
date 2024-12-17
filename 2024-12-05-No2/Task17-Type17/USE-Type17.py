count = 0
data = [int(number) for number in open('17.txt')]
triplets = []
max123 = max([number for number in data if number%1000 == 123])

for i in range(len(data) - 2):
    cache = data[i:i+3]
    if sum(cache) <= max123: continue
    div3_ic = 0
    len5_ic = 0
    for number in cache:
        if number%3 == 0:
            div3_ic += 1
        if len(str(number)) == 5:
            len5_ic += 1
    if div3_ic != 1: continue
    if len5_ic < 2: continue
    triplets.append(sum(cache))

print(len(triplets), max(triplets))