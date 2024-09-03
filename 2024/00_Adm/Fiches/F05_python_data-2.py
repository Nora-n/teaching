import numpy as np

tab = np.array([1, 2, 3])  # créé le tableau [1, 2, 3]
tab+1                      # ajoute 1 à toutes les valeurs de tab
tab*2e-3                   # multiplie toutes les valeurs de tab par 0.002
np.sqrt(tab)               # applique racine carré à tous les éléments de tab
np.exp(tab)                # exponentielle
np.log(tab)                # logarithme NÉPÉRIEN (ln français)
np.log10(tab)              # logarithme décimal (log français)

np.linspace(min, max, nbre) # découpe [min, max] en nbre parties égales
np.mean(tab)                # donne la valeur moyenne de tab
np.std(tab, ddof=1)         # donne l'écart-type de tab

np.polyfit(X, Y, 1)         # donne les coefficients a et b de Y = a*X+b
