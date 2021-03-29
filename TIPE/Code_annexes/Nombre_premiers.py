from math import sqrt

# Fonction qui renvoi le plus grand nombre entier inférieur à x


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
