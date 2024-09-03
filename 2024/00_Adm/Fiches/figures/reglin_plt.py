import numpy as np
import matplotlib.pyplot as plt

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

abscisse = np.linspace(0, 10, 8)  # définit les abscisses qu'on tracera
ordonnee = [
    abscisse**2,
    2 * abscisse + 1 * np.random.uniform(-1, 1, len(abscisse)),
    2 * abscisse + 3 * np.sin(abscisse),
    2 * abscisse + 3 * np.random.uniform(-1, 1, len(abscisse)),
]
# et les ordonnées
erreurs = [
    15 * np.ones(len(abscisse)),
    1 * np.ones(len(abscisse)),
    1 * np.ones(len(abscisse)),
    5 * np.ones(len(abscisse)),
]

titles = ["A)", "B)", "C)", "D)"]

fig, axd = plt.subplots(2, 2, figsize=(12, 8))
axs = axd.ravel()

for i in range(4):
    a, b = np.polyfit(abscisse, ordonnee[i], 1)

    axs[i].grid(ls="dotted")

    axs[i].errorbar(
        abscisse,
        ordonnee[i],
        yerr=erreurs[i],
        fmt="o",
        capsize=3,
        color="cornflowerblue",
        label="Mesures",
    )

    axs[i].plot(abscisse, a * abscisse + b, color="orange", label="Régression")
    axs[i].set_xlabel(r"$x$ (unité)")  # nomme l'abscisse
    axs[i].set_ylabel(r"$y$ (unité)")  # nomme l'ordonnée

    # axs[i].set_title(titles[i], fontsize=20)

    axs[i].legend(fontsize="xx-large")
    t = axs[i].text(
        0.95,
        0.05,
        titles[i],
        ha="right",
        va="bottom",
        transform=axs[i].transAxes,
        fontsize=20,
    )
    t.set_bbox(dict(facecolor="white"))

# fig.subplots_adjust(hspace=0.5)
fig.savefig("reglin.pdf", bbox_inches="tight")

# X = np.linspace(0, 10, 8)
# Y = X**2
#
# plt.figure(figsize=(8, 6))  # dimension horizontale, verticale
# plt.grid()  # affiche un quadrillage de lecture
# plt.xticks(fontsize=20)  # affiche les nombres de l'axe x plus grand
# plt.yticks(fontsize=20)  # affiche les nombres de l'axe y plus grand
# plt.xlabel(
#     "$x$ en cm",  # Donne le nom de l'axe x, $ pour le mode math
#     fontsize=20,
# )  # en grand
# plt.ylabel(
#     "$y$ en cm",  # Donne le nom de l'axe y, $ pour le mode math
#     fontsize=20,
# )  # en grand
#
# plt.scatter(
#     X,
#     Y,  # nuage de points X en abscisse et Y en ordonnée
#     marker="x",
#     s=100,  # possibilité de customiser le tracé
#     color="blue",  # pour la couleur
#     label="Données",
# )  # pour la légende
#
# plt.errorbar(
#     X + 1,
#     Y + 1,  # nuage de points X abscisse et Y ordonnée
#     xerr=0.5,  # incertitude en x
#     yerr=5,  # incertitude en y
#     capsize=3,  # indique la limite des erreurs
#     color="orange",  # pour la couleur
#     label="Avec incertitudes",
# )
#
# plt.plot(
#     X - 1,
#     Y - 1,  # graphique relié
#     color="g",  # couleur
#     marker="^",  # marker
#     markersize=10,  # taille marker
#     linestyle="dotted",  # type de ligne
#     linewidth=2,  # épaisseur
#     label="Courbe verte diamant pointillés",
# )
#
# plt.title("Présentation des options de tracé", fontsize=20)
# plt.legend(fontsize=15)
#
# plt.tight_layout()  # évite les débordements ou rognages
# plt.xlim(min(X) - 0.1, max(X) + 2)  # pour les limites d'affichage en abscisse
# plt.ylim(min(Y) - 6, max(Y) + 10)  # pour les limites d'affichage en ordonnée
# # plt.show()
#
# plt.savefig("python_plt-2.pdf", bbox_inches="tight")
