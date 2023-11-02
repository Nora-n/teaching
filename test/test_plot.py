import numpy as np
import matplotlib.pyplot as plt

abscisse = np.linspace(0, 10, 8) # définit les abscisses qu'on tracera
ordonnee = abscisse**2           # et les ordonnées

plt.plot(abscisse, ordonnee)     # place les points, les relie par des segments
plt.xlabel('t (s)')              # nomme l'abscisse
plt.ylabel('x (m)')              # nomme l'ordonnée

# plt.show()                       # obligé pour afficher
plt.savefig("python_plt-1.pdf", bbox_inches="tight")
