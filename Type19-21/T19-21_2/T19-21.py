def game(pile, step):
    if pile >= 51:
        return step%2 == 0
    if step == 0:
        return 0

    moves = [
        game(pile+1, step-1),
        game(pile+4, step-1),
        game(pile*2, step-1)
    ]

    if step%2 == 0:
        return all(moves)
    return any(moves)

print([s for s in range(1, 51) if game(s, 2)])