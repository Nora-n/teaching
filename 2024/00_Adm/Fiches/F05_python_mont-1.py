import numpy as np

d = 12        # cm
Delta_d = 0.1 # demi-largeur de d
D = 50        # cm
Delta_D = 0.5 # demi-largeur de D

N = 10000     # nombre de régressions à effectuer

liste_f = []  # création de la liste vide pour stocker les valeurs
for i in range(N):
    # on prend des valeurs de d_simu parmi toutes les valeurs possibles
    # à l'aide d'un tirage aléatoire à l'intérieur de l'intervalle
    # [d ± Delta_d]
    d_simu = d + Delta_d * np.random.uniform(-1, 1)
    # Pareil pour D
    D_simu = D + Delta_D * np.random.uniform(-1, 1)

    # On calcule les f' simulés avec ces valeurs
    f_simu = (D_simu**2 - d_simu**2) / (4 * D_simu)

    # On les sauvegarde dans a liste correspondante
    liste_f.append(f_simu)

# La valeur moyenne est la moyenne de la liste
fmoy = np.mean(liste_f)
# L'incertitude est l'écart-type de la liste
uf = np.std(liste_f, ddof=1)
# Affichage, à modifier pour l'écriture scientifique
print(f"f' = {fmoy :.2f} +- {uf:.2f} cm")
