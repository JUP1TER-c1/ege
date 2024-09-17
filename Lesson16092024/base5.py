def base20toBase10(number):
    steck = '0123456789ABCDEFGHIJ'
    result = 0
    for i in range(len(number)):
        result += steck.index(number[i])*(20**(len(number) - (i + 1)))
    return result

print(base20toBase10('AB9CH'))

