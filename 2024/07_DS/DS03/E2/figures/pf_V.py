import numpy as np
import matplotlib as mpl
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

mpl.rc("text.latex", preamble=r"\usepackage{xcolor}\usepackage{amsmath}")

################### AMPLITUDE ###################

Ps = 1  # bar
R = 8.314  # J.K^-1.mol^-1
T = 473  # K
K = 52.6e-3

Pmax = K * Ps

n0 = 2.00e-3  # mol
Vlim = n0 * R * T / (2 * K * Ps)

Vlist = np.linspace(0, 3 * Vlim, 1000)
xmin, xmax = [min(Vlist), max(Vlist)]


def Pfunc(V):
    if V < Vlim:
        return Pmax
    else:
        return (n0 * R * T) / (2 * V)


Pf = np.vectorize(Pfunc)

fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

Pf_list = Pf(Vlist)
ymin, ymax = [min(Pf_list), max(Pf_list)]

ax.plot(Vlist, Pf_list, color="firebrick")
ax.axvline(Vlim, c="k", ls="--", lw=1)

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, 1.3 * ymax)

ax.set_xlabel("$V$", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_ylabel("$P_f$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([Vlim])
ax.set_xticklabels(["$V_{\\mathrm{lim}}$"])
ax.set_yticks([Pmax])
# ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
ax.set_yticklabels(["$P_{\\mathrm{max}}$"])

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.text(
    0.15,
    0.75,
    "Équilibre",
    fontsize=15,
    ha="center",
    va="center",
    bbox=dict(fc="none", ec="black", lw=1),
    transform=ax.transAxes,
)
ax.text(
    0.65,
    0.75,
    "Rupture d'équilibre",
    fontsize=15,
    ha="center",
    va="center",
    bbox=dict(fc="none", ec="black", lw=1),
    transform=ax.transAxes,
)
ax.text(
    2 * Vlim,
    1.05 * Pf(2 * Vlim),
    "$\\displaystyle P_f\\propto\\frac{1}{V}$",
    fontsize=12,
    ha="left",
    va="bottom",
)

fig.savefig("./pf_V.pdf", bbox_inches="tight")
