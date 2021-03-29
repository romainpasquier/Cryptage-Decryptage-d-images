from PIL import Image
from math import sqrt
import matplotlib.pyplot as plt
from datetime import datetime
import random
import os
import time

from statistics import mean

x_max = 500

y_max = 500

pas = 10

nb = 2

key = "601668515883179420210325235841203kmTRgpnLrDeKUGAlHVFBE6Mj7vd8wqI0WZ9i4hs2YQauCJcSP5O1oxfbtNX"


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














def creer_image(l):
    for i in range(len(l)):
        im = Image.new(mode="RGB", size = (l[i]))
        im.save("C:/Users/37rom/PycharmProjects/Application/Application android/image/" + str(i) + ".jpg")

def app_cryptage(filename):

    dep = time.time()

    img_source = Image.open(filename)
    x_img, y_img = img_source.size
    fond_crypte = Image.new('RGB', (x_img, y_img), (0, 255, 255))

    pas = 1

    def cryptage(img):
        x_img, y_img = img.size
        taille_x = dimensions(y_img // pas) + 1
        taille_y = dimensions(x_img // pas) + 1
        grille_2 = quadrillage(img)
        grille_crypte2 = zeros(taille_x, taille_y)
        for i in range(1, len(grille_2)):
            for j in range(1, len(grille_2[0])):
                x = (a * i + b) % (len(grille_2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
                y = (c * j + d) % (len(grille_2[0]) - 1)  # idem
                grille_crypte2[x + 1][y + 1] = grille_2[i][j]
        return grille_crypte2

    def dimensions(x):
        premier = [2]
        for i in range(3, x + 1):
            sqrtI = sqrt(i)
            for j in premier:
                if i % j == 0:
                    break
                if j > sqrtI:
                    premier.append(i)
                    break
        return premier[-1]

    def zeros(x, y):
        t_2 = []
        for i in range(x):
            t_2.append([])
            for j in range(y):
                t_2[i].append((0, 0))
        return t_2

    def quadrillage(img):
        x_img, y_img = img.size
        taille_x = dimensions(y_img // pas)
        taille_y = dimensions(x_img // pas)
        grille_2 = zeros(taille_x + 1, taille_y + 1)
        for x in range(taille_x):
            for y in range(taille_y):
                grille_2[x + 1][y + 1] = (y * pas, x * pas)
        return grille_2

    def transpo_clef(ecrit):
            for i in range(len(ecrit)):
                ecrit[i] = int(ecrit[i])
            return ecrit

    X = [[1531, 1894, 1403, 512, 588, 1709, 460, 606, 1537, 286],
             [925, 1901, 1803, 318, 1299, 1680, 1465, 599, 762, 453],
             [1475, 1819, 587, 1684, 1589, 534, 1533, 1435, 607, 850],
             [1667, 1244, 1405, 818, 523, 667, 600, 1364, 499, 11],
             [621, 304, 312, 159, 1871, 190, 741, 1202, 1809, 1247],
             [810, 266, 807, 1144, 1526, 187, 1075, 184, 1494, 1251],
             [1370, 348, 1590, 1841, 923, 87, 346, 308, 1584, 606],
             [1074, 43, 913, 900, 1135, 1628, 1599, 1855, 267, 930],
             [456, 151, 1714, 49, 1037, 364, 1625, 1352, 767, 1493],
             [705, 84, 477, 1081, 1613, 1035, 32, 1471, 1106, 789]]

    envoi = "6016685158831794202103"
    date = str(datetime.now())

    aa1 = date[0:2]
    aa2 = date[2:4]
    mm = date[5:7]
    jj = date[8:10]
    hh = date[11:13]
    mi = date[14:16]
    ss = date[17:19]
    cc = date[20:22]

    test = list(envoi)
    date1 = [int(aa1), int(aa2), int(mm), int(jj), int(hh), int(mi), int(ss), int(cc)]
    clef1 = transpo_clef(test)

    clef = clef1 + date1
    ecrit = envoi + aa1 + aa2 + mm + jj + hh +mi + ss +cc

    p = 16

    a_clefx = clef[(clef[16]) % p]
    a_clefy = clef[(clef[17]) % p]

    b_clefx = clef[(clef[18]) % p]
    b_clefy = clef[(clef[19]) % p]

    c_clefx = clef[(clef[20]) % p]
    c_clefy = clef[(clef[21]) % p]

    d_clefx = clef[(clef[22]) % p]
    d_clefy = clef[(clef[23]) % p]

    a = X[a_clefx][a_clefy]
    b = X[b_clefx][b_clefy]
    c = X[c_clefx][c_clefy]
    d = X[d_clefx][d_clefy]

    clef.pop(a_clefx)
    clef.pop(a_clefy)

    clef.pop(b_clefx)
    clef.pop(b_clefy)

    clef.pop(c_clefx)
    clef.pop(c_clefy)

    clef.pop(d_clefx)
    clef.pop(d_clefy)

    a1 = clef[0]
    b1 = clef[1]
    c1 = clef[2]
    d1 = clef[3]

    def rotate(lst, x):
        if x >= 0:
            for i in range(x):
                lastNum = lst.pop(-1)
                lst.insert(0, lastNum)
        else:
            for i in range(abs(x)):
                firstNum = lst.pop(0)
                lst.append(firstNum)
        return lst

    def rotate_crypte(img, a, b, c, d):
        x_img, y_img = img.size
        a = a % 3
        b = b % 3
        for i in range(x_img):
            for j in range(y_img):
                (R, V, B) = img.getpixel((i, j))
                if j % 2 == 0 and i % 2 == 0:
                    rot = rotate([R, V, B], a)
                if j % 2 == 1 and i % 2 == 1:
                    rot = rotate([R, V, B], b)
                if i % 2 == 0 and j % 2 == 1:
                    rot = rotate([R, V, B], c)
                if i % 2 == 1 and j % 2 == 1:
                    rot = rotate([R, V, B], d)

                img.putpixel((i, j), (rot[0], rot[1], rot[2]))

    def cryptage_img(img):
        grille_2 = quadrillage(img)
        grille_crypte2 = cryptage(img_source)
        for i in range(1, len(grille_2)):
            for j in range(1, len(grille_2[0])):
                bloc_img = img.getpixel(grille_2[i][j])
                fond_crypte.putpixel(grille_crypte2[i][j], bloc_img)

    grille_2 = quadrillage(img_source)
    x_lim, y_lim = grille_2[len(grille_2) - 1][len(grille_2[0]) - 1]

    rotate_crypte(img_source, a1, b1, c1, d1)
    cryptage_img(img_source)


    test_crypte = fond_crypte.crop((0, 0, x_lim + pas, y_lim + pas))
    test_crypte.save("image_.bmp")

    num = 60

    def getANewKey():
        keyValList = []
        numo = num
        if num < 10:
            numo = 10
        for x in range(10):
            keyValList.append(chr(48 + x))
            numo = numo - 1
        if (numo > 0 and numo < 26):
            for x in range(numo):
                keyValList.append(chr(65 + x))
                numo = numo - 1
        elif numo > 0 and numo > 26:
            for x in range(26):
                keyValList.append(chr(65 + x))
                numo = numo - 1
            if numo < 26:
                for x in range(numo):
                    keyValList.append(chr(97 + x))
                    numo = numo - 1
            else:
                print("num trop grand")
                return
        key = ""
        for x in range(len(keyValList)):
            newC = random.choice(keyValList)
            keyValList.remove(newC)
            key = key + newC
        return key

    def getANumericalKey(key):
        keyValListP = []
        numo = len(key)
        for x in range(10):
            keyValListP.append(chr(48 + x))
            numo = numo - 1
        if (numo > 0 and numo < 26):
            for x in range(numo):
                keyValListP.append(chr(65 + x))
                numo = numo - 1
        elif numo > 0 and numo > 26:
            for x in range(26):
                keyValListP.append(chr(65 + x))
                numo = numo - 1
            if numo < 26:
                for x in range(numo):
                    keyValListP.append(chr(97 + x))
                    numo = numo - 1
            else:
                print("key.lengh trop grand")
                return
        keyValList = []
        for x in range(len(key)):
            keyValList.append(key[x])
        keyNumValList = []
        for x in range(len(keyValList)):
            keyNumValList.append(keyValListP.index(keyValList[x]))
        return keyNumValList

    def generateOneComplexCrypt(img, imgName, numKey):
        complexList = []
        complexList.append([])
        complexList.append([])
        complexList.append([])
        complexList.append([])
        complexList[0].append(img.size)
        complexList[0].append(imgName[:len(imgName) - 4])
        complexList[1].append(RGBrotationForward(numKey[0] % 3, getPixels(get3RGB(img))))
        complexList[2].append([])
        complexList[2].append([])
        complexList[2].append([])
        return complexList

    def encodeImgPixels(imgList, numericalKey):
        i = 0
        while len(imgList[1][i]) / len(numericalKey) > 1:
            imgList[1].append([])
            imgList[1][i], imgList[1][i + 1] = encodeAList(imgList[1][i], numericalKey)
            i = i + 1
        return imgList

    def recreateImgPixelsRGBList(complex_img):
        pixelslisto = []
        # print(complex_img[1])
        for x in range(len(complex_img[1]) - 1):
            pixelslisto.append([])
            if x == 0:
                # print(complex_img[1][-1])
                for i in range(len(complex_img[1][-1])):
                    for j in range(len(complex_img[1][-1][i])):
                        pixelslisto[x].append(complex_img[1][-1][i][j])
            else:
                for i in range(len(pixelslisto[x - 1])):
                    for j in range(len(pixelslisto[x - 1][i])):
                        pixelslisto[x].append(pixelslisto[x - 1][i][j])
                    if x == 1:
                        # print(len(pixelslisto[x-1][i]))
                        pass
            for i in range(len(complex_img[1][len(complex_img[1]) - x - 2])):
                pixelslisto[x].append(complex_img[1][len(complex_img[1]) - x - 2][i])
        # print(pixelslisto[1][len(pixelslisto[1])-2])
        # print(pixelslisto[0][0][0])
        rlist = []
        glist = []
        blist = []
        for x in range(len(pixelslisto[-1])):
            rlist.append(pixelslisto[-1][x][0])
            glist.append(pixelslisto[-1][x][1])
            if len(pixelslisto[-1][x]) != 3:
                print("huh" + str(x))
                print(pixelslisto[-1][x])
            blist.append(pixelslisto[-1][x][2])
        return rlist, glist, blist

    def createAnImage(size, name, RGB):
        imgnr = Image.new("L", size)
        imgnr.putdata(RGB[0])
        imgng = Image.new("L", size)
        imgng.putdata(RGB[1])
        imgnb = Image.new("L", size)
        imgnb.putdata(RGB[2])
        imgnew = Image.merge("RGB", (imgnr, imgng, imgnb))
        imgnew.save(name)
        return

    def RGBrotationForward(rotationP, pixels):
        newpix = []
        lastpix = []
        delindex = []
        for x in range(len(pixels) % 3):
            lastpix.append(pixels[(len(pixels) - len(pixels) % 3) + x])
            delindex.append((len(pixels) - len(pixels) % 3) + x)

        for x in range(len(delindex)):
            pixels.pop(delindex[len(delindex) - x - 1])
        if rotationP == 0:
            for x in range(int(len(pixels) / 3)):
                newpix.append(pixels[x * 3])
                newpix.append([pixels[x * 3 + 1][2], pixels[x * 3 + 1][0], pixels[x * 3 + 1][1]])
                newpix.append([pixels[x * 3 + 2][1], pixels[x * 3 + 2][2], pixels[x * 3 + 2][0]])
        elif rotationP == 1:
            for x in range(int(len(pixels) / 3)):
                newpix.append([pixels[x * 3][1], pixels[x * 3][2], pixels[x * 3][0]])
                newpix.append(pixels[x * 3 + 1])
                newpix.append([pixels[x * 3 + 2][2], pixels[x * 3 + 2][0], pixels[x * 3 + 2][1]])
        elif rotationP == 2:
            for x in range(int(len(pixels) / 3)):
                newpix.append([pixels[x * 3][2], pixels[x * 3][0], pixels[x * 3][1]])
                newpix.append([pixels[x * 3 + 1][1], pixels[x * 3 + 1][2], pixels[x * 3 + 1][0]])
                newpix.append(pixels[x * 3 + 2])
        else:
            newpix = pixels

        for x in range(len(lastpix)):
            newpix.append(lastpix[x])
        return newpix

    def getPixels(img_rgb):
        pixels = []
        for x in range(len(img_rgb[0])):
            pixels.append([img_rgb[0][x], img_rgb[1][x], img_rgb[2][x]])
        return pixels

    def get3RGB(img):
        try:
            spliter = img.split()
        except:
            print("Erreur en rapport avec l'image selectionnée")
        r = list(spliter[0].getdata())
        g = list(spliter[1].getdata())
        b = list(spliter[2].getdata())
        return r, g, b

    def encodeAList(pixelsList, numericalKey):
        lastPixelsList = []
        newPackage = []
        indexremovelist = []
        for i in range(len(pixelsList) % len(numericalKey)):
            lastPixelsList.append(pixelsList[((len(pixelsList) - (len(pixelsList) % len(numericalKey))) + i)])
            indexremovelist.append((len(pixelsList) - (len(pixelsList) % len(numericalKey))) + i)
        for i in range(len(indexremovelist)):
            pixelsList.pop(indexremovelist[len(indexremovelist) - i - 1])
        for x in range(int(len(pixelsList) / len(numericalKey))):
            newPackage.append([])
            for i in range(len(numericalKey)):
                newPackage[x].append(pixelsList[x * len(numericalKey) + numericalKey[i]])
        return lastPixelsList, newPackage

    def mainoCryptOpti(name):
        key = getANewKey()
        numKey = getANumericalKey(key)
        img = Image.open(name)
        nameList = [name]
        complexList = generateOneComplexCrypt(img, nameList[0], numKey)
        del img
        complexList = encodeImgPixels(complexList, numKey)
        complexList[2][0], complexList[2][1], complexList[2][2] = recreateImgPixelsRGBList(complexList)
        createAnImage(complexList[0][0], complexList[0][1] + "crypte.bmp",
                      (complexList[2][0], complexList[2][1], complexList[2][2]))
        del complexList
        return key

    key = mainoCryptOpti("image_.bmp")

    image_crypte = Image.open("image_crypte.bmp")

    os.remove("image_.bmp")

    arv = time.time()
    return arv - dep

def temp_crypte(l):
    t = []
    for i in range(len(l)):
        filename = "C:/Users/37rom/PycharmProjects/Application/Application android/image/" + str(i) + ".jpg"
        t.append(app_cryptage(filename))
    return t

def lissage(Ly, Lx, p):
    Lyout = []
    Lxout = Lx[p: -p]
    for index in range(p, len(Ly) - p):
        average = sum(Ly[index - p: index + p + 1]) / (2 * p + 1)
        Lyout.append(average)
    return Lxout, Lyout

def tracer():

    X, Y = w, t

    fig = plt.figure(figsize=(100, 100))

    ax = fig.add_subplot(111)

    plt.plot(X, Y, "-r", label="Courbe")

    ax.set_title('Temps moyens crypte')
    ax.set_xlabel('Tailles (en pixels)')
    ax.set_ylabel('Temps (en seconde)')

    ax.legend(loc='best')
    plt.show()

