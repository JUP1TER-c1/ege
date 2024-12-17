def machine(n):
    cache = [int(n[0]) + int(n[1]), int(n[1]) + int(n[2]), int(n[2]) + int(n[3])]
    cache.remove(min(cache))
    cache.sort()
    result = str(min(cache)) + str(max(cache))
    return result

for i in range(1000, 10000):
    if machine(str(i)) == '1215':
        print(i)
        break