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

Um = 5.0  # V
Vm = 3.5  # V
R = 1e2  # O
r = 49  # O
L = 0.49  # H
T = 6.3e-2  # s
f = 1 / T  # Hz
w = 2 * np.pi * f  # rad.s^-1
phi = np.pi / 4  # rad

################## TIMESERIES ##################

tlist = np.linspace(-0.15 * T, 1.5 * T, 1000)
xmin, xmax = [min(tlist), max(tlist)]


def ufunc(t):
    return Um * np.cos(w * t)


def vfunc(t):
    return Vm * np.cos(w * t + phi)


u = np.vectorize(ufunc, otypes=[np.float64])
v = np.vectorize(vfunc, otypes=[np.float64])

fig = plt.figure(figsize=(7.5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)
    ax.spines[axe].set_position("zero")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

u_list = u(tlist)
v_list = v(tlist)
ymin, ymax = [min(u_list), max(u_list)]

ax.plot(tlist, u_list, color="cornflowerblue", label="$u(t)$")
ax.plot(tlist, v_list, ls="--", color="firebrick", label="$v(t)$")
# ax.axvline(Vlim, c="k", ls="--", lw=1)

ax.legend(loc="upper right", fontsize=15, framealpha=1)

ax.grid(visible=True, which="both")

ax.set_xlim(xmin, xmax)
ax.set_ylim(1.03 * ymin, 1.03 * ymax)

ax.set_xlabel("$t$ ($10^{-2}$s)", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(0.95, 0.57)
ax.set_ylabel("tensions (V)", fontsize=15, rotation=0, clip_on=False)
ax.yaxis.set_label_coords(0.091, 1.02)

ax.set_xticks(np.arange(1e-2, 9.1e-2, 1e-2))
ax.set_xticklabels(np.arange(1, 10, 1))
# plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
# lbls = ax.get_xticklabels()
# ax.set_xticklabels(lbls, rotation=45)
ax.set_yticks(np.arange(-5, 6, 1))
# ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
# ax.set_yticklabels(["$P_{\\mathrm{max}}$"])

# ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="x")

ax.plot(0.091, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.5, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# plt.show()

fig.savefig("./rd_Ul_time.pdf", bbox_inches="tight")
