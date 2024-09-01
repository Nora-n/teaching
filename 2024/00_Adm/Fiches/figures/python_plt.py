import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "EB Garamond",
        # "axes.labelsize": "x-large",
        # "xtick.labelsize": "x-large",
        # "ytick.labelsize": "x-large",
    }
)
plt.rcParams["figure.facecolor"] = "w"

abscisse = np.linspace(0, 10, 8)  # définit les abscisses qu'on tracera
ordonnee = abscisse**2  # et les ordonnées

plt.plot(abscisse, ordonnee)  # place les points, les relie par des segments
plt.xlabel("t (s)")  # nomme l'abscisse
plt.ylabel("x (m)")  # nomme l'ordonnée

# plt.show()                       # obligé pour afficher
plt.savefig("python_plt-1.pdf", bbox_inches="tight")

X = np.linspace(0, 10, 8)
Y = X**2

plt.figure(figsize=(8, 6))  # dimension horizontale, verticale
plt.grid()  # affiche un quadrillage de lecture
plt.xticks(fontsize=20)  # affiche les nombres de l'axe x plus grand
plt.yticks(fontsize=20)  # affiche les nombres de l'axe y plus grand
plt.xlabel(
    "$x$ en cm",  # Donne le nom de l'axe x, $ pour le mode math
    fontsize=20,
)  # en grand
plt.ylabel(
    "$y$ en cm",  # Donne le nom de l'axe y, $ pour le mode math
    fontsize=20,
)  # en grand

plt.scatter(
    X,
    Y,  # nuage de points X en abscisse et Y en ordonnée
    marker="x",
    s=100,  # possibilité de customiser le tracé
    color="blue",  # pour la couleur
    label="Données",
)  # pour la légende

plt.errorbar(
    X + 1,
    Y + 1,  # nuage de points X abscisse et Y ordonnée
    xerr=0.5,  # incertitude en x
    yerr=5,  # incertitude en y
    capsize=3,  # indique la limite des erreurs
    color="orange",  # pour la couleur
    label="Avec incertitudes",
)

plt.plot(
    X - 1,
    Y - 1,  # graphique relié
    color="g",  # couleur
    marker="^",  # marker
    markersize=10,  # taille marker
    linestyle="dotted",  # type de ligne
    linewidth=2,  # épaisseur
    label="Courbe verte diamant pointillés",
)

plt.title("Présentation des options de tracé", fontsize=20)
plt.legend(fontsize=15)

plt.tight_layout()  # évite les débordements ou rognages
plt.xlim(min(X) - 0.1, max(X) + 2)  # pour les limites d'affichage en abscisse
plt.ylim(min(Y) - 6, max(Y) + 10)  # pour les limites d'affichage en ordonnée
# plt.show()

plt.savefig("python_plt-2.pdf", bbox_inches="tight")
