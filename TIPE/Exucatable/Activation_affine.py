from PIL import Image
import time
from Code_annexes.Quadrillage import x_lim, y_lim
from Code_affine.Cryptage import cryptage_img
from Code_affine.Decryptage import decryptage_img
from Exucatable.Modification_affine import img_source, fond_crypte, fond_decrypte, pas
from Création_clef_et_matrice.Création_clef import ecrit, a1, b1, c1, d1
from Création_clef_et_matrice.Création_matrice import X
from Code_annexes.Rotate_RGB import rotate_crypte, rotate_decrypte


# Trafic d'images :
img_source.show()

rotate_crypte(img_source, a1, b1, c1, d1)

d_crypte = time.time()
cryptage_img(img_source)
a_crypte = time.time()

test_crypte = fond_crypte.crop((0, 0, x_lim + pas, y_lim + pas))
test_crypte.save(r"C:\Users\37rom\PycharmProjects\TIPE\Images\image_crypte.jpg")
image_crypte = Image.open(r"C:\Users\37rom\PycharmProjects\TIPE\Images\image_crypte.jpg")

image_crypte.show()

d_decrypte = time.time()
decryptage_img(fond_crypte)
a_decrypte = time.time()

rotate_decrypte(fond_decrypte, a1, b1, c1, d1)

test_decrypte = fond_decrypte.crop((0, 0, x_lim + pas, y_lim + pas))
test_decrypte.save(r"C:\Users\37rom\PycharmProjects\TIPE\Images\image_decrypte.jpg")
image_decrypte = Image.open(r"C:\Users\37rom\PycharmProjects\TIPE\Images\image_decrypte.jpg")

image_decrypte.show()

# Timer :
print("Clef :")
print(ecrit)

print("")

print("Matrice X :")
print(X)

print("")

print("Dimensions de l'image")
print(x_lim, y_lim)

print("")

print("Cryptage :")
print(a_crypte - d_crypte)
print(" secondes")

print("")

print("Decryptage :")
print(a_decrypte - d_decrypte)
print(" secondes")
