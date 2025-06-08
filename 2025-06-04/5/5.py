def algo(N):
    binN = bin(N)[2:]
    if binN.count('1') % 2 == 0:
        binN = '10' + binN[2:] + '0'
    else:
        binN = '11' + binN[2:] + '1'
    return int(binN, 2)

for n in range(1000):
    if algo(n) > 19:
        print(n)
        break
print(algo(8))