def machine(n):
    sum1 = int(n[0]) + int(n[1])
    sum2 = int(n[1]) + int(n[2])
    return str(min(sum1, sum2)) + str(max(sum1, sum2))

for i in range(100, 1000):
    if machine(str(i)) == '714':
        print(i)