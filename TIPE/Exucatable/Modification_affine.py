from PIL import Image

# Pour ouvrir l'image de base on a:
img_source = Image.open(r"C:\Users\37rom\PycharmProjects\TIPE\Images\sujet_3.jpg")
x_img, y_img = img_source.size

fond_crypte = Image.new('RGB', (x_img, y_img), (0, 255, 255))
fond_decrypte = Image.new('RGB', (x_img, y_img), (255, 255, 0))

# Pour le pas on prend :
pas = 1
