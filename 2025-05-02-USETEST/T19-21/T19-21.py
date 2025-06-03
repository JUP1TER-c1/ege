from math import floor


def game(pile, step):
    if pile <= 87:
        return step % 2 == 0
    if step == 0:
        return 0
    outcomes = [game(pile - 2, step - 1), game(floor(pile/2), step - 1)]

    if step % 2 != 0:
        return any(outcomes)
    return all(outcomes)

print([s for s in range(88, 300) if game(s, 2)])
print([s for s in range(88, 300) if not game(s, 1) and game(s, 3)])
print([s for s in range(88, 300) if not game(s, 2) and game(s, 4)])