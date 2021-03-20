from PIL import Image

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
    a = a%3
    b = b%3
    for i in range(x_img):
        for j in range(y_img):
            (R, V, B) = img.getpixel((i, j))
            if i%3 == 0:
                rot = rotate([R, V, B], a)
            if i%2 == 1:
                rot = rotate([R, V, B], b)
            if j%2 == 0:
                rot = rotate([R, V, B], c)
            if j%5 == 1:
                rot = rotate([R, V, B], d)

            img.putpixel((i, j), (rot[0], rot[1], rot[2]))

def rotate_decrypte(img, a, b, c, d):
    x_img, y_img = img.size
    a = a%3
    b = b%3
    c = c%3
    d = d%3
    a = -a
    b = -b
    c = -c
    d = -d
    for i in range(x_img):
        for j in range(y_img):
            (R, V, B) = img.getpixel((i, j))
            if i%3 == 0:
                rot = rotate([R, V, B], a)
            if i%2 == 1:
                rot = rotate([R, V, B], b)
            if j%2 == 0:
                rot = rotate([R, V, B], c)
            if j%5 == 1:
                rot = rotate([R, V, B], d)

            img.putpixel((i, j), (rot[0], rot[1], rot[2]))
