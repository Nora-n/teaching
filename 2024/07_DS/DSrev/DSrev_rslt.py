import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import colormaps
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
# dgmap = colormaps['viridis']

DS = "DSrev"

df = pd.read_csv(f'{DS}_note.csv')
bar = {"DS": 20,
       "E1": 36,
       "P1": 66,
       "P2": 73,
       "P3": 85}

Elett = ["E1", "P1", "P2", "P3"]
hist_step = {"E1": 3, "P1": 4, "P2": 5, "P3": 5}
lgd = {"DS": True, "E1": False, "P1": False, "P2": False, "P3": True}

dgmap = plt.colormaps.get_cmap('viridis')
def make_hist_E(E, ax=None, lgd=True,
                save_ind=True, stud=None, moy_word="moyenne"):
    if ax is None:
        fig = plt.figure(figsize=[8, 3])
        ax = fig.add_axes([0.1, 0.12, 0.90, 0.8])
    else:
        ax = ax
        fig = plt.gcf()
    # Extrait les notes de l'exercice
    if 'DS' in E:
        notes = df[f'{DS}']
    else:
        notes = df[E].dropna()

    nb = len(notes)
    # Calcule les quartiles pour les couleurs
    qs = np.quantile(notes, [0.25, 0.5, 0.75, 1])
    # Associe chaque note à un quartile
    notes_a = notes[notes <= qs[0]]
    notes_b = notes[(notes > qs[0]) & (notes <= qs[1])]
    notes_c = notes[(notes > qs[1]) & (notes <= qs[2])]
    notes_d = notes[notes > qs[2]]

    # Notes max et min pour tracer les limites de l'histogramme
    ntmax = int(np.ceil(max(notes)))
    nmax = bar[E]
    nmin = min(int(np.floor(min(notes))),0)

    # Explicite
    moy = np.mean(notes)
    med = np.median(notes)
    std = np.std(notes, ddof=1)

    # Trace moyenne et écart-type
    ax.axvline(moy, color='k', lw=2.0)
    ax.axvline(moy-std, color='grey', ls="--", lw=1.0)
    ax.axvline(moy+std, color='grey', ls="--", lw=1.0)
    ax.axvspan(moy-std, moy+std, color='k', alpha=.05, zorder=0)

    # # Ajoute ligne orange si stud donné
    # if stud is not None:
    #     if 'DS' in E:
    #         d = df_main.loc[stud]
    #         smoy = d[DS]
    #     else:
    #         D = df_stud[stud]
    #         smoy = D["Total"][E]
    #
    #     ax.axvline(float(smoy), color='orange', ls="-", lw=4.0, label=stud)

    # Trace l'histogramme sans les couleurs
    if 'DS' in E:
        # Assure d'avoir le min à 0 ou à la plus petite note (si négative)
        # Et d'avoir le max à 20 ou la plus grand note (si > 20)
        _, X, patches = ax.hist(notes,
                                bins=[i for i in range(
                                    nmin, max(ntmax, 20)+1)
                                     ],
                                histtype='step',
                                color='k', alpha=.5, zorder=2)
        ax.set_title(f'Résultat {DS} : moyenne = {moy:.2f}, '
                     + f'médiane = {med:.2f}, '
                     + f'écart-type = {std:.2f}',
                     fontsize=20) 
        ax.set_xticks(np.arange(min(nmin, 0), max(ntmax, 20)+1, step=1.0))
        ax.set_yticks(np.arange(0, np.max(_)+1, step=1.0))

        ax.set_xlim(min(nmin, 0), max(ntmax, 20))
    else:
        _, X, patches = ax.hist(notes,
                                bins=[i for i in range(nmin, nmax+1)],
                                histtype='step',
                                color='k', alpha=.5, zorder=2)
        ax.set_title(f'{E} : entrées = {nb}, ' +\
                     f'{moy_word} = {moy:.2f}/{bar[f"{E}"]}',
                     fontsize=20)
        # Quels sont les points affichés
        ax.set_xticks(np.arange(nmin, nmax+1, step=hist_step[E]))
        ax.set_xlim(nmin, nmax)

    # Colorie pour chaque quartile
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

    # paramètres des ticks
    ax.tick_params(labelsize=20)
    ax.tick_params(direction='in',
               length=3, width=1,
               labelsize=20,
               top=True, right=True)
    ax.yaxis.set_tick_params(labelbottom=True)

    ax.set_xlabel("Points", fontsize=20)
    ax.set_ylabel(r"$N_\mathrm{notes}$ ", fontsize=20)

    if lgd:
        ax.legend(fontsize=16)

    if save_ind:
        fig.savefig(f'{DS}/hist_{E}.pdf', bbox_inches='tight')

fig = plt.figure(figsize=(13, 15), constrained_layout=False)
gs = fig.add_gridspec(3, 2, hspace=.25, wspace=.1)
# axd = gs.subplots(sharey=True, sharex=True)
ax = fig.add_subplot(gs[0,:])
ax1 = fig.add_subplot(gs[1,0])
ax2 = fig.add_subplot(gs[1,1])
ax3 = fig.add_subplot(gs[2,0])
ax4 = fig.add_subplot(gs[2,1])

axs = [ax, ax1, ax2, ax3, ax4]

for E, ax in zip(["DS"]+Elett, axs):
    make_hist_E(E, ax=ax, lgd=lgd[E], save_ind=False)
    # ax.grid(zorder=0)
    if "DS" not in E:
        if "E1" in E:
            ax.set_xlabel("")
        elif "P1" in E:
             ax.set_ylabel("")
             ax.set_xlabel("")
        elif "P2" in E:
            pass
        else:
            ax.set_ylabel("")
        # if "P" not in E:
        #     ax.set_xlabel("")
        # if "1" not in E:
        #     ax.set_xlabel("")

fig.suptitle(f'Histogrammes des points obtenus par exercice du {DS}',
                fontsize=25, y=.93)

dir_path = os.path.dirname(os.path.realpath(__file__))

fig = plt.gcf()
fig.savefig(dir_path + f'/{DS}_hist_all.pdf',
            bbox_inches='tight')

# fig.savefig(f'{DS}/hist_all.pdf', bbox_inches='tight')
# fig.savefig(f'../../../07_DS/{DS}/{DS}_hist_all.pdf',
#             bbox_inches='tight')
