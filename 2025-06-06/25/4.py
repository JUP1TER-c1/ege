from infEGE import factorize

cnt = 0
for num in range(2422000, 2422081):
    if len(factorize(num)) == 1:
        cnt += 1
        print(cnt, num)
