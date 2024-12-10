def round(pile1, pile2, moves):
    if pile1+pile2>=82: return moves%2==0
    if moves==0:return 0
    h=[round(pile1 + 1, pile2, moves - 1), round(pile1 * 4, pile2, moves - 1), round(pile1, pile2 + 1, moves - 1), round(pile1, pile2 * 4, moves - 1)]
    return any(h) if (moves - 1) % 2 == 0 else all(h)

print(19, [s for s in range(1,77+1) if round(4, s, 2)])
print(20, [S for S in range(1, 77 + 1) if not round(4, S, 1) and round(4, S, 3)])
print(21, [s for s in range(1,77+1) if not round(4, s, 2) and round(4, s, 4)])