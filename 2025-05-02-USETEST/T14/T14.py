alphabet = "0123456789ABCDEFGHIJK"
for x in alphabet:
    equation = int('82934'+x+'2', 21) + int('2924'+x+x+'7', 21) + int('67564'+x+'8', 21)
    if equation % 20 == 0:
        print(x, equation/20)