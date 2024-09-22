print('z, x, y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not ((x or y) <= (y == z)):
                print(f'{z}, {x}, {y}')