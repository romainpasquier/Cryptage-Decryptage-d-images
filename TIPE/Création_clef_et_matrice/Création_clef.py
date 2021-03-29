from random import randint
from Création_clef_et_matrice.Création_matrice import X
from Création_clef_et_matrice.Transpositon_clef import transpo_clef
from datetime import datetime


# Clef sous forme de liste de longueur 24

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
ecrit = envoi + aa1 + aa2 + mm + jj + hh + mi + ss + cc

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