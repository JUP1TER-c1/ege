def auto(N):
    N = str(N)
    cache1 = str(int(N[0]) + int(N[1]))
    cache2 = str(int(N[1]) + int(N[2]))
    return cache1 + cache2 if int(cache1) <= int(cache2) else cache2 + cache1

for n in range(100, 1000):
    if int(auto(n)) == 714:
        print(n)
        break
print(auto(168) == 714)