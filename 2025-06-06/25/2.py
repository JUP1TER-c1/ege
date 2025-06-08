def task(n):
    res = [n]
    for delimiter in range(1, (n//2) + 1):
        if n % delimiter == 0:
            res.append(delimiter)
    return str(sum(res))
num = 500000
while True:
    R = task(num)
    if R[-1] == '6':
        print(num, R)
    num += 1