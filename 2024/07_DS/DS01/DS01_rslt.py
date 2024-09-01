import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
dgmap = colormaps['viridis']

notes = np.sort(np.genfromtxt('DS01_note.csv', skip_header=1))
# print(notes)

qs = np.quantile(notes, [0.25, 0.5, 0.75, 1])
notes_a = notes[notes <= qs[0]]
notes_b = notes[(notes > qs[0]) & (notes <= qs[1])]
notes_c = notes[(notes > qs[1]) & (notes <= qs[2])]
notes_d = notes[notes > qs[2]]
nmax = int(np.ceil(max(notes)))
nmin = int(np.floor(min(notes)))
print(qs)

moy = np.mean(notes)
med = np.median(notes)
std = np.std(notes, ddof=1)

fig = plt.figure(figsize=[8, 3])
ax = fig.add_axes([0.1, 0.12, 0.90, 0.8])

ax.axvline(moy,
           color='k',
           lw=1.0)

ax.axvspan(moy-std,
           moy+std,
           color='k',
           alpha=.05,
           zorder=0)

_, X, patches = ax.hist(notes, bins=[i for i in range(min(nmin, 0), nmax+1)],
                        histtype='step',
                        color='k', alpha=.5, zorder=2)

for ll, cc, qq in zip([notes_a, notes_b, notes_c, notes_d],
                      [0, 100, 200, 300],
                      ['Q4', 'Q3', 'Q2', 'Q1']):
    if len(ll) > 0:
        ax.axvspan(np.min(ll),
                   np.max(ll),
                   color=dgmap(cc),
                   alpha=.5,
                   clip_path=patches[0],
                   label=qq,
                   zorder=1)

ax.tick_params(direction='in',
               length=3, width=1,
               labelsize=20,
               top=True, right=True)

ax.set_xticks(np.arange(min(nmin, 0), nmax+1, step=1.0))
ax.set_yticks(np.arange(0, np.max(_)+1, step=1.0))

ax.set_xlim((min(nmin, 0), nmax))

ax.set_xlabel(r"$\mathrm{Notes}$ ", fontsize=20)
ax.set_ylabel(r"$\mathrm{N}_\mathrm{notes}$ ", fontsize=20)

ax.legend(fontsize=18)

ax.set_title(f'Résultat DS01 : moyenne = {moy:.2f}, '
             + f'médiane = {med:.2f}, '
             + f'écart-type = {std:.2f}',
             fontsize=20)

dir_path = os.path.dirname(os.path.realpath(__file__))

fig = plt.gcf()
fig.savefig(dir_path + '/DS01_rslt.pdf',
            bbox_inches='tight')
