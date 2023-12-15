import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
plt.rc('text.latex',
       preamble=r'\usepackage[detect-all,locale=FR]{siunitx}[=v2]')

data = {"t":
        np.array([10*i for i in range(1,11)]),
        "x0":
        np.array([0.5, 0.90, 1.35, 1.65, 1.95, 2.25, 2.45, 2.65, 2.80,
                  2.90])*1e-3}
V0 = 0.1  # L
ca = 0.10 # mol.L^-1

data["x1"] = np.log((ca*V0 - 2*data["x0"])/(ca*V0))
data["x2"] = 1/(ca*V0 - 2*data["x0"]) - 1/(ca*V0)

ttl = [fr"$x = f(t)$",
       fr"$\ln(1-200x) = f(t)$",
       fr"$\frac{{1}}{{0.01-2x}}-100 = f(t)$"]

a = dict()
b = dict()
for i in range(3):
    x = data["t"]
    y = data["x"+str(i)]
    a, b = np.polyfit(x, y, 1)

    fig = plt.figure(figsize=(7,5))
    rect = 0.1, 0.10, 0.8, 0.8
    ax = fig.add_axes(rect)

    ax.scatter(x, y, s=200,
               marker="+",
               # color="orange",
               color="black",
               label="Données")
    ax.plot(x, a*x+b,
            # color="cornflowerblue",
            color="black",
            label="Régression")
    ax.set_xlabel("$x$",fontsize=20)
    ax.set_ylabel("$y$",fontsize=20)
    ax.legend(fontsize=15)
    ax.set_title(ttl[i] + "\n" +\
                fr"$y=\num{{{b:.2e}}}+\num{{{a:.2e}}}x$",
                fontsize=25)
    fig.savefig(f"./graph_{i+1}.pdf",
                bbox_inches="tight")
