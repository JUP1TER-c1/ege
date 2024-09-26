dictionary = {0: 'A', 1: 'K', 2:'P', 3:'Y'}
for l1 in range(4):
    for l2 in range(4):
        for l3 in range(4):
            for l4 in range(4):
                for l5 in range(4):
                    if l5 + (4*l4) + (4*4*l3) + (4*4*4*l2) + (4*4*4*4*l1) + 1 == 450:
                        print(dictionary[l1] + dictionary[l2] + dictionary[l3] + dictionary[l4] + dictionary[l5])

