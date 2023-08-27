# %%
# lissage MT

import matplotlib.pyplot as plt

from scipy.interpolate import pchip

# %%
# DATA résonance mécanique ()

import numpy as np              # pour les tableaux

f = np.array([4.7, 5.3, 6.0, 6.5, 6.8, 7.1, 7.6, 8.4, 9.0,
              10.0, 11.0, 12.0, 13.0, 14.0, 15.0])  # enHz
w = 2*np.pi*f
wreg = np.linspace(min(w), max(w), 300)

A = np.array([0.045, 0.073, 0.138, 0.411, 1.932, 0.79, 0.283, 0.161,
              0.127, 0.101, 0.087, 0.079, 0.077, 0.075, 0.075])  # enm.s^-2
V = A/w
Z = V/w

Vlisse_pch = pchip(w, V)
Vreg_pch = Vlisse_pch(wreg)

# alias ... pour la réutilisation de mon ancien code !
lx = w
ly = V

# %%
# régression linéaire de ly=f(lx). Retourne les coeffs (a,b) de la droite de
# régression y = a x + b


def reglin(lx, ly):
    sx = sy = sxy = sx2 = 0
    n = len(lx)
    for i in range(n):
        sx += lx[i]
        sy += ly[i]
        sx2 += lx[i]**2
        sxy += lx[i] * ly[i]
    a = (sxy - sx * sy / n)/(sx2 - sx**2 / n)
    b = sy / n - a * sx / n
    return (a, b)

# %%
# lissage
# calcul de la dérivée première
# Les points de lx n'étant pas équidistants, la dérivée au point d'index i est
# calculée à partir de la parabole
# passant pas les points i-1, i, i+1


def derive(lx, ly):
    ld = [0] * len(ly)

    for i in range(1, len(ld)-1):
        x1 = lx[i]-lx[i-1]
        x2 = lx[i+1]-lx[i-1]
        y1 = ly[i]-ly[i-1]
        y2 = ly[i+1]-ly[i-1]

        if i == 1:
            ld[0] = (x2**2 * y1 - x1**2 * y2) \
                / (x1 * x2 * (x2 - x1))
        elif i == len(ld)-2:
            ld[-1] = (-2 * x1 * x2 * y2 + x2**2 * y1 + x1**2 * y2) \
                / (x1 * x2**2 - x1**2 * x2)

        ld[i] = (-2 * x1 * x2 * y1 + x2**2 * y1 + x1**2 * y2) \
            / (x1 * x2**2 - x1**2 * x2)
    return ld

# calcul de l'intégrale de la dérivée, avec F(x0)=0 (méthode des trapèzes)


def integre(lx, ld):
    lid = [0] * len(ld)
    for i in range(1, len(ld)):
        lid[i] = lid[i-1] + (lx[i] - lx[i-1]) * (ld[i] + ld[i-1]) / 2
    return lid


# %%
ld = derive(lx, ly)
lid = integre(lx, ld)
a, b = reglin(lid, ly)
liss = [a * y + b for y in lid]
ldliss = [a * yp for yp in ld]

# %%
# tracé de la courbe de lissage.
# on utilise pour ce tracé un nombre de points bien plus important que le nombre de points de données
# (pour avoir un tracé bien régulier)

n = 200   # nbre de points pour le tracé

# la liste des abscisses des points servant au tracé
lpx = [lx[0] + (lx[-1]-lx[0]) / n * i for i in range(n)]

# Chaque point pour le tracé se trouve dans un intervalle défini par les points de données.
# pour un point du lissage, il faut donc savoir dans quel intervalle il se trouve.
#

# lpi est la liste de taille n des index d'intervalle :
# le point d'index ip pour le lissage se trouve dans l'intervalle lpi[ip] défini par les points de données
lpi = [0]
ix = 0
for ip in range(1, n):
    while lpx[ip] > lx[ix]:
        ix += 1
    lpi.append(ix-1)

# la liste des ordonnées est calculée à partir des valeurs lissées de y et y' pour chacun
# des intervalles définis par les points de données.
# La valeur calculée est déterminée par le polynôme de lissage (de degré 2) défini entre
# deux points successifs de données (ce polynôme change en fonction de l'intervalle considéré)
lpy = []
for i in range(n):
    ii = lpi[i]
    rx = lpx[i] - lx[ii]
    lpy.append(liss[ii] + ldliss[ii] * rx + 1/2 *
               (ldliss[ii+1]-ldliss[ii])/(lx[ii+1]-lx[ii]) * rx**2)

# %%

# Tracé de la fonction de lissage, des points de données
plt.figure('lissage', figsize=(6, 4), dpi=200)
plt.grid()
plt.plot(lpx, lpy)
plt.plot(wreg, Vreg_pch,
         linestyle='-',
         color='purple',
         label='p-chip')
plt.scatter(lx, ly, marker='+')
plt.scatter(lx, liss)
plt.legend()
plt.show()

# %%
