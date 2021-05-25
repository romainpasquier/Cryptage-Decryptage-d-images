import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import sqrt
import time

taille_image_max = 35
nb_moyenne = 50

def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme

def moyenne(liste):
    return somme(liste)/len(liste)

def dimensions(x):
    premier = [2]

    for i in range(3, x+1):
        sqrtI = sqrt(i)
        for j in premier:
            if i % j == 0:
                break
            if j > sqrtI:
                premier.append(i)
                break

    return premier[-1]

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
    taille_x = dimensions(x)

    _, grille_2 = zeros(taille_x + 1, taille_x + 1)

    for x in range(taille_x):
        for y in range(taille_x):
            grille_2[x + 1][y + 1] = (y, x)
    return grille_2

def combinaisons(n):
    L = []
    for a in range(1,n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                for d in range(1, n+1):
                    L.append([a, b, c, d])
    return L

def cryptage_tab(x, a, b, c, d):
    taille_x = dimensions(x)
    grille_2 = decoupage_tab(x)
    _, grille_crypte2 = zeros(taille_x + 1, taille_x + 1)

    for i in range(1, len(grille_2)):
        for j in range(1, len(grille_2[0])):
            x = (a * i + b) % (len(grille_2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_2[0]) - 1)  # idem

            grille_crypte2[x + 1][y + 1] = grille_2[i][j]

    return grille_crypte2

def decryptage_temps(x, a, b, c, d):
    taille_x = taille_x = dimensions(x)
    grille_crypte2 = cryptage_tab(x, a, b, c, d)
    _, grille_decrypte2 = zeros(taille_x+1, taille_x+1)

    for i in range(1, len(grille_crypte2)):
        for j in range(1, len(grille_crypte2[0])):
            x = (a * i + b) % (len(
                grille_crypte2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_crypte2[0]) - 1)  # idem

            grille_decrypte2[i][j] = grille_crypte2[x + 1][y + 1]

    return grille_decrypte2

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

def decrypte_tab(x, n):
    tab = []
    for i in range(1, x+1):
        tps = moyenne_temps(i, n)
        tab.append(tps)
    return tab

def decrypte_tab_affine(x, n):
    tab = []
    for i in range(1, x+1):
        tps = moy_temps_affine(i, n)
        tab.append(tps)
    return tab

x = np.linspace(1, taille_image_max, taille_image_max)
y = decrypte_tab(taille_image_max, nb_moyenne)
z = decrypte_tab_affine(taille_image_max, nb_moyenne)

dep = time.time()

fig = plt.figure(figsize=(100, 100))
ax = fig.add_subplot(111)

plt.plot(x, y, "-r", label="Force brut")
plt.plot(x, z, "-b", label="Mon code")

ax.set_title('Comparaison des temps moyens d éxécution')
ax.set_xlabel('Tailles images carrées (en pixels)')
ax.set_ylabel('Temps (en secondes)')

ax.legend(loc='best')
plt.show()

arv = time.time()

print(arv-dep)