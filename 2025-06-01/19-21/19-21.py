#def game(pile, step):
#    if pile >= 51: return step % 2 == 0
#    if step == 0: return 0
#    moves = [game(pile + 1, step - 1), game(pile + 4, step - 1), game(pile * 2, step - 1)]
#    return any(moves) if step % 2 == 1 else all(moves)
#
#print([s for s in range(51) if game(s, 2)])

def game(pile, step):
    if pile >= 51: return step % 2 == 0
    if step == 0: return 0
    moves = [game(pile + 1, step - 1), game(pile + 4, step - 1), game(pile * 2, step - 1)]
    return any(moves) if step % 2 == 1 else all(moves)

print([s for s in range(51) if game(s, 4) and not game(s, 2)])