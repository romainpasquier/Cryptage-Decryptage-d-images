from math import sqrt
import matplotlib.pyplot as plt

x_max = 1080

y_max = 1920

def creer_couple(a, b):

    def couple(x, y):
        A = []
        for i in range(1, x+1):
            for j in range(1, y+1):
                A.append((i, j))
        return A

    def produit(A):
        (a, b) = A
        return a*b

    def enlever(A):
        for i in range(len(A)):
            for k in A:
                try:
                    if produit(k) == produit(A[i]) and not(k == A[i]):
                        A.remove(k)
                except:
                    pass
        return A

    X = couple(a, b)
    Y = enlever(X)


    return X

couple = creer_couple(x_max, y_max)
print(couple)

def creer_aire(l):
    A = []
    for i in range(len(l)):
        (a, b) = l[i]
        c = a*b
        A.append(c)
    return A

aire_couple = (creer_aire(couple))
print(aire_couple)

def perte_ind(x):
    premier = [2]

    if x == 0 or x == 1:
        return x

    else:
        for i in range(3, x+1):
            sqrtI = sqrt(i)
            for j in premier:
                if i % j == 0:
                    break
                if j > sqrtI:
                    premier.append(i)
                    break

        return premier[-1]

def perte(l):
    A = []
    for i in range(len(l)):
        (a,b) = l[i]
        x = perte_ind(a)
        y = perte_ind(b)
        A.append((x, y))
    return A

couple_dim = perte(couple)
print(couple_dim)

aire_couple_dim = creer_aire(couple_dim)
print(aire_couple_dim)
def proportions(l1, l2):
    A = []
    for i in range(len(l1)):
        a1 = l1[i]
        a2 = l2[i]

        if a2 == a1:
            A.append(0)
        else:
            per = ((a1-a2)/a1) * 100
            A.append(per)
    return A

prop = proportions(aire_couple, aire_couple_dim)
print(prop)

def somme(liste):
    _somme = 0
    for i in liste:
        _somme = _somme + i
    return _somme

def moyenne(liste):
    return somme(liste)/len(liste)

moy = moyenne(prop)
print(moy)

def list_moyenne(moy, aire):
    A = []
    for i in range(len(aire)):
        A.append(moy)
    return A

list_moy = list_moyenne(moy, aire_couple)
print(list_moy)

def tracer(aire, prop, list_moy):

    fig = plt.figure(figsize=(100, 100))

    ax = fig.add_subplot(111)

    plt.plot(aire, prop, "-r", label="Taille de l'image x_max = " + str(x_max) + " , y_max = " + str(y_max))
    plt.plot(aire, list_moy, "-b", label="Proportion perdu moyen = " + str(moy)[:3] + " %")

    ax.set_title('Proportion de limage perdu')
    ax.set_xlabel('Taille de l image (en pixels x pixels)')
    ax.set_ylabel('Proportion de l image perdu (en %)')

    ax.legend(loc='best')
    plt.show()

tracer(aire_couple, prop, list_moy)
