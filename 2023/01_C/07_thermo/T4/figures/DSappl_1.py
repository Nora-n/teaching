import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'


fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

R = 8.314 # J.K.mol^-1
g = 7/5
Cvm = R/(g-1)

xs = np.linspace(0,5,1000)
def Scr(x):
    return(Cvm*(x-1-np.log(x)))

ax.plot(xs, Scr(xs), c='cornflowerblue', ls='none')

ax.set_xlabel(r'$\displaystyle x = \frac{T_i}{T_f}$')
ax.set_ylabel(r'$\displaystyle S_{{\rm cr}, m}$ (J$\cdot$K$^{-1}\cdot$mol$^{-1}$)')

ax.grid()

fig.savefig('./2023/01_C/07_thermo/T4/figures/DSappl_1-stud.pdf',
            bbox_inches="tight")

ax.plot(xs, Scr(xs), c='cornflowerblue')

fig.savefig('./2023/01_C/07_thermo/T4/figures/DSappl_1.pdf',
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
