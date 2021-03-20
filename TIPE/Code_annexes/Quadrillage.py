from Exucatable.Modification_affine import pas, img_source
from Code_annexes.Nombre_premiers import dimensions

# Création tableau de 0 avec une ligne et une collonne de plus que requis :


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

# Création de notre grille :


def quadrillage(img):
    x_img, y_img = img.size

    taille_x = dimensions(y_img // pas)
    taille_y = dimensions(x_img // pas)

    grille_4, grille_2 = zeros(taille_x + 1, taille_y + 1)

    for x in range(taille_x):
        for y in range(taille_y):
            grille_4[x + 1][y + 1] = (y * pas, x * pas, y * pas + pas, x * pas + pas)
            grille_2[x + 1][y + 1] = (y * pas, x * pas)
    return grille_4, grille_2


grille_4, grille_2 = quadrillage(img_source)

# Valeurs limites :
x_lim, y_lim = grille_2[len(grille_2)-1][len(grille_2[0])-1]
