from Code_annexes.Nombre_premiers import dimensions
from Exucatable.Modification_affine import pas, img_source, fond_crypte, fond_decrypte
from Code_affine.Cryptage import cryptage
from Code_annexes.Quadrillage import zeros
from Création_clef_et_matrice.Création_clef import a, b, c, d


def decryptage(img):
    x_img, y_img = img.size

    taille_x = dimensions(y_img // pas) + 1
    taille_y = dimensions(x_img // pas) + 1

    grille_crypte4, grille_crypte2 = cryptage(img)
    grille_decrypte4, grille_decrypte2 = zeros(taille_x, taille_y)

    for i in range(1, len(grille_crypte2)):
        for j in range(1, len(grille_crypte2[0])):
            x = (a * i + b) % (len(
                grille_crypte2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
            y = (c * j + d) % (len(grille_crypte2[0]) - 1)  # idem

            grille_decrypte2[i][j] = grille_crypte2[x + 1][y + 1]

    return grille_decrypte4, grille_decrypte2


def decryptage_img(img):

    grille_crypte4, grille_crypte2 = cryptage(img)
    grille_decrypte4, grille_decrypte2 = decryptage(img)

    for i in range(1, len(grille_crypte2)):
        for j in range(1, len(grille_crypte2[0])):
            bloc_img = img.crop(grille_crypte4[i][j])

            fond_decrypte.paste(bloc_img, grille_decrypte2[i][j])
