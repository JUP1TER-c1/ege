def algorithm(n):
    bin_n = bin(n)[2:]
    if n % 2: bin_n += '10'
    else: bin_n += '01'
    return int(bin_n, 2)

for i in range(0, 1400):
    R = algorithm(i)
    if R > 102:
        print(R)
        break