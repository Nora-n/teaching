x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # unité
ux = 0.1 * np.ones(len(x))  # incertitude de 0.1 sur chaque valeur

y = np.array(
    [2.20, 2.00, 1.60, 1.55, 1.16, 1.00, 0.95, 0.60, 0.36, 0.36, 0.18]
)  # unité
uy = 0.12 * np.ones(len(y))  # incertitude de 0.12 sur chaque valeur

Delta_x = ux * np.sqrt(3)  # demi-largeur x
Delta_y = uy * np.sqrt(3)  # demi-largeur y

N = 10000  # nombre de régressions à effectuer

liste_a, liste_b = [], []  # création des listes vides pour stocker les valeurs
for i in range(N):
    # on prend des valeurs de x_simu parmi toutes les valeurs possibles
    # à l'aide d'un tirage aléatoire à l'intérieur de l'intervalle
    # [x ± Delta_x]
    x_simu = x + Delta_x * np.random.uniform(-1, 1)
    # Pareil pour y
    y_simu = y + Delta_y * np.random.uniform(-1, 1)

    # On fait une régression linéaire avec ces données « simulées »
    a_simu, b_simu = np.polyfit(x_simu, y_simu, 1)

    # On les sauvegarde dans les listes correspondantes
    liste_a.append(a_simu)
    liste_b.append(b_simu)

# Les valeurs moyennes sont les moyennes des listes
a_moy, b_moy = np.mean(liste_a), np.mean(liste_b)
# Les incertitudes sont l'écart-type des listes
ua, ub = np.std(liste_a, ddof=1), np.std(liste_b, ddof=1)

# Affichage, à modifier pour l'écriture scientifique
print(f"Coef.directeur = {a_moy:.3e} +- {ua:.3e}")
print(f"Ordonnée à l'origine = {b_moy:.3e} +- {ub:.3e}")
