def get_delimiters_mod(n):
    res = []
    for candidate in range(2, n//2 + 1):
        if n % candidate == 0:
            res.append(candidate)
    return 0 if res == [] else res[-1] + res[0]

result = []
i = 700_000
while len(result) < 5:
    M = get_delimiters_mod(i)
    if str(M)[-1] == '4':
        print(i, M)
        result.append(i)
    i += 1

