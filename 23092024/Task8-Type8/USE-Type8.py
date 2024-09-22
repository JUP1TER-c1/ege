from itertools import product
count = 0
for p in product("012345678", repeat=5):
    if p.count("5") == 1 and p[0]!="0":
        i = p.index('5')
        if i != 0 and i != 4:
            if p[i - 1] not in '137' and p[i + 1] not in '137':
                count+=1
        elif i == 0:
            if p[1] not in '137':
                count+=1
        elif i == 4:
            if p[3] not in '137':
                count += 1
print(count)