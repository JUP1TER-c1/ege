print('z, w, x, y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (y <= z) and not ((y or w) <= (z and x)):
                    print(f'{z}, {w}, {x}, {y}')