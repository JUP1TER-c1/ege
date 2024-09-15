n = 1
while True:
    binNumber = bin(n)
    strBinNumber = str(binNumber)[2:]

    strBinNumber += str((strBinNumber.count("1")) % 2)
    strBinNumber += str((strBinNumber.count("1")) % 2)

    result = int(strBinNumber, 2)

    if result > 97:
        print(result)
        break

    n+=1

# Ответ - 102