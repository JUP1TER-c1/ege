for A in range(0, 300):
    k = 0
    for m in range(0, 300):
        for n in range(0, 300):
            if (3*m + 4*n > 63) or ((m <= A) and (n < A)):
                k += 1
    if k == 90_000:
        print(A)
        break