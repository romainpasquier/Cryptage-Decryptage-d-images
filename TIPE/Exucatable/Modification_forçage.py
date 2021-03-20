import numpy as np
from Code_forçage.Decryptage_tab import decrypte_tab
from Temps.Temps_affine import decrypte_tab_affine


# Forçage :

taille_image_max = 500
nb_moyenne = 100

x = np.linspace(1, taille_image_max, taille_image_max)
y = decrypte_tab(taille_image_max, nb_moyenne)
z = decrypte_tab_affine(taille_image_max, nb_moyenne)
