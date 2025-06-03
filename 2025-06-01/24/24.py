seq = open('24.txt').readline()
seq = seq.replace('*', '+')
seq = seq.replace('-', '+')
seq = seq.replace('+0+', '+5+')
banned_combs = ['++', '+0', '+|', '|+', '|0', '||']
flag = any([(comb in seq) for comb in banned_combs])
while flag:
    for comb in banned_combs:
        seq = seq.replace(comb, '|')
    flag = any([(comb in seq) for comb in banned_combs])

print(seq)
equations = seq.split('|')
maxlen = max(equations, key=len)
print(maxlen, len(maxlen))