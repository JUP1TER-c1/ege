def algo(N):
    binN = bin(N)[2:]
    if sum(list(map(int, str(int(binN, 2)).split()))) % 2 == 1:
        binN += '1'
    else: binN += '0'

    if sum(list(map(int, str(int(binN, 2)).split()))) % 2 == 1:
        binN += '1'
    else: binN += '0'

    if sum(list(map(int, str(int(binN, 2)).split()))) % 2 == 1:
        binN += '1'
    else: binN += '0'

    return int(binN, 2)

for N in range(2025):
    if algo(N) > 2025:
        print(N)
        break