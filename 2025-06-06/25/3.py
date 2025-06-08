def task(n):
    res = 1
    cnt = 0
    for delim in range(2, n + 1):
        if n % delim == 0:
            res *= delim
            cnt += 1
        if cnt == 5:
            return res
    return 0


res = []
N = 500_000_001
while len(res) < 5:
    M = task(N)
    #print(M)
    if 0 < M < N:
        res.append(M)
        print(M)
    N += 1
print(res)