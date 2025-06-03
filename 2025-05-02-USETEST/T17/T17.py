

data = list(map(int, open("17.txt").read().split('\n')))
negatives = [number for number in data if number < 0]
result = []
for i in range(len(data)-2):
    triplet = [data[i], data[i+1], data[i+2]]
    if (max(triplet) * min(triplet)) > sum(negatives):
        result.append(sum(triplet))

print(len(result), max(result))