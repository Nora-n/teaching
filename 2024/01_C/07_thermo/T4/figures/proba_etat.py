import matplotlib.pyplot as plt
import numpy as np
from math import comb
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'

Ntot:list = [10, 100, 1000, 10000]
mks:list = ['+', 'x', '--', '-']
clrs:list = ['orchid', 'cornflowerblue', 'limegreen', 'orange']

fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

for N,mk,cl in zip(Ntot,mks,clrs):
    X = []
    Y = []
    for K in range(1, N):
        X.append(K)
        Y.append(comb(N, K))
    X = np.asarray(X)
    X = X/N
    Y = np.asarray(Y)
    Y = Y/max(Y)
    ax.plot(X, Y, mk, c=cl, label=fr'$N_{{\rm tot}} = {N}$')

ax.axvline(0.5, c='k', ls=':', label=fr'$N_{{\rm tot}} \to \infty$')

ax.set_xticks(np.arange(0, 1.1, 0.1))
ax.set_xlim(0,1)

ax.set_xlabel(r'$\displaystyle\frac{N_g}{N_{\rm tot}}$',
              fontsize='large')
ax.set_ylabel(r'$\displaystyle\frac{\Omega(N_g)}{\Omega_{\rm max}}$',
              rotation=0, ha='right', va='center',
              fontsize='large')

ax.legend(fontsize='large')
fig.savefig('./2023/01_C/07_thermo/T4/figures/proba_etat.pdf',
            bbox_inches="tight")

# fig = plt.figure(figsize=(5, 3))
# ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))
#
# ax.plot(t1_list, Tint_coupe_hlist,
#         lw=2, color='orange',
#         label='Arrêt complet chauffage')
# ax.plot([0,tau_h],[Tc,Text],
#         ls='--', c='cornflowerblue',
#         label=r'$\tau$')
#
# ax.set_xlabel(r'$\tau$ (h)', x=1, ha='right', va='top')
# ax.set_ylabel(r'$T_{\rm int}$ (K)', y=1.05, rotation=0, ha='left')
#
# ax.set_xlim(left=0)
# ax.set_ylim(bottom=Text)
#
# ax.legend(fontsize='x-large')
# ax.spines[['right', 'top']].set_visible(False)
# ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
# ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)
#
# fig.savefig('proba_etat.pdf', bbox_inches="tight")
