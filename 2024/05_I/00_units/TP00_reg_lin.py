# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #

import numpy as np
import matplotlib.pyplot as plt
# UNE ACTIVITÉ CAPYTALE EST DISPONIBLE EN LIGNE POUR LES RENDUS DE SCRIPTS~:
# https://capytale2.ac-paris.fr/web/c/d3aa-1325055

plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})

# =========================================================================== #
#                                   Mesures                                   #
# =========================================================================== #

X = np.array([1, 2, 3, 4, 5, 6])*1e-2            # À modifier
Y = np.array([10, 15, 26, 45, 65, 100]) # À modifier

# =========================================================================== #
#                                  Régression                                 #
# =========================================================================== #

# Donne a le coefficient directeur et b l'ordonnée à l'origine
a, b = np.polyfit(X, Y, 1)
# Affiche a et b. .3f pour 3 valeurs après la virgule
print(f"a = {a:.3f}, b = {b:.2f}")

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

# Liste fine des abscisses à tracer
# découpe l'intervalle [min(X), max(X)] en 100 points
xliste = np.linspace(0, 0.07, 100)

# Fonction qui à x, a, b associe y
def yfunc(abscisse, coeff_dir, ord_ori):
    return coeff_dir*abscisse + ord_ori

# Liste des points y_i obtenus par régression
yliste = yfunc(xliste, a, b)

# =========================================================================== #
#                                    Tracé                                    #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('$I$ (mA)', fontsize=20)
plt.ylabel('$U$ (V)', fontsize=20)

plt.plot(xliste, a*xliste+b,
         'r', label='Régression linéaire')
plt.scatter(X, Y, color='b', label='Mesures')

plt.title("Accord des données à la loi d'Ohm", fontsize=20)
plt.legend(fontsize=15)
# plt.show()
plt.savefig("reglin.pdf", bbox_inches="tight")
