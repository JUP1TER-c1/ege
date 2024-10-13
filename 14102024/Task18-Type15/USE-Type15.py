for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if  (x < a) or (y < a) or (x + 2 * y > 50):
                k += 1
    if k == 90_000:
        print(a)
        break