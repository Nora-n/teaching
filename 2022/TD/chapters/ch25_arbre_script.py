from scipy.integrate import quad  # Module d'intégration "quad"
import numpy as np

# Intervalle d'intégration
theta_0 = 1.5
theta_f = 0

# Constantes
L = 10
g = 9.81
K = np.sqrt(L/(3*g))

# Fonction à intégrer


def function(theta):
    return K/(np.sqrt(np.sin(theta_0) - np.sin(theta)))


# Calcul de l'intégrale
res, err = quad(function, theta_f, theta_0)

# Affichage du résultat
# Module d'intégration "quad"
print(f"Résultat de l'intégrale = {res:.2f} ± {err:.2f}")
