def DIV(n, m):
    return n % m == 0

def F(x, A):
    return (DIV(x, 2) <= (not DIV(x, 5))) or (x + A >= 90)

for A in range(-3000, 3000):
    if all([F(x, A) for x in range(1, 3000)]):
        print(A)
        break
