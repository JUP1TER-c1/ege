def algo(N):
    N = bin(N)[2:]
    digisum = sum(int(d) for d in N)
    N += str(digisum%2)
    digisum = sum(int(d) for d in N)
    N += str(digisum % 2)
    return int(N, 2)

print(algo(12) == 48, algo(7) == 30)

for N in range(253):
    if algo(N) > 253:
        print(N)
        break
