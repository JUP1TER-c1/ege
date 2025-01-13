def alg(N):
    tmp = bin(N)[2:]
    for i in range(3):
        digi_sum = sum(list(map(int, list(str(int(tmp, 2))))))
        if digi_sum % 2 == 1:
            tmp += '1'
        else:
            tmp += '0'

    return int(tmp, 2)

for i in range(200):
    print(f'Input: {i}\nOutput: {alg(i)}\nOut//8: {alg(i)//8}\n')
print((1_987_654_321//8) - (123_456_789//8))
print(alg(1_987_654_321//8))