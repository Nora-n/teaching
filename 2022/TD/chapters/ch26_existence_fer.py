# PRECIPITATION D'HYDROXYDES SELON LE pH

import numpy as np
import matplotlib.pyplot as plt

# Saisie des valeurs des produits de solubilité
pKs1 = 15  # hydroxyde de fer II
# Concentrations des ions dans le mélange initial
CFe = 1e-2  # ions fer, en mol/L

# Création d'une liste de valeurs d'abscisses, ici pH
pH = np.linspace(0, 14, 300)

# Boucles de calcul des concentrations d'ions non précipités selon le pH
fFe = []

for x in pH:
    if CFe*10**(2*(x-14)) > 10**(-pKs1):
        fFe.append(10**(-pKs1-2*x+28)/CFe)
    else:
        fFe.append(1)

# Tracé des courbes
plt.figure(1)
plt.plot(pH, fFe, 'b-', label='Proportion de Fer')
plt.plot([7.5, 7.5], [0, 1], 'k--', lw=1)
plt.xlabel('pH')
plt.ylabel('Proportions')
plt.ylim(0, 1.01)

plt.title('Proportion des ions fer non précipités')
plt.legend()
plt.grid()
plt.show()
