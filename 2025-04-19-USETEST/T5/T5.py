def base10tobase3(n):
    result = ''
    while n > 0:
        result += str(n % 3)
        n //= 3

    return result[::-1]

def algo(N):
    b3N = base10tobase3(N)
    if N % 3 == 0:
        b3N += b3N[-2:]
    else:
        b3N += base10tobase3((N%3)*3)
    return int(b3N, 3)

for i in range(1, 150):
    if algo(i) <= 150:
        print(i)
print(algo(16), algo(17))