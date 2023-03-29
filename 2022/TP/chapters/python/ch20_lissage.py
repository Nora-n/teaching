# =========================================================================== #
#                                  Imports                                    #
# =========================================================================== #

import numpy as np              # pour les tableaux
import matplotlib.pyplot as plt  # pour les graphiques

from scipy.interpolate import interp1d  # pour le lissage
from scipy.interpolate import make_interp_spline
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import pchip

# =========================================================================== #
#                                  Données                                    #
# =========================================================================== #

# Lot
# f = np.array([4, 5, 5.5, 6, 6.5, 7, 7.25, 7.5, 8, 9, 10, 11, 12, 13, 15])
# w = 2*np.pi*f
# wreg = np.linspace(min(w), max(w), 300)
#
# A = np.array([0.14, 0.21, 0.295, 0.55, 1.2, 1.85, 1.2, 0.825,
#               0.55, 0.35, 0.31, 0.26, 0.24, 0.23, 0.22])

# Arifi
f = np.array([4.7, 5.3, 6.0, 6.5, 6.8, 7.1, 7.6, 8.4, 9.0,
              10.0, 11.0, 12.0, 13.0, 14.0, 15.0])  # enHz
w = 2*np.pi*f
wreg = np.linspace(min(w), max(w), 300)

A = np.array([0.045, 0.073, 0.138, 0.411, 1.932, 0.79, 0.283, 0.161,
              0.127, 0.101, 0.087, 0.079, 0.077, 0.075, 0.075])  # enm.s^-2

V = A/w
Z = V/w

# =========================================================================== #
#                                  Lissages                                   #
# =========================================================================== #

Vlisse_cub = interp1d(w, V, kind='cubic')
Vreg_cub = Vlisse_cub(wreg)

Vlisse_spline = make_interp_spline(w, V)
Vreg_spline = Vlisse_spline(wreg)

Vlisse_uspline = UnivariateSpline(w, V)
Vreg_uspline = Vlisse_uspline(wreg)

Vlisse_quad = interp1d(w, V, kind='quadratic')
Vreg_quad = Vlisse_quad(wreg)

Vlisse_pch = pchip(w, V)
Vreg_pch = Vlisse_pch(wreg)

# =========================================================================== #
#                                                                             #
#                                    Tracé                                    #
#                                                                             #
# =========================================================================== #

fig = plt.figure(figsize=(10, 6))
plt.grid()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# =========================================================================== #
#                                    Vitesse                                  #
# =========================================================================== #

plt.scatter(w, V,
            marker='x', s=100,
            color='blue',
            label='Vitesse')

# plt.plot(wreg, Vreg_cub,
#          linestyle='-',
#          color='blue',
#          label='interp1d cubic')

plt.plot(wreg, Vreg_spline,
         linestyle='-',
         color='green',
         label='spline')

# plt.plot(wreg, Vreg_uspline,
#          linestyle='-',
#          color='orange',
#          label='Univariate spline')

plt.plot(wreg, Vreg_pch,
         linestyle='-',
         color='orange',
         label='p-chip')

# plt.plot(wreg, Vreg_quad,
#          linestyle='-',
#          color='firebrick',
#          label='interp quad')

# plt.plot(w, V,
#          color='purple',
#          label='Simple plot')

plt.xlabel(r'$\omega$ (rad.s$^{-1}$)',
           fontsize=15)
plt.ylabel(r'$v$ (m.s$^{-1}$)',
           fontsize=15)

# =========================================================================== #
#                               Titre, légende                                #
# =========================================================================== #

plt.xlim(25, 55)

plt.title("Étude de la résonance d'un ressort", fontsize=20)
plt.legend(fontsize=15, loc='best')

plt.tight_layout()
plt.show()

fig.savefig('ch20_lissage_lot.pdf', bbox_inches='tight')
# fig.savefig('ch20_lissage_lot.png', bbox_inches='tight', dpi=600)
