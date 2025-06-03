def DEL(n, m):
    return n % m == 0

def func(x, A):
    inB = 60 <= x <= 80
    return DEL(x, A) or (inB <= (not DEL(x, 22)))

for A in range(1, 2048):
    if all([func(x, A) for x in range(1, 10001)]):
        print(A)