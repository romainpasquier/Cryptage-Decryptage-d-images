# -*- coding: utf-8 -*-
from PIL import Image
import os
import random

num = 60


def mainocrypt(path):
    
    os.chdir(path)
    
    img_list_names = getEveryImgName()
    print("Folder " + path + " scanned")
    img_list_names, img_list = openImgList(img_list_names)
    print("Images opened")
    img_size_list = getSizeList(img_list)
    print("Size list extracted")
    img_rgb_list = get3RGBLists(img_list)
    print("img_rgb_list generated")
    del img_list
    img_pixels_list = getPixelsList(img_rgb_list)
    print("img_pixels_list generated")
    #img_fpackage_list = generateFirstPackageList(img_pixels_list)
    #print("img_fpackage_list generated")
    key = getANewKey()
    numKey = getANumericalKey(key)
    print("Key generated")
    complex_img_list = generateComplex(img_pixels_list, img_size_list, img_list_names)
    print("Complex step 1")
    del img_pixels_list
    complex_img_list = rotateForwardRGBComplex(complex_img_list, numKey)
    print("Pixels RGB rotated")
    complex_img_list = encodeComplexList(complex_img_list, numKey)
    print("Complex step 2")
    complex_img_list = recreateImgListPixelsRGBList(complex_img_list)
    print("Images crypted")
    #print("len : " + str(complex_img_list[0][0][0][0]*complex_img_list[0][0][0][1]))
    
    createCryptedFolder("Crypted_Images")
    print("Crypted images folder created")
    
    
    createNewImagesFromComplex(complex_img_list)
    
    print("Crypted Images generated")
    
    print("KEY : " + key)
    return key
    
    
    
    
    
    
    
    """
    for x in range(len(complex_img_list)):
        tot = 0
        for i in range(len(complex_img_list[x][1])):
            v = len(complex_img_list[x][1][i])*16**i
            print(len(complex_img_list[x][1][i])*16**i)
            tot = tot + v
        print(tot)
        print("len : " + str(complex_img_list[x][0][0][0]*complex_img_list[x][0][0][1]))
    """

def getEveryImgName():
    files_names_list = os.listdir()
    final_files_names_list = []
    for x in range(len(files_names_list)):
        if (files_names_list[x][len(files_names_list[x])-4:] == ".png") or (files_names_list[x][len(files_names_list[x])-4:] == ".jpg") or (files_names_list[x][len(files_names_list[x])-4:] == ".bmp") or (files_names_list[x][len(files_names_list[x])-4:] == ".PNG") or (files_names_list[x][len(files_names_list[x])-4:] == ".JPG") or (files_names_list[x][len(files_names_list[x])-4:] == ".BMP"):
            final_files_names_list.append(files_names_list[x])
    return final_files_names_list



def openImgList(img_names_list):
    img_list = []
    for x in range(len(img_names_list)):
        try:    
            img_list.append(Image.open(img_names_list[x]))
        except:
            print("Erreur lors de l'ouverture de : \"" + img_names_list[x] + "\"")
            img_names_list.remove(img_names_list[x])
    
    return img_names_list, img_list


def getSizeList(img_list):
    img_size_list = []
    for x in range(len(img_list)):
        img_size_list.append(img_list[x].size)
    return img_size_list






def get3RGBLists(img_list):
    img_rgb_list = []
    for x in range(len(img_list)):
        img_rgb_list.append(get3RGB(img_list[x]))
    return img_rgb_list
    
    
    

def get3RGB(img):
    try:
        spliter = img.split()
    except:
        print("Erreur en rapport avec l'image selectionnée")
    r = list(spliter[0].getdata())
    g = list(spliter[1].getdata())
    b = list(spliter[2].getdata())
    return r, g, b

def getPixelsList(img_rgb_list):
    img_pixels_list = []
    for x in range(len(img_rgb_list)):
        img_pixels_list.append(getPixels(img_rgb_list[x]))
    return img_pixels_list

def getPixels(img_rgb):
    pixels = []
    for x in range(len(img_rgb[0])):
        pixels.append([img_rgb[0][x], img_rgb[1][x], img_rgb[2][x]])
    return pixels
    

def generateFirstPackageList(img_pixels_list):
    img_fpackage_list = []
    for x in range(len(img_pixels_list)):
        img_fpackage_list.append(generateFirstPackage(img_pixels_list[x]))
    return img_fpackage_list


def generateFirstPackage(pixels):
    fpackage = []
    if len(pixels)/num < 1:
        fpackage.append([pixels[a] for a in range(len(pixels))])
        return fpackage
    for x in range(int((len(pixels)-len(pixels)%num)/num)):
        fpackage.append([])
        for i in range(x*num, (x+1)*num):
            fpackage[x].append(pixels[i])
    return fpackage

def getANewKey():
    keyValList = []
    numo = num
    if num < 10 : 
        numo = 10
    for x in range(10):
        keyValList.append(chr(48+x))
        numo = numo-1
    if (numo > 0 and numo < 26):
        for x in range(numo):
            keyValList.append(chr(65+x))
            numo = numo-1
    elif numo > 0 and numo > 26:
        for x in range(26):
            keyValList.append(chr(65+x))
            numo = numo-1
        if numo < 26:
            for x in range(numo):
                keyValList.append(chr(97+x))
                numo = numo-1
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
        keyValListP.append(chr(48+x))
        numo = numo-1
    if (numo > 0 and numo < 26):
        for x in range(numo):
            keyValListP.append(chr(65+x))
            numo = numo-1
    elif numo > 0 and numo > 26:
        for x in range(26):
            keyValListP.append(chr(65+x))
            numo = numo-1
        if numo < 26:
            for x in range(numo):
                keyValListP.append(chr(97+x))
                numo = numo-1
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



def generateComplex(img_pixels_list, img_list, img_list_names):
    if len(img_list) != len(img_pixels_list):
        return
    complexList = []
    for x in range(len(img_pixels_list)):
        complexList.append([])
        complexList[x].append([])
        complexList[x].append([])
        complexList[x].append([])
        complexList[x][0].append(img_list[x])
        complexList[x][0].append(img_list_names[x][:len(img_list_names[x])-4])
        
        complexList[x][1].append(img_pixels_list[x])
        
        complexList[x][2].append([])
        complexList[x][2].append([])
        complexList[x][2].append([])
        
    return complexList


def encodeAList(pixelsList, numericalKey):
    
    lastPixelsList = []
    newPackage = []
    indexremovelist = []
    for i in range(len(pixelsList)%len(numericalKey)):
        lastPixelsList.append(pixelsList[((len(pixelsList)-(len(pixelsList)%len(numericalKey)))+i)])
        indexremovelist.append((len(pixelsList)-(len(pixelsList)%len(numericalKey)))+i)
    for i in range(len(indexremovelist)):
        pixelsList.pop(indexremovelist[len(indexremovelist)-i-1])
    
    for x in range(int(len(pixelsList)/len(numericalKey))):
        newPackage.append([])
        for i in range(len(numericalKey)):    
            newPackage[x].append(pixelsList[x*len(numericalKey)+numericalKey[i]])
    return lastPixelsList, newPackage


def encodeComplexList(complexList, numericalKey):
    for x in range(len(complexList)):
        complexList[x] = encodeImgPixels(complexList[x], numericalKey)
    return complexList

def encodeImgPixels(imgList, numericalKey):
    
    i=0
    
    while len(imgList[1][i])/len(numericalKey) > 1:
        imgList[1].append([])
        imgList[1][i], imgList[1][i+1] = encodeAList(imgList[1][i], numericalKey)
        i = i+1
    
    return imgList


def recreateImgPixelsRGBList(complex_img):
    pixelslisto = []
    
    #print(complex_img[1])
    
    for x in range(len(complex_img[1])-1):
        pixelslisto.append([])
        if x == 0:
            #print(complex_img[1][-1])
            for i in range(len(complex_img[1][-1])):
                for j in range(len(complex_img[1][-1][i])):    
                    pixelslisto[x].append(complex_img[1][-1][i][j])
        else:
            for i in range(len(pixelslisto[x-1])):
                for j in range(len(pixelslisto[x-1][i])):    
                    pixelslisto[x].append(pixelslisto[x-1][i][j])
                if x == 1:
                    #print(len(pixelslisto[x-1][i]))
                    pass
        for i in range(len(complex_img[1][len(complex_img[1])-x-2])):
            pixelslisto[x].append(complex_img[1][len(complex_img[1])-x-2][i])
    #print(pixelslisto[1][len(pixelslisto[1])-2])
    #print(pixelslisto[0][0][0])
    
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
    
    
    
def recreateImgListPixelsRGBList(complex_img_list):
    for x in range(len(complex_img_list)):
        complex_img_list[x][2][0], complex_img_list[x][2][1], complex_img_list[x][2][2] = recreateImgPixelsRGBList(complex_img_list[x])
    return complex_img_list

def createCryptedFolder(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    
    os.chdir(folderName)

def createNewImagesFromComplex(complex_img_list):
    for x in range(len(complex_img_list)):
        createAnImage(complex_img_list[x][0][0], complex_img_list[x][0][1] + ".bmp", (complex_img_list[x][2][0], complex_img_list[x][2][1], complex_img_list[x][2][2]))


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








def mainodecrypt(path, key):
    os.chdir(path)
    img_list_names = getEveryImgName()
    print("Folder " + path + " scanned")
    img_list_names, img_list = openImgList(img_list_names)
    print("Images opened")
    img_rgb_list = get3RGBLists(img_list)
    print("img_rgb_list generated")
    img_pixels_list = getPixelsList(img_rgb_list)
    print("img_pixels_list generated")
    numKey = getANumericalKey(key)
    complex_img_list = generateComplex(img_pixels_list, img_list, img_list_names)
    print("Complex step 1")
    complex_img_list = decodeComplexList(complex_img_list, numKey)
    print("Complex step 2")
    complex_img_list = rotateBackwardRGBComplex(complex_img_list, numKey)
    print("Pixels RGB rotated")
    complex_img_list = getRGBtranlastionOnComplex(complex_img_list)
    print("Complex step 3")


    createCryptedFolder("Uncrypted Images")
    createNewImagesFromComplex(complex_img_list)















def decodeComplexList(complexList, numericalKey):
    for x in range(len(complexList)):
        complexList[x] = decodeImgPixels(complexList[x], numericalKey)
    return complexList



def decodeImgPixels(imgList, numericalKey):
    
    i=0
    
    while len(imgList[1][i])/len(numericalKey) > 1:
        imgList[1].append([])
        imgList[1][i], imgList[1][i+1] = packAList(imgList[1][i], numericalKey)
        i = i+1
    pixels = decodePackages(imgList[1], numericalKey)
    imgList[1].append(pixels)
    return imgList



def packAList(pixelsList, numericalKey):
    
    lastPixelsList = []
    newPackage = []
    indexremovelist = []
    for i in range(len(pixelsList)%len(numericalKey)):
        lastPixelsList.append(pixelsList[((len(pixelsList)-(len(pixelsList)%len(numericalKey)))+i)])
        indexremovelist.append((len(pixelsList)-(len(pixelsList)%len(numericalKey)))+i)
    for i in range(len(indexremovelist)):
        pixelsList.pop(indexremovelist[len(indexremovelist)-i-1])
    
    for x in range(int(len(pixelsList)/len(numericalKey))):
        newPackage.append([])
    
    for x in range(int(len(pixelsList)/len(numericalKey))):
        for i in range(len(numericalKey)):
            newPackage[x].append(pixelsList[x*len(numericalKey)+i])
    
    
    
    
    """
    for x in range(int(len(pixelsList)/len(numericalKey))):
        for j in range(len(pixelsList[x])):
            newPackage.append([])
        
        
        for i in range(len(pixelsList[x])):
            print(len(pixelsList))
            
            newPackage[x][i] = [(pixelsList[x][x*len(numericalKey)+i])]
    """
    return lastPixelsList, newPackage



def decodePackages(packagesList, numericalKey):
    
    pixelslisto = []
    for x in range(len(packagesList)-1):
        pixelslisto.append([])
        if x == 0:
            for i in range(len(packagesList[-1])):
                for j in range(len(packagesList[-1][i])):
                    pixelslisto[x].append([])
                for j in range(len(packagesList[-1][i])):
                    pixelslisto[x][i*len(packagesList[-1][i])+numericalKey[j]] = packagesList[-1][i][j]
        else:
            for i in range(len(pixelslisto[x-1])):
                for j in range(len(pixelslisto[x-1][i])):
                    pixelslisto[x].append([])
                    
                    
                    
                for j in range(len(pixelslisto[x-1][i])):
                    pixelslisto[x][i*len(pixelslisto[x-1][i])+numericalKey[j]] = pixelslisto[x-1][i][j]      #[len(packagesList)-x-1][i][numericalKey[j]]
                    
                    
                    
                    
        for i in range(len(packagesList[len(packagesList)-x-2])):
            pixelslisto[x].append(packagesList[len(packagesList)-x-2][i])
    
    return pixelslisto[-1]



def getRGBtranlastionOnComplex(complexList):
    for x in range(len(complexList)):
        complexList[x][2][0], complexList[x][2][1], complexList[x][2][2] = getRGBListsFromPixels(complexList[x][1][-1])
    return complexList


def getRGBListsFromPixels(pixels):
    
    rlist = []
    glist = []
    blist = []
    
    for x in range(len(pixels)):
        rlist.append(pixels[x][0])
        glist.append(pixels[x][1])
        blist.append(pixels[x][2])
    
    return rlist, glist, blist


def rotateForwardRGBComplex(complexList, numericalKey):
    for x in range(len(complexList)):
        complexList[x][1][0] = RGBrotationForward(numericalKey[0]%3, complexList[x][1][0])
    return complexList
    

def RGBrotationForward(rotationP, pixels):
    newpix = []
    lastpix = []
    delindex = []
    for x in range(len(pixels)%3):
        lastpix.append(pixels[(len(pixels)-len(pixels)%3)+x])
        delindex.append((len(pixels)-len(pixels)%3)+x)
    
    for x in range(len(delindex)):
        pixels.pop(delindex[len(delindex)-x-1])
    if rotationP == 0:
        for x in range(int(len(pixels)/3)):
            newpix.append(pixels[x*3])
            newpix.append([pixels[x*3+1][2], pixels[x*3+1][0], pixels[x*3+1][1]])
            newpix.append([pixels[x*3+2][1], pixels[x*3+2][2], pixels[x*3+2][0]])
    elif rotationP == 1:
        for x in range(int(len(pixels)/3)):
            newpix.append([pixels[x*3][1], pixels[x*3][2], pixels[x*3][0]])
            newpix.append(pixels[x*3+1])
            newpix.append([pixels[x*3+2][2], pixels[x*3+2][0], pixels[x*3+2][1]])
    elif rotationP == 2:
        for x in range(int(len(pixels)/3)):
            newpix.append([pixels[x*3][2], pixels[x*3][0], pixels[x*3][1]])
            newpix.append([pixels[x*3+1][1], pixels[x*3+1][2], pixels[x*3+1][0]])
            newpix.append(pixels[x*3+2])
    else:
        newpix = pixels

    for x in range(len(lastpix)):
        newpix.append(lastpix[x])
    return newpix


def rotateBackwardRGBComplex(complexList, numericalKey):
    for x in range(len(complexList)):
        complexList[x][1][-1] = RGBrotationBackward(numericalKey[0]%3, complexList[x][1][-1])
    return complexList


def RGBrotationBackward(rotationP, pixels):
    newpix = []
    lastpix = []
    delindex = []
    for x in range(len(pixels)%3):
        lastpix.append(pixels[(len(pixels)-len(pixels)%3)+x])
        delindex.append((len(pixels)-len(pixels)%3)+x)
    
    for x in range(len(delindex)):
        pixels.pop(delindex[len(delindex)-x-1])
    if rotationP == 0:
        for x in range(int(len(pixels)/3)):
            newpix.append(pixels[x*3])
            newpix.append([pixels[x*3+1][1], pixels[x*3+1][2], pixels[x*3+1][0]])
            newpix.append([pixels[x*3+2][2], pixels[x*3+2][0], pixels[x*3+2][1]])
    elif rotationP == 1:
        for x in range(int(len(pixels)/3)):
            newpix.append([pixels[x*3][2], pixels[x*3][0], pixels[x*3][1]])
            newpix.append(pixels[x*3+1])
            newpix.append([pixels[x*3+2][1], pixels[x*3+2][2], pixels[x*3+2][0]])
    elif rotationP == 2:
        for x in range(int(len(pixels)/3)):
            newpix.append([pixels[x*3][1], pixels[x*3][2], pixels[x*3][0]])
            newpix.append([pixels[x*3+1][2], pixels[x*3+1][0], pixels[x*3+1][1]])
            newpix.append(pixels[x*3+2])
    else:
        newpix = pixels

    for x in range(len(lastpix)):
        newpix.append(lastpix[x])
    return newpix

def mainoCryptOpti(path):
    
    os.chdir(path)
    nameList = getEveryImgName()
    key = getANewKey()
    numKey = getANumericalKey(key)
    imgNumber = len(nameList)
    for x in range(len(nameList)):
        
        img = imgOpen(nameList[x])
        if img == False:
            continue
        complexList = generateOneComplexCrypt(img, nameList[x], numKey)
        del img
        complexList = encodeImgPixels(complexList, numKey)
        complexList[2][0], complexList[2][1], complexList[2][2] = recreateImgPixelsRGBList(complexList)
        if x == 0:
            createCryptedFolder("Crypted_Images")
        else:
            os.chdir("Crypted_Images")
        createAnImage(complexList[0][0], complexList[0][1] + ".bmp", (complexList[2][0], complexList[2][1], complexList[2][2]))
        del complexList
        os.chdir("..")
        print(str(round((x+1)*100/imgNumber)) + "% du cryptage effectué.")
    print("KEY : " + key)
    return key



def mainoDecryptOpti(path, key):
    
    os.chdir(path)
    nameList = getEveryImgName()
    numKey = getANumericalKey(key)
    imgNumber = len(nameList)
    
    for x in range(len(nameList)):
                    
        img = imgOpen(nameList[x])
        if img == False:
            continue
        complexList = generateOneComplexDecrypt(img, nameList[x], numKey)
        del img
        complexList = decodeImgPixels(complexList, numKey)
        complexList[1][-1] = RGBrotationBackward(numKey[0]%3, complexList[1][-1])
        complexList[2][0], complexList[2][1], complexList[2][2] = recreateImgPixelsOnlyRGB(complexList)
        if x == 0:
            createCryptedFolder("Uncrypted_Images")
        else:
            os.chdir("Uncrypted_Images")
        createAnImage(complexList[0][0], complexList[0][1] + ".bmp", (complexList[2][0], complexList[2][1], complexList[2][2]))
        del complexList
        os.chdir("..")
        print(str(round((x+1)*100/imgNumber)) + "% du decryptage effectué.")
    
    
    
    
def imgOpen(imgName):
    try:
        img = Image.open(imgName)
    except:
        print("Erreur lors de l'ouverture de : \"" + imgName + "\"")
        img = False
    return img


def generateOneComplexCrypt(img, imgName, numKey):
    complexList = []
    
    complexList.append([])
    complexList.append([])
    complexList.append([])
    complexList.append([])
    complexList[0].append(img.size)
    complexList[0].append(imgName[:len(imgName)-4])
    
    complexList[1].append(RGBrotationForward(numKey[0]%3, getPixels(get3RGB(img))))
    
    complexList[2].append([])
    complexList[2].append([])
    complexList[2].append([])
        
    return complexList


def generateOneComplexDecrypt(img, imgName, numKey):
    complexList = []
    
    complexList.append([])
    complexList.append([])
    complexList.append([])
    complexList.append([])
    complexList[0].append(img.size)
    complexList[0].append(imgName[:len(imgName)-4])
    
    complexList[1].append(getPixels(get3RGB(img)))
    
    complexList[2].append([])
    complexList[2].append([])
    complexList[2].append([])
        
    return complexList

def recreateImgPixelsOnlyRGB(complex_img_list):
    rlist = []
    glist = []
    blist = []
    for x in range(len(complex_img_list[1][-1])):
        rlist.append(complex_img_list[1][-1][x][0])
        glist.append(complex_img_list[1][-1][x][1])
        blist.append(complex_img_list[1][-1][x][2])
    
    return rlist, glist, blist

key = mainoCryptOpti("cryptimg")
mainoDecryptOpti("Crypted_Images", key)
