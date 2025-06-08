def algo(N):
    binN = bin(N)[2:]
    cache = bin(binN.count('1'))[2:] + bin(binN.count('0'))[2:]
    return int(cache, 2)
for n in range(100000000, 1000000000):
    if algo(n) == 183:
        print(n)
        break