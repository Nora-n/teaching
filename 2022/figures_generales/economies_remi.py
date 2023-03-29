import numpy as np
import matplotlib.pyplot as plt

base = 42


def cout(x, fixe, pourcent):
    return pourcent*base*x + fixe


xliste = np.linspace(0, 50, 1000)
cout_stand = cout(xliste, 0, 1)
cout_remi = cout(xliste, 30, 0.66)
cout_rplu = cout(xliste, 200, 0.50)

idx_sr = np.argwhere(np.diff(np.sign(cout_stand - cout_remi))).flatten()
idx_srp = np.argwhere(np.diff(np.sign(cout_stand - cout_rplu))).flatten()
idx_rp = np.argwhere(np.diff(np.sign(cout_remi - cout_rplu))).flatten()

fig, ax = plt.subplots(figsize=[8, 6])

plt.grid(linestyle='--')

ax.plot(xliste, cout_stand,
        color='orange',
        label='Standard')
ax.plot(xliste, cout_remi,
        color='firebrick',
        label='Remi')
ax.plot(xliste, cout_rplu,
        color='cornflowerblue',
        label='Remi +')

ax.scatter(xliste[idx_sr], cout_stand[idx_sr],
           color='firebrick',
           label=f'J = {xliste[idx_sr][0]:.1f}')
ax.scatter(xliste[idx_srp], cout_stand[idx_srp],
           color='orange',
           label=f'J = {xliste[idx_srp][0]:.1f}')
ax.scatter(xliste[idx_rp], cout_remi[idx_rp],
           color='cornflowerblue',
           label=f'J = {xliste[idx_rp][0]:.1f}')

ax.set_xlim(min(xliste), max(xliste))
ax.set_ylim(bottom=0)

ax.set_xlabel('Jours', fontsize=15)
ax.set_ylabel('Prix (€)', fontsize=15)

ax.tick_params(labelsize=15)

ax.legend(fontsize=15)
ax.set_title('Étude des économies réalisées pour les cartes Rémi')
plt.show()
