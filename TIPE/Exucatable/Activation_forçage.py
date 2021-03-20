import matplotlib.pyplot as plt
from Exucatable.Modification_forçage import x, z, y

# Forcçage :

fig = plt.figure(figsize=(100, 100))
ax = fig.add_subplot(111)

plt.plot(x, y, "-r", label="Force brut")
plt.plot(x, z, "-b", label="Mon code")

ax.set_title('Comparaison des temps moyens d éxécution')
ax.set_xlabel('Tailles images carrées (en pixels)')
ax.set_ylabel('Temps (en seconde)')

ax.legend(loc='best')
plt.show()

