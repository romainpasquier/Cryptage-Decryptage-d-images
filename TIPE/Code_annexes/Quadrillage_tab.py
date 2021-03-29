from Code_annexes.Nombre_premiers import dimensions

pat = 1

def zeros(x, y):
    t_4 = []
    t_2 = []
    for i in range(x):
        t_4.append([])
        t_2.append([])
        for j in range(y):
            t_4[i].append((0, 0, 0, 0))
            t_2[i].append((0, 0))
    return t_4, t_2


def decoupage_tab(x):
    taille_x = dimensions(x // pat)

    _, grille_2 = zeros(taille_x + 1, taille_x + 1)

    for x in range(taille_x):
        for y in range(taille_x):
            grille_2[x + 1][y + 1] = (y * pat, x * pat)
    return grille_2
