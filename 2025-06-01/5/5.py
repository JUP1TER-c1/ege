def algo(N):
    binN = bin(N)[2:]
    if N % 2 == 0:
        binN = '10' + binN
    else:
        binN = '1' + binN + '01'
    return int(binN, 2)

ress = [algo(n) for n in range(12)]
print(max(ress), ress)