print('w, z, y, x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((z and y) or ((x <= z ) == (y <= w))):
                    print(f'{w}, {z}, {y}, {x}')