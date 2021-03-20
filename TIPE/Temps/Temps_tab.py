from random import randint
import time
from Code_forçage.Crypyage_tab import cryptage_tab
from Code_annexes.Moyenne import moyenne
from Création_clef_et_matrice.Création_combinaisons import combinaisons


def moyenne_temps(x, n):
    tab = []
    dep1 = time.time()
    t = combinaisons(x)
    arv1 = time.time()
    for i in range(1, n+1):
        dep = time.time()

        a0 = randint(1, x)
        b0 = randint(1, x)
        c0 = randint(1, x)
        d0 = randint(1, x)

        for j in range(len(t)):
            a, b, c, d = t[j]
            if cryptage_tab(x, a0, b0, c0, d0) != cryptage_tab(x, a, b, c, d):
                pass
            else:
                break
        arv = time.time()
        tab.append((arv1 - dep1) + (arv - dep))
    return moyenne(tab)

