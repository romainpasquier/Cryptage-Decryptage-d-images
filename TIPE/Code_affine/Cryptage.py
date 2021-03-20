from Code_annexes.Nombre_premiers import dimensions
from Exucatable.Modification_affine import pas, img_source, fond_crypte
from Code_annexes.Quadrillage import quadrillage, zeros
from Création_clef_et_matrice.Création_clef import a, b, c, d


def cryptage(img):
    x_img, y_img = img.size

    taille_x = dimensions(y_img // pas) + 1
    taille_y = dimensions(x_img // pas) + 1

    grille_4, grille_2 = quadrillage(img)
    grille_crypte4, grille_crypte2 = zeros(taille_x, taille_y)

    for i in range(1, len(grille_2)):
        for j in range(1, len(grille_2[0])):
            x = (a * i + b) % (len(
                grille_2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_2[0]) - 1)  # idem

            grille_crypte4[x + 1][y + 1] = grille_4[i][j]
            grille_crypte2[x + 1][y + 1] = grille_2[i][j]

    return grille_crypte4, grille_crypte2


def cryptage_img(img):

    grille_4, grille_2 = quadrillage(img)
    grille_crypte4, grille_crypte2 = cryptage(img_source)

    for i in range(1, len(grille_2)):
        for j in range(1, len(grille_2[0])):
            bloc_img = img.crop(grille_4[i][j])

            fond_crypte.paste(bloc_img, grille_crypte2[i][j])
