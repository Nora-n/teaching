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

x = np.array([0.01, 2.5, 5, 7.5, 10])
y = np.array([2.2, 7.7, 12.4, 17.7, 21.1])

# =========================================================================== #
#                                  Précision                                  #
# =========================================================================== #

Delta_x = 0.05*x
Delta_y = np.ones(len(y))

# =========================================================================== #
#                                                                             #
#                                  Régression                                 #
#                                                                             #
# =========================================================================== #

# Donne a le coefficient directeur et b l'ordonnée à l'origine
a, b = np.polyfit(x, y, 1)

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
    nbpts = len(x)
    # On simule l'addition d'une erreur aux valeurs mesurées
    # en ajoutant une valeur aléatoire entre les bornes de l'incertitude
    x_simu = x + Delta_x*np.random.uniform(-1, 1, nbpts)
    y_simu = y + Delta_y*np.random.uniform(-1, 1, nbpts)
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
# Les meilleures valeurs de a et b sont les moyennes de alist et blist
a = np.mean(alist)
b = np.mean(blist)

# Équation de la droite de régression (pour le tracé)


def yfunc(x, a, b):
    return a*x+b


xliste = np.linspace(min(x), max(x), 2)
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

plt.plot(xliste, yliste,
         'r', label='Régression linéaire')
plt.errorbar(x, y,
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
