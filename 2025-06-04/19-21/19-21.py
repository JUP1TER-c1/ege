def game(pile1, pile2, step):
    if pile1 + pile2 >= 81: return step % 2 == 0
    if step == 0: return 0
    outcomes = [game(pile1 + 1, pile2, step - 1), game(pile1 * 2, pile2, step - 1), game(pile1, pile2 + 1, step - 1), game(pile1, pile2 * 2, step - 1)]
    return any(outcomes) if step % 2 == 1 else all(outcomes)

print('20', [s for s in range(1, 74) if game(7, s, 4) and not game(7, s, 2)])