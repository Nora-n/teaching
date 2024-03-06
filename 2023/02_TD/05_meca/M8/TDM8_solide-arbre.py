from scipy.integrate import quad  # Module d'intégration "quad"
import numpy as np

# Intervalle d'intégration
theta_0 = 1.5 # rad
theta_f = 0   # rad

# Constantes
L = 10               # m
g = 9.81             # m.s^-2
K = np.sqrt(L/(3*g)) # s

# Fonction à intégrer
def function(theta):
    return K/(np.sqrt(np.sin(theta_0) - np.sin(theta)))

# Calcul de l'intégrale
res, err = quad(function, theta_f, theta_0)

# Affichage du résultat
print(f"Résultat de l'intégrale = {res:.2f} ± {err:.2f}")
