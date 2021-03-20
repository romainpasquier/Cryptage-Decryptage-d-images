from random import randint
from Exucatable.Modification_affine import x_img, y_img

# Créer la matrice X


def mat(x):
    X = []
    for i in range(x):
        X.append([])
        for j in range(x):
            X[i].append(randint(1, min(x_img, y_img)))
    return X

X = mat(10)
