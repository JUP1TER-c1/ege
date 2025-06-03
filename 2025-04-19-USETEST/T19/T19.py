def game(pile, moves):
    if pile >= 128:
        return moves%2 == 0
    if moves == 0:
        return 0
    outcomes = [game(pile + 2, moves - 1), game(pile + 5, moves - 1), game(pile * 2, moves - 1)]
    if moves%2 != 0:
        return any(outcomes)
    return all(outcomes)

print([s for s in range(1, 128) if game(s, 2)])
print([s for s in range(1, 128) if not game(s, 1) and game(s, 3)])
print([s for s in range(1, 128) if not game(s, 2) and (game(s, 2) or game(s, 4))])