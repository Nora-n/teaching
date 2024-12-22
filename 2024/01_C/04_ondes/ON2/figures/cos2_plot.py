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

################## TIMESERIES ##################

T = 1  # s
f = 1 / T  # Hz
w = 2 * np.pi * f  # rad.s^-1
A = 1  # V

tlist = np.linspace(0, 1.5 * T, 1000)
xmin, xmax = [min(tlist), max(tlist)]


def ufunc(t):
    return A * np.cos(w * t)


u = np.vectorize(ufunc, otypes=[np.float64])

fig = plt.figure(figsize=(3, 1.5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

u_list = u(tlist)
ymin, ymax = [min(u_list**2), max(u_list)]

# ax.legend(loc="upper right", fontsize=15, framealpha=1)

ax.grid(visible=True, which="both")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False, zorder=7)
ax.xaxis.set_label_coords(1.02, 0.20)
ax.set_ylabel("$\\cos^2(\\omega t)$", fontsize=15, rotation=0, clip_on=False)
ax.yaxis.set_label_coords(0, 1.05)

ax.set_xticks(np.arange(0, 1.6 * T, 0.5 * T))
# plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
# lbls = ax.get_xticklabels()
ax.set_xticklabels(["0"] + [f"{k}$T$" for k in np.arange(0.5, 1.6, 0.5)])
# ax.set_yticks(np.arange(-10, 10.1, 1))
# ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
# ax.set_yticklabels(["$P_{\\mathrm{max}}$"])

# ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="x")

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./cos2_stud.pdf", bbox_inches="tight")

ax.plot(tlist, u_list**2, ls="-", color="firebrick", label="$s^2(t)$")
ax.axhline(0.5, ls="--", lw=2, color="black")

# plt.show()

fig.savefig("./cos2_prof.pdf", bbox_inches="tight")
