# -*- coding: utf-8 -*-
from PIL import Image

rlist = []
gList = []
bList = []

l = 9
L = 9

for x in range(l*L):
    rlist.append(x)
    gList.append(0)
    bList.append(0)



imgnr = Image.new("L", (l, L))
imgnr.putdata(rlist)

imgng = Image.new("L", (l, L))
imgng.putdata(gList)

imgnb = Image.new("L", (l, L))
imgnb.putdata(bList)

imgnew = Image.merge("RGB", (imgnr, imgng, imgnb))

imgnew.save("imgTest2.bmp")