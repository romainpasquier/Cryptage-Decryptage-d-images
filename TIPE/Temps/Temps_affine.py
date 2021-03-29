from Code_forçage.Crypyage_tab import  cryptage_tab
from Code_annexes.Quadrillage_tab import zeros
import time
from random import randint
from Code_annexes.Moyenne import moyenne
from Code_annexes.Nombre_premiers import dimensions

pat = 1


def decryptage_temps(x, a, b, c, d):
    taille_x = taille_x = dimensions(x // pat)
    grille_crypte2 = cryptage_tab(x, a, b, c, d)
    _, grille_decrypte2 = zeros(taille_x+1, taille_x+1)

    for i in range(1, len(grille_crypte2)):
        for j in range(1, len(grille_crypte2[0])):
            x = (a * i + b) % (len(
                grille_crypte2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_crypte2[0]) - 1)  # idem

            grille_decrypte2[i][j] = grille_crypte2[x + 1][y + 1]

    return grille_decrypte2


def moy_temps_affine(x, n):
    tab = []

    a = randint(1, x)
    b = randint(1, x)
    c = randint(1, x)
    d = randint(1, x)

    for i in range(1, n+1):
        dep = time.time()
        decryptage_temps(x, a, b, c, d)
        arv = time.time()

        tab.append(arv - dep)
    return moyenne(tab)


def decrypte_tab_affine(x, n):
    tab = []
    for i in range(1, x+1):
        tps = moy_temps_affine(i, n)
        tab.append(tps)
    return tab
