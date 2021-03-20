from tkinter import *
import tkinter
from tkinter import filedialog
from PIL import Image
from math import sqrt
from random import randint
from datetime import datetime
import random
import os
import time

fenetre = Tk()
fenetre.title("Cryptage/Decryptage")
fenetre.geometry("281x0")

def app_cryptage():
    app = tkinter.Toplevel(fenetre)
    app.geometry("300x120")
    app.title("Cryptage")

    def GetFiles():
        filename = filedialog.askopenfilename(title="Select File", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

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

        envoi = str(randint(100000000000000, 9999999999999999))
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

        img_source.show()

        dep1 = time.time()
        rotate_crypte(img_source, a1, b1, c1, d1)
        cryptage_img(img_source)
        arv1 = time.time()

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

        dep2 = time.time()
        key = mainoCryptOpti("image_.bmp")
        arv2 = time.time()

        image_crypte = Image.open("image_crypte.bmp")
        image_crypte.show()

        os.remove("image_.bmp")

        lblclef = Label(app, text="Clef : ")
        lblclef.pack()

        data_string = StringVar()
        data_string.set(ecrit + str(key))
        ent1 = Entry(app, textvariable=data_string, fg="black", bg="white", bd=0, state="readonly")
        ent1.pack()

        def copie1():
            # fonction copier
            app.clipboard_clear()
            app.clipboard_append(ent1.get())

        bouton1 = Button(app, text="Copier_clef", command=copie1)
        bouton1.pack()

        lbltemps = Label(app, text="Cryptage terminé en : " + str(int(arv1-dep1 + arv2-dep2)) +" secondes")
        lbltemps.pack()

    bouton_getfiles = Button(app, text="Choisir une image jpeg", command=GetFiles)
    bouton_getfiles.pack()

def app_decryptage():
    app = tkinter.Toplevel(fenetre)
    app.title("Decryptage")
    app.geometry("300x120")
    def GetFiles():
        filename = filedialog.askopenfilename(title="Select File", filetypes=(("bmp files", ".bmp"), ("all files", "*.*")))
        img_source = Image.open(filename)
        img_source.show()
        x_img, y_img = img_source.size
        fond_decrypte = Image.new('RGB', (x_img, y_img), (255, 255, 0))

        pas = 1
        ecrit = clef1.get()

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

        clef = [int(ecrit[0:1]), int(ecrit[1:2]), int(ecrit[2:3]), int(ecrit[3:4]), int(ecrit[4:5]), int(ecrit[5:6]), int(ecrit[6:7]), int(ecrit[7:8]), int(ecrit[8:9]), int(ecrit[9:10]), int(ecrit[10:11]), int(ecrit[11:12]), int(ecrit[12:13]), int(ecrit[13:14]), int(ecrit[14:15]), int(ecrit[15:16]), int(ecrit[16:18]), int(ecrit[18:20]), int(ecrit[20:22]), int(ecrit[22:24]), int(ecrit[24:26]),int(ecrit[26:28]), int(ecrit[28:30]), int(ecrit[30:32])]

        key = ecrit[32::]

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

        def generateOneComplexDecrypt(img, imgName, numKey):
            complexList = []
            complexList.append([])
            complexList.append([])
            complexList.append([])
            complexList.append([])
            complexList[0].append(img.size)
            complexList[0].append(imgName[:len(imgName) - 4])
            complexList[1].append(getPixels(get3RGB(img)))
            complexList[2].append([])
            complexList[2].append([])
            complexList[2].append([])
            return complexList

        def decodeImgPixels(imgList, numericalKey):
            i = 0
            while len(imgList[1][i]) / len(numericalKey) > 1:
                imgList[1].append([])
                imgList[1][i], imgList[1][i + 1] = packAList(imgList[1][i], numericalKey)
                i = i + 1
            pixels = decodePackages(imgList[1], numericalKey)
            imgList[1].append(pixels)
            return imgList

        def RGBrotationBackward(rotationP, pixels):
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
                    newpix.append([pixels[x * 3 + 1][1], pixels[x * 3 + 1][2], pixels[x * 3 + 1][0]])
                    newpix.append([pixels[x * 3 + 2][2], pixels[x * 3 + 2][0], pixels[x * 3 + 2][1]])
            elif rotationP == 1:
                for x in range(int(len(pixels) / 3)):
                    newpix.append([pixels[x * 3][2], pixels[x * 3][0], pixels[x * 3][1]])
                    newpix.append(pixels[x * 3 + 1])
                    newpix.append([pixels[x * 3 + 2][1], pixels[x * 3 + 2][2], pixels[x * 3 + 2][0]])
            elif rotationP == 2:
                for x in range(int(len(pixels) / 3)):
                    newpix.append([pixels[x * 3][1], pixels[x * 3][2], pixels[x * 3][0]])
                    newpix.append([pixels[x * 3 + 1][2], pixels[x * 3 + 1][0], pixels[x * 3 + 1][1]])
                    newpix.append(pixels[x * 3 + 2])
            else:
                newpix = pixels

            for x in range(len(lastpix)):
                newpix.append(lastpix[x])
            return newpix

        def recreateImgPixelsOnlyRGB(complex_img_list):
            rlist = []
            glist = []
            blist = []
            for x in range(len(complex_img_list[1][-1])):
                rlist.append(complex_img_list[1][-1][x][0])
                glist.append(complex_img_list[1][-1][x][1])
                blist.append(complex_img_list[1][-1][x][2])
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

        def packAList(pixelsList, numericalKey):
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

            for x in range(int(len(pixelsList) / len(numericalKey))):
                for i in range(len(numericalKey)):
                    newPackage[x].append(pixelsList[x * len(numericalKey) + i])
            return lastPixelsList, newPackage

        def decodePackages(packagesList, numericalKey):
            pixelslisto = []
            for x in range(len(packagesList) - 1):
                pixelslisto.append([])
                if x == 0:
                    for i in range(len(packagesList[-1])):
                        for j in range(len(packagesList[-1][i])):
                            pixelslisto[x].append([])
                        for j in range(len(packagesList[-1][i])):
                            pixelslisto[x][i * len(packagesList[-1][i]) + numericalKey[j]] = packagesList[-1][i][j]
                else:
                    for i in range(len(pixelslisto[x - 1])):
                        for j in range(len(pixelslisto[x - 1][i])):
                            pixelslisto[x].append([])

                        for j in range(len(pixelslisto[x - 1][i])):
                            pixelslisto[x][i * len(pixelslisto[x - 1][i]) + numericalKey[j]] = pixelslisto[x - 1][i][
                                j]  # [len(packagesList)-x-1][i][numericalKey[j]]

                for i in range(len(packagesList[len(packagesList) - x - 2])):
                    pixelslisto[x].append(packagesList[len(packagesList) - x - 2][i])
            return pixelslisto[-1]

        def mainoDecryptOpti(key, name):
            numKey = getANumericalKey(key)
            img = Image.open(name)
            nameList = [name]
            complexList = generateOneComplexDecrypt(img, nameList[0], numKey)
            del img
            complexList = decodeImgPixels(complexList, numKey)
            complexList[1][-1] = RGBrotationBackward(numKey[0] % 3, complexList[1][-1])
            complexList[2][0], complexList[2][1], complexList[2][2] = recreateImgPixelsOnlyRGB(complexList)
            createAnImage(complexList[0][0], complexList[0][1] + "2.bmp",
                          (complexList[2][0], complexList[2][1], complexList[2][2]))
            del complexList

        dep1 = time.time()
        mainoDecryptOpti(key, filename)
        arv1 = time.time()

        img_source1 = Image.open(filename.replace(".bmp", "") + "2.bmp")

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

        def rotate_decrypte(img, a, b, c, d):
            x_img, y_img = img.size
            a = a % 3
            b = b % 3
            c = c % 3
            d = d % 3
            a = -a
            b = -b
            c = -c
            d = -d
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

        def cryptage(img):
            x_img, y_img = img.size
            taille_x = dimensions(y_img // pas) + 1
            taille_y = dimensions(x_img // pas) + 1
            grille_2 = quadrillage(img)
            grille_crypte2 = zeros(taille_x, taille_y)
            for i in range(1, len(grille_2)):
                for j in range(1, len(grille_2[0])):
                    x = (a * i + b) % (len(
                        grille_2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
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

        grille_2 = quadrillage(img_source)
        x_lim, y_lim = grille_2[len(grille_2) - 1][len(grille_2[0]) - 1]

        def decryptage(img):
            x_img, y_img = img.size
            taille_x = dimensions(y_img // pas) + 1
            taille_y = dimensions(x_img // pas) + 1
            grille_crypte2 = cryptage(img)
            grille_decrypte2 = zeros(taille_x, taille_y)
            for i in range(1, len(grille_crypte2)):
                for j in range(1, len(grille_crypte2[0])):
                    x = (a * i + b) % (len(
                        grille_crypte2) - 1)  # car sinon ce n'est plus un nombre premier (dut à la boucle qui ne va que jusqu'a n-1)
                    y = (c * j + d) % (len(grille_crypte2[0]) - 1)  # idem
                    grille_decrypte2[i][j] = grille_crypte2[x + 1][y + 1]
            return grille_decrypte2

        def decryptage_img(img):
            grille_crypte2 = cryptage(img)
            grille_decrypte2 = decryptage(img)
            for i in range(1, len(grille_crypte2)):
                for j in range(1, len(grille_crypte2[0])):
                    bloc_img = img.getpixel(grille_crypte2[i][j])
                    fond_decrypte.putpixel(grille_decrypte2[i][j], bloc_img)

        dep2 = time.time()
        decryptage_img(img_source1)
        rotate_decrypte(fond_decrypte, a1, b1, c1, d1)
        arv2 = time.time()

        test_decrypte = fond_decrypte.crop((0, 0, x_lim + pas, y_lim + pas))
        test_decrypte.save("image_decrypte.jpg")
        image_decrypte = Image.open("image_decrypte.jpg")

        image_decrypte.show()

        os.remove("image_crypte2.bmp")

        lbltemps = Label(app, text="Decryptage terminé en : " + str(int(arv1-dep1 + arv2-dep2)) +" secondes")
        lbltemps.pack()

    lblclef = Label(app, text="Saisir clef :")
    clef1 = Entry(app)
    lblclef.pack()
    clef1.pack()

    bouton_getfiles = Button(app, text="Choisir une image bmp", command=GetFiles)
    bouton_getfiles.pack()

mainmenu = tkinter.Menu(fenetre)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Cryptage", command=app_cryptage)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Decrytage", command=app_decryptage)

mainmenu.add_cascade(label="Cryptage", menu = first_menu)
mainmenu.add_cascade(label="Decryptage", menu = second_menu)

fenetre.config(menu=mainmenu)
fenetre.mainloop()
