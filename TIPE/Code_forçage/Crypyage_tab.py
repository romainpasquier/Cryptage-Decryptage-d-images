from Code_annexes.Nombre_premiers import dimensions
from Code_annexes.Quadrillage_tab import decoupage_tab, zeros

pat = 1


def cryptage_tab(x, a, b, c, d):
    taille_x = dimensions(x // pat)
    grille_2 = decoupage_tab(x)
    _, grille_crypte2 = zeros(taille_x + 1, taille_x + 1)

    for i in range(1, len(grille_2)):
        for j in range(1, len(grille_2[0])):
            x = (a * i + b) % (len(grille_2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_2[0]) - 1)  # idem

            grille_crypte2[x + 1][y + 1] = grille_2[i][j]

    return grille_crypte2
