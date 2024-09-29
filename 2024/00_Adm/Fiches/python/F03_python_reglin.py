# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #

import numpy as np               # pour les tableaux et la gestion des données
import matplotlib.pyplot as plt  # pour les graphiques, l'affichage des données

# =========================================================================== #
#                            Données expérimentales                           #
# =========================================================================== #

X = np.array([0, 2, 4, 6, 8, 10])            # À modifier + écrire unité
uX = 0.1*np.ones(len(X))                     # À modifier + écrire unité
Y = np.array([0.5, 7.9, 11, 17.5, 26, 31.8]) # À modifier + écrire unité
uY = 0.1*np.ones(len(Y))                     # À modifier + écrire unité

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
xliste = np.linspace(min(X), max(X), 100)

# Fonction qui à `abscisse`, `coeff_dir`, `ord_ori` associe y
def yfunc(abscisse, coeff_dir, ord_ori):
    return coeff_dir*abscisse + ord_ori

# Liste des points y_i obtenus par régression
yliste = yfunc(xliste, a, b)

# =========================================================================== #
#                                    Tracé                                    #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('$grandeur$ en UNITÉ', fontsize=20)
plt.ylabel('$grandeur$ en UNITÉ', fontsize=20)

plt.errorbar(X, Y,
             xerr=uX, yerr=uY,
             linestyle='None', capsize=3,
             color='b', label='Mesures')
plt.plot(xliste, yliste,
         'r', label='Régression linéaire')

plt.title('Titre efficace et descriptif', fontsize=20)
plt.legend(fontsize=15)
plt.show()
