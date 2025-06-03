from itertools import product
al = []
maxx = 0
for i in product('12', repeat=13):
    i = str(''.join(i))
    if i.count('1') == 10 and i.count('2') == 3:
        if not(i in al):
            al.append(i)
for a in al:
    c = 0
    while '11' in a:
        if '112' in a:
            a = a.replace('112','6',1)
        else:
            a = a.replace('11','5',1)
    for k in a:
        c = c + int(k)
    if c > maxx:
        maxx = c
print(maxx)