def distance(index1, index2, total):
    return min(abs(index1 - index2), abs((total - abs(index1 - index2))))

fileA = list(map(int, open('27_A.txt').read().split()))
amount = fileA.pop(0)
for i in range(amount):
    fileA[i] *= 3


