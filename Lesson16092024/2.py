array = [i for i in range(1, 101)]

for index, value in enumerate(array):
    if value%2 == 0:
        array[index] = 0

print(array)