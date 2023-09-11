# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #

import numpy as np
import matplotlib.pyplot as plt
# UNE ACTIVITÉ CAPYTALE EST DISPONIBLE EN LIGNE POUR LES RENDUS DE SCRIPTS~:
# https://capytale2.ac-paris.fr/web/c/d3aa-1325055

# =========================================================================== #
#                                                                             #
#                            Données expérimentales                           #
#                                                                             #
# =========================================================================== #

# =========================================================================== #
#                                   Mesures                                   #
# =========================================================================== #

X = np.array([0, 2, 4, 6, 8, 10])            # À modifier
Y = np.array([0.5, 7.9, 11, 17.5, 26, 31.8]) # À modifier

# =========================================================================== #
#                                  Précision                                  #
# =========================================================================== #

Delta_x = 0.05 * X
Delta_y = 1

# =========================================================================== #
#                                                                             #
#                                  Régression                                 #
#                                                                             #
# =========================================================================== #

# Donne a le coefficient directeur et b l'ordonnée à l'origine
a, b = np.polyfit(X, Y, 1)
# Affiche a et b. .3f pour 3 valeurs après la virgule
print(f"a = {a:.3f}, b = {b:.2f}")

# =========================================================================== #
#                                                                             #
#                                 Monte-Carlo                                 #
#                                                                             #
# =========================================================================== #

# =========================================================================== #
#                                   Calculs                                   #
# =========================================================================== #

# Estimation de son incertitude-type par simulation Monte-Carlo :
# On réalise N tirages aléatoires des valeurs de x et de y dans
# leur intervalle (fixés par Delta_x et Delta_y)
N = 10000
# Pour chacune de ces simulations, on va trouver une valeur de a et de b ; on
# créé les listes vides qui vont nous permettre de stocker les valeurs
alist, blist = [], []
for i in range(0, N):
    # On simule l'addition d'une erreur aux valeurs mesurées
    # en ajoutant une valeur aléatoire entre les bornes de l'incertitude
    d_simu = d + Delta_d*np.random.uniform(-1, 1)
    D_simu = D + Delta_D*np.random.uniform(-1, 1)
    # On réalise une reg lin sur ce nouveau jeu de données
    p = np.polyfit(x_simu, y_simu, 1)
    # On stocke les valeurs de coefficient directeur et ordonnées à l'origine
    alist.append(p[0])
    blist.append(p[1])

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

# On calcule l'écart-type (standard deviation en anglais, d'où « std ») sur les
# valeurs de a et b simulées
u_a = np.std(alist, ddof=1)
u_b = np.std(blist, ddof=1)

# Liste fine des abscisses à tracer
# découpe l'intervalle [min(X), max(X)] en 100 points
xliste = np.linspace(min(X), max(X), 100)

# Fonction qui à x, a, b associe y
def yfunc(abscisse, coeff_dir, ord_ori):
    return coeff_dir*abscisse + ord_ori

# Liste des points y_i obtenus par régression
yliste = yfunc(xliste, a, b)

# =========================================================================== #
#                                                                             #
#                                    Tracé                                    #
#                                                                             #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('$grandeur$ en UNITÉ', fontsize=20)
plt.ylabel('$grandeur$ en UNITÉ', fontsize=20)

plt.plot(xliste, a*xliste+b,
         'r', label='Régression linéaire')
plt.errorbar(X, Y,
             xerr=Delta_x, yerr=Delta_y,
             linestyle='None', capsize=3,
             color='b', label='Mesures')

plt.title('Titre efficace et descriptif', fontsize=20)
plt.legend(fontsize=15)
plt.show()

print('Coef.directeur =', f'{a:.3e}',
      '±', f'{u_a:.3f}')
print("Ordonnée à l'origine =", f'{b:.3e}',
      '±', f'{u_b:.3f}')
