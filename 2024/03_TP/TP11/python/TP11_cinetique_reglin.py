# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #

import numpy as np               # pour les tableaux et la gestion des données
import matplotlib.pyplot as plt  # pour les graphiques, l'affichage des données

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "EB Garamond",
        "axes.labelsize": "x-large",
        "xtick.labelsize": "x-large",
        "ytick.labelsize": "x-large",
    }
)
plt.rcParams["figure.facecolor"] = "w"
plt.rc('text.latex', preamble=r'\usepackage[detect-all,locale=FR,separate-uncertainty]{siunitx}[=v2]')

# =========================================================================== #
#                            Données expérimentales                           #
# =========================================================================== #

sigma_0: float = 9.83  # mS.cm^-1
sigma_inf: float = 3.64  # mS.cm^-1
t_tab: np.ndarray = np.array([30 * k for k in range(1, 41)])  # s
# incertitude sur le temps : une demi-seconde de demi-intervalle
ut_tab: np.ndarray = np.ones(len(t_tab))*0.5/np.sqrt(3) # s
sigma_tab: np.ndarray = np.array(  # ms.cm^-1
    [
        9.33,
        8.70,
        8.18,
        7.75,
        7.40,  # 5
        7.11,
        6.85,
        6.64,
        6.45,
        6.30,  # 10
        6.14,
        6.01,
        5.89,
        5.79,
        5.69,  # 15
        5.61,
        5.53,
        5.45,
        5.39,
        5.32,  # 20
        5.27,
        5.21,
        5.17,
        5.11,
        5.07,  # 25
        5.03,
        4.99,
        4.95,
        4.92,
        4.88,  # 30
        4.85,
        4.82,
        4.80,
        4.77,
        4.74,  # 35
        4.72,
        4.70,
        4.68,
        4.65,
        4.64,  # 40
    ]
)
# incertitude sur la conductivité : 0.02 de demi-intervalle
usigma_tab: np.ndarray = np.ones(len(sigma_tab))*0.02/np.sqrt(3) # mS.cm^-1

# =========================================================================== #
#                                Données brutes                               #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.xlabel("$t$ en secondes", fontsize=20)
plt.ylabel("$\\sigma$ en ms.cm$^{-1}$", fontsize=20)

plt.errorbar(t_tab, sigma_tab,
             xerr=ut_tab, yerr=usigma_tab,
             linestyle='None', capsize=3,
             color='orange', label='Mesures')
# plt.scatter(t_tab, sigma_tab, marker="+", s=100, label="Données")

plt.title("Évolution de la conductivité", fontsize=20)
plt.legend(fontsize=15)
plt.savefig("../figures/TP11_cinetique_sigma_brut.pdf", bbox_inches="tight")

# =========================================================================== #
#                                  Régression                                 #
# =========================================================================== #

# incertitude sur la grandeur avec Monte-Carlo
N = 10000 # nombre de simulations
a_list = [] # pour stocker les coefficients directeurs
b_list = [] # pour stocker les ordonnées à l'origine
sigma_reglin_list = [] # pour stocker les valeurs de sigma_reglin simulés

Delta_t = ut_tab*np.sqrt(3) # demi-intervalle des valeurs possibles
Delta_s = usigma_tab*np.sqrt(3) # même demi-intervalle pour tous les sigma

for i in range(N):
    t_tab_simu = t_tab + Delta_t*np.random.uniform(-1,1)
    X_simu = t_tab_simu

    sigma_0_simu = sigma_0 + Delta_s*np.random.uniform(-1,1)
    sigma_inf_simu = sigma_inf + Delta_s*np.random.uniform(-1,1)
    sigma_tab_simu = sigma_tab + Delta_s*np.random.uniform(-1,1)

    sigma_reglin_simu = \
    (sigma_0_simu - sigma_inf_simu) / (sigma_tab_simu - sigma_inf_simu)
    Y_simu = sigma_reglin_simu

    sigma_reglin_list.append(sigma_reglin_simu)

    a_simu, b_simu = np.polyfit(X_simu, Y_simu, 1)
    a_list.append(a_simu)
    b_list.append(b_simu)

# exploitation des données :
# meilleure sigma_reglin = moyenne
sigma_reglin_moy = np.mean(sigma_reglin_list, axis=0)
# incertitude sur chaque valeur = écart-type
usigma_reglin = np.std(sigma_reglin_list, ddof=1, axis=0)

# idem pour a, b
# Les valeurs moyennes sont les moyennes des listes
a_moy, b_moy = np.mean(a_list), np.mean(b_list)
# Les incertitudes sont l'écart-type des listes
ua, ub = np.std(a_list, ddof=1), np.std(b_list, ddof=1)

print(f"Coef.directeur = ({a_moy*1e3:.3f} ± {ua*1e3:.3f})⋅10^-3 s^-1")
print(f"Ordonnée à l'origine = ({b_moy:.3f} ± {ub:.3f})")

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

# Liste fine des abscisses à tracer
# découpe l'intervalle [min(X), max(X)] en 100 points
xliste = np.linspace(min(t_tab), max(t_tab), 100)

# Fonction qui à `abscisse`, `coeff_dir`, `ord_ori` associe y
def yfunc(abscisse, coeff_dir, ord_ori):
    return coeff_dir*abscisse + ord_ori

# Liste des points y_i obtenus par régression
yliste = yfunc(xliste, a_moy, b_moy)

# =========================================================================== #
#                                    Tracé                                    #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("$t$ en secondes", fontsize=20)
plt.ylabel(
    "$\\displaystyle\\frac{\\sigma_0 - \\sigma_{\\infty}}{\\sigma - \\sigma_{\\infty}}$", fontsize=20
)

plt.errorbar(t_tab, sigma_reglin_moy,
             xerr=ut_tab, yerr=usigma_reglin,
             linestyle='None', capsize=3,
             color='orange', label='Mesures')
plt.plot(xliste, yliste,
         'cornflowerblue',
         label='Régression\n' + fr'\begin{{eqnarray*}}a &=& \SI{{{a_moy*1e3:.3f}\pm{ua*1e3:.3f}e-3}}{{s^{{-1}}}}\\b &=& \num{{{b_moy:.3f}\pm{ub:.3f}}}\end{{eqnarray*}}'
         )

plt.title("Vérification de l'hypothèse ordre 2", fontsize=20)
plt.legend(fontsize=15)
# plt.show()
plt.savefig("../figures/TP11_cinetique_sigma_reglin.pdf", bbox_inches="tight")

# =========================================================================== #
#                                 Calcul de k                                 #
# =========================================================================== #

c0 = 0.050  # mol.L-1
k = a_moy / c0
uk = ua / c0

print(f"k = ({k*1e2:.2f} ± {uk*1e2:.2f})*10^-2 mol.L^-1.s^-1")

# =========================================================================== #
#                                Données de Ea                                #
# =========================================================================== #

theta: np.ndarray = np.array([25, 35, 40, 45])  # °C
T: np.ndarray = theta + 273  # K
k_tab: np.ndarray = [k, 0.188, 0.257, 0.356]  # mol.L^-1.s^-1

# =========================================================================== #
#                                  Régression                                 #
# =========================================================================== #

X = 1 / T
Y = np.log(k_tab)
a, b = np.polyfit(X, Y, 1)
print(f"a = {a:.3f} K, b = {b:.3f}")

# Liste fine des abscisses à tracer
# découpe l'intervalle [min(X), max(X)] en 100 points
xliste = np.linspace(min(X), max(X), 100)

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

# Fonction qui à `abscisse`, `coeff_dir`, `ord_ori` associe y
def yfunc(abscisse, coeff_dir, ord_ori):
    return coeff_dir * abscisse + ord_ori

# Liste des points y_i obtenus par régression
yliste = yfunc(xliste, a, b)

# =========================================================================== #
#                                    Tracé                                    #
# =========================================================================== #

plt.figure(figsize=(8, 6))
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.xlabel("$\\displaystyle\\frac{1}{T}$ en K$^{-1}$", fontsize=20)
plt.ylabel("$\\ln(k(T))$", fontsize=20)

plt.scatter(X, Y, marker="+", s=100, color="orange", label="Données")
plt.plot(xliste, yliste, "cornflowerblue",
         # label="Régression linéaire"
         label='Régression\n' + fr'\begin{{eqnarray*}}a &=& \SI{{{a:.2e}}}{{K}}\\b &=& \num{{{b:.1f}}}\end{{eqnarray*}}'
         )

plt.title("Détermination de l'énergie d'activation par régression", fontsize=20)
plt.legend(fontsize=15)
# plt.show()
plt.savefig("../figures/TP11_cinetique_reglin_Ea.pdf", bbox_inches="tight")

# =========================================================================== #
#                                Calcul de Ea                                 #
# =========================================================================== #

R = 8.314  # J.K^-1.mol^-1
Ea = -a * R
print(f"E_a = {Ea:.1e} J.mol^-1")

